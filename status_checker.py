import socket
import time
import urllib.request
import urllib.error
from urllib.parse import urlparse

website = input("🌐 Target Website: ")

if not website.startswith(("http://", "https://")):
    website = "https://" + website

hostname =  urlparse(website).netloc

ip_address = socket.gethostbyname(hostname)
print("\nScanning...\n")

try:
    start = time.perf_counter()

    response = urllib.request.urlopen(website)

    end = time.perf_counter()

    print("\n" + "=" * 50)
    print("          🔥 CYBERLAB STATUS CHECKER 🔥")
    print("=" * 50)

    print(f"📍 IP Address  : {ip_address}")
    print(f"🌐 Target      : {website}")
    print(f"📡 Status Code : {response.status}")
    print(f"🖥️  Server      : {response.headers.get('Server')}")
    print(f"⚡ Response    : {end-start:.3f} sec")

    print("=" * 50)
except urllib.error.URLError as e:
    print(f"\n❌ Error: {e}")
    
    