# Example: scrape quotes from http://quotes.toscrape.com/
# Save results to quotes.csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

BASE_URL = "http://quotes.toscrape.com"

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ExampleBot/1.0)"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.text

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in quote.select(".tags .tag")]
        rows.append({"text": text, "author": author, "tags": ",".join(tags)})
    return rows

def scrape_all_pages():
    data = []
    url = BASE_URL
    while True:
        html = fetch_page(url)
        data.extend(parse_quotes(html))
        soup = BeautifulSoup(html, "html.parser")
        next_btn = soup.select_one("li.next > a")
        if not next_btn:
            break
        next_path = next_btn["href"]
        url = BASE_URL + next_path
        time.sleep(random.uniform(0.5, 1.5))  # polite crawling
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = scrape_all_pages()
    print(df.head())
    df.to_csv("quotes.csv", index=False)
    print("Saved quotes.csv with", len(df), "rows")