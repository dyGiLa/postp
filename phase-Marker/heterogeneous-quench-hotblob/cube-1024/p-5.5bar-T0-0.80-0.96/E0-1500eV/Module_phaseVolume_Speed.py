import pandas as pd
import numpy as np
from collections import defaultdict

import glob
import os


def pvSpeedDicts(root_dir: str):

    ####################
    # Recursively find all CSV files
    # Base glob pattern to match all pv.csv files under RSeed-* folders
    pattern = os.path.join(root_dir, "RSeed-*-T0-0.80-0.96", "p-5.5-T1-*", "stats", "phaseVolume-stream.csv")
    print("pattern", pattern)

    csv_files = glob.glob(pattern)
    print("csv_files = ", csv_files)

############################################################
#    build dictinarys of VSpeed for last momentum  px      #
############################################################
    p9VSpeed_last_by_T1 = defaultdict(list)
    p5VSpeed_last_by_T1 = defaultdict(list)
    p3VSpeed_last_by_T1 = defaultdict(list)

    for csv_file in csv_files:

        print("\n")
        print("csv file : ", csv_file)
        
        # Read the CSV
        df = pd.read_csv(csv_file)

        # Compute the numerical derivative using numpy's gradient
        dt = df["t"][1] - df["t"][0]
        # df["xxx"].values to force return numpy array    
        dVrp5dt = np.gradient(df["Vratio_p5_acc"].values, dt)
        dVrp9dt = np.gradient(df["Vratio_p9_acc"].values, dt)
        dVrp3dt = np.gradient(df["Vratio_p3_acc"].values, dt)
        #dVrp1dt = np.gradient(df["Vratio_p1_acc"].values, dt)    

        print("\n")
        print("dVrp5dt[-1] : ", dVrp5dt[-1])
        print("dVrp9dt[-1] : ", dVrp9dt[-1])
        print("dVrp3dt[-1] : ", dVrp3dt[-1])

        try:
            # Extract T1 from folder name: "p-5.5-T1-#",
            # This works as key for appending Vratio_px.
            parent_dir = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
            print("parent_dir = ",parent_dir)
            T1Val_str = parent_dir.replace("p-5.5-T1-", "")
            print("T1Val_str = ", T1Val_str)        
            T1Val_val = float(T1Val_str)

            # missing keys T1 are added when append/access
            p9VSpeed_last_by_T1[T1Val_val].append(dVrp9dt[-1])
            p5VSpeed_last_by_T1[T1Val_val].append(dVrp5dt[-1])
            p3VSpeed_last_by_T1[T1Val_val].append(dVrp3dt[-1])            
        except Exception as e:
            print(f"Failed on {csv_file}: {e}")

    return p9VSpeed_last_by_T1, p5VSpeed_last_by_T1, p3VSpeed_last_by_T1
        
