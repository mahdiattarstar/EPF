import requests
from bs4 import BeautifulSoup
import json

# File to track processed pages
TRACKING_FILE = "processed_pages.json"

# Load processed pages from file
def load_processed_pages():
    try:
        with open(TRACKING_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save processed pages to file
def save_processed_pages(pages):
    with open(TRACKING_FILE, "w") as f:
        json.dump(pages, f)

# Main scraping function
def scrape_site(base_url, start_page=1):
    processed_pages = load_processed_pages()
    current_page = start_page

    while True:
        url = f"{base_url}?page={current_page}"
        if url in processed_pages:
            print(f"Skipping already processed page: {url}")
            current_page += 1
            continue

        print(f"Processing page: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page: {url}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract desired data here
        # Example: titles = [item.text for item in soup.select(".title")]
        # print(titles)

        # Mark the page as processed
        processed_pages.append(url)
        save_processed_pages(processed_pages)

        # Check if there is a "next" page
        next_button = soup.select_one("a.next")
        if not next_button:
            print("No more pages to process.")
            break

        current_page += 1

# Run the scraper
scrape_site("https://example.com/items")
