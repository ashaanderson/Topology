 Network Topology Discovery Project

## Project Goal
The goal of this project is to discover and document the network topology of the Howard University campus network.

## Approach
We have employed a systematic approach to uncover the network topology. This involved running traceroute to various IP addresses within the Howard University network. The Python code below was used to automate the process:

### Setup Virtual Environment
Create a Python virtual environment using the following command:
```shell
python -m venv venv
```
**Note:** This is a one time operation.

### Activate Virtual Environment
To activate the virtual environment:
- MacOS: `source venv/bin/activate`
- Windows: `.\venv\Scripts\activate`

### Install dependencies
Install all required dependencies from `Dependencies.txt` file
```shell
pip install -r Dependencies.txt
```

### Run Tracing Program
This script generates all other addresses found from a access point. The result is stored under `./result` directory locally.
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
