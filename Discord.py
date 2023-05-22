

import os
import discord
from dotenv import load_dotenv
intents = discord.Intents().all()
client = discord.Client(intents=intents)
load_dotenv()
TOKEN = os.getenv('MTAwODA5MzAwMzU5MzgxODE2Mw.G4Rnwd.EjFghjRJec0GulvcAHyq-hj8kdqu5uVgcZopNc')



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)