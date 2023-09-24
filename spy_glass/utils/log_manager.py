import os
import pandas as pd


class LogManager:
    def __init__(self):
        self.dir_path = os.path.dirname(__file__)
        self.root_path = os.path.split(self.dir_path)[0]
        self.log_dir_path = os.path.join(self.root_path, 'log')
        self.log_file_path = os.path.join(self.log_dir_path, 'log.csv')
        self.history_log_file_path = os.path.join(self.log_dir_path, 'log_history.csv')
        self.actual_log = pd.read_csv(self.log_file_path)
        self.post_to_exclude = [int(post_id) for post_id in list(self.actual_log['id'])]

    def update_log_file(self, df):
        df['telegram_date'] = pd.Timestamp.today()
        df = df[['id', 'telegram_date']]
        to_update_df = pd.concat([self.actual_log, df])
        os.remove(self.log_file_path)
        to_update_df[['id', 'telegram_date']].to_csv(self.log_file_path)

    def update_log_history_file(self, df):
        history_log = pd.read_csv(self.history_log_file_path)
        df['telegram_date'] = pd.Timestamp.today()
        df = df[['id', 'telegram_date']]
        to_update_df = pd.concat([history_log, df])
        os.remove(self.history_log_file_path)
        to_update_df[['id', 'telegram_date']].to_csv(self.history_log_file_path)

    def filter_df_for_telegram_message(self, df):
        return df[~df['id'].isin(self.post_to_exclude)]
