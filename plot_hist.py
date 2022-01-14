import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dct = {}
    dirname = sys.argv[1]
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    for name in range(len(filenames)):
        f = pd.read_csv(filenames[name])
        syscall_names, program_count = f[f.columns[1]], f[f.columns[2]]
        plt.figure(figsize=(18, 5))
        plt.bar(syscall_names[:10], program_count[:10])
        plt.savefig(f"./saved_figs/{filenames[name][6:-4]}_plot", transparent=True)