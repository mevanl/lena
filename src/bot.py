import os
import asyncio
import dotenv
import discord 
from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv() 

# Check if in debug/dev modes
DEBUG_MODE = os.getenv("DEBUG", "").upper() == "TRUE"
DEBUG_GUILD_ID = int(os.getenv("DEBUG_GUILD", "1379896842950541396")) if DEBUG_MODE else 0


# Setup intents and bot
intents = discord.Intents.default()
intents.message_content = True 
lena = commands.Bot(command_prefix=".", intents=intents, help_command=None)
command_categories = {}

@lena.event
async def on_ready():

    # Uncomment this only when you want to clean up old global commands
    # await lena.tree.clear_commands(guild=None)

    if DEBUG_MODE and DEBUG_GUILD_ID:
        print("Debug mode enabled.")
        guild = discord.Object(id=DEBUG_GUILD_ID)
        synced = await lena.tree.sync(guild=guild)
    else:
        print("Global mode enabled.")
        synced = await lena.tree.sync()

    print(f"Synced {len(synced)} command(s):")
    for cmd in synced:
        print(f"- {cmd.name}")

    print(f'Logged in as: {lena.user}.')


async def start():
    await load_cogs()
    await lena.start(os.getenv('TOKEN'))

async def load_cogs():

    # dir is a category each holding different commands (cogs)
    for dir in os.listdir('./cogs'):

        # utility is helpers for cogs 
        if dir == "utility":
            continue

        # each category will have a list of cogs in it
        command_categories[dir] = []

        for file in os.listdir('./cogs/' + dir):
            if file.endswith('.py'):
                command_categories[dir].append(file)
                await lena.load_extension(f'cogs.{dir}.{file[:-3]}') 

if __name__ == "__main__":
    asyncio.run(start())

