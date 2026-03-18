import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

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
root_dir = '/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/lumi-project_462000960/project_462000960/heterogenouos-quench/cube-512/H-30mT/p-5.5bar-T0-0.5-0.95/E0-150eV'

# Base glob pattern to match all pv.csv files under RSeed-* folders
pattern = os.path.join(root_dir, "RSeed-*-T0-0.5-0.95", "p-5.5-T1-*", "stats", "phaseVolume-stream.csv")
csv_files = glob.glob(pattern)
# print("csv_files = ", csv_files)

# plot marker sizes
s=[50, 70, 90, 110]

# A-phase remaining failed Threshold
AfT = 0.75

# B-phase proliferation success Threshold
BsT = 0.01

# phase marker 1 portion label Threshold
p1T = 0.1


# python Dictionary to hold Vratio_px values per px #
p9CSV_last_by_T1 = defaultdict(list)
p5CSV_last_by_T1 = defaultdict(list)
p1CSV_last_by_T1 = defaultdict(list)

for csv_file in csv_files:
    try:
        # Extract T1 from folder name: "p-5.5-T1-#"
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
        # print("parent_dir = ",parent_dir)
        T1Val_str = parent_dir.replace("p-5.5-T1-", "")
        # print("T1Val_str = ", T1Val_str)
        
        T1Val_val = float(T1Val_str)

        df = pd.read_csv(csv_file)
        if not df.empty:
            p9CSV_last = df.iloc[-1]["Vratio_p9_acc"]
            p5CSV_last = df.iloc[-1]["Vratio_p5_acc"]
            p1CSV_last = df.iloc[-1]["Vratio_p1_acc"]            
            p9CSV_last_by_T1[T1Val_val].append(p9CSV_last)
            p5CSV_last_by_T1[T1Val_val].append(p5CSV_last)
            p1CSV_last_by_T1[T1Val_val].append(p1CSV_last)            
    except Exception as e:
        print(f"Failed on {csv_file}: {e}")

# print("p9CSV_last_by_T1",p9CSV_last_by_T1)
        
# Compute probability for each T1 value
T1_values = sorted(p9CSV_last_by_T1.keys())
print("T1_values = ", T1_values)

probabilities = []

for T1 in T1_values:
    p9CSV_vals = p9CSV_last_by_T1[T1]
    p5CSV_vals = p5CSV_last_by_T1[T1]
    p1CSV_vals = p1CSV_last_by_T1[T1]
    
    # count = sum(p9CSV > failure_threshold for p9CSV in p9CSV_vals)
    count = sum(p5CSV > BsT for p5CSV in p5CSV_vals)

    # count = sum(
    #     (
    #         BWinning_cond_group2(p5, BsT, p1T)
    #         # or condition_group2(p9, p5, p1)
    #         # or condition_group3(p9, p5, p1)
    #     )
    #    for p9, p5, p1 in zip(p9CSV_vals, p5CSV_vals, p1CSV_vals)
    # )
    
    print("count = ",count, " for T1 = ", T1)
    total = len(p9CSV_vals)
    print("total = ",total)
    
    prob = (count / total) if total > 0 else 0
    probabilities.append(prob)

    
# Plotting

fig, ax = plt.subplots(1,1,figsize=(12, 7));

# E0Array=np.array([80, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])
# T0Array=np.array([0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95])
T0Array=np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])

ax.plot(T0Array, probabilities, linestyle='--', color='red')
ax.scatter(T0Array, probabilities, marker='o', s=s[2], color='blue', label=fr'B-phase winning prob, 5.5 bar 30mT, $E_{{0}}=150eV$ ')

ax.set_xlabel(r'$T_{ambient}/T_c$',fontsize = 26.0)
ax.set_ylabel(r'Probability',fontsize = 26.0)
ax.set_xlim(0.5, 0.95)    
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
    
plot_name = 'B-phase-winning-probability-p5.5-H30mT-Ei150eV-T0-0.5-0.95.png'
output_path = os.path.join(root_dir, plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)
# plt.close(fig1)
plt.close(fig)
