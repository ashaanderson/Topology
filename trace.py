from scapy.all import *

from scapy.all import *

def trace_route(ip_address):
    print("Current IP Address:", ip_address)
    
    found_ip_addresses = []
    for i in range(1, 28):
        pkt = IP(dst=ip_address, ttl=i) / UDP(dport=33434)
        try:
            # Send the packet and get a reply
            reply = sr1(pkt, verbose=0, timeout=10)
            if reply is None:
                # No reply
                break
            elif reply.type == 3:
                # We've reached our destination
                if reply.src.startswith("138") or reply.src.startswith("10"):
                    print("Done!", reply.src)
                    found_ip_addresses.append(reply.src)
                break
            elif reply.src.startswith("138") or reply.src.startswith("10"):
                print(f"{i} hops away: {reply.src}")
                found_ip_addresses.append(reply.src)
        except KeyboardInterrupt as ex:
            print("Stopping traceroute...")
            raise ex
        except Exception as ex:
            print(f"Error occurred at {i} hops:")
            print(ex)
            break

    return found_ip_addresses

# Usage
if __name__ == "__main__":
    # Trace the route and get the results
    result = trace_route("destination_ip_address")

    # Print the collected IP addresses
    for ip in result:
        print(ip)