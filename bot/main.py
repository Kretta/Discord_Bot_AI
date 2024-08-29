# bot/main.py

import discord
from bot.config import DISCORD_TOKEN
from events.on_ready import beim_starten
from events.on_message import beim_nachricht_empfangen

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await beim_starten(client)

@client.event
async def on_message(message):
    await beim_nachricht_empfangen(message)

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
