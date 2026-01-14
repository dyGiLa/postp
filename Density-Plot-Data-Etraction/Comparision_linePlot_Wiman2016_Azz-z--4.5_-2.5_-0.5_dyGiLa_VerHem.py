import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from linePlotData_harvester import linePlotData_harvester

# plot line color
lineColors = [
    (0.121, 0.466, 0.705),  # Blue
    (1.000, 0.498, 0.054),  # Orange
    (0.172, 0.627, 0.172),  # Green
    (0.839, 0.153, 0.157),  # Red
    (0.580, 0.404, 0.741),  # Purple
    (0.549, 0.337, 0.294),   # Brown
    (0.05, 0.05, 0.20),      # Dark Navy
    (0., 0., 0.)            # Black
]

# line styles
line_styles = ['-', '--', ':', '-.', (0, (5, 10)), (0, (3, 2, 1, 2, 1, 2)) ]

LineWidth=3.5
LineWidth2=2.0

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

#------------------------------------------------------------#
#------ plot data from Wiman2016 DP RGB csv file ------------#
#------------------------------------------------------------#

image_file = '/home/heidi/Pictures/DenityPlot-3-Azz-LowHalf-0--5.png'
cbar_file = '/home/heidi/Pictures/colorbar-2.png'
plot_box = (0,411,0,84)
cbar_box = (0, 22, 0, 205)
cValues = (-0.88648, 0.869189184)
x_range = (-11.77897574, 11.77897574)
y_range = (-5.,0.)
output_csv = 'DP-3-x--11.77xi0-11.77xi0-y--5xi0-0xi.csv'
orientation = 'vertical'

slice_axis = 'y'
slice_coord_n45 = -4.5
slice_coord_n25 = -2.5
slice_coord_n05 = -0.5

gamma = 5.0
# -------------------------------------------------
# line data harvesting
# -------------------------------------------------

# z = -4.5 lineDataarray
lineCoord_n45, lineDataArray_n45 = linePlotData_harvester(
    image_file,
    cbar_file,
    plot_box,
    cbar_box,
    cValues,
    x_range,
    y_range,
    output_csv,
    slice_axis,
    slice_coord_n45,
    orientation    
)

# z = -2.5 lineDataarray
lineCoord_n25, lineDataArray_n25 = linePlotData_harvester(
    image_file,
    cbar_file,
    plot_box,
    cbar_box,
    cValues,
    x_range,
    y_range,
    output_csv,
    slice_axis,
    slice_coord_n25,
    orientation    
)

# z = -0.5 lineDataarray
lineCoord_n05, lineDataArray_n05 = linePlotData_harvester(
    image_file,
    cbar_file,
    plot_box,
    cbar_box,
    cValues,
    x_range,
    y_range,
    output_csv,
    slice_axis,
    slice_coord_n05,
    orientation    
)


# plot
ax.plot(lineCoord_n45, lineDataArray_n45,
        linewidth=LineWidth, 
        label=fr'$A_{{zz}}$ Wiman2016 RGB Digitized, $z=-4.5\xi_0$',
        linestyle=line_styles[0], color=lineColors[7])

ax.plot(lineCoord_n25, lineDataArray_n25,
        linewidth=LineWidth, 
        label=fr'$A_{{zz}}$ Wiman2016 RGB Digitized, $z=-2.5\xi_0$',
        linestyle=line_styles[1], color=lineColors[7])

ax.plot(lineCoord_n05, lineDataArray_n05,
        linewidth=LineWidth, 
        label=fr'$A_{{zz}}$ Wiman2016 RGB Digitized, $z=-0.5\xi_0$',
        linestyle=line_styles[3], color=lineColors[7])


#------------------------------------------------------------#
#------      plot data from dyGiLa csv file      ------------#
#------------------------------------------------------------#
# x-axis 0 point
x0 = 25.1636906

dyGiLa_file_path_n45 = "./Wiman2016-dyGiLa-Azz-z--4.5xi0-x--11.01xi0-11.01xi0-t5000.csv"
dyGiLa_file_path_n25 = "./Wiman2016-dyGiLa-Azz-z--2.5xi0-x--11.01xi0-11.01xi0-t5000.csv"
dyGiLa_file_path_n05 = "./Wiman2016-dyGiLa-Azz-z--0.5xi0-x--11.01xi0-11.01xi0-t5000.csv"


# Read csv data
df_n45 = pd.read_csv(dyGiLa_file_path_n45)
df_n25 = pd.read_csv(dyGiLa_file_path_n25)
df_n05 = pd.read_csv(dyGiLa_file_path_n05)

# shift 0-point to x0
x_arr_dyGiLa_n45 = np.array(df_n45["Points:0"]) - x0
x_arr_dyGiLa_n25 = np.array(df_n25["Points:0"]) - x0
x_arr_dyGiLa_n05 = np.array(df_n05["Points:0"]) - x0

# ReA11 array
ReA11Array_n45 = np.array(df_n45["ReAxx"])
ReA11Array_n25 = np.array(df_n25["ReAxx"])
ReA11Array_n05 = np.array(df_n05["ReAxx"])

# plot
ax.plot(x_arr_dyGiLa_n45, ReA11Array_n45,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}\,,z=-4.5\xi_{{0}}$',
        linestyle=line_styles[0], color=lineColors[1])    

ax.plot(x_arr_dyGiLa_n25, ReA11Array_n25,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}\,,z=-2.5\xi_{{0}}$',
        linestyle=line_styles[1], color=lineColors[1])    

ax.plot(x_arr_dyGiLa_n05, ReA11Array_n05,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}\,,z=-0.5\xi_{{0}}$',
        linestyle=line_styles[3], color=lineColors[1])    



#------------------------------------------------------------#
#------      plot data from verhem csv file      ------------#
#------------------------------------------------------------#
# x-axis 0 point, -28.05
x0 = -27.9047394

verhem_file_path_n45 = "./Wiman2016-VerHem15MDoF-ReAzz-ZTScalingOnly-z--4.5xi0-x--11.77-to-11.77xi0-3e-13L2.csv"
verhem_file_path_n25 = "./Wiman2016-VerHem15MDoF-ReAzz-ZTScalingOnly-z--2.5xi0-x--11.77-to-11.77xi0-3e-13L2.csv"
verhem_file_path_n05 = "./Wiman2016-VerHem15MDoF-ReAzz-ZTScalingOnly-z--0.5xi0-x--11.77-to-11.77xi0-3e-13L2.csv"


# Read csv data
df_n45 = pd.read_csv(verhem_file_path_n45)
df_n25 = pd.read_csv(verhem_file_path_n25)
df_n05 = pd.read_csv(verhem_file_path_n05)

# shift 0-point to x0
x_arr_verhem_n45 = np.array(df_n45["Points:0"]) - x0
x_arr_verhem_n25 = np.array(df_n25["Points:0"]) - x0
x_arr_verhem_n05 = np.array(df_n05["Points:0"]) - x0

# ReA11 array
ReA11Array_n45 = np.array(df_n45["ReAaj"])
ReA11Array_n25 = np.array(df_n25["ReAaj"])
ReA11Array_n05 = np.array(df_n05["ReAaj"])

# plot
ax.plot(x_arr_verhem_n45, ReA11Array_n45,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,VerHem\,|residual|_{{L_2}}= 3e-13\,,z=-4.5\xi_{{0}}$',
        linestyle=line_styles[0], color=lineColors[2])    

ax.plot(x_arr_verhem_n25, ReA11Array_n25,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,VerHem\,|residual|_{{L_2}}= 3e-13\,,z=-2.5\xi_{{0}}$',
        linestyle=line_styles[1], color=lineColors[2])    

ax.plot(x_arr_verhem_n05, ReA11Array_n05,
        linewidth=LineWidth, 
        label=fr'$ReA_{{zz}}\,,VerHem\,|residual|_{{L_2}}= 3e-13\,,z=-0.5\xi_{{0}}$',
        linestyle=line_styles[3], color=lineColors[2])    

#------------------------------------------------------------#
#--------               Plot make up        -----------------#
#------------------------------------------------------------#


ax.set_xlabel(r"$x/\xi_0$", fontsize=26.0)
ax.set_ylabel(r"$ReA_{{zz}}/\frac{{\Delta_B}}{{\sqrt{{3}}}}$", fontsize=26.0)
ax.set_xlim(-11.77, 11.77)
ax.set_ylim(-1.0, 1.0)
ax.tick_params(axis='both', which='major', labelsize=30)
ax.set_title(fr"Wiman2016 Stripe B-phase at ${{3}}$bar ${{D=12\xi_{{0}}}}$ Compared with dyGiLa, VerHem's Results", fontsize=26, pad=15)
ax.legend(handlelength=3.2, fontsize=16, title_fontsize=14)
ax.grid(True, alpha=0.9, linestyle='-')

#plt.tight_layout()
plt.show()


