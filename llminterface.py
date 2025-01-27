import os
import dotenv
from mistralai import Mistral

dotenv.load_dotenv()

class LLMInterface:
    def __init__(self):
        self.api_key = os.environ["MISTRAL_API_KEY"]
        self.model = "mistral-larget-latest"
        self.client = Mistral(api_key=self.api_key)

    def extract_plot_details(self, user_input):
        response = self.client.chat.complete(
            model=self.model,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"]