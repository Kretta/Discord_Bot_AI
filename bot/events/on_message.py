# bot/events/on_message.py

import openai
from bot.config import BOT_NAME, OPENAI_API_KEY
from bot.commands import chat

openai.api_key = OPENAI_API_KEY

async def beim_nachricht_empfangen(nachricht):
    if nachricht.author == nachricht.guild.me:
        return

    if nachricht.guild.me.mentioned_in(nachricht) or nachricht.content.startswith('!'):
        if nachricht.guild.me.mentioned_in(nachricht):
            prompt = nachricht.content.replace(f'@{BOT_NAME}', '').strip()
        else:
            prompt = nachricht.content[1:]  # Entfernt das "!" von der Nachricht

        antwort_text = await chat.handle(prompt)
        await nachricht.channel.send(antwort_text)
