import dns
import dns.resolver
import socket

def reverse_dns(ip):
    """
    Perform a reverse DNS lookup for the given IP address and print the result.
    :param ip: The target IP address to resolve.
    :return: A list of resolved hostnames or an empty list if not found.
    """
    try:
        # Perform reverse DNS resolution
        result = socket.gethostbyaddr(ip)
        print(f"IP {ip} resolved to {result[0]}")
        return [result[0]]+result[1]
    except socket.herror:
        print(f"IP {ip} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []

def DNSRequest(domain):
    """
    Perform a DNS request for the given domain and print the result.
    :param domain: The target domain to resolve.
    :return: None
    """
    try:
        # Perform DNS resolution
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"Domain {domain} resolved to {ipval}")
            # Perform reverse DNS resolution
            print(f"Domain names : {reverse_dns(str(ipval))}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"Domain {domain} does not exist.")
        # pass
    except Exception as e:
        print(f"An error occurred: {e}")
        # pass

def subdomain_search(domain, subdomains, numbered):
    """
    Search for subdomains of a given domain using a list of common subdomains.
    :param domain: The target domain to search for subdomains.
    :param subdomains: A list of common subdomains to check.
    :param numbered: if True, Check subdomains with numbers appended (e.g., subdomain1, subdomain2).
    :return: None
    """
    for subdomain in subdomains:
        subdomain_url = f"{subdomain}.{domain}"
        DNSRequest(subdomain_url)
        if numbered:
            for i in range(1, 10):
                subdomain_url = f"{subdomain}{i}.{domain}"
                DNSRequest(subdomain_url)

if __name__ == "__main__":
    subdomains = [
        "www", "mail", "remote", "blog", "ftp", "test", "dev", "staging", "api", "admin",
        "portal", "webmail", "vpn", "secure", "support", "shop", "store", "forum",
        "docs", "wiki", "news", "events", "calendar", "status", "community", "partners",
        "careers", "jobs", "about", "contact", "privacy", "terms", "legal", "help", "feedback", 
        "resources", "downloads", "media", "press", "gallery", "videos", "podcasts", 
        "blog", "social"
    ]
    domain = input("Enter the target domain: ")
    numbered = True
    subdomain_search(domain, subdomains, numbered)