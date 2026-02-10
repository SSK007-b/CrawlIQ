import requests
from bs4 import BeautifulSoup
from app.services.utils import clean_text


class GenericScraper:

    def __init__(self, url: str):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        }

    def fetch(self):
        response = requests.get(self.url,headers=self.header, timeout=10)
        return response.text

    def extract(self):
        html = self.fetch()
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        paragraphs = [p.get_text() for p in soup.find_all("p")]
        raw_text = " ".join(paragraphs)

        cleaned = clean_text(raw_text)

        return {"url": self.url, "product_name": title, "cleaned_text": cleaned}
