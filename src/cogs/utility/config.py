import os
import discord 

DEBUG = os.getenv("DEBUG", "").upper() == "TRUE"
DEBUG_GUILD_ID = int(os.getenv("DEBUG_GUILD", "1379896842950541396"))

def debug_guild_decorator():
    if DEBUG:
        return discord.app_commands.guilds(discord.Object(id=DEBUG_GUILD_ID))
    return lambda f: f  # No-op decorator if not in debug