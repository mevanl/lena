import discord.ext.commands as commands
import random


coinflip_options = ['heads', 'tails']


class Coinflip(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx, userChoice: str):
        flip = random.choice(coinflip_options)
        await ctx.send(f'The coin landed on *{flip}!*')

        if userChoice[:5].lower() not in coinflip_options:
            await ctx.send('Please choose *heads* or *tails*.')
            return

        if userChoice[:5].lower() == flip:
            await ctx.send('***You won!***')
            return

        await ctx.send('***You lost!***')


async def setup(bot):
    await bot.add_cog(Coinflip(bot=bot))