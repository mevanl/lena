import os
import random
import discord
import discord.ext.commands as commands
from ..utility import config 


rps_options = ['Rock!', 'Paper!', 'Scissors']



class RPS(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="rps", description="Play rock, paper, scissors with Lena.")
    @discord.app_commands.describe(user_choice="Choose rock, paper, or scissors!")
    @config.debug_guild_decorator()
    async def rps(self, ctx: commands.Context, user_choice: str):
        await self._play_rps(ctx.send, user_choice)

    # autocomplete choices for slash command
    @rps.autocomplete('user_choice')
    async def user_choice_autocomplete(self, interaction: discord.Interaction, current_msg: str):
       return [
           discord.app_commands.Choice(name=opt[:-1], value=opt[:-1].lower())
           for opt in rps_options if current_msg.lower() in opt.lower()
       ]

    # rps logic 
    async def _play_rps(self, send_func, user_choice: str):
        lena_choice = random.choice(rps_options)
        await send_func(f'{lena_choice}')

        user_choice = user_choice[0].lower()
        lena_choice = lena_choice[0].lower()

        if user_choice == lena_choice:
            await send_func('***We tied!***')
        elif (user_choice == 'r' and lena_choice == 's') or (user_choice == 's' and lena_choice == 'p') or (user_choice == 'p' and lena_choice == 'r'):
            await send_func('***You won!***')
        else:
            await send_func('***You lost!***')


async def setup(bot: commands.Bot):
    await bot.add_cog(RPS(bot))