import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://geonode.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://geonode.com/",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


def filter_http_proxies(input_file, output_file):
    with open(input_file) as file:
        proxies = file.readlines()

    with open(output_file, "w") as file:
        for proxy in proxies:
            if "http" in proxy:
                file.write(proxy)
        print("Completed filtering proxies") 


def scrape_proxy_from_geonode(page):
    url = f"https://proxylist.geonode.com/api/proxy-list?limit=100&page={page}&sort_by=lastChecked&sort_type=desc"

    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def bulk_scrape_proxies_from_geonode(input_file):
    with open(input_file, "a") as file:
        # file.write("PROTOCOL://IP:PORT|ANONYMITY|LATENCY(ms)|SPEED(ms)|COUNTRY\n")
        for page in range(1, 30):
            proxies = scrape_proxy_from_geonode(page)
            for proxy in proxies.get("data", []):
                ip = proxy.get("ip")
                port = proxy.get("port")
                latency = proxy.get("latency", "")
                speed = proxy.get("speed", "")
                protocol = proxy.get("protocols", [""])[0]
                country = proxy.get("country", "")
                anonimity = proxy.get("anonymityLevel", "")
                file.write(
                    f"{protocol}://{ip}:{port}\n"
                )
            print(f"{page=} scraped")
        print("Completed scraping proxies")

if __name__ == "__main__":
    input_file = "proxies.txt"
    output_file = "http_proxies.txt"
    bulk_scrape_proxies_from_geonode(input_file)
    filter_http_proxies(input_file, output_file)