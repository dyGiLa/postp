import numpy as np
import matplotlib.pyplot as plt

from linePlotData_harvester import linePlotData_harvester

# -------------------------------------------------
#  parameters
# -------------------------------------------------
image_file = '/home/heidi/Pictures/DenityPlot-2-Axx-LowHalf-0--5.png'
cbar_file = '/home/heidi/Pictures/colorbar-1.png'
plot_box = (0,874,0,178)
cbar_box = (0, 67, 0, 615)
cValues = (0.9, 1.12)
x_range = (-11.77897574, 11.77897574)
y_range = (-5.,0.)
output_csv = 'DP-2-x-11.77-y-5.csv'
orientation = 'vertical'

slice_axis = 'y'
slice_coord = -4.5

# -------------------------------------------------
# line data harvesting
# -------------------------------------------------

lineCoord, lineDataArray = linePlotData_harvester(
    image_file,
    cbar_file,
    plot_box,
    cbar_box,
    cValues,
    x_range,
    y_range,
    output_csv,
    slice_axis,
    slice_coord,
    orientation    
)
# -------------------------------------------------
# Plot
# -------------------------------------------------
fig, ax = plt.subplots()

ax.plot(lineCoord, lineDataArray, lw=2)
# ax.set_xlabel(xlabel)
# ax.set_ylabel("value")
# ax.set_title(f"1D slice at {label}")
ax.grid(True)

plt.show()

