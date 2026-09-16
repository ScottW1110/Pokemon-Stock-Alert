import os
import requests

PRODUCT_CODE = "9951370"

url = f"https://www.argos.co.uk/product/{PRODUCT_CODE}"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1"
}

response = requests.get(url, headers=headers, timeout=15)

print("Status:", response.status_code)
print("Page length:", len(response.text))

if "__NEXT_DATA__" in response.text:
    print("NEXT_DATA_FOUND")
else:
    print("NEXT_DATA_NOT_FOUND")
