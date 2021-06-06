# coding: UTF-8

# Packages
import discord
from discord.ext import commands
import platform
import random

# Custom Libraries
import loadenv
import phrases
import reversi

# '<OS name> <version>をプレイ中'
client = discord.Client(activity=discord.Game(
    name=platform.system() + ' ' + platform.release()))


class MyBot(commands.Bot):

    async def on_ready(self):
        print('USER: ' + self.user.name)
        print('ID: ' + self.user.id)
        print('ready...')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Commands
    if message.content.startswith('remoko'):
        l = message.content.split()[1:]

        # Reversi
        if l[0] == 'reversi':
            b = ""
            if bool(l[1:]) == False:
                b = bool(random.getrandbits(1))
            elif l[1] == 'b':
                b = True
            elif l[1] == 'w':
                b = False
            else:
                b = bool(random.getrandbits(1))

            if b:
                await message.channel.send(
                    phrases.reversiReady.format(message.author.name, '黒'))
            else:
                await message.channel.send(
                    phrases.reversiReady.format(message.author.name, '白'))

            await message.channel.send(reversi.playReversi(b))


# Run
if __name__ == '__main__':
    bot = MyBot(command_prefix='>', activity=discord.Game(
        name=platform.system() + ' ' + platform.release()))
    bot.run(loadenv.TOKEN)
