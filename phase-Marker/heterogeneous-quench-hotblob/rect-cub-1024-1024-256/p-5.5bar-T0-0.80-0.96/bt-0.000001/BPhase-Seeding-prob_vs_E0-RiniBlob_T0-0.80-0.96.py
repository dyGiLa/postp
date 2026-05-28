import os
import re
import glob
import csv
from collections import defaultdict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


############################################################
# CONFIG
############################################################

ROOT_DIR = "/home/heidi/ReHD3/dyGiLa-project/project_462000960/heterogenouos-quench/rect-cub-1024-1024-256/p-5.5bar-T0-0.80-0.96/bt-0.000001"

# fixed T0 mapping
T0_VALUES = [0.80, 0.82, 0.84, 0.86, 0.88,
             0.90, 0.92, 0.94, 0.96]

# plotting marker sizes
MARKER_SIZE = 70


############################################################
# STORAGE
############################################################

# Structure:
#
# data_by_T0[T0][R_iniBlob_um] = list of dictionaries
#
# each dictionary corresponds to ONE statistical try
#
# {
#     "p9VR": ...,
#     "p5VR": ...,
#     "p9VSpeed": ...,
#     "p5VSpeed": ...
# }

data_by_T0 = defaultdict(lambda: defaultdict(list))

# maps R_iniBlob_um -> E0
R_to_E0 = {}

############################################################
# FIND ALL phaseVolume-stream.csv FILES
############################################################

pattern = os.path.join(
    ROOT_DIR,
    "E0-*eV",
    "RSeed-*-T0-0.80-0.96",
    "p-5.5-T1-*",
    "stats",
    "phaseVolume-stream.csv"
)

csv_files = glob.glob(pattern)

print("\nFound CSV files =", len(csv_files))


############################################################
# PROCESS EACH FILE
############################################################

for csv_file in csv_files:

    try:

        print("\nProcessing:")
        print(csv_file)

        ####################################################
        # Read CSV
        ####################################################

        df = pd.read_csv(csv_file)

        if df.empty:
            print("Empty CSV, skipping.")
            continue

        ####################################################
        # Extract T1 from folder name
        ####################################################

        # path:
        # .../p-5.5-T1-2.24277/stats/phaseVolume-stream.csv

        p_dir = os.path.basename(
            os.path.dirname(
                os.path.dirname(csv_file)
            )
        )

        T1_str = p_dir.replace("p-5.5-T1-", "")
        T1_val = float(T1_str)
        print("T1_val: ", T1_val)

        ####################################################
        # Extract E0 folder
        ####################################################

        # .../E0-450eV/... /E0-512.5/...

        parts = csv_file.split(os.sep)

        E0_folder = None

        for p in parts:
            if re.match(r"E0-\d+\.?\d*eV", p):
                E0_folder = p
                break

        if E0_folder is None:
            print("Cannot find E0 folder.")
            continue

        print("E0_folder: ", E0_folder)
        ####################################################
        # Extract numeric E0
        ####################################################

        match_E0 = re.search(r"E0-(\d+\.?\d*)eV", E0_folder)
        print("match_E0: ", match_E0)
        print("match_E0.group(): ", match_E0.group())

        if match_E0 is None:
            print("Cannot parse E0.")
            continue

        E0_value = float(match_E0.group(1))
        print("E0_value: ", E0_value)

        ####################################################
        # Collect all T1 folders under same E0
        ####################################################

        t1_pattern = os.path.join(
            ROOT_DIR,
            E0_folder,
            "RSeed-*-T0-0.80-0.96",
            "p-5.5-T1-*"
        )

        t1_dirs = glob.glob(t1_pattern)

        unique_T1 = set()

        for d in t1_dirs:

            dname = os.path.basename(d)

            try:
                t1_tmp = float(
                    dname.replace("p-5.5-T1-", "")
                )
                unique_T1.add(t1_tmp)

            except:
                pass

        unique_T1 = sorted(unique_T1)

        ####################################################
        # Map T1 -> T0 index
        ####################################################

        if T1_val not in unique_T1:
            print("T1 not found in unique_T1")
            continue

        T1_index = unique_T1.index(T1_val)

        if T1_index >= len(T0_VALUES):
            print("T1 index exceeds T0 mapping.")
            continue

        T0 = T0_VALUES[T1_index]

        ####################################################
        # Extract R_iniBlob_um
        ####################################################

        R_iniBlob_um = float(df.iloc[0]["R_iniBlob_um"])
        R_to_E0[R_iniBlob_um] = E0_value

        ####################################################
        # Last values
        ####################################################

        p9VR = df.iloc[-1]["Vratio_p9_acc"]
        p5VR = df.iloc[-1]["Vratio_p5_acc"]

        ####################################################
        # Compute speeds
        ####################################################

        dt = df["t"].iloc[1] - df["t"].iloc[0]

        dVrp9dt = np.gradient(df["Vratio_p9_acc"].values, dt)
        dVrp5dt = np.gradient(df["Vratio_p5_acc"].values, dt)

        p9VSpeed = dVrp9dt[-1]
        p5VSpeed = dVrp5dt[-1]

        ####################################################
        # Save
        ####################################################

        data_by_T0[T0][R_iniBlob_um].append({

            "p9VR": p9VR,
            "p5VR": p5VR,
            "p9VSpeed": p9VSpeed,
            "p5VSpeed": p5VSpeed

        })

    except Exception as e:

        print(f"Failed on {csv_file}")
        print(e)

print("data_by_T0: ", data_by_T0)
print("data_by_T0.keys: ", data_by_T0.keys)
print("R_to_E0: ", R_to_E0)
############################################################
# CALCULATE PROBABILITIES
############################################################

# probability_by_T0[T0] = [(R, prob), ...]
probability_by_T0 = defaultdict(list)

for T0 in sorted(data_by_T0.keys()):

    print("\n")
    print("================================================")
    print("Processing T0 =", T0)
    print("================================================")

    R_values = sorted(data_by_T0[T0].keys())
    print("R_values: ", R_values)

    for R in R_values:

        tries = data_by_T0[T0][R]

        p9VR = np.array([x["p9VR"] for x in tries])
        p5VR = np.array([x["p5VR"] for x in tries])

        p9VSpeed = np.array([x["p9VSpeed"] for x in tries])
        p5VSpeed = np.array([x["p5VSpeed"] for x in tries])

        ####################################################
        # YOUR FILTERS
        ####################################################
        tol = 1e-12
        
        # case of A-phase decay
        # BSucSeedingFilter1 = (
        #     (p9VR != 0.) &
        #     (p5VR != 0.) &
        #     (p9VSpeed < 0.) &
        #     (p5VSpeed > 0.)
        # )

        BSucSeedingFilter1 = (
            (np.abs(p9VR) > tol) &
            (np.abs(p5VR) > tol) &
            (p9VSpeed < 0.) &
            (p5VSpeed > 0.)
        )

        
        # # case of A-phase eliminated
        # BSucSeedingFilter2 = (
        #     (p9VR == 0.) &
        #     (p5VR != 0.) &
        #     (p9VSpeed == 0.)
        # )

        # # case of A-phase eliminated but moving
        # BSucSeedingFilter3 = (
        #     (p9VR == 0.) &
        #     (p5VR != 0.) &
        #     (p9VSpeed < 0.)
        # )

        # case of A-phase eliminated
        BSucSeedingFilter2 = (
            (np.abs(p9VR) < tol) &
            (np.abs(p5VR) > tol) &
            (np.abs(p9VSpeed) < tol)
        )

        # case of A-phase eliminated but moving
        BSucSeedingFilter3 = (
            (np.abs(p9VR) < tol) &
            (np.abs(p5VR) > tol) &
            (p9VSpeed < 0.)
        )
        
        # unusual B-phase defects
        # BSucSeedingFilter4 = (
        #     (p9VR != 0.) &
        #     (p5VR != 0.) &
        #     ((p9VSpeed * p5VSpeed) > 0.)
        # )

        BSucSeedingFilter4 = (
            (np.abs(p9VR) > tol) &
            (np.abs(p5VR) > tol) &
            ((p9VSpeed * p5VSpeed) > 0.)
        )
        
        ####################################################
        # COUNT EVENTS
        ####################################################

        eventCountFilter1 = np.sum(BSucSeedingFilter1)
        eventCountFilter2 = np.sum(BSucSeedingFilter2)
        eventCountFilter3 = np.sum(BSucSeedingFilter3)
        eventCountFilter4 = np.sum(BSucSeedingFilter4)

        BSucEventsCount = (
            eventCountFilter1 +
            eventCountFilter2 +
            eventCountFilter3 +
            eventCountFilter4
        )

        numOfTry = len(tries)

        prob = (
            BSucEventsCount / numOfTry
            if numOfTry > 0 else 0
        )

        ####################################################
        # PRINT DEBUG INFORMATION
        ####################################################

        print("\n")
        print("================================================")
        print(f"T0 = {T0:.2f}")
        print(f"R_iniBlob_um = {R}")
        print("================================================")

        print("\n")
        print("p9VR =")
        print(p9VR)

        print("\n")
        print("p5VR =")
        print(p5VR)

        print("\n")
        print("p9VSpeed =")
        print(p9VSpeed)

        print("\n")
        print("p5VSpeed =")
        print(p5VSpeed)

        ####################################################
        # PRINT FILTER CONTENTS
        ####################################################

        print("\n")
        print("BSucSeedingFilter1 =")
        print(BSucSeedingFilter1)

        print("\n")
        print("BSucSeedingFilter2 =")
        print(BSucSeedingFilter2)

        print("\n")
        print("BSucSeedingFilter3 =")
        print(BSucSeedingFilter3)

        print("\n")
        print("BSucSeedingFilter4 =")
        print(BSucSeedingFilter4)

        ####################################################
        # PRINT COUNTS
        ####################################################

        print("\n")
        print("eventCountFilter1 =", eventCountFilter1)

        print("eventCountFilter2 =", eventCountFilter2)

        print("eventCountFilter3 =", eventCountFilter3)

        print("eventCountFilter4 =", eventCountFilter4)

        print("\n")
        print("BSucEventsCount =", BSucEventsCount)

        print("numOfTry =", numOfTry)

        print("probability =", prob)

        print("\n")
        ####################################################
        # SAVE
        ####################################################

        probability_by_T0[T0].append((R, prob))


############################################################
# SAVE CSV FILES
############################################################

output_csv_dir = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Probability_CSV"
)

os.makedirs(output_csv_dir, exist_ok=True)

for T0 in sorted(probability_by_T0.keys()):

    csv_path = os.path.join(
        output_csv_dir,
        f"BSucSeedingProbability-T0-{T0:.2f}.csv"
    )

    with open(csv_path, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "E0_value",
            "R_iniBlob_um",
            "BSucSeedingProbability"
        ])

        for R, prob in sorted(probability_by_T0[T0]):

            writer.writerow([R_to_E0[R], R, prob])

    print("\nSaved:", csv_path)


############################################################
# PLOT
############################################################

fig, ax = plt.subplots(figsize=(12, 8))

colors = [
    'red',
    'blue',
    'black',
    'magenta',
    'darkorange',
    'darkcyan',
    'purple',
    'brown',
    'deeppink'
]

for i, T0 in enumerate(sorted(probability_by_T0.keys())):

    data = sorted(probability_by_T0[T0])

    R_vals = [x[0] for x in data]
    probs = [x[1] for x in data]

    ax.plot(
        R_vals,
        probs,
        linestyle='--',
        color=colors[i]
    )

    ax.scatter(
        R_vals,
        probs,
        s=MARKER_SIZE,
        color=colors[i],
        label=fr'$T_0={T0:.2f}T_c$'
    )

############################################################
# LABELS
############################################################

ax.set_xlabel(
    r'$R_{iniBlob}/\mu m$',
    fontsize=24
)

ax.set_ylabel(
    r'B-phase Seeding Probability',
    fontsize=24
)

ax.set_title(
    "B-phase Seeding Prob vs. Radius of Ini-Blob within $3.23 \mu m$ Slab",
    fontsize=18,
    pad=20
)

ax.set_ylim(-0.05, 1.05)

ax.minorticks_on()

ax.grid(
    True,
    which='major',
    linestyle='-',
    linewidth=0.8
)

ax.grid(
    True,
    which='minor',
    linestyle=':',
    linewidth=0.5,
    color='gray'
)

ax.tick_params(
    axis='both',
    which='major',
    labelsize=18
)

# ax.legend(
#     prop={'size': 14},
#     loc='best'
# )

handles, labels = ax.get_legend_handles_labels()

if len(handles) > 0:
    ax.legend(
        handles,
        labels,
        prop={'size': 14},
        loc='best'
    )

fig.subplots_adjust(
    left=0.15,
    bottom=0.15,
    top=0.80
)
    
############################################################
# SAVE FIGURE
############################################################
plot_name = os.path.join(
    ROOT_DIR,
    "BSucSeedingProbability_vs_RiniBlob.png"
)


fig.savefig(
    plot_name,
    dpi=300,
    pad_inches=0.02
)

plt.close(fig)

print("\nSaved plot:")
print(plot_name)

############################################################
# INDIVIDUAL T0 PLOTS
############################################################

individual_plot_dir = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Probability_vs_RiniBlob_T0-0.80-0.96"
)

os.makedirs(individual_plot_dir, exist_ok=True)

# use same colors as combined plot
plot_colors = [
    'red',
    'blue',
    'black',
    'magenta',
    'darkorange',
    'darkcyan',
    'purple',
    'brown',
    'deeppink'
]

for i, T0 in enumerate(sorted(probability_by_T0.keys())):

    fig_single, ax_single = plt.subplots(
        figsize=(12, 8)
    )

    data = sorted(probability_by_T0[T0])

    R_vals = [x[0] for x in data]
    probs = [x[1] for x in data]

    color = plot_colors[i % len(plot_colors)]

    ########################################################
    # plot
    ########################################################

    ax_single.plot(
        R_vals,
        probs,
        linestyle='--',
        linewidth=2,
        color=color
    )

    ax_single.scatter(
        R_vals,
        probs,
        s=MARKER_SIZE,
        color=color,
        label=fr'$T_0={T0:.2f}$'
    )

    ########################################################
    # labels
    ########################################################

    ax_single.set_xlabel(
        r'$R_{iniBlob}\ [\mu m]$',
        fontsize=24
    )

    ax_single.set_ylabel(
        r'B-phase Seeding Probability',
        fontsize=24
    )

    ax_single.set_ylim(-0.05, 1.05)

    ax_single.minorticks_on()

    ax_single.grid(
        True,
        which='major',
        linestyle='-',
        linewidth=0.8
    )

    ax_single.grid(
        True,
        which='minor',
        linestyle=':',
        linewidth=0.5,
        color='gray'
    )

    ax_single.tick_params(
        axis='both',
        which='major',
        labelsize=18
    )

    ax_single.legend(
        prop={'size': 18},
        loc='best'
    )

    fig_single.subplots_adjust(
        left=0.15,
        bottom=0.15
    )

    ########################################################
    # save
    ########################################################

    single_plot_path = os.path.join(
        individual_plot_dir,
        f"BSucSeedingProbability_vs_RiniBlob_T0-{T0:.2f}.png"
    )

    fig_single.savefig(
        single_plot_path,
        dpi=300,
        pad_inches=0.02
    )

    plt.close(fig_single)

    print("\nSaved:")
    print(single_plot_path)
