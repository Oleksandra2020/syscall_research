import pandas as pd
import sys
import os

def collect_syscalls(dct, file_name):
    seen_execve = False
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            syscall = line.split('(')[0]
            if syscall == "execve":
                seen_execve = True
                continue
            if "SIG" not in syscall and "exited" not in syscall and seen_execve:
                if syscall not in dct:
                    dct[syscall] = 0
                dct[syscall] += 1
    return dct

if __name__ == "__main__":
    dct = {}
    dirname = sys.argv[1]
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    for name in range(len(filenames)):
        collect_syscalls(dct, filenames[name])

    for k in dct:
        dct[k] /= len(filenames)
    data = pd.DataFrame.from_dict(dct, orient="index")
    data.rename(columns={0:dirname}, inplace=True)
    data.sort_index(inplace=True)
    data = data.reset_index()
    data.rename(columns={"index": "syscall_names"}, inplace=True)
    print(data)
    data.to_csv("result.csv")