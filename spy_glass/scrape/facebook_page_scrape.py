import pandas as pd
from facebook_page_scraper import Facebook_scraper
import os


class PageScrape:
    def __init__(self, user, password, browser = "chrome", proxy_port = 10001):
        self.user = user
        self.password = password
        self.browser = browser
        self.proxy_port_start = proxy_port
        self.posts_count = 100
        self.timeout = 600  # 600 seconds
        self.headless = False
        self.result_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir, 'result'))

    def scrape_groups(self, groups, post_count=None):
        if post_count is None:
            post_number = self.posts_count
        else:
            post_number = post_count
        proxy_port = self.proxy_port_start

        for group in groups:
            page = f'groups/{group}'
            proxy = f'{self.user}:{self.password}@us.smartproxy.com:{proxy_port}'
            scraper = Facebook_scraper(page, post_number, self.browser, proxy=proxy,
                                       timeout=self.timeout, headless=self.headless)

            filename = group
            scraper.scrap_to_csv(filename, self.result_dir)

            proxy_port += 1

    def load_scraped_data(self):
        os.chdir(self.result_dir)
        file_list = os.listdir()
        dfs = [pd.read_csv(os.path.join(self.result_dir, file))for file in file_list]
        return pd.concat(dfs).reset_index()

    def delete_old_scraped(self):
        os.chdir(self.result_dir)
        file_list = os.listdir()
        for file in file_list:
            os.remove(os.path.join(self.result_dir, file))
