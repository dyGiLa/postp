import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re


# Function to load the pickle file
def load_pickle_file(file_path):
    """Load a pickle file and return the data."""
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

# Function to process the data for plotting
def process_data(data):
    """Extract and return the necessary data for plotting."""
    if not data:
        return None, None, None

    grid_data = data['grid']
    x = grid_data['x']  # Grid for x > 0
    x_minus = grid_data['x_minus']  
    x_minus = -np.abs(x_minus[1:])  # x-coords for x<0

    print(x)
    print(x_minus)
    
    x_arr = np.concatenate((x_minus, x))
    x_arr = np.sort(x_arr)
    
    #x_array = np.concatenate((x_minus, x))  # Combining x <0 and x>0 grids
    
    A = data['A']  # The solution matrix

    # Extract the real part of A
    A_real = [np.real(matrix) for matrix in A]
    # Extract the img part of A
    A_img = [np.imag(matrix) for matrix in A]
    
    return x_arr[::2]*0.5, np.array(A_real), np.array(A_img)

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#

# plot line color
lineColors = [
    (0.121, 0.466, 0.705),  # Blue
    (1.000, 0.498, 0.054),  # Orange
    (0.172, 0.627, 0.172),  # Green
    (0.839, 0.153, 0.157),  # Red
    (0.580, 0.404, 0.741),  # Purple
    (0.549, 0.337, 0.294),   # Brown
    (0.05, 0.05, 0.20),      # Dark Navy
    (0., 0., 0.)            # Black
]

# line styles
line_styles = ['-', '--', ':', '-.', (0, (5, 10)), (0, (3, 2, 1, 2, 1, 2)) ]

LineWidth=3.5
LineWidth2=2.0

# x-coord shift
x_shift=64.

# Find all CSV files
files = sorted(glob.glob("AB-DWall-28bar-TAB-gamma-3.0-5000tGL-128xi0GL.csv"))

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
    
    # ax.plot(df["Points:0"]-x_shift, df["gapA"],
    #         linewidth=LineWidth, 
    #         label=fr'$\sqrt{{A^{{\dagger}}A}}\,,\gamma = {gamma}$',
    #         linestyle=line_styles[0], color=lineColors[0])
    
    # compute gapA array
    gapA_arr= np.sqrt(df["u11"]**2 + df["u12"]**2 + df["u13"]**2
                      + df["u21"]**2 + df["u22"]**2 + df["u23"]**2
                      + df["u31"]**2 + df["u32"]**2 + df["u33"]**2
                      + df["v11"]**2 + df["v12"]**2 + df["v13"]**2
                      + df["v21"]**2 + df["v22"]**2 + df["v23"]**2
                      + df["v31"]**2 + df["v32"]**2 + df["v33"]**2)
    # find gapA min point index
    idx_gapAmin_dyGiLa = np.argmin(gapA_arr)

    # shift 0-point to gapA-min
    x_arr_dyGiLa = np.array(df["Points:0"]) - np.array(df["Points:0"])[idx_gapAmin_dyGiLa]

    ax.plot(x_arr_dyGiLa, gapA_arr,
            linewidth=LineWidth, 
            label=fr'$\sqrt{{A^{{\dagger}}A}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[7])    
    
    ax.plot(x_arr_dyGiLa, df["u11"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{11}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[1])
    
    ax.plot(x_arr_dyGiLa, df["u22"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{22}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[2])

    ax.plot(x_arr_dyGiLa, df["u33"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{33}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[3])

    ax.plot(x_arr_dyGiLa, df["v12"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{12}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[4])

    ax.plot(x_arr_dyGiLa, df["v21"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{21}}\,,dyGiLa\,\gamma = {gamma}\,, 5000t_{{GL}}$',
            linestyle=line_styles[0], color=lineColors[5])

#------------------------------------------------------------#
#--------     plot data from VerHem csv file-----------------#
#------------------------------------------------------------#
filesVerHem = sorted(glob.glob("AB-DWall-VerHem-28bar-TAB-128x12x12xi0GL-lParallelWall-yz-periodic-convgTol1e-4-residual1.2e-13.csv"))

for file_path in filesVerHem:
    
    # Read csv data
    df = pd.read_csv(file_path)
    
    # ax.plot(df["Points:0"]-x_shift, df["gapA"],
    #         linewidth=LineWidth, 
    #         label=fr'$\sqrt{{A^{{\dagger}}A}}\,,\gamma = {gamma}$',
    #         linestyle=line_styles[0], color=lineColors[0])

    gapA_verhem_arr= np.sqrt(df["u_11"]**2 + df["u_12"]**2 + df["u_13"]**2
                             + df["u_21"]**2 + df["u_22"]**2 + df["u_23"]**2
                             + df["u_31"]**2 + df["u_32"]**2 + df["u_33"]**2
                             + df["v_11"]**2 + df["v_12"]**2 + df["v_13"]**2
                             + df["v_21"]**2 + df["v_22"]**2 + df["v_23"]**2
                             + df["v_31"]**2 + df["v_32"]**2 + df["v_33"]**2)

    # find gapA min point index
    idx_gapAmin_verhem = np.argmin(gapA_verhem_arr)

    # shift 0-point to gapA-min
    x_arr_verhem = np.array(df["Points:0"]) - np.array(df["Points:0"])[idx_gapAmin_verhem]
        
    ax.plot(x_arr_verhem, gapA_verhem_arr,
            linewidth=LineWidth, 
            label=fr'$\sqrt{{A^{{\dagger}}A}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[7])
        
    ax.plot(x_arr_verhem, df["u_11"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{11}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[1])
    
    ax.plot(x_arr_verhem, df["u_22"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{22}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[2])

    ax.plot(x_arr_verhem, df["u_33"],
            linewidth=LineWidth, 
            label=fr'$ReA_{{33}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[3])

    ax.plot(x_arr_verhem, df["v_12"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{12}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[4])

    ax.plot(x_arr_verhem, df["v_21"],
            linewidth=LineWidth, 
            label=fr'$ImA_{{21}}\,,VerHem\, |Residul|_{{L_{{2}}}} = 1.3e-6$',
            linestyle=line_styles[3], color=lineColors[5])
    
#------------------------------------------------------------#
#--------     plot data from Mark's plk file-----------------#
#------------------------------------------------------------#

# pklfile_path = 'AB_wall_data_p28.pkl'  # Replace with your actual pickle file path
# pkldata = load_pickle_file(pklfile_path)

# # Step 2: Process the data to extract the necessary arrays
# x_arr, A_real, A_img = process_data(pkldata)

# gapA_Mark_arr= np.sqrt(A_real[:, 0, 0]**2 + A_real[:, 1, 1]**2 + A_real[:, 2, 2]**2 + A_img[:, 0, 1]**2 + A_img[:, 1, 0]**2)
# # find gapA min point index
# idx_gapAmin_MarkSolver = np.argmin(gapA_Mark_arr)

# # shift 0-point to gapA-min
# x_arr = x_arr - x_arr[idx_gapAmin_MarkSolver]



# ax.plot(x_arr, gapA_Mark_arr, linewidth=LineWidth2, label=fr"$\sqrt{{A^{{\dagger}}A}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[7])

# # plot ReA and ImA
# ax.plot(x_arr, A_real[:, 0, 0], linewidth=LineWidth2, label=fr"$ReA_{{11}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[1])
# ax.plot(x_arr, A_real[:, 1, 1], linewidth=LineWidth2, label=fr"$ReA_{{22}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[2])
# ax.plot(x_arr, A_real[:, 2, 2], linewidth=LineWidth2, label=fr"$ReA_{{33}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[3])

# ax.plot(x_arr, A_img[:, 0, 1], linewidth=LineWidth2, label=fr"$ImA_{{12}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[4])
# ax.plot(x_arr, A_img[:, 1, 0], linewidth=LineWidth2, label=fr"$ImA_{{21}}$ Mark's Solver", linestyle=line_styles[1], color=lineColors[5])


#------------------------------------------------------------#
#--------               Plot make up        -----------------#
#------------------------------------------------------------#

ax.set_xlabel(r"$x/\xi^0_{GL}$", fontsize=26.0)
ax.set_ylabel(r"$X/k_B T_C$", fontsize=26.0)
ax.set_xlim(-40, 40)
ax.set_ylim(-0.25, 2.5)
ax.tick_params(axis='both', which='major', labelsize=30)
ax.set_title(fr"AB Domain Wall configuration at ${{28}}$bar from dyGiLa, VerHem and Mark's Solver", fontsize=26, pad=15)
ax.legend(handlelength=3.2, fontsize=11, title_fontsize=14)
ax.grid(True, alpha=0.9, linestyle='-')

plt.tight_layout()
plt.show()

fig.savefig('AB-DWall-diff_Solvers-verhem-lPerpWall-yz-periodic-128x6x6-res1en13', dpi=300, pad_inches=0.0)
plt.close(fig)
