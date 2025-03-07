import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# >>>>>>>>>>>>>>>             README, pls          <<<<<<<<<<<<<<< #

'''This script is used for vatulazation the stats/*csv files 

generated by dyGiLa write_energies() func.
''' 

# >>>>>>>>>>>>> load the *csv files into numpy array <<<<<<<<<<<<< #

# with open('measure-stream.csv') as t_mesures:
#     mesure_data = csv.reader(t_mesures, delimiter=' ')


#measureData_h30mT_tauQ125 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ125-H30/stats/measure-stream-run-1.csv', sep=' ', header=None)
measureData_h30mT_tauQ300 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ300-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ450-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ550-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ650-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ750-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ850-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ950-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1050-H30/stats/measure-stream.csv', sep=' ', header=None)
#measureData_h30mT_tauQ1150 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1150-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1250 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1250-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1350 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1350-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1450-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1550-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1650-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1750-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1850-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ1950-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2050-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2150 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2150-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2250 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2250-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2350 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2350-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2450-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2550-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2650-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2750-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2850-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ2950-H30/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ3050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/mahti-runs/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/tauQ3050-H30/stats/measure-stream.csv', sep=' ', header=None)
# measureData_relexingt1750b = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quench-II-7-C-b/stats/measure-stream.csv', sep=' ', header=None)
# measureData_relexingt1750c = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quench-II-7-C-c/stats/measure-stream.csv', sep=' ', header=None)
# measureData_relexingt1750d = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quench-II-7-C-d/stats/measure-stream.csv', sep=' ', header=None)


#print(measureData_relexingt320.values[:,0])
#print(measureData_relexingt320.values[:,1])


#print(np.concatenate((measureData_relexingt386.values[0:43,0], measureData_relexingt386.values[44:,0])))
#print(np.concatenate((measureData_relexingt386.values[0:43,2], measureData_relexingt386.values[44:,4])))
#print(measureData_relexingt386.values[0:53,2])

### For all *csv files, delimiter is comma * *.
### Every line corresponds to a common pressure value,
### the 0th element of every line is sim time t, gol.t in unit of tGL
### the 1st element of every line is temperature of homogenous quench (mK),
### the 2nd element of every line .

                                              
# # >>>>>>>>>>>>>        gap plot        <<<<<<<<<<<<<<< #
Tcp = 2.378 # mK at 26 bar
LineWidth=3.5

fig1, ax1 = plt.subplots(1,1);

# for r in range(0, row, 30):
    
#     ax1.plot(gaps_A[r,1]*np.linspace(0.,1.,col-2), gaps_A[r,2:],'-', label="A: {} bar".format(gaps_A[r,0]))
#     ax1.plot(gaps_B[r,1]*np.linspace(0.,1.,col-2), gaps_B[r,2:],'--', label="B: {} bar".format(gaps_B[r,0]))

#ax1.plot(measureData_h30mT_tauQ125.values[:,0], measureData_h30mT_tauQ125.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ300.values[:,0], measureData_h30mT_tauQ300.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ450.values[:,0], measureData_h30mT_tauQ450.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ550.values[:,0], measureData_h30mT_tauQ550.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ650.values[:,0], measureData_h30mT_tauQ650.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ750.values[:,0], measureData_h30mT_tauQ750.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ850.values[:,0], measureData_h30mT_tauQ850.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ950.values[:,0], measureData_h30mT_tauQ950.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

ax1.plot(measureData_h30mT_tauQ1050.values[:,0], measureData_h30mT_tauQ1050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
#ax1.plot(measureData_h30mT_tauQ1150.values[:,0], measureData_h30mT_tauQ1150.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1250.values[:,0], measureData_h30mT_tauQ1250.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1350.values[:,0], measureData_h30mT_tauQ1350.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1450.values[:,0], measureData_h30mT_tauQ1450.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1550.values[:,0], measureData_h30mT_tauQ1550.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1650.values[:,0], measureData_h30mT_tauQ1650.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1750.values[:,0], measureData_h30mT_tauQ1750.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1850.values[:,0], measureData_h30mT_tauQ1850.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1950.values[:,0], measureData_h30mT_tauQ1950.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

ax1.plot(measureData_h30mT_tauQ2050.values[:,0], measureData_h30mT_tauQ2050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2150.values[:,0], measureData_h30mT_tauQ2150.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2250.values[:,0], measureData_h30mT_tauQ2250.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2350.values[:,0], measureData_h30mT_tauQ2350.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2450.values[:,0], measureData_h30mT_tauQ2450.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2550.values[:,0], measureData_h30mT_tauQ2550.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2650.values[:,0], measureData_h30mT_tauQ2650.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2750.values[:,0], measureData_h30mT_tauQ2750.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2850.values[:,0], measureData_h30mT_tauQ2850.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ2950.values[:,0], measureData_h30mT_tauQ2950.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

ax1.plot(measureData_h30mT_tauQ3050.values[:,0], measureData_h30mT_tauQ3050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

# ax1.plot(measureData_relexingt1750d.values[:,0], measureData_relexingt1750d.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=125t^{0}_{GL}$', linestyle='solid', color=(1.0, 0.5, 0.1))
# ax1.plot(measureData_relexingt1750c.values[:,0], measureData_relexingt1750c.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=250t^{0}_{GL}$', linestyle='solid', color=(0, 0.6, 0.6))
# ax1.plot(measureData_relexingt1750b.values[:,0], measureData_relexingt1750b.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=500t^{0}_{GL}$', linestyle='solid', color=(0, 1.0, 0.0))



ax2 = ax1.twinx()
index_join_normal_sf = 119

#ax2.plot(measureData_h30mT_tauQ125.values[:,0], np.concatenate((measureData_h30mT_tauQ125.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ125.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ300.values[:,0], np.concatenate((measureData_h30mT_tauQ300.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ300.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ450.values[:,0], np.concatenate((measureData_h30mT_tauQ450.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ450.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ550.values[:,0], np.concatenate((measureData_h30mT_tauQ550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ550.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ650.values[:,0], np.concatenate((measureData_h30mT_tauQ650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ650.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ750.values[:,0], np.concatenate((measureData_h30mT_tauQ750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ750.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ850.values[:,0], np.concatenate((measureData_h30mT_tauQ850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ850.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ950.values[:,0], np.concatenate((measureData_h30mT_tauQ950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

ax2.plot(measureData_h30mT_tauQ1050.values[:,0], np.concatenate((measureData_h30mT_tauQ950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
#ax2.plot(measureData_h30mT_tauQ1150.values[:,0], np.concatenate((measureData_h30mT_tauQ950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1250.values[:,0], np.concatenate((measureData_h30mT_tauQ1250.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1250.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1350.values[:,0], np.concatenate((measureData_h30mT_tauQ1350.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1350.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1450.values[:,0], np.concatenate((measureData_h30mT_tauQ1450.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1450.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1550.values[:,0], np.concatenate((measureData_h30mT_tauQ1550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1550.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1650.values[:,0], np.concatenate((measureData_h30mT_tauQ1650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1650.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1750.values[:,0], np.concatenate((measureData_h30mT_tauQ1750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1750.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1850.values[:,0], np.concatenate((measureData_h30mT_tauQ1850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1850.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ1950.values[:,0], np.concatenate((measureData_h30mT_tauQ1950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

ax2.plot(measureData_h30mT_tauQ2050.values[:,0], np.concatenate((measureData_h30mT_tauQ2050.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2050.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2150.values[:,0], np.concatenate((measureData_h30mT_tauQ2150.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2150.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2250.values[:,0], np.concatenate((measureData_h30mT_tauQ2250.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2250.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2350.values[:,0], np.concatenate((measureData_h30mT_tauQ2350.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2350.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2450.values[:,0], np.concatenate((measureData_h30mT_tauQ2450.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2450.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2550.values[:,0], np.concatenate((measureData_h30mT_tauQ2550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2550.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2650.values[:,0], np.concatenate((measureData_h30mT_tauQ2650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2650.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2750.values[:,0], np.concatenate((measureData_h30mT_tauQ2750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2750.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2850.values[:,0], np.concatenate((measureData_h30mT_tauQ2850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2850.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_h30mT_tauQ2950.values[:,0], np.concatenate((measureData_h30mT_tauQ2950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

ax2.plot(measureData_h30mT_tauQ3050.values[:,0], np.concatenate((measureData_h30mT_tauQ3050.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ3050.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))



# ax2.plot(measureData_relexingt1750d.values[:,0], np.concatenate((measureData_relexingt1750d.values[0:index_join_normal_sf,2], measureData_relexingt1750d.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=125t^{0}_{GL}$', linestyle='dashdot', color=(1.0, 0.5, 0.1))
# ax2.plot(measureData_relexingt1750c.values[:,0], np.concatenate((measureData_relexingt1750c.values[0:index_join_normal_sf,2], measureData_relexingt1750c.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=250t^{0}_{GL}$', linestyle='dashdot', color=(0, 0.6, 0.6))
# ax2.plot(measureData_relexingt1750b.values[:,0], np.concatenate((measureData_relexingt1750b.values[0:index_join_normal_sf,2], measureData_relexingt1750b.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=500t^{0}_{GL}$', linestyle='dashdot', color=(0, 1.0, 0.0))


ax1.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 18.0)
#ax1.set_ylabel(r'$\Delta_{A(B)}/k_{b}T_{c}(p)$',fontsize = 18.0)
ax1.set_ylabel(r'$T/T_{c}(p)$',fontsize = 18.0)
ax1.tick_params(axis='both', which='major', labelsize=30)

ax2.set_ylabel(r'$\sqrt{A^{\dagger}}A$',fontsize = 18.0)
ax2.tick_params(axis='both', which='major', labelsize=30)


# ax1.legend(prop={'size': 18}, loc=1);
ax1.grid(True)
ax1.legend(prop={'size': 18}, bbox_to_anchor=(1.54, 1.0), loc='upper right')
ax2.legend(prop={'size': 18}, bbox_to_anchor=(1.54, 0.0), loc='lower right')


# fig2, ax2 = plt.subplots(1,1);

# for r in range(100, row, 20):
    
#     ax2.plot(gaps_A[r,1]*np.linspace(0.,1.,col-2), gaps_A[r,2:],'-', label="A: {} bar".format(gaps_A[r,0]))
#     ax2.plot(gaps_B[r,1]*np.linspace(0.,1.,col-2), gaps_B[r,2:],'--', label="B: {} bar".format(gaps_B[r,0]))
    
    
# ax2.set_xlabel(r'$T/mK$',fontsize = 18.0)
# ax2.set_ylabel(r'$\Delta_{A(B)}/k_{b}T_{c}(p)$',fontsize = 18.0)

# ax2.legend(prop={'size': 18}, loc=1);
# ax2.grid(True)



# # >>>>>>>>>>>>>   fulk free energy plot   <<<<<<<<<<<<<<< #

# fig3, ax3 = plt.subplots(1,1);

# for r in range(0, row, 30):
    
#     ax3.plot(f_A[r,1]*np.linspace(0.,1.,col-2), f_A[r,2:],'-', label="A: {} bar".format(f_A[r,0]))
#     ax3.plot(f_B[r,1]*np.linspace(0.,1.,col-2), f_B[r,2:],'--', label="B: {} bar".format(f_B[r,0]))
    
    
# ax3.set_xlabel(r'$T/mK$',fontsize = 18.0)
# ax3.set_ylabel(r'$f_{A(B)}/{\frac{1}{3}N(0)(k_{b}T_{c})^{2}}$',fontsize = 18.0)

# ax3.legend(prop={'size': 18}, loc=4);
# ax3.grid(True)

# fig4, ax4 = plt.subplots(1,1);

# for r in range(110, row, 20):
    
#     ax4.plot(f_A[r,1]*np.linspace(0.,1.,col-2), f_A[r,2:],'-', label="A: {} bar".format(f_A[r,0]))
#     ax4.plot(f_B[r,1]*np.linspace(0.,1.,col-2), f_B[r,2:],'--', label="B: {} bar".format(f_B[r,0]))
    
    
# ax4.set_xlabel(r'$T/mK$',fontsize = 18.0)
# ax4.set_ylabel(r'$f_{A(B)}/{\frac{1}{3}N(0)(k_{b}T_{c})^{2}}$',fontsize = 18.0)

# ax4.legend(prop={'size': 18}, loc=4);
# ax4.grid(True)

# # >>>>>>>>>>>>>>>>  free plot for rth row <<<<<<<<<<<<<<<< #

# fig5, ax5 = plt.subplots(1,1)

# r = round(30/0.17); print(" r is ", r, " r*0.17 = ", r*0.17)

# ax5.plot(f_A[r,1]*np.linspace(0.,1.,col-2), f_A[r,2:],'-', label="A: {} bar".format(f_A[r,0]))
# ax5.plot(f_B[r,1]*np.linspace(0.,1.,col-2), f_B[r,2:],'--', label="B: {} bar".format(f_B[r,0]))

# ax5.set_xlabel(r'$T/mK$',fontsize = 18.0)
# ax5.set_ylabel(r'$f_{A(B)}/{\frac{1}{3}N(0)(k_{b}T_{c})^{2}}$',fontsize = 18.0)

# ax5.legend(prop={'size': 18}, loc=4)
# ax5.grid(True)


# # ******************************************************** #
# # >>>>>>>>>>>>    equlibrium phase diagram   <<<<<<<<<<<<< #
# # ******************************************************** #


# fig6, ax6 = plt.subplots(1,1)

# ax6.plot(pd[:,2], pd[:,0], 'b-', label=r"$T_{c}^{Greywall}$")

# boolean_arr = pd[:,1] != 0.
# # print(boolean_arr," \n\n ", pd[:,1][boolean_arr])
# ax6.plot(pd[:,1][boolean_arr], pd[:,0][boolean_arr], 'r-', label=r"$T_{AB}^{rws19}$")

# ax6.set_xlabel(r'$T/mK$',fontsize = 18.0)
# ax6.set_ylabel(r'$p/bar$',fontsize = 18.0)

# ax6.legend(prop={'size': 18}, loc=2)
# # ax6.grid(True)
# ax6.set_ylim([0., 34.]);ax6.set_xlim([0., 2.486]);
# ax6.set_title(r"bulk equlibrium phase diagram, $H=0$")

# text_kwargs1 = dict(ha='center', va='center', fontsize=28, color='C1')
# text_kwargs2 = dict(ha='center', va='center', fontsize=28, color='blue')
# text_kwargs3 = dict(ha='center', va='center', fontsize=28, color='black')
# plt.text(2.212, 30., 'A', **text_kwargs1)
# plt.text(1.4, 17., 'B', **text_kwargs2)
# plt.text(2.1, 4.7, 'Normal', **text_kwargs3)

plt.show()
