import pandas as pd
import numpy as np

import glob
import os
import re

import sys
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as sc

import matplotlib.pyplot as plt

# >>>>>>>>>>>>>>>             README, pls          <<<<<<<<<<<<<<< #

'''This script is used for plot B-phase Rc vs t
''' 

# >>>>>>>>>>>>> load the *csv files into numpy array <<<<<<<<<<<<< #

# Base directory to start searching
base_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-pyhton-plot-tools/thin-wall-B-phase-critical-radius-data/'

# Recursively find all txt files
# csv_files = glob.glob(os.path.join(base_dir, '**', 'critical_radius_vs_t_22.00bar.txt'), recursive=True)
csv_files = glob.glob(os.path.join(base_dir, '**', '*.csv'), recursive=True)

print("csv_files ", csv_files)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>   parampeters definations  <<<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# p = 23 # bar
# Tcp = sc.Tcp_mK(p) # mK at 26 bar

LineWidth=3.5
zeroTol = 6e-2

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

# regular expression
# re_pattern = r"critical_radius_vs_t_(\d+\.\d+|\.?\d+)bar\.csv"
re_pattern = r"critical_radius_vs_t_([0-9]*\.?[0-9]+)bar\.csv"


fig2, ax2 = plt.subplots(1,1,figsize=(12, 7));
color_idx = 0


for csv_path in csv_files:

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>>>>>>>>> extract quench time tauQ <<<<<<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

    # Extract the subA directory name from the path
    parts = csv_path.split(os.sep)
    print("parts is ", parts)
    
    # Make sure we don't go out of bounds (e.g., subA is the 4th or 5th level depending on your tree)
    # ptauQ_dir = None
    for part in parts:
        # Find a directory name that starts with 'subA' and contains a number
        print("part is ", part)
        match = re.search(re_pattern, part)
        print("match is ", match)
        if match:
            pressure = match.group(1)
            print("pressure ", pressure)
            break
    else:
        print(f"Could not find pressure number in path: {csv_path}")
        continue

    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# >>>>>>>>> Check the first few rows (optional) <<<<<<<<<< #
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
    # Read the txt
    df = pd.read_csv(csv_path, delim_whitespace=True, quotechar='"')
    
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# # >>>>>>>>>>>>>     phase Marker plot      <<<<<<<<<<<<<<< #
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

    ax2.plot(df["t"], df["Rc"], linewidth=LineWidth, label=fr'$p={pressure}$ bar', linestyle=line_styles[0], color=lineColors[color_idx])
    color_idx += 1
   
    ax2.set_xlabel(r'$t/t^{0}_{GL}$',fontsize = 26.0)
    ax2.set_ylabel(r'$R_{{C}}/nm$',fontsize = 26.0)
    ax2.set_xlim(0.5, 1.0)    
    ax2.set_ylim(0, 5000)
    ax2.tick_params(axis='both', which='major', labelsize=30)
    # ax2.legend(prop={'size': 18}, bbox_to_anchor=(1.0, 0.5), loc='right')
    ax2.legend(prop={'size': 18}, loc='best')    
    ax2.grid(True)

    fig2.subplots_adjust(left=0.15, bottom=0.18)  # space for labels

# Create a unique filename based on path
relative_path = os.path.relpath(csv_path, base_dir)
print("relative_path : ", relative_path)
    
plot_name = relative_path.replace(os.sep, '-').replace('.csv', '.png')
output_path = os.path.join(base_dir, 'Rc-plot', plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig2.savefig(output_path, dpi=300, pad_inches=0.01)

plt.close(fig2)    

