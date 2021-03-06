# Characterization of POSIX IPC system calls usage of modern workloads

Based on a previous study on POSIX.1-2008 IPC standard, we aim to investigate and determine whether POSIX.1-2017 IPC standard syscalls are still being equally utilized by present-day workloads.

## Installation
To install from our GitHub repository, you can do:
```bash
git clone https://github.com/Oleksandra2020/syscall_research.git
cd syscall_research
```

## Requirements
The following command installs all necessary packages:
```bash
pip install -r requirements.txt
```

## Data
To conduct our research we collected syscalls invocations of different modern workloads.

To accomplish that we utilized `strace` tool. Below you can see the table with used software and types of operation for 
data collection:

Type | Application | Operations
--- | --- | ---
console utilities	| htop	| 3 min
compilers	| gcc	| compile a library Glog
browsers | chrome	| browse, bookmark
browsers	|firefox	|browse, bookmark
ai/ml packages	|ai algorithm	|train SVM  classifier on 5000 samples
office packages	|libreoffice	|write a text, insert an image, bold the  text, save doc as  file on disk
console utilities	|gzip	|compress 20 Gb file and decompress
networking utilities	|openssh	|connect to remote server, ls command, mkdir test && cd test, cd .., rm -rf test
video player	|VLC media player|	watch 5 min of video, speed up
http server 	|Apache	|POST and GET for 100 requests with Apache Benchmark

## Metrics for evaluation
1. no. of (IPC) system calls: number of syscall invocation  / number of experiments
2. importance of (IPC) system calls: number of workloads that use syscall
3. % of IPC system calls: number of IPC system call / number of IPC system calls in total

## Usage
* Number of invocations of each syscall:
```bash
python3 parser.py <directory with all files>
python3 paser.py <directory with files with one type of software results>
```
* importance:
```bash
python3 importance_metric.py <directory with all files>
python3 importance_metric.py <directory with files with one type of software results>
```
* Number of IPC syscalls:
```bash
python3 extract_ipc.py <directory with all files>
python3 extract_ipc.py <directory with files with one type of software results>
```
* importance of IPC syscalls:
```bash
python3 importance_ipc.py <directory with all files>
python3 importance_ipc.py <directory with files with one type of software results>
```
* % of IPC syscalls:
```bash
python3 calculate_ipc.py <directory with all files>
python3 calculate_ipc.py <directory with files with one type of software results>
```

## Results
![IPC system calls count across applications without outliers](https://user-images.githubusercontent.com/57792587/149616383-0d3b37aa-3b9a-4244-a140-ca8121846006.png)
![importance of IPC syscalls](https://user-images.githubusercontent.com/57792587/149616388-d1cd3a75-c9e2-45d3-a712-a4d5a170f7df.png)
![sum of IPC syscalls' importance by type](https://user-images.githubusercontent.com/57792587/149616390-ca2707cc-79d1-4be7-90d0-53e38f9f5da4.png)




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate (ha!).
