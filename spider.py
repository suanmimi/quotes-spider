import json
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    rst = requests.get(url, timeout = 10)
    if rst.status_code !=200:
        return []
    return parse_page(rst.text)

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    data = []
    for i in quotes:
        txt = i.find("span", class_="text")
        ath = i.find("small", class_="author")
        data.append({"名句": txt.text, "作者": ath.text})
    return data

def main():
    page = 1
    all_rows = []
    while True:
        urls = []
        batch = []
        for i in range (page, page + 10):
            urls.append("https://quotes.toscrape.com/page/" + str(i) + "/")
        with ThreadPoolExecutor(max_workers=10) as url_pool:
            threads = [url_pool.submit(fetch_page, url) for url in urls]
            batch += [f.result() for f in threads]
            all_rows += batch
        if all(len(r) == 0 for r in batch):
            break
        page += 10
    
    table = []
    for content in all_rows:
        table += content
    print(len(table))
    
    with open("/tmp/quotes2.json", "w", encoding="utf-8") as file:
        json.dump(table, file, ensure_ascii=False, indent=2)    

if __name__ == "__main__":
    main()
