import os
import asyncio
import discord 
from discord.ext import commands

import dotenv 
dotenv.load_dotenv() 

# Setup intents and bot
intents = discord.Intents.default()
intents.message_content = True 
lena = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@lena.event
async def on_ready():
    print(f'Logged in as: {lena.user}')


asyncio.run(lena.start(os.getenv('TOKEN')))