import pandas as pd
import sys
import os


def collect_syscalls(dct, file_name):
    mprotect_num = 3
    i = 0
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            syscall = line.split('(')[0]
            if i < mprotect_num:
                if syscall == "mprotect":
                    i += 1
                else:
                    i = 0
                continue
            if "SIG" not in syscall and "exit" not in syscall:
                if syscall not in dct: dct[syscall] = 0
                dct[syscall] += 1
    return dct

if __name__ == "__main__":
    dct = {}
    dirname = sys.argv[1]
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    for name in range(len(filenames)):
        dct = collect_syscalls(dct, filenames[name])

    for k in dct:
        dct[k] /= len(filenames)
    data = pd.DataFrame.from_dict(dct, orient="index")
    data.rename(columns={0:dirname}, inplace=True)
    data.sort_values(by=dirname, inplace=True, ascending=False)
    data.reset_index(inplace=True)
    data.rename(columns={"index": "syscall_names"}, inplace=True)
    print(data)
    data.to_csv(f"./results/{dirname}_result.csv")