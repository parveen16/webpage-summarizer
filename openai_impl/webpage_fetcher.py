import requests
from bs4 import BeautifulSoup

# Headers to mimic a real browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

class Website:
    """
    Downloads a webpage, removes unnecessary elements, and extracts
    clean, readable text along with the title.
    """
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"

        # Remove scripts, styles, images, inputs
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()

        # Extract readable text
        self.text = soup.body.get_text(separator="\n", strip=True)