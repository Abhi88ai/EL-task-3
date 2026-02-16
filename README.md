# EL-task-3
# Web Scraper for News Headlines

## Objective
To scrape top news headlines from a public news website and store them in a text file using Python.

## Tools Used
- Python
- requests
- BeautifulSoup

## Files Included
- news_scraper.py → Python scraping script
- headlines.txt → Scraped news headlines
- README.md → Project documentation

## How It Works
1. Sends an HTTP request to Times of India website
2. Parses HTML using BeautifulSoup
3. Extracts headline text
4. Saves headlines into a .txt file

## How to Run
bash
pip install requests beautifulsoup4
python news_scraper.py
