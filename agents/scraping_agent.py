
import requests
from bs4 import BeautifulSoup

class ScrapingAgent:
    def __init__(self, url):
        self.url = url

    def scrape_filings(self):
        """
        Fetches and parses filings or documents from the given URL.
        Returns a list of extracted text contents relevant to filings.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: extract all paragraphs text
            paragraphs = soup.find_all('p')
            filings_text = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

            return filings_text

        except requests.exceptions.RequestException as e:
            print(f"Error while fetching data: {e}")
            return []
