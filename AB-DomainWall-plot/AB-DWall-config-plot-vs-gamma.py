import pandas as pd
import matplotlib.pyplot as plt
import glob
import re

# plot line color
lineColors = [
    (0.121, 0.466, 0.705),  # Blue
    (1.000, 0.498, 0.054),  # Orange
    (0.172, 0.627, 0.172),  # Green
    (0.839, 0.153, 0.157),  # Red
    (0.580, 0.404, 0.741),  # Purple
    (0.549, 0.337, 0.294),   # Brown
    (0.05, 0.05, 0.20)      # Dark Navy
]

# line styles
line_styles = ['-', '--', ':', '-.', (0, (5, 10)), (0, (3, 2, 1, 2, 1, 2)) ]

LineWidth=3.5

# x-coord shift
x_shift=25.5

# Find all CSV files
files = sorted(glob.glob("AB-DWall-28bar-TAB-gamma-*-1000tGL.csv"))

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Regex to extract gamma value
gamma_pattern = re.compile(r"AB-DWall-28bar-TAB-gamma-([0-9]+\.?[0-9]*)-")

for file_path in files:
    # Extract gamma from filename
    filename = file_path.split('/')[-1]  
    match = gamma_pattern.search(filename)
    if not match:
        raise ValueError(f"Could not extract gamma from {filename}")
    
    gamma = float(match.group(1))
    
    # Read csv data
    df = pd.read_csv(file_path)
    
    ax.plot(df["Points:0"]-x_shift, df["gapA"],
            linewidth=LineWidth, 
            label=fr'$\sqrt{{A^{{\dagger}}A}}\,,\gamma = {gamma}$',
            linestyle=line_styles[0], color=lineColors[0])

    ax.plot(df["Points:0"]-x_shift, df["u11"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{11}}\,,\gamma = {gamma}$',
            linestyle=line_styles[1], color=lineColors[1])
    
    ax.plot(df["Points:0"]-x_shift, df["u22"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{22}}\,,\gamma = {gamma}$',
            linestyle=line_styles[2], color=lineColors[2])

    ax.plot(df["Points:0"]-x_shift, df["u33"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{33}}\,,\gamma = {gamma}$',
            linestyle=line_styles[3], color=lineColors[3])

    ax.plot(df["Points:0"]-x_shift, df["v12"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{12}}\,,\gamma = {gamma}$',
            linestyle=line_styles[0], color=lineColors[4])

    ax.plot(df["Points:0"]-x_shift, df["v21"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{21}}\,,\gamma = {gamma}$',
            linestyle=line_styles[3], color=lineColors[5])
        
# Beautify the plot
ax.set_xlabel(r"$x/\xi^0_{GL}$", fontsize=14)
ax.set_ylabel(r"$X/k_B T_C$", fontsize=14)
ax.set_title(fr"AB Domain Wall configuration at ${{28}}$bar from dyGiLa", fontsize=16, pad=15)
ax.legend(fontsize=13, title_fontsize=14)
ax.grid(True, alpha=0.9, linestyle='-')

plt.tight_layout()
plt.show()
