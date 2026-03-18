import os
import glob
import pandas as pd

# Root directory where your RSeed-* folders are located
root_dir = '/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-blob-quenches-Hfield/lum-runs/lumi-G/project_462000960/heterogenouos-quench/cube-512/H-30mT/p-5.5bar'

# Pattern to find all pv.csv files
pattern = os.path.join(root_dir, "RSeed-*-T1-0.81-2.77-t1-0.005", "p-5.5-T1-0.838269", "stats", "phaseVolume-stream.csv")

# Get list of matching files
csv_files = glob.glob(pattern)

# B-phase occupation failed
failure_threshold = 0.99

# Counter for condition Vratio_p9_acc > failure_threshold
count_Vratio_p9_gt_FT = 0
total_samples = 0

for csv_file in csv_files:
    try:
        df = pd.read_csv(csv_file)
        if not df.empty:
            p9CSV_last = df.iloc[-1]["Vratio_p9_acc"]
            total_samples += 1
            if p9CSV_last > failure_threshold:
                count_Vratio_p9_gt_FT += 1
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

# Calculate probability
if total_samples > 0:
    probability = 1 - (count_Vratio_p9_gt_FT / total_samples)
    print(f"Total samples: {total_samples}")
    print(f"p9VR > failure_threshold count: {count_Vratio_p9_gt_FT}")
    print(f"Estimated B-phase winning Probability: {probability:.4f}")
else:
    print("No valid pv.csv files found.")
