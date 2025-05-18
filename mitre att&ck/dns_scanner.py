from scapy.all import sr, IP, UDP, DNS , DNSQR

def dns_scan(host):
    """
    Perform a DNS scan on the target host for the specified ports.
    :param host: Target IP address
    :return: None
    """
    # DNS query
    dns_query = DNS(rd=1, qd=DNSQR(qname="facebook.com", qtype="A"))
    
    # Send DNS query to the target host
    ans, unans = sr(IP(dst=host)/UDP(dport=53)/dns_query, timeout=2, verbose=0)
    for s, r in ans:
        if r.haslayer(DNS) and r[DNS].ancount > 0:
            print(f"DNS response from {host}: {r[DNS].summary()}")
        else:
            print(f"No DNS response from {host}")

if __name__ == "__main__":
    host = input("Enter the target IP address: ")
    dns_scan(host)