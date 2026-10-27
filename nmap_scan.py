# nmap_scan.py
# Automates an Nmap TCP port scan (ports 21-443) against a target host
# using the python-nmap library.
# Requires: nmap installed, and `pip install python-nmap`
# Rebuilt from VU23215 Cert IV Cyber Security lab work (Kali Linux, April 2024).

import nmap

nm = nmap.PortScanner()
nm.scan('10.10.10.1', '21-443')

for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
