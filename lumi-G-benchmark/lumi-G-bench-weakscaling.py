import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# >>>>>>>>>>>>>>>             README, pls          <<<<<<<<<<<<<<< #

'''This script is used for vatulazation the lumi benchmark data 

simulation times and mesurement times
''' 

# >>>>>>>>>>>>> load the *csv files into numpy array <<<<<<<<<<<<< #

# with open('measure-stream.csv') as t_mesures:
#     mesure_data = csv.reader(t_mesures, delimiter=' ')


lumiG_bench1_256 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-weak-scaling-256.csv', sep=' ', header=None)
lumiG_bench1_512 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-weak-scaling-512.csv', sep=' ', header=None)

### For all *csv files, delimiter is comma * *.
### Every line corresponds to a given number of GCDs of MI250
### the 0th element of every line is no. GCDs
### the 1st element of every line is simulation times,
### the 2nd element of every line is mesurement times.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>   parampeters definations  <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# Tcp = 2.378 # mK at 26 bar
LineWidthG=3.5
LineWidthC=5
# zeroTol = 6e-2

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>> simulation time plot log-y <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig1, ax1 = plt.subplots(1,1);

ax1.plot(lumiG_bench1_256.values[:,0], lumiG_bench1_256.values[:,2], linewidth=LineWidthG, label=r'Wall times with $256^{3}$ sites per GCD', linestyle='solid', marker='o', markersize=20, color=(0.0, 0, 1.0))

ax1.plot(lumiG_bench1_512.values[:,0], lumiG_bench1_512.values[:,2], linewidth=LineWidthG, label=r'Wall times with $512^{3}$ sites per GCD', linestyle='solid', marker='D', markersize=20, color=(0.9, 0.5, 0.0))

# ax1.plot(lumiG_bench1_256.values[:10,0], lumiG_bench1_256.values[:10,2], linewidth=LineWidthG, label=r'Mesurement times with AMD MI250X', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

# ax1.plot(lumiG_bench1_2046cube_estimated_noGCDs, lumiG_bench1_2046cube_estimated_simTimes, 'o', c='red', markersize=21)

ax1.set_xlabel(r'$No.\,of\,\,\,GCDs$',fontsize = 36.0)
ax1.set_ylabel(r'$time/s$',fontsize = 36.0)

major_ticks_x = np.arange(0.1, 600, 50)
minor_ticks_x = np.arange(0.1, 600, 20)

major_ticks_y = np.arange(1000, 60000, 370)
minor_ticks_y = np.arange(1000, 60000, 37)


ax1.set_xticks(major_ticks_x)
ax1.set_xticks(minor_ticks_x, minor=True)
ax1.set_yticks(major_ticks_y)
ax1.set_yticks(minor_ticks_y, minor=True)

ax1.set_xlim(0.9, 600)
ax1.set_ylim(1000, 60000)
ax1.set_xscale('log')
ax1.set_yscale('log')


# ax1.grid(which='both')
ax1.tick_params(axis='both',which='major', width=4, length=7, labelsize=26)
ax1.tick_params(axis='y',which='minor', width=4, length=7, labelsize=26)

#ax1.set_xlim(40, 250)

ax1.grid(which="major", alpha=0.9)
ax1.grid(which="minor", alpha=0.6)

#ax1.legend(prop={'size': 24}, bbox_to_anchor=(0.0005, 0.0), loc='upper right')
ax1.legend(prop={'size': 24}, bbox_to_anchor=(0.99, 0.2), loc='upper right')
fig1.suptitle('Weak scaling benchmark of dyGiLa on LUMI-G/Mi250x',fontsize = 36.0)
ax1.grid(True)


# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# # >>>>>>>>>>>>> Efficiency plot log-x <<<<<<<<<<<<<<< #
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig3, ax3 = plt.subplots(1,1);


ax3.plot(lumiG_bench1_256.values[:,0], lumiG_bench1_256.values[:,3], linewidth=LineWidthG, label=r'Efficiency with $256^{3}$ sites per GCD', linestyle='solid', marker='o', markersize=20, color=(0.0, 0, 1.0))

ax3.plot(lumiG_bench1_512.values[:,0], lumiG_bench1_512.values[:,3], linewidth=LineWidthG, label=r'Efficiency with $512^{3}$ sites per GCD', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

# ax3.plot(lumiG_bench1_2046cube_estimated_noGCDs, NoGCDsESimT, 'o', c='red', markersize=21)

ax3.set_xlabel(r'$No.\,of\,\,\,GCDs$',fontsize = 36.0)
ax3.set_ylabel(r'Efficiency $(t_{1}/t_{N})$',fontsize = 36.0)

major_ticks_x = np.arange(0.9, 600, 50)
minor_ticks_x = np.arange(0.9, 600, 20)

major_ticks_y = np.arange(0.5, 1.5, 0.1)
minor_ticks_y = np.arange(0.5, 1.5, 0.01)

# ax3.plot(major_ticks_x, NoCOREsSimT, linewidth=LineWidthC, label=r'Cumulated Simulation time with AMD EPYC milan 8192 cores', linestyle='dashed', color=(0.5, 0.0, 0.5))

ax3.set_xticks(major_ticks_x)
ax3.set_xticks(minor_ticks_x, minor=True)
ax3.set_yticks(major_ticks_y)
ax3.set_yticks(minor_ticks_y, minor=True)

ax3.set_xlim(0.9, 600)
ax3.set_ylim(0.5, 1.5)
ax3.set_xscale('log')
ax3.set_yscale('linear')

# ax1.grid(which='both')
ax3.tick_params(axis='both',which='major', width=4, length=7, labelsize=26)
ax3.tick_params(axis='both',which='minor', width=4, length=7, labelsize=26)

ax3.grid(which="major", alpha=0.9)
ax3.grid(which="minor", alpha=0.6)

ax3.legend(prop={'size': 22}, bbox_to_anchor=(0.0005, 0.1), loc='lower left')
fig3.suptitle('Weak scaling benchmark of dyGiLa on LUMI-G/Mi250x',fontsize = 36.0)
ax3.grid(True)


plt.show()
