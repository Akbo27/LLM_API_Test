import os
import dotenv
from mistralai import Mistral

dotenv.load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-larget-latest"

client = Mistral(api_key=api_key)

def get_graph_details(user_input):
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        return {
            "function_name": chat_response["function_name"],
            "x_min": float(chat_response["x_min"]),
            "x_max": float(chat_response["x_max"])
        }
    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return {}