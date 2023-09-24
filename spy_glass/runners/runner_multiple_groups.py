from spy_glass.scrape.facebook_page_scrape import PageScrape
from spy_glass.config_default import config_default
from spy_glass.lang_analysis.lang_chat import Chat
from spy_glass.telegram.telegram_bot import MessageBot
from spy_glass.telegram.messages import message_real_estate
from spy_glass.utils.log_manager import LogManager

credentials = (config_default['username'], config_default['password'])
page_scraper = PageScrape(credentials[0], credentials[1])
page_scraper.delete_old_scraped()
page_scraper.scrape_groups(config_default['group_list'], post_count=10)
scraped_df = page_scraper.load_scraped_data()
log_manager = LogManager()
fresh_scraped_df = log_manager.filter_df_for_telegram_message(scraped_df)
chat = Chat(config_default['template_prompt'], config_default['openai_api_key'])
lang_df = chat.add_chat_column(fresh_scraped_df, config_default['lang_col'])
message_lang_df = lang_df[lang_df[config_default['lang_col']]]

bot = MessageBot(config_default['bot_token'], config_default['chat_id'], message_real_estate)
bot.send_message_for_df_rows(message_lang_df, config_default['message_col'])
log_manager.update_log_file(message_lang_df)
log_manager.update_log_history_file(message_lang_df)
