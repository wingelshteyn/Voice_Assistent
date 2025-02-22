from g4f.client import Client


class Neuro():
    def __init__(self):
        self.client = Client()

    def make_answer(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
        )
        if type(response) == dict:
            return "вернул словарь"
        return response.choices[0].message.content

    # def make_picture(self, prompt):
    #     response = self.client.images.generate(
    #       model="gemini",
    #       prompt=prompt,
    #     )
    #     image_url = response.data[0].url
    # короче тут с картинками у меня
