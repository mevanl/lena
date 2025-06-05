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
command_categories = {}

@lena.event
async def on_ready():
    print(f'Logged in as: {lena.user}')


async def start():
    await load_cogs()
    await lena.start(os.getenv('TOKEN'))

async def load_cogs():

    # dir is a category each holding different commands (cogs)
    for dir in os.listdir('./cogs'):

        # each category will have a list of cogs in it
        command_categories[dir] = []

        for file in os.listdir('./cogs/' + dir):
            if file.endswith('.py'):
                command_categories[dir].append(file)
                await lena.load_extension(f'cogs.{dir}.{file[:-3]}') 

if __name__ == "__main__":
    asyncio.run(start())

