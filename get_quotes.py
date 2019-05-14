"""
    Scrapes Quotes for Developers
"""

import requests
from bs4 import BeautifulSoup


def get_quotes():
    """Returns a lit of scrapped quotes"""

    scrape_url = "https://fortrabbit.github.io/quotes/"
    url_raw_data = requests.get(scrape_url)
    data = url_raw_data.text
    soup = BeautifulSoup(data, 'html5lib')
    quotes = []

    for block in soup.find_all('blockquote', attrs={'class': "hero-quote third half-t"}):
        quote = {}
        quote["quote"] = block.p.text.strip()
        quote["author"] = block.div.text
        quotes.append(quote)

    return quotes
