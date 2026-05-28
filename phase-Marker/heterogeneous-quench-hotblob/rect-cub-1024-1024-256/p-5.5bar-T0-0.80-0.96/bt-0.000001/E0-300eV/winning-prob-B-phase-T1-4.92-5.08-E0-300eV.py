import re
import os
import glob
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import Module_phaseVolume_Speed as VS

# Root directory where RSeed-* folders are located
root_dir = '/home/heidi/ReHD3/dyGiLa-project/project_462000960/heterogenouos-quench/rect-cub-1024-1024-256/p-5.5bar-T0-0.80-0.96/bt-0.000001/E0-300eV'

# Base glob pattern to match all pv.csv files under RSeed-* folders
pattern = os.path.join(root_dir, "RSeed-*-T0-0.80-0.96", "p-5.5-T1-*", "stats", "phaseVolume-stream.csv")
print("patter", pattern)

csv_files = glob.glob(pattern)
print("csv_files = ", csv_files)

# plot marker sizes
s=[50, 70, 90, 110]


#fig.savefig("plot.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
fig.savefig(output_path, dpi=300, pad_inches=0.01)
# plt.close(fig1)
plt.close(fig)
