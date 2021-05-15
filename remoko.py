# Packages
import discord
import platform

# Custom Libraries
import config
import phrases


client = discord.Client(activity=discord.Game(
    name=platform.system() + ' ' + platform.release()))


@client.event
async def on_ready():
    print('ready...')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Good Morning
    if 'おはよ' in message.content:
        await message.channel.send(phrases.goodMorning)

client.run(config.TOKEN)
