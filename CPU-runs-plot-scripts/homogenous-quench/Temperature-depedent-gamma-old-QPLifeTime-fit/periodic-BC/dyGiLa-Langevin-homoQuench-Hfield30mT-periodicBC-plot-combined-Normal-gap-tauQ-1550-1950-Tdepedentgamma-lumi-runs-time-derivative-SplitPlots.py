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


measureData_h30mT_tauQ50 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ50/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ150 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-pairBreakingBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ150/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ250 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ250/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ350 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ350/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ450/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ550/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ650/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ750/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ850/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ950/stats/measure-stream.csv', sep=' ', header=None)

measureData_h30mT_tauQ1050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1050/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1150 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1150/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1250 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1250/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1350 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1350/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1450/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1550/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1650/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1750/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1850/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ1950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ1950/stats/measure-stream.csv', sep=' ', header=None)

measureData_h30mT_tauQ2050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2050/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2150 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2150/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2250 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2250/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2350 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2350/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2450 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2450/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2550 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2550/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2650 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2650/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2750 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2750/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2850 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2850/stats/measure-stream.csv', sep=' ', header=None)
measureData_h30mT_tauQ2950 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ2950/stats/measure-stream.csv', sep=' ', header=None)

measureData_h30mT_tauQ3050 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-C/tauQ125-tauQ3000-H30-RSeed-1-periodicBC/p-26.0-tauQ50-3050-Tdpendentgamma/p-26.0-tauQ3050/stats/measure-stream.csv', sep=' ', header=None)

### For all *csv files, delimiter is comma * *.
### Every line corresponds to a common pressure value,
### the 0th element of every line is sim time t, gol.t in unit of tGL
### the 1st element of every line is temperature of homogenous quench (mK),
### the 2nd element of every line .

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>   parampeters definations  <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

Tcp = 2.378 # mK at 26 bar
LineWidth=3.5
zeroTol = 6.5e-2

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>    Tempratue profile plot  <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
fig1, ax1 = plt.subplots(1,1);

# for r in range(0, row, 30):
    
#     ax1.plot(gaps_A[r,1]*np.linspace(0.,1.,col-2), gaps_A[r,2:],'-', label="A: {} bar".format(gaps_A[r,0]))
#     ax1.plot(gaps_B[r,1]*np.linspace(0.,1.,col-2), gaps_B[r,2:],'--', label="B: {} bar".format(gaps_B[r,0]))

# ax1.plot(measureData_h30mT_tauQ1050.values[:,0], measureData_h30mT_tauQ1050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1050t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))
# ax1.plot(measureData_h30mT_tauQ1150.values[:,0], measureData_h30mT_tauQ1150.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1150t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))
# ax1.plot(measureData_h30mT_tauQ1250.values[:,0], measureData_h30mT_tauQ1250.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1250t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))
# ax1.plot(measureData_h30mT_tauQ1350.values[:,0], measureData_h30mT_tauQ1350.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1350t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))
# ax1.plot(measureData_h30mT_tauQ1450.values[:,0], measureData_h30mT_tauQ1450.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1450t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))

ax1.plot(measureData_h30mT_tauQ1550.values[:,0], measureData_h30mT_tauQ1550.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1550t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1650.values[:,0], measureData_h30mT_tauQ1650.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1650t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1750.values[:,0], measureData_h30mT_tauQ1750.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1750t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1850.values[:,0], measureData_h30mT_tauQ1850.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1850t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_h30mT_tauQ1950.values[:,0], measureData_h30mT_tauQ1950.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,\tau_{Q}=1950t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))

# ax1.plot(measureData_h30mT_tauQ2050.values[:,0], measureData_h30mT_tauQ2050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2150.values[:,0], measureData_h30mT_tauQ2150.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2250.values[:,0], measureData_h30mT_tauQ2250.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2350.values[:,0], measureData_h30mT_tauQ2350.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2450.values[:,0], measureData_h30mT_tauQ2450.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2550.values[:,0], measureData_h30mT_tauQ2550.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2650.values[:,0], measureData_h30mT_tauQ2650.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2750.values[:,0], measureData_h30mT_tauQ2750.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2850.values[:,0], measureData_h30mT_tauQ2850.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))
# ax1.plot(measureData_h30mT_tauQ2950.values[:,0], measureData_h30mT_tauQ2950.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

# ax1.plot(measureData_h30mT_tauQ3050.values[:,0], measureData_h30mT_tauQ3050.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='solid', color=(0, 0, 1.0))

# ax1.plot(measureData_relexingt1750d.values[:,0], measureData_relexingt1750d.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=125t^{0}_{GL}$', linestyle='solid', color=(1.0, 0.5, 0.1))
# ax1.plot(measureData_relexingt1750c.values[:,0], measureData_relexingt1750c.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=250t^{0}_{GL}$', linestyle='solid', color=(0, 0.6, 0.6))
# ax1.plot(measureData_relexingt1750b.values[:,0], measureData_relexingt1750b.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=500t^{0}_{GL}$', linestyle='solid', color=(0, 1.0, 0.0))

ax1.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 22.0)
#ax1.set_ylabel(r'$\Delta_{A(B)}/k_{b}T_{c}(p)$',fontsize = 18.0)
ax1.set_ylabel(r'$T/T_{c}(p)$',fontsize = 22.0)
ax1.tick_params(axis='both', which='major', labelsize=30)
ax1.legend(prop={'size': 18}, bbox_to_anchor=(1.54, 1.0), loc='upper right')
ax1.grid(True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>> gap \sqrt{A^dagger.A} plot <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig2, ax2 = plt.subplots(1,1);

#measureData_h30mT_tauQ50.values[:,2][np.where(measureData_h30mT_tauQ50.values[:,2] <= 1e-1)]

# index_join_normal_sf = np.where(measureData_h30mT_tauQ1050.values[0:,2] >= zeroTol)[0][0]
# print(index_join_normal_sf)
# ax2.plot(measureData_h30mT_tauQ1050.values[:,0], np.concatenate((measureData_h30mT_tauQ1050.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1050.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1050t_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

# index_join_normal_sf = np.where(measureData_h30mT_tauQ1150.values[0:,2] >= zeroTol)[0][0]
# print(index_join_normal_sf)
# ax2.plot(measureData_h30mT_tauQ1150.values[:,0], np.concatenate((measureData_h30mT_tauQ1150.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1150.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1150t_{GL}$', linestyle='dashdot', color=(0, 1.0, 0.0))

# index_join_normal_sf = np.where(measureData_h30mT_tauQ1250.values[0:,2] >= zeroTol)[0][0]
# print(index_join_normal_sf)
# ax2.plot(measureData_h30mT_tauQ1250.values[:,0], np.concatenate((measureData_h30mT_tauQ1250.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1250.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1250t_{GL}$', linestyle='dashdot', color=(1.0, 0, 0.0))

# index_join_normal_sf = np.where(measureData_h30mT_tauQ1350.values[0:,2] >= zeroTol)[0][0]
# print(index_join_normal_sf)
# ax2.plot(measureData_h30mT_tauQ1350.values[:,0], np.concatenate((measureData_h30mT_tauQ1350.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1350.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1350t_{GL}$', linestyle='dashdot', color=(0.5, 0, 1.0))

# index_join_normal_sf = np.where(measureData_h30mT_tauQ1450.values[0:,2] >= zeroTol)[0][0]
# print(index_join_normal_sf)
# ax2.plot(measureData_h30mT_tauQ1450.values[:,0], np.concatenate((measureData_h30mT_tauQ1450.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1450.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1450t_{GL}$', linestyle='dashdot', color=(0.7, 0.6, 0.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1550.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax2.plot(measureData_h30mT_tauQ1550.values[:,0], np.concatenate((measureData_h30mT_tauQ1550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1550.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1550t_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1650.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax2.plot(measureData_h30mT_tauQ1650.values[:,0], np.concatenate((measureData_h30mT_tauQ1650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1650.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1650t_{GL}$', linestyle='dashdot', color=(0, 1.0, 0.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1750.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax2.plot(measureData_h30mT_tauQ1750.values[:,0], np.concatenate((measureData_h30mT_tauQ1750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1750.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1750t_{GL}$', linestyle='dashdot', color=(1.0, 0, 0.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1850.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax2.plot(measureData_h30mT_tauQ1850.values[:,0], np.concatenate((measureData_h30mT_tauQ1850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1850.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1850t_{GL}$', linestyle='dashdot', color=(0.5, 0, 1.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1950.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax2.plot(measureData_h30mT_tauQ1950.values[:,0], np.concatenate((measureData_h30mT_tauQ1950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,\tau_{Q}=1950t_{GL}$', linestyle='dashdot', color=(0.7, 0.6, 0.0))

# ax2.plot(measureData_h30mT_tauQ2050.values[:,0], np.concatenate((measureData_h30mT_tauQ2050.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2050.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2150.values[:,0], np.concatenate((measureData_h30mT_tauQ2150.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2150.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2250.values[:,0], np.concatenate((measureData_h30mT_tauQ2250.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2250.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2350.values[:,0], np.concatenate((measureData_h30mT_tauQ2350.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2350.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2450.values[:,0], np.concatenate((measureData_h30mT_tauQ2450.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2450.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2550.values[:,0], np.concatenate((measureData_h30mT_tauQ2550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2550.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2650.values[:,0], np.concatenate((measureData_h30mT_tauQ2650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2650.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2750.values[:,0], np.concatenate((measureData_h30mT_tauQ2750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2750.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2850.values[:,0], np.concatenate((measureData_h30mT_tauQ2850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2850.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
# ax2.plot(measureData_h30mT_tauQ2950.values[:,0], np.concatenate((measureData_h30mT_tauQ2950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ2950.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

# ax2.plot(measureData_h30mT_tauQ3050.values[:,0], np.concatenate((measureData_h30mT_tauQ3050.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ3050.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1750t_{GL}\,,\tau_{Q2}=50t^{0}_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))


# #ax1.set_ylabel(r'$\Delta_{A(B)}/k_{b}T_{c}(p)$',fontsize = 18.0)
# ax1.set_ylabel(r'$T/T_{c}(p)$',fontsize = 18.0)
# ax1.tick_params(axis='both', which='major', labelsize=30)

ax2.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 26.0)
ax2.set_ylabel(r'$<\sqrt{A^{\dagger}}A>/k_{B}T_{C}$',fontsize = 26.0)
ax2.tick_params(axis='both', which='major', labelsize=30)
ax2.legend(prop={'size': 18}, bbox_to_anchor=(1.0, 0.0), loc='lower right')
ax2.grid(True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>         dgap/dt  plot      <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig2, ax3 = plt.subplots(1,1);

index_join_normal_sf = np.where(measureData_h30mT_tauQ1550.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax3.plot(measureData_h30mT_tauQ1550.values[:,0], np.gradient(np.concatenate((measureData_h30mT_tauQ1550.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1550.values[index_join_normal_sf:,4])), measureData_h30mT_tauQ1550.values[:,0]), linewidth=LineWidth, label=r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}\,,\tau_{Q}=1550t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1650.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax3.plot(measureData_h30mT_tauQ1650.values[:,0], np.gradient(np.concatenate((measureData_h30mT_tauQ1650.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1650.values[index_join_normal_sf:,4])), measureData_h30mT_tauQ1650.values[:,0]), linewidth=LineWidth, label=r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}\,,\tau_{Q}=1650t_{GL}}$', linestyle='solid', color=(0, 1.0, 0.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1750.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax3.plot(measureData_h30mT_tauQ1750.values[:,0], np.gradient(np.concatenate((measureData_h30mT_tauQ1750.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1750.values[index_join_normal_sf:,4])), measureData_h30mT_tauQ1750.values[:,0]), linewidth=LineWidth, label=r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}\,,\tau_{Q}=1750t_{GL}}$', linestyle='solid', color=(1.0, 0, 0.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1850.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax3.plot(measureData_h30mT_tauQ1350.values[:,0], np.gradient(np.concatenate((measureData_h30mT_tauQ1850.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1850.values[index_join_normal_sf:,4])), measureData_h30mT_tauQ1850.values[:,0]), linewidth=LineWidth, label=r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}\,,\tau_{Q}=1850t_{GL}}$', linestyle='solid', color=(0.5, 0, 1.0))

index_join_normal_sf = np.where(measureData_h30mT_tauQ1950.values[0:,2] >= zeroTol)[0][0]
print(index_join_normal_sf)
ax3.plot(measureData_h30mT_tauQ1950.values[:,0], np.gradient(np.concatenate((measureData_h30mT_tauQ1950.values[0:index_join_normal_sf,2], measureData_h30mT_tauQ1950.values[index_join_normal_sf:,4])), measureData_h30mT_tauQ1950.values[:,0]), linewidth=LineWidth, label=r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}\,,\tau_{Q}=1950t_{GL}}$', linestyle='solid', color=(0.7, 0.6, 0.0))

ax3.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 26.0)
ax3.set_ylabel(r'$\frac{d<\sqrt{A^{\dagger}A}>}{dt}/k_{B}T_{C}t^{-1}_{GL}$',fontsize = 26.0)
ax3.tick_params(axis='both', which='major', labelsize=30)
ax3.legend(prop={'size': 18}, bbox_to_anchor=(1.0, 1.0), loc='upper right')
ax3.grid(True)


plt.show()
