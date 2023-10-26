 Network Topology Discovery Project

## Project Goal
The goal of this project is to discover and document the network topology of the Howard University campus network.

## Approach
We have employed a systematic approach to uncover the network topology. This involved running traceroute to various IP addresses within the Howard University network. The Python code below was used to automate the process:

### Setup Virtual Environment
Set up a Python virtual environment by executing the subsequent command:
```shell
python -m venv venv
```
**Note:** Use only once

### Install dependencies
Install all required dependencies from `Dependencies.txt` file
```shell
pip install -r Dependencies.txt
```

### Run Tracing Program
This script produces additional addresses discovered from an access point. The output is saved locally within the `./result` directory.
```shell
python main.py
```

Note: `scapy` module might require admin privileges to run. If you get the following error:
```shell
Permission denied: could not open /dev/bpf0. Make sure to be running Scapy as root ! (sudo)
```
Run the above script as sudo:
```shell
sudo python main.py
```
>>>>>>> 23d9fea (Initial commit)
