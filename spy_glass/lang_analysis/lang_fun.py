

def ask_chat_bot(post, chat, template):
    customer_messages = template.format_messages(
        post=post)
    customer_response = chat(customer_messages)
    return customer_response.content
