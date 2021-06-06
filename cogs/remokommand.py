from discord.ext import commands
import phrases

# For pi command
import subprocess

# For sendwol command
import binascii
import socket

# Custom Libraries
import loadenv

# from: https://emptypage.jp/gadgets/wol.html
def sendWol(macs, ipaddr, port):
    print('Command > wol')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    for mac in macs:
        for sep in ':-':
            if sep in mac:
                mac = ''.join([x.rjust(2, '0') for x in mac.split(sep)])
                break
        mac = mac.rjust(12, '0')
        p = '\xff' * 6 + binascii.unhexlify(mac) * 16
        s.sendto(p, (ipaddr, port))
    s.close()
    print('sent magic packet.')
    return 0

class remokommand(commands.Cog):

    # コンストラクタ: インスタンス生成時に1回だけ呼び出し
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "remokommand" is instantiated.')

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

    @pi.command()
    async def mem(self, ctx):
        status = subprocess.getoutput(
            'vcgencmd get_mem arm').split('=')[1] + 'B'
        await ctx.send(phrases.statusMem.format(status))
        print('Inf: Replied to Command > pi mem')


    @commands.command()
    async def wol(self, ctx):
        s = sendWol(loadenv.ADDRESS, loadenv.IP, 9)
        if s == 0:
            await ctx.send(phrases.wolSuccess)
        else:
            await ctx.send(phrases.wolFailure)

def setup(bot):
    bot.add_cog(remokommand(bot))
