import pandas as pd
import matplotlib.pyplot as plt
import os

root_dir = '/home/heidi/ReHD3/dyGiLa-project/project_462000960/heterogenouos-quench/rect-cub-1024-1024-256/p-5.5bar-T0-0.80-0.96/bt-0.000001/'
BPhaseSeedingProbCSV = 'BPhase-Seeding-prob_T0-0.80-0.96.csv'
# Read CSV
CSV_Path = os.path.join(root_dir, BPhaseSeedingProbCSV)
df = pd.read_csv(CSV_Path, skipinitialspace=True)

############################################################
#                   plot params sets                       #
############################################################

LineWidth=3.5
zeroTol = 6e-2

# plot line color
lineColors = [
    (0.121, 0.466, 0.705),  # Blue
    (1.000, 0.498, 0.054),  # Orange
    (0.172, 0.627, 0.172),  # Green
    (0.839, 0.153, 0.157),  # Red
    (0.580, 0.404, 0.741),  # Purple
    (0.549, 0.337, 0.294),  # Brown
    (0.890, 0.467, 0.761),  # Pink
    (0.498, 0.498, 0.498),  # Gray
    (0.737, 0.741, 0.133),  # Olive
    (0.090, 0.745, 0.811),  # Cyan
]
# line styles
line_styles = ['-', '--', ':', '-.', (0, (5, 10)), (0, (3, 2, 1, 2, 1, 2)) ]

# plot marker sizes
s=[50, 70, 90, 110]

############################################################
#             plot every E0 prob array                     #
############################################################

# ambient temperature T0
T0Array=[0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96]

fig, ax = plt.subplots(1,1,figsize=(12, 7));

# Plot every row
for idx, row in df.iterrows():
    E0_Value = row["E0"]
    probE0_Values = row[1:]

    ax.plot(T0Array, probE0_Values, linestyle=line_styles[1], color=lineColors[idx % 10])
    ax.scatter(T0Array, probE0_Values,
           marker='o', s=s[0], color=lineColors[idx % 10],
           label=fr'$E_{{0}}={E0_Value}eV$')

    
ax.set_xlabel(r'$T_{ambient}/T_c$',fontsize = 26.0)
ax.set_ylabel(r'B-phase Seeding Probability',fontsize = 26.0)
ax.set_xlim(0.8, 0.97)    
ax.set_ylim(-0.1, 1.5)


# Enable minor ticks
ax.minorticks_on()
# Show major grid
ax.grid(True, which='major', linestyle='-', linewidth=0.8)
# Show minor grid
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
# Set major tick label size
ax.tick_params(axis='both', which='major', labelsize=30)

# Legend
ax.legend(prop={'size': 16}, loc='best', ncol=4,
          columnspacing=0.6,   # space between columns
          handletextpad=0.3,   # space between line and text
          borderpad=0.2,       # padding inside legend box
          labelspacing=0.2)    # vertical spacing

# Title
ax.set_title(fr'$p_{{tHB}}$, $5.5$ bar $30mT$')

fig.subplots_adjust(left=0.15, bottom=0.18)  # space for labels

# Create a unique filename based on path
    
plot_name = 'B-phase-Seeding-probability-p5.5-H30mT-T0-0.80-0.96.png'
output_path = os.path.join(root_dir, plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)
# plt.close(fig1)
plt.close(fig)

