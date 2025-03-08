import openai
from g4f.client import Client

class Neuro():
    def __init__(self):
        self.client = Client()

    def make_answer(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text},],
            stream=True
        )
        if type(response) == dict:
            return "вернул словарь"
        return response.choices[0].message.content

