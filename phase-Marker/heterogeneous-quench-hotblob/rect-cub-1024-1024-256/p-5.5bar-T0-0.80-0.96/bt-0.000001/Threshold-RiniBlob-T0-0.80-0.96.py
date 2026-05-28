import os
import glob
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


############################################################
# CONFIG
############################################################

ROOT_DIR = (
    "/home/heidi/ReHD3/dyGiLa-project/"
    "project_462000960/"
    "heterogenouos-quench/"
    "rect-cub-1024-1024-256/"
    "p-5.5bar-T0-0.80-0.96/"
    "bt-0.000001"
)

CSV_DIR = os.path.join(
    ROOT_DIR,
    "BSucSeeding_Probability_CSV"
)

OUTPUT_PLOT = os.path.join(
    ROOT_DIR,
    "Threshold_RiniBlob_vs_T0.png"
)

OUTPUT_CSV = os.path.join(
    ROOT_DIR,
    "Threshold_RiniBlob_vs_T0.csv"
)

############################################################
# FIND ALL PROBABILITY CSV FILES
############################################################

pattern = os.path.join(
    CSV_DIR,
    "BSucSeedingProbability-T0-*.csv"
)

csv_files = sorted(glob.glob(pattern))

print("\nFound probability CSV files =", len(csv_files))

############################################################
# STORAGE
############################################################

T0_list = []
threshold_R_list = []

############################################################
# PROCESS EACH CSV
############################################################

for csv_file in csv_files:

    print("\nProcessing:")
    print(csv_file)

    ########################################################
    # EXTRACT T0 FROM FILE NAME
    ########################################################

    # example:
    # BSucSeedingProbability-T0-0.84.csv

    filename = os.path.basename(csv_file)

    match = re.search(
        r"T0-(\d+\.\d+)",
        filename
    )

    if match is None:
        print("Cannot parse T0.")
        continue

    T0 = float(match.group(1))

    ########################################################
    # READ CSV
    ########################################################

    df = pd.read_csv(csv_file)

    if df.empty:
        print("Empty CSV.")
        continue

    ########################################################
    # SORT BY R
    ########################################################

    # df = df.sort_values(
    #     by="R_iniBlob_um"
    # )
    df = df.sort_values(
        by="E0_value"
    )

    
    ########################################################
    # FIND THRESHOLD
    ########################################################

    # threshold =
    # smallest R_iniBlob with probability > 0

    positive_df = df[
        df["BSucSeedingProbability"] > 0
    ]

    if len(positive_df) == 0:

        print("No nonzero probability found.")

        threshold_R = np.nan

    else:

        # threshold_R = positive_df.iloc[0][
        #     "R_iniBlob_um"
        # ]
        threshold_R = positive_df.iloc[0][
            "E0_value"
        ]

    ########################################################
    # SAVE
    ########################################################

    T0_list.append(T0)
    threshold_R_list.append(threshold_R)

    ########################################################
    # PRINT
    ########################################################

    print(f"T0 = {T0:.2f}")
    print(f"threshold R_iniBlob_um = {threshold_R}")

############################################################
# SAVE THRESHOLD CSV
############################################################

threshold_df = pd.DataFrame({

    "T0": T0_list,
    "Threshold_R_iniBlob_um": threshold_R_list

})

threshold_df = threshold_df.sort_values(
    by="T0"
)

threshold_df.to_csv(
    OUTPUT_CSV,
    index=False
)

print("\nSaved threshold CSV:")
print(OUTPUT_CSV)

############################################################
# PLOT
############################################################

fig, ax = plt.subplots(
    figsize=(10, 7)
)

############################################################
# SORT DATA
############################################################

sorted_pairs = sorted(
    zip(T0_list, threshold_R_list),
    key=lambda x: x[0]
)

T0_fit = np.array([x[0] for x in sorted_pairs])
R_fit = np.array([x[1] for x in sorted_pairs])

############################################################
# REMOVE NaN VALUES
############################################################

mask = ~np.isnan(R_fit)

T0_fit = T0_fit[mask]
R_fit = R_fit[mask]

############################################################
# CRITICAL FITS
############################################################

from scipy.optimize import curve_fit

############################################################
# FIT FUNCTION 1
# fixed Tc = 1
############################################################

def critical_fit_fixedTc(T0, A, gamma):

    return A / ((1.0 - T0) ** gamma)

############################################################
# FIT FUNCTION 2
# free Tc
############################################################

def critical_fit_freeTc(T0, A, Tc, gamma):

    return A / ((Tc - T0) ** gamma)

############################################################
# INITIAL GUESSES
############################################################

initial_guess_fixed = [
    1.0,   # A
    1.0    # gamma
]

initial_guess_free = [
    1.0,   # A
    1.0,   # Tc
    1.0    # gamma
]

############################################################
# FIT 1 : FIXED Tc = 1
############################################################

popt_fixed, pcov_fixed = curve_fit(

    critical_fit_fixedTc,
    T0_fit,
    R_fit,

    p0=initial_guess_fixed,

    maxfev=100000
)

A_fixed = popt_fixed[0]
gamma_fixed = popt_fixed[1]

############################################################
# FIT 2 : FREE Tc
############################################################

popt_free, pcov_free = curve_fit(

    critical_fit_freeTc,
    T0_fit,
    R_fit,

    p0=initial_guess_free,

    maxfev=100000
)

A_free = popt_free[0]
Tc_free = popt_free[1]
gamma_free = popt_free[2]

############################################################
# PRINT RESULTS
############################################################

print("\n")
print("================================================")
print("Fit 1 : fixed Tc = 1")
print("================================================")

print(f"A      = {A_fixed:.6f}")
print(f"gamma  = {gamma_fixed:.6f}")

print("\n")
print("================================================")
print("Fit 2 : free Tc")
print("================================================")

print(f"A      = {A_free:.6f}")
print(f"Tc     = {Tc_free:.6f}")
print(f"gamma  = {gamma_free:.6f}")

############################################################
# SMOOTH CURVES
############################################################

T0_smooth = np.linspace(
    np.min(T0_fit),
    np.max(T0_fit),
    500
)

R_smooth_fixed = critical_fit_fixedTc(
    T0_smooth,
    A_fixed,
    gamma_fixed
)

R_smooth_free = critical_fit_freeTc(
    T0_smooth,
    A_free,
    Tc_free,
    gamma_free
)

############################################################
# LABELS
############################################################

fit_label_fixed = (
    #r'Fixed $T_c=1$' + '\n'
    rf'$R^{{threshold}}={A_fixed:.3f}/(1-T_0)^{{{gamma_fixed:.3f}}}$'
)

fit_label_free = (
    #r'Free $T_c$' + '\n'
    rf'$R^{{threshold}}={A_free:.3f}/({Tc_free:.3f}-T_0)^{{{gamma_free:.3f}}}$'
)

############################################################
# PLOT FITS
############################################################

ax.plot(
    T0_smooth,
    R_smooth_fixed,
    linestyle='--',
    linewidth=2.5,
    color='darkblue',
    label=fit_label_fixed
)

ax.plot(
    T0_smooth,
    R_smooth_free,
    linestyle='-.',
    linewidth=2.5,
    color='darkgreen',
    label=fit_label_free
)

############################################################
# SCATTER POINTS
############################################################

ax.scatter(
    T0_fit,
    R_fit,
    s=100,
    color='crimson',
    zorder=3,
    label='Measured Thresholds from Sims.'
)

############################################################
# LABELS
############################################################

ax.set_xlabel(
    r'$T_0/T_c$',
    fontsize=22
)

ax.set_ylabel(
    r'Threshold $R_{iniBlob}/\mu m$',
    fontsize=22
)

ax.set_title(
    r'Threshold $R_{iniBlob}$ vs. $T_0$ in $3.32\mu m$ Slab at $5.5$bar',
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
# LEGEND
############################################################

ax.legend(
    fontsize=14,
    loc='best'
)

############################################################
# LAYOUT
############################################################

fig.subplots_adjust(
    left=0.16,
    bottom=0.15,
    top=0.88
)

############################################################
# SAVE FIGURE
############################################################

fig.savefig(
    OUTPUT_PLOT,
    dpi=300,
    pad_inches=0.02
)

plt.close(fig)

print("\nSaved plot:")
print(OUTPUT_PLOT)
