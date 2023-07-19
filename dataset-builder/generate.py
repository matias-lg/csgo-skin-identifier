from icrawler.builtin import GoogleImageCrawler
from search_terms import CSGO_SKIN_NAMES
import os

def search_and_save_term(search_term: str, output_dir, max_downloads: int = 100):
    google_crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
    google_crawler.crawl(keyword=search_term, max_num=max_downloads)

if __name__ == "__main__":
    dataset_dir = os.path.join(os.getcwd(), "dataset")
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)

    for skin_name in CSGO_SKIN_NAMES:
        search_and_save_term(f"{skin_name} csgo", os.path.join(os.getcwd(), "dataset", skin_name), 100)