# Packages
import discord
import platform

import os
import subprocess

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

        if l[1] == 'pi':
            if l[2] == 'temp':
                temp = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
                await message.channel.send(temp)
                print('sent pi temp.')
            else:
                await message.channel.send(phrases.invalidArg)
                print('command args error.')
                    
            
        await message.channel.send(l)
        print('command split test')
        return

client.run(config.TOKEN)
