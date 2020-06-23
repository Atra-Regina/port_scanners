import time # to make a little sleep time to not get bombarded with all info at once
import nmap # You need to install nmap on your machine (pip install --user python-nmap)

# initialize scanner
nm = nmap.PortScanner()
host = '127.0.0.1' # define the host

nm.scan(host, '1-1024', '-v --version-all') #host, ports range and version

print("Stats: ", nm.scanstats())
print("\nWaiting >>>>")
time.sleep(2) # wait 2 secs before information explosion

print("State: ", nm[host].state())
print("Hostnames are: ", nm[host].hostnames())
print("All IP ports: ", nm[host].all_ip())
print("All protocols detected: ", nm[host].all_protocols())
print("TCP port numbers detected: ", nm[host]['tcp'].keys())
# print(nm[host].tcp(22)) # uncomment that and put the tcp port from dict_keys
