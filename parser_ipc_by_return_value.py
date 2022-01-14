import pandas as pd
import sys
import os


IPC_SYSCALL_LST = 'pipe pipe2 tee splice vmsplice shmget shmctl shmat shmdt semget semctl semop semtimedop futex ' \
                  'set_robust_list get_robust_list msgget msgctl msgsnd msgrcv mq_open mq_unlink mq_getsetattr ' \
                  'mq_timedsend mq_timedreceive mq_notify socket socketpair setsockopt getsockopt getsockname ' \
                  'getpeername bind listen accept accept4 connect shutdown recvfrom recvmsg recvmmsg sendto sendmsg ' \
                  'sendmmsg sethostname setdomainname'.split()

def collect_syscalls(dct, file_name):
    mprotect_num = 3
    i = 0
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            syscall = line.split('(')[0]
            equals_split = line.strip().split(') =')
            if (len(equals_split) > 1):
                ret_val = equals_split[1].strip().split()[0]
                neg_sign_stripped = ret_val.lstrip('-')
                if neg_sign_stripped.isdigit() and ret_val[0] == '-':
                    continue
            if i < mprotect_num:
                if syscall == "mprotect":
                    i += 1
                else:
                    i = 0
                continue
            if "SIG" not in syscall and "exit" not in syscall:
                if syscall in IPC_SYSCALL_LST:
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
    if dct != {}:
        data = pd.DataFrame.from_dict(dct, orient="index")
        data.rename(columns={0:dirname}, inplace=True)
        data.sort_values(by=dirname, inplace=True, ascending=False)
        data.reset_index(inplace=True)
        data.rename(columns={"index": "syscall_names"}, inplace=True)
        print(data)
        data.to_csv(f"./ipc_return_parsed_results/{dirname}_result.csv")