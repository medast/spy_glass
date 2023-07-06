from facebook_scraper import get_posts
import pandas as pd
from typing import List
import time

from spy_glass.scrape.scrape_config import info_required


class Scrape:

    @staticmethod
    def scrape_from_group(group_id: str):
        posts_list = []
        for post in get_posts(f'groups/{group_id}/'):
            post_subset = {k: post[k] for k in info_required}
            posts_list.append(post_subset)
        return pd.DataFrame.from_dict(posts_list)

    @staticmethod
    def scrape_from_groups(groups: List[str]):
        posts_list = []
        for group_id in groups:
            for post in get_posts(f'groups/{group_id}/'):
                post_subset = {k: post[k] for k in info_required}
                posts_list.append(post_subset)
            time.sleep(5)
        return pd.DataFrame.from_dict(posts_list)


