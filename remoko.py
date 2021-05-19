# coding: UTF-8

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

# ラズパイのハードウェア情報を出すコマンド


def piStatus(l):
    if l[1] == 'temp':
        print('Command > pi temp')
        status = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]

    elif l[1] == 'clock':
        print('Command > pi clock')
        status = subprocess.getoutput(
            'vcgencmd measure_clock arm').split('=')[1]

    elif l[1] == 'volt':
        print('Command > pi volt')
        status = subprocess.getoutput(
            'vcgencmd measure_volts core').split('=')[1]

    elif l[1] == 'mem':
        print('Command > pi mem')
        status = subprocess.getoutput('vcgencmd measure_mem arm').split('=')[1]

    else:  # show all
        print('Command > pi')

        if bool(l[2:]):
            print('Unknown args after "pi".')

        status = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
        status += '\n' + \
            subprocess.getoutput('vcgencmd measure_clock arm').split('=')[1]
        status += '\n' + \
            subprocess.getoutput('vcgencmd measure_volts core').split('=')[1]
        status += '\n' + \
            subprocess.getoutput('vcgencmd measure_mem arm').split('=')[1]

    return status


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

        if l[0] == 'pi':
            status = piStatus(l)
            await message.channel.send(status)
        else:
            await message.channel.send(l)
            print('command split test')
        return

client.run(config.TOKEN)
