import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, rfft, fftfreq, fftshift

# >>>>>>>>>>>>>>>             README, pls          <<<<<<<<<<<<<<< #

'''This script is used for vatulazation the stats/*csv files 

generated by dyGiLa write_energies() func.
''' 

# >>>>>>>>>>>>> load the *csv files into numpy array <<<<<<<<<<<<< #

t=2*np.pi*np.arange(0,2,0.01)
print(t.size)

x=np.sin(t)
y=np.cos(2*t)
z=x+y

LineWidth = 3.5
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>   parampeters definations  <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

fig1, ax1 = plt.subplots(1,1)

ax1.plot(t,x,linewidth=LineWidth, label=r'$sin(x)$', linestyle='solid', color=(0, 0, 1.0))
ax1.plot(t,y,linewidth=LineWidth, label=r'$cos(2x)$', linestyle='solid', color=(1.0, 0, 0.0))
ax1.plot(t,z,linewidth=LineWidth, label=r'$sinx+cosx$', linestyle='solid', color=(0.0, 1.0, 0.0))

ax1.grid()
ax1.legend(prop={'size': 18}, bbox_to_anchor=(1.0, 1.0), loc='upper right')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>          gap \sqrt{A^dagger.A} FFT plot           <<#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# # FFT operations
# sp = fftshift(fft(Deltat_pick))
# #print(spDup.shape)

# freqNP = fftshift(fftfreq(t_pick.shape[-1]))
# #print(freqNP.shape)

# index_Pos_freq = np.where(freqNP >= 0)[0][0]
# freq = freqNP[index_Pos_freq:]
# sp   = spDup[index_Pos_freq:]
# #print(freqNP)
# #print(abs(sp))
# ax1.semilogy(freq, np.abs(sp), linewidth=LineWidth, label=r'$<\Delta>(\nu),\tau_{Q}=1550t_{GL}}$', linestyle='solid', color=(0, 0, 1.0))


###################
fig2, ax2 = plt.subplots(1,1)


# FFT operations
aspx = fftshift(fft(x))
aspy = fftshift(fft(y))
aspz = fftshift(fft(z))
#print(spDup.shape)

freq = fftshift(fftfreq(t.shape[0],0.01))
print(freq)

# index_Pos_freq = np.where(freqNP >= 0)[0][0]
# freq = freqNP[index_Pos_freq:]
# sp   = spDup[index_Pos_freq:]
#print(freqNP)
#print(abs(sp))
ax2.semilogy(freq, np.abs(aspx), linewidth=LineWidth, label=r'$fftx$', linestyle='solid',marker='D', color=(0.0, 0.0, 1.0))
ax2.semilogy(freq, np.abs(aspy), linewidth=LineWidth, label=r'$ffty$', linestyle='solid',marker='D', color=(1.0, 0.0, 0.0))
ax2.semilogy(freq, np.abs(aspz), linewidth=LineWidth, label=r'$fftz$', linestyle='solid',marker='D', color=(0.0, 1.0, 0.0))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>>>>>  bulk fft plots <<<<<<<<<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #


ax2.set_xlabel(r'$\nu$',fontsize = 26.0)
ax2.set_ylabel(r'$|fft|$',fontsize = 26.0)
# ax1.tick_params(axis='both', which='major', labelsize=30)
ax2.legend(prop={'size': 18}, bbox_to_anchor=(1.0, 1.0), loc='upper right')

ax2.grid(True)

plt.show()
