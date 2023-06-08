import openai

from constants import *

# tokens and keys saved in contants.py file

messages = []

openai.api_key = key2

def chatgpt(query):

    messages.append({"role": "user", "content": query})

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(chat_response)
    messages.append({"role": "assistant", "content": chat_response})
    return(chat_response)