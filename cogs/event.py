from asyncio import events
from discord.ext import commands
import phrases

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "event" is instantiated.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Good Morning
        if 'おはよ' in message.content:
            await message.channel.send(phrases.goodMorning)
            print('sent goodMorning.')
            return

        # Love
        if 'すき' in message.content:
            await message.channel.send(phrases.love)
            print('sent love.')
            return


def setup(bot):
    bot.add_cog(event(bot))
    