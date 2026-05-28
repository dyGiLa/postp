import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import Module_phaseVolume_Speed as VS

#######################################
#  condition groups for success count #
#######################################

def BWinning_cond_group(p9, p5, p1, AfailT, BsuccT, pM1T):
    return (p9 < AfailT and p5 > BsuccT and p1 < p1T)

def BWinning_cond_group2(p5, BsuccT, pM1T):
    return (p5 > BsuccT)

def AWinning_cond_group(p9, p5, p1, BfailT, pM1T):
    return (p9 > 0. and p5 < 0.1 and p1 > pM1T)

# def AWinning_cond2_group(p9, p5, p1, AServiveT, BfailT, p1T):
#     return (p9 > 0.1 and p5 < 0.1 and p1 > 0.9)


# Root directory where RSeed-* folders are located
root_dir = '/home/heidi/ReHD3/dyGiLa-project/project_462000960/heterogenouos-quench/cube-1024/H-30mT/p-5.5bar-T0-0.80-0.96/E0-1500eV'

# Base glob pattern to match all pv.csv files under RSeed-* folders
pattern = os.path.join(root_dir, "RSeed-*-T0-0.80-0.96", "p-5.5-T1-*", "stats", "phaseVolume-stream.csv")
print("patter", pattern)

csv_files = glob.glob(pattern)
print("csv_files = ", csv_files)

# plot marker sizes
s=[50, 70, 90, 110]

# A-phase remaining failed Threshold
AfT = 0.75

# B-phase proliferation success Threshold
BsT = 0.005

# phase marker 1 portion label Threshold
p1T = 0.1

############################################################
#   build dictionaries of last momentum portion of px      #
############################################################

# python Dictionary to hold Vratio_px values per px
# defaultdict(list) creates empty list for missing key T1,
# which will be added later.
p9CSV_last_by_T1 = defaultdict(list)
p5CSV_last_by_T1 = defaultdict(list)
p1CSV_last_by_T1 = defaultdict(list)

for csv_file in csv_files:
    try:
        # Extract T1 from folder name: "p-5.5-T1-#",
        # This works as key for appending Vratio_px.
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
        print("parent_dir = ",parent_dir)
        T1Val_str = parent_dir.replace("p-5.5-T1-", "")
        print("T1Val_str = ", T1Val_str)        
        T1Val_val = float(T1Val_str)

        df = pd.read_csv(csv_file)
        if not df.empty:
            # check the last line for last momentum of px
            p9CSV_last = df.iloc[-1]["Vratio_p9_acc"]
            p5CSV_last = df.iloc[-1]["Vratio_p5_acc"]
            p1CSV_last = df.iloc[-1]["Vratio_p1_acc"]

            # missing keys T1 are added when append/access
            p9CSV_last_by_T1[T1Val_val].append(p9CSV_last)
            p5CSV_last_by_T1[T1Val_val].append(p5CSV_last)
            p1CSV_last_by_T1[T1Val_val].append(p1CSV_last)            
    except Exception as e:
        print(f"Failed on {csv_file}: {e}")

print("\n")        
print("p9CSV_last_by_T1: ",list(p9CSV_last_by_T1.keys()))        
print("\n")
print("p9CSV_last_by_T1",p9CSV_last_by_T1)
print("\n")
print("p5CSV_last_by_T1",p5CSV_last_by_T1)
print("\n")
print("p1CSV_last_by_T1",p1CSV_last_by_T1)
print("\n")
        
# Compute probability for each T1 value
T1_values = sorted(p9CSV_last_by_T1.keys())
print("T1_values = ", T1_values)


############################################################
#         Return Volume Speed dictionaries of px           #
############################################################
p9VSpeed_last_by_T1, p5VSpeed_last_by_T1, _ = VS.pvSpeedDicts(root_dir)

print("\n")        
print("p9VSpeed_last_by_T1: ",list(p9VSpeed_last_by_T1.keys()))        
print("\n")
print("p9VSpeed_last_by_T1",p9VSpeed_last_by_T1)
print("\n")
print("p5VSpeed_last_by_T1",p5VSpeed_last_by_T1)
print("\n")

############################################################
# calculate the Empirical probability of B-phase seeding   #
############################################################

#probabilities = defaultdict(list)
probabilities = []

for T1 in T1_values:
    p9VR = np.array(p9CSV_last_by_T1[T1])
    p5VR = np.array(p5CSV_last_by_T1[T1])
    p9VSpeed = np.array(p9VSpeed_last_by_T1[T1])
    p5VSpeed = np.array(p5VSpeed_last_by_T1[T1])
    
    print("\n")
    print("p9VR : ", p9VR)
    print("\n")
    print("p5Vspeed : ",p5VSpeed)

    # case of A-phase decay
    BSucSeedingFilter1 = (p9VR != 0.) & (p5VR != 0.) & (p9VSpeed < 0.) & (p5VSpeed > 0.)
    # case of A-phase has been iliminated
    BSucSeedingFilter2 = (p9VR == 0.) & (p5VR != 0.) & (p9VSpeed == 0.)
    # case of unusually B-phase defects formed'
    BSucSeedingFilter3 = (p9VR != 0.) & (p5VR != 0.) & (p9VSpeed * p5VSpeed > 0.)    
    

    print("\n", "T1 = ", T1)
    print("BSucSeedingFilter1 : ", BSucSeedingFilter1)
    print("BSucSeedingFilter2 : ", BSucSeedingFilter2)
    print("BSucSeedingFilter3 : ", BSucSeedingFilter3)    

    eventCountFilter1 = sum(BSucSeedingFilter1)
    eventCountFilter2 = sum(BSucSeedingFilter2)
    eventCountFilter3 = sum(BSucSeedingFilter3)    

    print("\n")
    print("eventCountFilter1 : ", eventCountFilter1)
    print("eventCountFilter2 : ", eventCountFilter2)
    print("eventCountFilter3 : ", eventCountFilter3)    

    #BSucEventsCount_T1 = eventCountFilter1 if eventCountFilter1 != 0 else eventCountFilter2
    BSucEventsCount_T1 = eventCountFilter1 + eventCountFilter2 + eventCountFilter3
    
    print("BSucEventsCount_T1 : ",BSucEventsCount_T1, " for T1 = ", T1)
    numOfTry = len(p5VR)
    print("numOfTry = ", numOfTry)
    
    prob = (BSucEventsCount_T1 / numOfTry) if numOfTry > 0 else 0
    #probabilities[T1].append(prob)
    probabilities.append(prob)
    

print("\n")
print("probabilities : ", probabilities)
    
############################################################
#     plot Empirical probability of B-phase seeding        #
############################################################

fig, ax = plt.subplots(1,1,figsize=(12, 7));

T0Array=np.array([0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96])

ax.plot(T0Array, probabilities, linestyle='--', color='red')
ax.scatter(T0Array, probabilities,
           marker='o', s=s[2], color='blue',
           label=fr'$p_{{iHB}}$, $5.5$ bar $30mT$, $E_{{0}}=1500eV$ ')

ax.set_xlabel(r'$T_{ambient}/T_c$',fontsize = 26.0)
ax.set_ylabel(r'B-phase Seeding Probability',fontsize = 26.0)
ax.set_xlim(0.8, 0.97)    
ax.set_ylim(-0.1, 1.2)


# Enable minor ticks
ax.minorticks_on()
# Show major grid
ax.grid(True, which='major', linestyle='-', linewidth=0.8)
# Show minor grid
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
# Set major tick label size
ax.tick_params(axis='both', which='major', labelsize=30)

# Legend
ax.legend(prop={'size': 18}, loc='best')

fig.subplots_adjust(left=0.15, bottom=0.18)  # space for labels

# Create a unique filename based on path
    
plot_name = 'B-phase-Seeding-probability-p5.5-H30mT-E0-1500eV-T0-0.80-0.96.png'
output_path = os.path.join(root_dir, plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)
# plt.close(fig1)
plt.close(fig)
