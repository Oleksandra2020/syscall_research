import pandas as pd
import sys
import os
import parser

if __name__ == "__main__":
    sc_names = []
    dirname = sys.argv[1]  # directory here should contain all the files for all the software
    filenames = []
    for name in os.scandir(dirname):
        filenames.append(name.path)
    for name in range(len(filenames)):
        dct = {}
        parser.collect_syscalls(dct, filenames[name])
        sc_names.append(list(dct.keys()))

    sc_imp = {}
    for key_list in sc_names:
        for sc in key_list:
            if not sc in sc_imp:
                sc_imp[sc] = sum([lst.count(sc) for lst in sc_names])

    data = pd.DataFrame.from_dict(sc_imp, orient="index")
    data.rename(columns={0: dirname}, inplace=True)
    data.sort_index(inplace=True)
    data = data.reset_index()
    data.rename(columns={"index": "syscall_names"}, inplace=True)
    print(data)
    data.to_csv("../results/importance_metric_result.csv")
