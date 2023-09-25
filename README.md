# spy_glass
Using a basic RAG model as a tool to generate alerts from scraped Facebook information and report them to the user via a Telegram bot.

Divided into three parts:

-Facebook scraper: Given a Facebook account and a list of pages, it scrapes the data.
-LLM RAG model: Utilizes a language model to filter relevant information based on a custom template prompt.
-Telegram bot: Sends alerts to the user containing relevant information for their web research.
