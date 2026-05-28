import os
import re
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------- CONFIGURATION --------------------------

base_folder = "/home/heidi/ReHD3/dyGiLa-project/project_462000960/homogenous-quench/box-retangular/box-4096-4096-440/p-0.0bar/t_0.7419035846724351"

time_col = "t"

items_columns = ["sumk1Re_VA", "sumk2Re_VA", "sumk3Re_VA", "sumaRe_VA", "sumb1Re_VA", "sumb2Re_VA", "sumb3Re_VA", "sumb4Re_VA", "sumb5Re_VA"]
# items_columns = ["sumaRe_VA", "sumb1Re_VA", "sumb2Re_VA", "sumb3Re_VA", "sumb4Re_VA", "sumb5Re_VA"]
#items_columns = ["sumk1Re_VA", "sumk2Re_VA", "sumk3Re_VA"]



group1 = {"11326", "313"}
group2 = {"1224", "256", "5951", "795"}
group3 = {"18025", "4", "9784"}
group4 = {"40"}

# Plot styling
lineColors = [
    (0.121, 0.466, 0.705),  # Blue
    (1.000, 0.498, 0.054),  # Orange
    (0.172, 0.627, 0.172),  # Green
    (0.839, 0.153, 0.157),  # Red
    (0.580, 0.404, 0.741),  # Purple
    (0.549, 0.337, 0.294),  # Brown
    (0.890, 0.466, 0.760),  # Pink
    (0.498, 0.498, 0.498),  # Gray
    (0.737, 0.741, 0.133),  # Olive
    (0.090, 0.745, 0.811),  # Cyan
]

line_styles = ['-', '--', ':', '-.']

LineWidth = 2.5

# -------------------------------------------------------------------


def load_GLFE(folder_path):
    """
    Load measure-stream.csv and compute GLFE using NumPy arrays.

    Returns:
        t        : numpy array
        glfe_va  : numpy array
    """

    csv_path = os.path.join(folder_path, "stats", "measure-stream.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find:\n{csv_path}")

    # Read CSV
    df = pd.read_csv(csv_path)

    # Validate columns
    required_cols = [time_col] + items_columns

    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        raise KeyError(
            f"Missing columns in {csv_path}:\n{missing}"
        )

    # Extract NumPy arrays WITHOUT modifying dataframe
    t = df[time_col].to_numpy()

    values = df[items_columns].to_numpy()

    # Sum columns row-wise
    glfe_va = np.sum(values, axis=1)

    return t, glfe_va


# -------------------------------------------------------------------
# Scan all RSeed-* folders
# -------------------------------------------------------------------

pattern = re.compile(r"^RSeed-\d+$")

all_folders = glob.glob(os.path.join(base_folder, "RSeed-*"))

seed_folders = sorted(
    folder for folder in all_folders
    if pattern.match(os.path.basename(folder))
)

if len(seed_folders) == 0:
    raise RuntimeError(
        f"No RSeed-* folders found in:\n{base_folder}"
    )

print(f"Found {len(seed_folders)} seed folders.")

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 7))

for i, folder in enumerate(seed_folders):

    seed_name = os.path.basename(folder)

    try:
        t, glGradfe = load_GLFE(folder)

        color = lineColors[i % len(lineColors)]
        #linestyle = line_styles[i % len(line_styles)]
        #linestyle = line_styles[0]
        # Assign linestyle by group
        seed_id = seed_name.replace("RSeed-", "")
        if seed_id in group1:
            #
            linestyle = line_styles[0]
        elif seed_id in group2:
            linestyle = line_styles[1]
        elif seed_id in group3:
            linestyle = line_styles[2]
        else:
            linestyle = '-.'        

        ax.plot(
            t,
            glGradfe,
            label=seed_name,
            linewidth=LineWidth,
            linestyle=linestyle,
            color=color
        )

        print(f"Loaded: {seed_name}")

    except Exception as e:
        print(f"Skipping {seed_name}: {e}")


# -------------------------------------------------------------------
# Figure styling
# -------------------------------------------------------------------

ax.set_xlabel(
    r'$t/t^{0}_{GL}$',
    fontsize=26
)

ax.set_ylabel(
    r' Free Energy Density '
    r'$\{f^{V}_{B} + f^{V}_{Grad}\}/\frac{1}{3}k_{B}T_{C}.{(\xi^0_{GL})}^{-3}$',
    fontsize=20
)

ax.set_xlim(0, 5000)    
ax.set_ylim(83.6, 84.5)

ax.set_title(
    fr'Volumetric Averaged GL Energy density with $1.1{{\mu}}m$ $T=0.689mK$ at $0bar$',
    fontsize=20,
    pad=25
)

ax.tick_params(
    axis='both',
    which='major',
    labelsize=22
)

ax.minorticks_on()

ax.grid(
    True,
    which="both",
    linestyle="--",
    alpha=0.5
)

ax.legend(
    fontsize=12,
    ncol=2
)

fig.tight_layout()

# Save figure under base_folder
save_path = os.path.join(base_folder, "GLFE_D-1.1um-p-0.0bar-T-0.689mK.png")

fig.savefig(
    save_path,
    dpi=300,
    bbox_inches="tight"
)

print(f"Figure saved to:\n{save_path}")

plt.close()
