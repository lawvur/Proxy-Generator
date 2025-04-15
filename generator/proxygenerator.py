import requests
import random

def fetch_proxies(proxy_type="http"):
    print(f"Fetching {proxy_type.upper()} proxies...")

    urls = {
        "http": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all",
        "socks4": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
        "socks5": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
    }

    url = urls.get(proxy_type.lower())
    if not url:
        print("❌ Invalid proxy type.")
        return []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.text.strip().split('\n')
            proxies = [proxy for proxy in proxies if proxy]
            print(f"Fetched {len(proxies)} proxies.")
            return proxies
        else:
            print(f"Failed to fetch proxies: Status code {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching proxies: {e}")
        return []

def save_proxies_to_file(proxies, proxy_type):
    if not proxies:
        print("No proxies to save.")
        return

    filename = f"{proxy_type}_proxies.txt"
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(proxy + "\n")
    print(f"Saved to {filename}")

def main():
    print("Proxy Generator by Paranoia (@listeningon)")
    proxy_type = input("proxy type (http / https / socks4 / socks5): ").strip().lower()
    amount = input("how many proxies to save? (leave blank for all): ").strip()

    proxies = fetch_proxies(proxy_type)
    if amount.isdigit():
        proxies = random.sample(proxies, min(int(amount), len(proxies)))

    save_proxies_to_file(proxies, proxy_type)

if __name__ == "__main__":
    main()
