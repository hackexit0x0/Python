from scapy.all import ARP, Ether, srp
import platform
import os
import ipaddress

def network_scanner(gateway_ip):
    # Get the subnet from the gateway IP
    gateway = ipaddress.ip_address(gateway_ip)
    subnet = ipaddress.ip_network(f"{gateway}/24", strict=False)

    # Create ARP request
    arp = ARP(pdst=str(subnet))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Lists to hold live hosts
    live_hosts = []

    for sent, received in result:
        live_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

    return live_hosts

def identify_os(ip):
    # Attempt to identify the OS
    try:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")  # For Linux/Unix
        if response == 0:
            # Here, you can expand the logic to use Nmap or similar tools
            return platform.system()  # This will return the OS of the machine running the script
        else:
            return "Unknown"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    gateway_ip = "192.168.1.1"  # Replace with your gateway IP
    live_hosts = network_scanner(gateway_ip)

    print("Live hosts in the network:")
    for host in live_hosts:
        os_version = identify_os(host['ip'])  # Identify the OS of the live host
        print(f"IP: {host['ip']}, MAC: {host['mac']}, OS: {os_version}")
