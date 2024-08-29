# bot/events/on_ready.py

from xmlrpc import client


# events/on_ready.py

async def beim_starten(client):
    print(f'Bot ist bereit und eingeloggt als {client.user}')



