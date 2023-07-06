import telebot


class MessageBot:
    def __init__(self, bot_token, chat_id, message):
        self.bot_token = bot_token
        self.bot = telebot.TeleBot(self.bot_token)
        self.chat_id = chat_id
        self.message = message

    def send_message_for_df_rows(self, df, col_link):
        for link in df[col_link]:
            formatted_message = self.message.format(link=link)
            self.bot.send_message(chat_id=self.chat_id,
                                  text=formatted_message)
