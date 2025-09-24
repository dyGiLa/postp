import os
import glob
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Root directory where your RSeed-* folders are located
root_dir = '/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/lumi-project_462000960/project_462000960/heterogenouos-quench/cube-512/H-30mT/p-5.5bar-T0-0.5-0.95/E0-80eV'

# Pattern to find all pv.csv files
pattern = os.path.join(root_dir, "RSeed-*-T0-0.5-0.95", "p-5.5-T1-0.760615", "stats", "phaseVolume-stream.csv")

# Get list of matching files
csv_files = glob.glob(pattern)

# 5.5 physics parameters
xi0GLp=26.29543017470303 # nm
thinwall_Rc = 587.2193436960276 # nm

# Extended plot line color palette (10 colors)
lineColors = [
    (0.000, 0.450, 0.700),  # Blue
    (0.000, 0.675, 0.937),  # Cyan (replaces Rust)
    (0.000, 0.620, 0.450),  # Teal
    (0.580, 0.404, 0.741),  # Purple
    (0.870, 0.560, 0.050),  # Gold
    (0.400, 0.760, 0.647),  # Seafoam
    (0.850, 0.325, 0.098),  # Vermilion (Red)
    (0.800, 0.475, 0.655),  # Pink
    (0.565, 0.933, 0.133),  # Lime Green
    (0.337, 0.706, 0.914)   # Sky Blue
]

LineWidth=3.5

# line styles
line_styles = ['-', '--', ':', '-.', (0, (5, 10)), (0, (3, 2, 1, 2, 1, 2)) ]

# B-phase occupation failed
failure_threshold = 0.99

# Counter for condition Vratio_p9_acc > failure_threshold
count_Vratio_p9_gt_FT = 0
total_samples = 0

##############################
# Plot V_p5_acc along time t #
##############################
fig, ax = plt.subplots(1,1,figsize=(12, 11));
RSeed_counter = 0

for csv_file in csv_files:
    print("RSeed_counter is ", RSeed_counter, ", current csv_file is ", csv_file, "\n")
    try:
        df = pd.read_csv(csv_file)
        if not df.empty:
            
            # make event 6, which is RSeed 4702 distinguishble from RSeeed 1728
            if RSeed_counter == 6:
                ax.plot(df["t"], df["V_p5_acc"], linewidth=LineWidth, label=fr'$Vol_{{B}}\,,RandS \#{RSeed_counter}$', linestyle=line_styles[1], color=lineColors[RSeed_counter])
            else:
                ax.plot(df["t"], df["V_p5_acc"], linewidth=LineWidth, label=fr'$Vol_{{B}}\,,RandS \#{RSeed_counter}$', linestyle=line_styles[0], color=lineColors[RSeed_counter])
                            
        RSeed_counter += 1    
            
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

# spherical thin wall critical bubble volume
ax.axhline(y=(4/3)*np.pi*((thinwall_Rc/xi0GLp)**3), label='Thin-Wall critic volume', color='black', linestyle='-.', linewidth=4)

# Actully criticl volume
ax.axhline(y=4683.88, label='critic volume', color='red', linestyle='-.', linewidth=4)  

ax.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 26.0)
ax.set_ylabel(r'B-phase Single-Bubble or Clusters Volume/$(\xi^{0}_{GL})^3$',fontsize = 26.0)
ax.set_xlim(0.0, 2000.0)
# ax.set_xlim(1e-2, 2e3)
# ax.set_xscale('log')
ax.set_ylim([1e-1, 2e7])
ax.set_yscale('log')
ax.tick_params(axis='both', which='major', labelsize=30)

ax.legend(prop={'size': 18}, loc='best')    
ax.grid(True)

fig.subplots_adjust(left=0.15, bottom=0.18)  # space for labels
    
plot_name = 'B-phase-Bubble-Beheavior-E0-80eV-blobR-1.068um-AllSamples.png'
output_path = os.path.join(root_dir, plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)

plt.close(fig)
#plt.show()
