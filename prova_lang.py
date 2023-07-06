from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from spy_glass.lang_analysis.lang_fun import is_immobiliare_chat_ai

chat = ChatOpenAI(temperature=0.0)

template_string = """Dimmi se il post \
delimitato tra triplici apici riguarda la compravendita di un'immobile o una casa \
oppure l'affitto di un'immobile o una casa o comunque ha per argomento il mercato immobiliare. \
Rispondi si o no. \
post: ```{post}```
"""

post = """Vendo appartamento in zona Centocelle,piano terra , interamente da ristrutturare per questo il prezzo è basso.
Composto da angolo cottura ,bagno e camera da letto .
50 mq.
Il prezzo non è trattabile."""

prompt_template = ChatPromptTemplate.from_template(template_string)

customer_messages = prompt_template.format_messages(
                    post=post)

customer_response = chat(customer_messages)

print(customer_response.content)


a = is_immobiliare_chat_ai(post, chat, prompt_template)
print('7777777')
print(a)


