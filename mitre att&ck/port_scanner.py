from scapy.all import sr, IP, TCP

# ports to scan
# ftp, ssh, telnet, smtp, dns, http, pop3, msrpc, netbios-ssn, imap4, snmp, https, smb, rdp
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 161, 443, 445, 3389]


def SynScan(host):
    """
    Perform a SYN scan on the target host for the specified ports.
    SYN scan is a stealthy way to determine if ports are open, here we send a SYN packet and wait for a SYN-ACK response. here TCP 3 way handshake is not completed.
    :param host: Target IP address
    :return: None
    """

    # answered and unanswered packets
    # sr is a function that sends and receives packets
    # IP(dst=host) creates an IP packet with the destination set to the target host
    # TCP(sport=5555, dport=ports, flags="S") creates a TCP packet with the source port set to 5555, destination ports set to the list of ports, and the SYN flag set
    ans, unans = sr(IP(dst=host)/TCP(sport=5555, dport=ports, flags="S"), timeout=10, verbose=1)
    for s, r in ans:
        flags = r.sprintf("%TCP.flags%")
        if flags == "SA":  # SYN-ACK => open port
            print(f"Port {s[TCP].dport} is OPEN")
        elif flags == "RA":  # RST-ACK => closed port
            print(f"Port {s[TCP].dport} is CLOSED")
        else:
            print(f"Port {s[TCP].dport} got unexpected flags: {flags}")

if __name__ == "__main__":
    host = input("Enter the target IP address: ")
    SynScan(host)