import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Root directory where RSeed-* folders are located
root_dir = '/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-blob-quenches-Hfield/lum-runs/lumi-G/project_462000960/heterogenouos-quench/cube-512/H-30mT/p-5.5bar'

# Base glob pattern to match all pv.csv files under RSeed-* folders
pattern = os.path.join(root_dir, "RSeed-*-T1-0.81-2.77-t1-0.005", "p-5.5-T1-*", "stats", "phaseVolume-stream.csv")
csv_files = glob.glob(pattern)

# plot marker sizes
s=[50, 70, 90, 110]

# B-phase occupation failed
failure_threshold = 0.99

# Dictionary to hold d3 values per yyy#
p9CSV_last_by_T1 = defaultdict(list)

for csv_file in csv_files:
    try:
        # Extract T1 from folder name: "p-5.5-T1-#"
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
        T1Val_str = parent_dir.replace("p-5.5-T1-", "")
        T1Val_val = float(T1Val_str)

        df = pd.read_csv(csv_file)
        if not df.empty:
            p9CSV_last = df.iloc[-1]["Vratio_p9_acc"]
            p9CSV_last_by_T1[T1Val_val].append(p9CSV_last)
    except Exception as e:
        print(f"Failed on {csv_file}: {e}")

# Compute probability for each T1 value
T1_values = sorted(p9CSV_last_by_T1.keys())
probabilities = []

for T1 in T1_values:
    p9CSV_vals = p9CSV_last_by_T1[T1]
    count = sum(p9CSV > failure_threshold for p9CSV in p9CSV_vals)
    total = len(p9CSV_vals)
    prob = (1-(count / total)) if total > 0 else 0
    probabilities.append(prob)

    
# Plotting

fig, ax = plt.subplots(1,1,figsize=(12, 7));

E0Array=np.array([80, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])

ax.plot(E0Array, probabilities, linestyle='--', color='red')
ax.scatter(E0Array, probabilities, marker='o', s=s[2], color='blue', label=fr'B-phase winning prob, 5.5 bar 30mT, $T_{{des}}=0.7T_c$ ')

ax.set_xlabel(r'Injected Heat $E_0/eV$',fontsize = 26.0)
ax.set_ylabel(r'Probability',fontsize = 26.0)
ax.set_xlim(0, 1000)    
ax.set_ylim(-0.1, 1.2)


# Enable minor ticks
ax.minorticks_on()
# Show major grid
ax.grid(True, which='major', linestyle='-', linewidth=0.8)
# Show minor grid
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
# Set major tick label size
ax.tick_params(axis='both', which='major', labelsize=30)

# Legend
ax.legend(prop={'size': 18}, loc='best')

fig.subplots_adjust(left=0.15, bottom=0.18)  # space for labels

# Create a unique filename based on path
    
plot_name = 'B-phase-winning-probability.png'
output_path = os.path.join(root_dir, plot_name)
print("output_path : ", output_path)
        
# Ensure output directory exists, only gets the folder part
os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)
# plt.close(fig1)
plt.close(fig)
