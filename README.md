# CSCI-449-Project-1

## Setup Development Environment

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
Install all required dependencies from `requirements.txt` file
```shell
pip install -r requirements.txt
```

### Run Tracing Program
This script generates all other addresses found from a access point. The result is stored under `./results` directory locally.
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