from discord.ext import commands
import phrases

# For pi command
import subprocess

class remokommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send(phrases.testPhrase)
        print('Inf: Sent the test phrase.')

    @commands.group()
    async def pi(self, ctx):
        if ctx.invoked_subcommand is None:

            print('Command > pi')
            temp = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
            clock = '{0:.2f}'.format(float(subprocess.getoutput(
            'vcgencmd measure_clock arm').split('=')[1]) / 1000000000) + 'GHz'
            volt = subprocess.getoutput(
            'vcgencmd measure_volts core').split('=')[1]
            mem = subprocess.getoutput('vcgencmd get_mem arm').split('=')[1] + 'B'

            await ctx.send(phrases.statusAll.format(temp, clock, volt, mem))
            print('Inf: Replied to Command > pi')

    @pi.command()
    async def temp(self, ctx):
        status = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
        await ctx.send(phrases.statusTemp.format(status))
        print('Inf: Replied to Command > pi temp')

    @pi.command()
    async def clock(self, ctx):
        status = '{0:.2f}'.format(float(subprocess.getoutput(
            'vcgencmd measure_clock arm').split('=')[1]) / 1000000000) + 'GHz'
        await ctx.send(phrases.statusClock.format(status))
        print('Inf: Replied to Command > pi clock')

    @pi.command()
    async def vold(self, ctx):
        status = subprocess.getoutput(
            'vcgencmd measure_volts core').split('=')[1]
        await ctx.send(phrases.statusVolt.format(status))
        print('Inf: Replied to Command > pi volt')