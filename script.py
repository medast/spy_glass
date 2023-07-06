from facebook_scraper import get_posts
import pandas as pd
from spy_glass.lang_analysis.lang_fun import is_immobiliare_chat_ai
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

posts_list = []
info_required = ['post_id', 'text', 'post_text', 'shared_text', 'original_text', 'time', 'timestamp', 'shares', 'post_url',
                 'link', 'links', 'user_id', 'username', 'user_url']
# for post in get_posts('groups/215708061952730/',  page_limit=10):
for post in get_posts('groups/215708061952730/', pages=10):
    post_subset = {k: post[k] for k in info_required}
    posts_list.append(post_subset)

print(len(posts_list))

df = pd.DataFrame.from_dict(posts_list)


chat = ChatOpenAI(temperature=0.0)

template_string = """Dimmi se il post \
delimitato tra triplici apici riguarda la compravendita di un'immobile o una casa \
oppure l'affitto di un'immobile o una casa o comunque ha per argomento il mercato immobiliare. \
Rispondi solamente si o no. \
post: ```{post}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)
#df['immobiliare'] = df.apply(lambda x: is_immobiliare_chat_ai(x['text'], chat, prompt_template))
df['immobiliare'] = df['text'].apply(lambda x: is_immobiliare_chat_ai(x, chat, prompt_template))


path_save = 'C:\\Users\\medas\\Desktop\\Chiara_Facebook\\project\\result\\seconda_prova.xlsx'
df[['text', 'immobiliare', 'time', 'timestamp']].to_excel(path_save)
