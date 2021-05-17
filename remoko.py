# Packages
import discord
import platform

# Custom Libraries
import config
import phrases

# '<OS name> <version>をプレイ中'
client = discord.Client(activity=discord.Game(
    name=platform.system() + ' ' + platform.release()))


@client.event
async def on_ready():
    print('ready...')

# def commandSwitch(l):
#     if l[0] == 

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Good Morning
    if 'おはよ' in message.content:
        await message.channel.send(phrases.goodMorning)
        print('sent goodMorning.')
        return

    # Commands
    if message.content.startswith('remoko'):
        l = message.content.split()[1:]

        await message.channel.send(l)
        print('command split test')
        return

client.run(config.TOKEN)
