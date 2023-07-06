from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from spy_glass.lang_analysis.lang_fun import ask_chat_bot


class Chat:
    def __init__(self, template_prompt, temperature=0.0):
        self.template_prompt = template_prompt
        self.temperature = temperature
        self.chat = ChatOpenAI(temperature=temperature)

    def add_chat_column(self, df, col_name):
        prompt_template = ChatPromptTemplate.from_template(self.template_prompt)
        df[col_name] = df['text'].apply(lambda x: bool(ask_chat_bot(x, self.chat, prompt_template)))
        return df
