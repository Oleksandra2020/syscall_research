import pandas as pd
import sys
import os

def add_syscalls(filename, dct):
    f = pd.read_csv(filename)
    syscall_names, program_count = f[f.columns[1]], f[f.columns[2]]
    for i in range(len(syscall_names)):
        if syscall_names[i] not in dct: dct[syscall_names[i]] = 0
        dct[syscall_names[i]] += program_count[i]
    return dct

if __name__ == "__main__":
    dct = {}
    dirname = sys.argv[1]
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    for name in range(len(filenames)):
        print(filenames[name])
        dct = add_syscalls(filenames[name], dct)

    data = pd.DataFrame.from_dict(dct, orient="index")
    data.rename(columns={0:dirname}, inplace=True)
    data.sort_index(inplace=True)
    data = data.reset_index()
    data.rename(columns={"index": "syscall_names"}, inplace=True)
    print(data)
    data.to_csv(f"../results/general_result.csv")
