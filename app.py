
from groq import Groq

client = Groq(
    api_key="",
)


def talk(query):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
                
            }
        ],
        model="llama-3.1-8b-instant",
    )
    print("Bot: ", chat_completion.choices[0].message.content)


while True:
    query = input("USER_: ")
    if query == "exit":
        break
    else:
        talk(query)

