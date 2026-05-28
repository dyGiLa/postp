import os
import glob
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
import os

############################################################
# ADD LL_calculator MODULE PATH
############################################################

LL_CALCULATOR_DIR = os.path.expanduser(
    "~/Documents/GL-Calculator"
)

sys.path.append(LL_CALCULATOR_DIR)

############################################################
# IMPORT
############################################################

from Module_GLSCC_calculator import evetRateOfRHULSim as eventRate


from scipy.interpolate import interp1d

############################################################
# IMPORT YOUR EVENT RATE MODEL
############################################################

#from LL_calculator import eventRate

############################################################
# CONFIG
############################################################

ROOT_DIR = "/home/heidi/ReHD3/dyGiLa-project/project_462000960/heterogenouos-quench/rect-cub-1024-1024-256/p-5.5bar-T0-0.80-0.96/bt-0.000001"

CSV_DIR = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Probability_CSV"
)

############################################################
# FIND ALL PROBABILITY CSV FILES
############################################################

csv_files = sorted(
    glob.glob(
        os.path.join(
            CSV_DIR,
            "BSucSeedingProbability-T0-*.csv"
        )
    )
)

print("\nFound probability CSV files:")
for f in csv_files:
    print(f)

############################################################
# STORAGE
############################################################

T0_list = []
tau_list = []

############################################################
# PROCESS EACH T0
############################################################

for csv_path in csv_files:

    print("\n================================================")
    print("Processing:")
    print(csv_path)
    print("================================================")

    ########################################################
    # EXTRACT T0
    ########################################################

    match = re.search(
        r"T0-(\d+\.\d+)",
        os.path.basename(csv_path)
    )

    if match is None:
        print("Cannot parse T0")
        continue

    T0 = float(match.group(1))

    ########################################################
    # LOAD PROBABILITY DATA
    ########################################################

    df = pd.read_csv(csv_path)

    E0_vals = df["E0_value"].values
    P_vals = df["BSucSeedingProbability"].values
    print("E0_vals: ", E0_vals)
    print("P_vals: ", P_vals)    

    ########################################################
    # IMPORTANT:
    # REPLACE THIS WITH TRUE E0 VALUES
    #
    # CURRENTLY:
    # using R_iniBlob_um as surrogate x-axis
    #
    # IF YOU HAVE TRUE E0 VALUES SAVED,
    # use them directly instead.
    ########################################################

    #
    # Example:
    #
    # E0_vals = df["E0_eV"].values
    #
    ########################################################

    ########################################################
    # INTERPOLATION OF PROBABILITY
    ########################################################

    P_interp = interp1d(
        E0_vals,
        P_vals,
        kind='linear',
        bounds_error=False,
        fill_value=(0.0, 1.0)
    )

    ########################################################
    # BUILD ENERGY GRID
    ########################################################

    Emin = np.min(E0_vals)
    Emax = np.max(E0_vals)

    E_grid = np.linspace(
        Emin,
        Emax,
        2000
    )
    print("E_grid", E_grid)
    
    ########################################################
    # COMPUTE EVENT RATE
    ########################################################

    #
    # eventRate(E)
    #
    # is assumed to return:
    #
    #   EVENTS / TIME
    #
    # for each energy bin / point
    #
    ########################################################

    rate_vals = np.array([
        eventRate(E, 0.05, 0.02)
        for E in E_grid
    ])

    print("rate_vals", rate_vals)

    ########################################################
    # COMPUTE B-SUCCESS RATE
    ########################################################

    P_grid = P_interp(E_grid)

    #
    # Since eventRate already has unit:
    #
    #   EVENTS / TIME
    #
    # we SUM instead of integrate
    #
    ########################################################

    Gamma_BS = np.sum(
        rate_vals * P_grid
    )

    ########################################################
    # LIFETIME
    ########################################################

    if Gamma_BS > 0.0:
        tau = 1.0 / Gamma_BS
    else:
        tau = np.inf

    ########################################################
    # SAVE
    ########################################################

    T0_list.append(T0)
    tau_list.append(tau)

    ########################################################
    # PRINT
    ########################################################

    print("\nT0 =", T0)

    print("Gamma_BS =", Gamma_BS)

    print("tau =", tau)

############################################################
# SORT
############################################################

sorted_pairs = sorted(
    zip(T0_list, tau_list),
    key=lambda x: x[0]
)

T0_sorted = [x[0] for x in sorted_pairs]
tau_sorted = [x[1] for x in sorted_pairs]

############################################################
# SAVE TAU TABLE
############################################################

tau_csv_path = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Lifetime_vs_T0.csv"
)

tau_df = pd.DataFrame({

    "T0": T0_sorted,
    "tau": tau_sorted

})

tau_df.to_csv(
    tau_csv_path,
    index=False
)

print("\nSaved:")
print(tau_csv_path)

############################################################
# PLOT TAU vs T0
############################################################

fig, ax = plt.subplots(
    figsize=(10, 7)
)

ax.plot(
    T0_sorted,
    tau_sorted,
    linestyle='--',
    linewidth=2,
    color='darkblue'
)

ax.scatter(
    T0_sorted,
    tau_sorted,
    s=90,
    color='crimson'
)

############################################################
# LABELS
############################################################

ax.set_xlabel(
    r'$T_0$',
    fontsize=22
)

ax.set_ylabel(
    r'$\tau$/day',
    fontsize=22
)

ax.set_title(
    r'B-phase Seeding Lifetime vs $T_0$',
    fontsize=20,
    pad=18
)

############################################################
# GRID
############################################################

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

############################################################
# TICKS
############################################################

ax.tick_params(
    axis='both',
    which='major',
    labelsize=16
)

############################################################
# LAYOUT
############################################################

fig.subplots_adjust(
    left=0.16,
    bottom=0.14,
    top=0.88
)

############################################################
# SAVE FIGURE
############################################################

plot_path = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Lifetime_vs_T0.png"
)

fig.savefig(
    plot_path,
    dpi=300,
    pad_inches=0.02
)

plt.close(fig)

print("\nSaved plot:")
print(plot_path)
