import requests
import os
import dotenv
from mistralai import Mistral

dotenv.load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-larget-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model
    messages= [
        {
            "role":"user",
            "content": "Hi! I need a plot of sine function on interval from -5 to 5"
        }
    ]
)