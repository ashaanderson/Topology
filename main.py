from trace import trace_route
import result

public_ipaddr = "138.238.{}.{}"

def main():
    result.init()
    for i in range(0, 256):
        for j in range(0, 256):
            current_ip_address = public_ipaddr.format(i, j)
            found_ip_addresses = trace_route(current_ip_address)
            
            # Store the IP addresses found for the current IP Address
            result.dump_trace(current_ip_address, found_ip_addresses)
            
        #     break
        # break

if __name__ == "__main__":
    main()