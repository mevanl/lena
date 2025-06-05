import discord.ext.commands as commands
import random

rps_options = ['Rock!', 'Paper!', 'Scissors']


class RPS(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, user_choice: str):
        lena_choice: str = random.choice(rps_options)
        await ctx.send(f'{lena_choice}')

        # same choice
        if lena_choice[0].lower() == user_choice[0].lower():
            await ctx.send('***We tied!***')
            return

        # lena chose rock
        if lena_choice[0].lower() == 'r' and user_choice[0].lower() == 'p':
            await ctx.send('***You won!***')
            return

        if lena_choice[0].lower() == 'r' and user_choice[0].lower() == 's':
            await ctx.send('***You lost!***')
            return

        # lena chose scissors
        if lena_choice[0].lower() == 's' and user_choice[0].lower() == 'r':
            await ctx.send('***You won!***')
            return

        if lena_choice[0].lower() == 's' and user_choice[0].lower() == 'p':
            await ctx.send('***You lost!***')
            return

        # lena chose paper
        if lena_choice[0].lower() == 'p' and user_choice[0].lower() == 's':
            await ctx.send('***You won!***')
            return

        if lena_choice[0].lower() == 'p' and user_choice[0].lower() == 'r':
            await ctx.send('***You lost!***')
            return


async def setup(bot):
    await bot.add_cog(RPS(bot=bot))