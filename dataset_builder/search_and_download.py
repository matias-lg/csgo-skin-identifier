from icrawler.builtin import GoogleImageCrawler
from search_terms import CSGO_SKIN_NAMES
import os

def search_and_save_term(search_term: str, output_dir, max_downloads: int = 100):
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': output_dir}
        )
    google_crawler.crawl(keyword=search_term, max_num=max_downloads)

if __name__ == "__main__":
    output_dir = os.path.join(os.getcwd(), "downloaded_images")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for skin_name in CSGO_SKIN_NAMES:
        print(skin_name)
        [weapon_search_term, skin_name, weapon_full_name] = skin_name
        search_term = f"{weapon_search_term} {skin_name}"
        label_name = f"{weapon_full_name} | {skin_name}"
        search_and_save_term(search_term, os.path.join(os.getcwd(), "dataset", label_name), 70)