import os
import shutil
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

OUTPUT_DIRECTORY = "tagesschau_dump"

BASE_URL = "https://www.tagesschau.de"
DATUM = [
    "2025-07-03",
]
FILTER = [
    "ausland",
    "inland",
    "wirtschaft"
]


def get_article_links(
        archive_url,
):
    res = requests.get(archive_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    links = set()
    # Find all article links in the archive. Adjust the selector if necessary.
    for a in soup.select('a.teaser-right__link'):
        href = a.get('href')
        if href and href.startswith("/"):
            full_url = BASE_URL + href
            links.add(full_url)
    return list(links)


def scrape_article(
        url,
):
    res = requests.get(url)
    res.raise_for_status()
    main_content = BeautifulSoup(res.text, "html.parser")

    for selector in [
        'script',
        'style',  # Scripts and styles
        '.header',
        '.header-fancy-v2',
        '.copytext-element-wrapper',
        '.footer',
        '.meldungsfooter',
        '.absatzbild__info__text'
    ]:
        for elem in main_content.select(selector):
            elem.decompose()
    further_articles = main_content.find_all("aside")

    for article in further_articles:
        article.decompose()

    article_text = ""
    for tag in main_content.find_all(
            [
                'p',
                'h1',
                'h2'
            ],
    ):
        article_text += tag.text + "\n\n"

    return article_text


def main():
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for datum in DATUM:
        # Delete only the specific date folder if it exists
        date_dir_path = os.path.join(OUTPUT_DIRECTORY, datum)
        if os.path.exists(date_dir_path):
            shutil.rmtree(date_dir_path)
            print(f"Removed existing date folder: {date_dir_path}")
        
        for category in FILTER:
            archive_url = BASE_URL + "/archiv?datum=" + datum + "&filter=" + category
            article_links = get_article_links(archive_url)

            article_count = 0
            output_dir_path = os.path.join(OUTPUT_DIRECTORY, datum, category)
            os.makedirs(output_dir_path, exist_ok=True)
            
            # Use tqdm for progress bar
            progress_bar = tqdm(article_links, desc=f"Scraping {datum}/{category}", unit="article")
            for url in progress_bar:
                try:
                    # Update progress bar with current URL
                    progress_bar.set_postfix_str(url, refresh=True)
                    article = scrape_article(url)
                    time.sleep(1)
                    article_name = "article_" + str(article_count) + ".md"
                    file_path = os.path.join(output_dir_path, article_name)
                    article_count += 1
                    with open(file_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(article)
                except Exception as e:
                    progress_bar.write(f"Failed to scrape {url}: {e}")


if __name__ == "__main__":
    main()
