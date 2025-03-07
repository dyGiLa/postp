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


lumiG_bench1_512cube = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-strong-scaling-512.csv', sep=' ', header=None)
lumiG_bench1_1024cube = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-strong-scaling-1024.csv', sep=' ', header=None)
lumiG_bench1_checkpoint = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-strong-scaling-checkpoints.csv', sep=' ', header=None)
#lumiG_bench1_512cube = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-Benchmark/lumi-G-becnh-strong-scaling-512.csv', sep=' ', header=None)

# print(lumiG_bench1_checkpoint)

lumiG_bench1_512cube_noGCDs = lumiG_bench1_512cube.values[:,0]
lumiG_bench1_512cube_simTimes = lumiG_bench1_512cube.values[:,1]

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

ax1.plot(lumiG_bench1_512cube.values[:,0], lumiG_bench1_512cube.values[:,1], linewidth=LineWidthG, label=r'$512^{3}$ lattice with AMD MI250X', linestyle='solid', marker='o', markersize=20, color=(0.0, 0, 1.0))

ax1.plot(lumiG_bench1_1024cube.values[:,0], lumiG_bench1_1024cube.values[:,1], linewidth=LineWidthG, label=r'$1024^{3}$ lattice with AMD MI250X', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

# ax1.plot(lumiG_bench1_512cube.values[:10,0], lumiG_bench1_512cube.values[:10,2], linewidth=LineWidthG, label=r'Mesurement times with AMD MI250X', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

#ax1.plot(lumiG_bench1_2046cube_estimated_noGCDs, lumiG_bench1_2046cube_estimated_simTimes, 'o', c='red', markersize=21)

ax1.set_xlabel(r'$No.\,of\,\,\,GCDs$',fontsize = 36.0)
ax1.set_ylabel(r'$time/s$',fontsize = 36.0)

major_ticks_x = np.arange(1, 10, 1)
minor_ticks_x = np.arange(1, 10, 0.55)

major_ticks_y = np.arange(3000, 40000, 1000)
minor_ticks_y = np.arange(3000, 40000, 500)

# # LUMI-C 64 node simulation time
# lumiC_bench1_2046cube_estimated_simTimes = np.full((major_ticks_x.size, 1), 202167.92339)

# ax1.plot(major_ticks_x,  lumiC_bench1_2046cube_estimated_simTimes, linewidth=LineWidthC, label=r'Simulation time with AMD EPYC milan 8192 cores', linestyle='dashed', color=(0.5, 0.0, 0.5))

ax1.set_xticks(major_ticks_x)
ax1.set_xticks(minor_ticks_x, minor=True)
ax1.set_yticks(major_ticks_y)
ax1.set_yticks(minor_ticks_y, minor=True)

ax1.set_xlim(0, 10)
ax1.set_ylim(3000, 40000)
ax1.set_yscale('log')


# ax1.grid(which='both')
ax1.tick_params(axis='both',which='major', width=4, length=7, labelsize=26)
ax1.tick_params(axis='y',which='minor', width=4, length=7, labelsize=26)

#ax1.set_xlim(40, 250)

ax1.grid(which="major", alpha=0.9)
ax1.grid(which="minor", alpha=0.6)

#ax1.legend(prop={'size': 24}, bbox_to_anchor=(0.0005, 0.0), loc='upper right')
ax1.legend(prop={'size': 24}, bbox_to_anchor=(0.99, 0.95), loc='upper right')
fig1.suptitle('Strong scaling benchmark of dyGiLa on LUMI supercomputer',fontsize = 36.0)
ax1.grid(True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>> simulation time plot log-xy <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig2, ax2 = plt.subplots(1,1);

ax2.plot(lumiG_bench1_512cube.values[:,0], lumiG_bench1_512cube.values[:,1], linewidth=LineWidthG, label=r'$512^{3}$ lattice', linestyle='solid', marker='o', markersize=20, color=(0.0, 0, 1.0))

ax2.plot(lumiG_bench1_1024cube.values[:,0], lumiG_bench1_1024cube.values[:,1], linewidth=LineWidthG, label=r'$1024^{3}$ lattice', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

## checkpoint benchmark

ax2.scatter(lumiG_bench1_checkpoint.values[:2,0],  lumiG_bench1_checkpoint.values[:2,1], c='tab:green', s=640, marker="*", label=r'insitu checkpoint $512^{3}$ lattice')

ax2.scatter(lumiG_bench1_checkpoint.values[2:4,0],  lumiG_bench1_checkpoint.values[2:4,1], c='rosybrown', s=640, marker="P", label=r'insitu checkpoint $1024^{3}$ lattice')

ax2.scatter(lumiG_bench1_checkpoint.values[4:5,0],  lumiG_bench1_checkpoint.values[4:5,1], c='darkviolet', s=640, marker="p", label=r'HDF5 checkpoint $512^{3}$ lattice')

ax2.scatter(lumiG_bench1_checkpoint.values[5:6,0],  lumiG_bench1_checkpoint.values[5:6,1], c='deeppink', s=640, marker="s", label=r'HDF5 checkpoint $1024^{3}$ lattice')

# ax2.plot(lumiG_bench1_512cube.values[:10,0], lumiG_bench1_512cube.values[:10,2], linewidth=LineWidthG, label=r'Mesurement wall times with AMD MI250X', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

ax2.set_xlabel(r'$No.\,of\,\,\,GCDs$',fontsize = 36.0)
ax2.set_ylabel(r'$time/s$',fontsize = 36.0)

major_ticks_x = np.arange(1, 150, 1)
minor_ticks_x = np.arange(1, 150, 0.5)

major_ticks_y = np.arange(3000, 50000, 1000)
minor_ticks_y = np.arange(3000, 50000, 500)

ax2.set_xticks(major_ticks_x)
ax2.set_xticks(minor_ticks_x, minor=True)
ax2.set_yticks(major_ticks_y)
ax2.set_yticks(minor_ticks_y, minor=True)

ax1.set_xlim(0, 150)
ax1.set_ylim(3000, 40000)
ax2.set_xscale('log')
ax2.set_yscale('log')

# ax1.grid(which='both')
ax2.tick_params(axis='both',which='major', width=4, length=7, labelsize=26)
ax2.tick_params(axis='both',which='minor', width=4, length=7, labelsize=26)

ax2.grid(which="major", alpha=0.9)
ax2.grid(which="minor", alpha=0.6)

ax2.legend(prop={'size': 22}, bbox_to_anchor=(0.0005, 0.0), loc='lower left')
fig2.suptitle('Strong scaling benchmark of dyGiLa on LUMI-G/Mi250x',fontsize = 36.0)
ax2.grid(True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>> speedup plot log-x <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig3, ax3 = plt.subplots(1,1);

ax3.plot(lumiG_bench1_512cube.values[:,0], lumiG_bench1_512cube.values[:,2], linewidth=LineWidthG, label=r'$512^{3}$ lattice', linestyle='solid', marker='o', markersize=20, color=(0.0, 0, 1.0))

ax3.plot(lumiG_bench1_1024cube.values[:,0], lumiG_bench1_1024cube.values[:,2], linewidth=LineWidthG, label=r'$1024^{3}$ lattice', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

# ax2.plot(lumiG_bench1_512cube.values[:10,0], lumiG_bench1_512cube.values[:10,2], linewidth=LineWidthG, label=r'Mesurement wall times with AMD MI250X', linestyle='solid', marker='D', markersize=20, color=(0.7, 0.3, 0.0))

ax3.set_xlabel(r'$No.\,of\,\,\,GCDs$',fontsize = 36.0)
ax3.set_ylabel(r'$SpeedUp$',fontsize = 36.0)

major_ticks_x = np.arange(1, 100, 1)
minor_ticks_x = np.arange(1, 100, 0.5)

major_ticks_y = np.arange(1, 50, 1)
minor_ticks_y = np.arange(1, 50, 0.5)

ax3.set_xticks(major_ticks_x)
ax3.set_xticks(minor_ticks_x, minor=True)
ax3.set_yticks(major_ticks_y)
ax3.set_yticks(minor_ticks_y, minor=True)

ax3.set_xlim(0.9, 100)
ax3.set_ylim(0.5, 100)
ax3.set_xscale('log')
ax3.set_yscale('log')


# ax1.grid(which='both')
ax3.tick_params(axis='both',which='major', width=4, length=7, labelsize=26)
ax3.tick_params(axis='y',which='minor', width=4, length=7, labelsize=26)

ax3.grid(which="major", alpha=0.9)
ax3.grid(which="minor", alpha=0.6)

ax3.legend(prop={'size': 22}, bbox_to_anchor=(0.0005, 0.98), loc='upper left')
fig3.suptitle('Strong scaling benchmark of dyGiLa on LUMI-G/Mi250x',fontsize = 36.0)
ax3.grid(True)


plt.show()
