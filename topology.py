import os
import networkx as nx
import matplotlib.pyplot as plt

def _get_all_traceroutes(directory):
    result = []
    for file in os.listdir(directory):
        current_file_path = os.path.join(directory, file)
        if os.path.isdir(current_file_path):
            result.extend(_get_all_traceroutes(current_file_path))
        else:
            result.append(current_file_path)
    return result

def build_topology(results_directory):
    topology = {}

    directories = [results_directory]  # Add the main results directory to the list

    # Get all directories (including subdirectories) within the results directory
    for root, dirs, files in os.walk(results_directory):
        for dir in dirs:
            directories.append(os.path.join(root, dir))

    # Iterate over all files in the directories
    for directory in directories:
        all_files = _get_all_traceroutes(directory)

        for file in all_files:
            try:
                with open(file) as fp:
                    ip_addresses = [x.strip() for x in fp.readlines() if len(x.strip()) > 0][:6]

                    for ip_addr in ip_addresses:
                        if ip_addr not in topology:
                            topology[ip_addr] = set()

                    for i in range(len(ip_addresses) - 1):
                        current_ip_address = ip_addresses[i]
                        parent_ip_address = ip_addresses[i+1]
                        topology[current_ip_address].add(parent_ip_address)
            except:
                print(f'Failed to read: {file}')

    return topology

def display_topology(topology, title="Combined Topology"):
    edges = []
    for ip_address, parent_ip_addresses in topology.items():
        for parent in parent_ip_addresses:
            edges.append([ip_address, parent])

    G = nx.Graph()
    G.add_edges_from(edges)

    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray')

    manager = plt.get_current_fig_manager()
    manager.set_window_title(title)
    manager.full_screen_toggle()

    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    building_name = ""  # Specify the building name directly here or leave it as an empty string
    results_path = os.path.join("result", building_name)

    topology = build_topology(results_path)

    display_topology(topology, title=building_name)
