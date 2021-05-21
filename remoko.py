# coding: UTF-8

# Packages
import discord
import platform
import random

import os
import subprocess

# Custom Libraries
import loadenv
import phrases
import reversi

# '<OS name> <version>をプレイ中'
client = discord.Client(activity=discord.Game(
    name=platform.system() + ' ' + platform.release()))


# ラズパイのハードウェア情報を出すコマンド
def piStatus(l):
    if bool(l[1:]) == False:
        print('Command > pi')
        temp = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
        clock = '{0:.2f}'.format(float(subprocess.getoutput(
            'vcgencmd measure_clock arm').split('=')[1]) / 1000000000) + 'GHz'
        volt = subprocess.getoutput(
            'vcgencmd measure_volts core').split('=')[1]
        mem = subprocess.getoutput('vcgencmd get_mem arm').split('=')[1] + 'B'
        return phrases.statusAll.format(temp, clock, volt, mem)

    if l[1] == 'temp':
        print('Command > pi temp')
        status = subprocess.getoutput('vcgencmd measure_temp').split('=')[1]
        return phrases.statusTemp.format(status)

    elif l[1] == 'clock':
        print('Command > pi clock')
        status = '{0:.2f}'.format(float(subprocess.getoutput(
            'vcgencmd measure_clock arm').split('=')[1]) / 1000000000) + 'GHz'
        return phrases.statusClock.format(status)

    elif l[1] == 'volt':
        print('Command > pi volt')
        status = subprocess.getoutput(
            'vcgencmd measure_volts core').split('=')[1]
        return phrases.statusVolt.format(status)

    elif l[1] == 'mem':
        print('Command > pi mem')
        status = subprocess.getoutput(
            'vcgencmd get_mem arm').split('=')[1] + 'B'
        return phrases.statusMem.format(status)

    else:
        print('Unknown args after "pi".')
        return phrases.invalidArg


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
            print('command pi sent.')

        elif l[0] == 'reversi':
            b = ""
            if bool(l[1]) and (l[1] == 'b'):
                b = True
            elif bool(l[1]) and (l[1] == 'w'):
                b = False
            else:
                b = bool(random.getrandbits(1))

            if b:
                message.channel.send(
                    phrases.reversiReady.format(message.author.name, '黒'))
            else:
                message.channel.send(
                    phrases.reversiReady.format(message.author.name, '白'))

            reversi.playReversi(b)

        else:
            await message.channel.send(l)
            print('command split test')
        return


client.run(loadenv.TOKEN)
