import discord
import discord.ext.commands as commands
import random
from ..utility import config 


coinflip_options = ['heads', 'tails']


class Coinflip(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="coinflip", description="Flip a coin.")
    @discord.app_commands.describe(user_choice="Pick heads or tails.")
    @config.debug_guild_decorator()
    async def coinflip(self, ctx, user_choice: str):
        flip = random.choice(coinflip_options)
        await ctx.send(f'The coin landed on *{flip}!*')

        if user_choice[:5].lower() not in coinflip_options:
            await ctx.send('Please choose *heads* or *tails*.')
            return

        if user_choice[:5].lower() == flip:
            await ctx.send('***You won!***')
            return

        await ctx.send('***You lost!***')


async def setup(bot):
    await bot.add_cog(Coinflip(bot=bot))