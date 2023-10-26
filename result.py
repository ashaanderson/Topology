import os

_RESULTS_DIRECTORY = "result"

# Create directory to store results if not existing
def init():
    if not os.path.exists(_RESULTS_DIRECTORY):
        os.makedirs(_RESULTS_DIRECTORY)

def dump_trace(ip_address, found_ip_addresses):
    result_file = f'{_RESULTS_DIRECTORY}/{ip_address}'
    with open(result_file, 'w') as fp:
        for ip_addr in found_ip_addresses:
            fp.write(f"{ip_addr}\n")