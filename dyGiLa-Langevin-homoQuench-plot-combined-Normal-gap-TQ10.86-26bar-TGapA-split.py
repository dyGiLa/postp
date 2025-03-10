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

measureData_relexingt320 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quenches_till-28-Oct-2024/thermal-bath-UniT-quench-V-2/stats/measure-stream.csv', sep=' ', header=None)
#print(measureData_relexingt320.values[:,0])
#print(measureData_relexingt320.values[:,1])

measureData_relexingt386 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quenches_till-28-Oct-2024/thermal-bath-UniT-quench-V-3/stats/measure-stream.csv', sep=' ', header=None)
#print(measureData_relexingt386.values[:,0])
#print(measureData_relexingt386.values[:,1])

measureData_relexingt493 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quenches_till-28-Oct-2024/thermal-bath-UniT-quench-V-4/stats/measure-stream.csv', sep=' ', header=None)

measureData_relexingt639 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quenches_till-28-Oct-2024/thermal-bath-UniT-quench-V-5/stats/measure-stream.csv', sep=' ', header=None)

measureData_relexingt1000 = pd.read_csv('/home/heidi/Documents/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-quenches_till-28-Oct-2024/thermal-bath-UniT-quench-V/stats/measure-stream.csv', sep=' ', header=None)
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

ax1.plot(measureData_relexingt320.values[:,0], measureData_relexingt320.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=320t_{GL}$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(measureData_relexingt386.values[:,0], measureData_relexingt386.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=386t_{GL}$', linestyle='solid', color=(0.0, 1.0, 0.0))
ax1.plot(measureData_relexingt493.values[:,0], measureData_relexingt493.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=493t_{GL}$', linestyle='solid', color=(0.0, 0.6, 0.6))
ax1.plot(measureData_relexingt639.values[:,0], measureData_relexingt639.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=639t_{GL}$', linestyle='solid', color=(1.0, 0.5, 0.1))
ax1.plot(measureData_relexingt1000.values[:,0], measureData_relexingt1000.values[:,1]/Tcp, linewidth=LineWidth, label=r'$T/T_{c}\,,t_{Q1relx}=1000t_{GL}$', linestyle='solid', color=(0.8, 0, 0.2))


fig2, ax2 = plt.subplots(1,1);
index_join_normal_sf = 52

ax2.plot(measureData_relexingt320.values[:,0], np.concatenate((measureData_relexingt320.values[0:index_join_normal_sf,2], measureData_relexingt320.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=320t_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))

ax2.plot(measureData_relexingt386.values[:,0], np.concatenate((measureData_relexingt386.values[0:index_join_normal_sf,2], measureData_relexingt386.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=386t_{GL}$', linestyle='dashdot', color=(0.0, 1.0, 0.0))
#ax2.plot(measureData_relexingt386.values[:,0], measureData_relexingt386.values[:,2], label=r'$|\Delta|\,,t_{Q1relx}=386t_{GL}$', linestyle='dashdot', color=(0, 0, 1.0))
ax2.plot(measureData_relexingt493.values[:,0], np.concatenate((measureData_relexingt493.values[0:index_join_normal_sf,2], measureData_relexingt493.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=493t_{GL}$', linestyle='dashdot', color=(0.0, 0.6, 0.6))
ax2.plot(measureData_relexingt639.values[:,0], np.concatenate((measureData_relexingt639.values[0:index_join_normal_sf,2], measureData_relexingt639.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=639t_{GL}$', linestyle='dashdot', color=(1.0, 0.5, 0.1))
ax2.plot(measureData_relexingt1000.values[:,0], np.concatenate((measureData_relexingt1000.values[0:index_join_normal_sf,2], measureData_relexingt1000.values[index_join_normal_sf:,4])), linewidth=LineWidth, label=r'$|\Delta|\,,t_{Q1relx}=1000t_{GL}$', linestyle='dashdot', color=(0.8, 0, 0.2))


ax1.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 18.0)
#ax1.set_ylabel(r'$\Delta_{A(B)}/k_{b}T_{c}(p)$',fontsize = 18.0)
ax1.set_ylabel(r'$T/T_{c}(p)$',fontsize = 18.0)
ax1.tick_params(axis='both', which='major', labelsize=30)

ax2.set_ylabel(r'$<\sqrt{A^{\dagger}}A>$',fontsize = 18.0)
ax2.tick_params(axis='both', which='major', labelsize=30)


# ax1.legend(prop={'size': 18}, loc=1);
ax1.grid(True)
ax1.legend(prop={'size': 18}, loc='upper right')

ax2.grid(True)
ax2.legend(prop={'size': 18}, loc='lower right')


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
