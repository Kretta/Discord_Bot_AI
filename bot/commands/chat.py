# bot/commands/chat.py

import openai
from bot.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def handle(prompt):
    try:
        antwort = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return antwort.choices[0].text.strip()
    except Exception as e:
        return f'Fehler bei der Anfrage: {str(e)}'
