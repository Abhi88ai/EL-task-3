import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch website")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# BBC headlines are in h2 tags
headlines = soup.find_all("h2")

today = datetime.now().strftime("%d-%m-%Y")

with open("headlines.txt", "w", encoding="utf-8") as file:
    file.write(f"Top Headlines Headlines - {today}\n")
    file.write("-" * 40 + "\n")

    count = 0
    for h in headlines:
        title = h.get_text(strip=True)
        if title and len(title) > 20:
            file.write(title + "\n")
            count += 1

print("✅ Headlines fetched and saved successfully!")
print("Total headlines:", count)
