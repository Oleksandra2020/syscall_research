import pandas as pd
import sys
import os

def collect_syscalls(dct, num_of_progs, ind, file_name):
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            syscall = line.split('(')[0]
            if "SIG" not in syscall and "exited" not in syscall:
                if syscall not in dct:
                    dct[syscall] = num_of_progs*[0]
                dct[syscall][ind] += 1
    return dct

if __name__ == "__main__":
    dct = {}
    dirname = sys.argv[1]
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    # filenames = ["./chrome.txt", "./chromium.txt", "./clang.txt", "./firefox.txt", "./gcc.txt", "./gnome_calc.txt"] + \
    #             ["./gnome_calendar.txt", "./gxx.txt", "./lo_calc.txt", "./loffice.txt", "./scipysignal.txt", "./sklearn.txt"]
    for name in range(len(filenames)):
        collect_syscalls(dct, len(filenames), name, filenames[name])
    del dct['\n']
    del dct[') = 68\n']
    cols = {i:filenames[i] for i in range(len(filenames))}
    data = pd.DataFrame.from_dict(dct, orient="index")
    data.rename(columns=cols, inplace=True)
    data.sort_index(inplace=True)
    data.to_csv("result.csv")