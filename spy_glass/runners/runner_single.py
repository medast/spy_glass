from spy_glass.scrape.facebook_scrape import Scrape
from spy_glass.config_default import config_default
from spy_glass.lang_analysis.lang_chat import Chat
from spy_glass.telegram.telegram_bot import MessageBot
from spy_glass.telegram.messages import message_real_estate


scraped_df = Scrape.scrape_from_group(config_default['group_id'])
chat = Chat(config_default['template_prompt'])
lang_df = chat.add_chat_column(scraped_df, config_default['lang_col'])
print(lang_df)
print(lang_df.info(True))
message_lang_df = lang_df[lang_df[config_default['lang_col']]]
print(message_lang_df)
bot = MessageBot(config_default['bot_token'], config_default['chat_id'], message_real_estate)
bot.send_message_for_df_rows(message_lang_df, config_default['message_col'])

