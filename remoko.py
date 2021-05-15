import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print('ready...')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Good Morning
    if 'おはよ' in message.content:
        await message.channel.send('おはよー！')

client.run(config.TOKEN)
