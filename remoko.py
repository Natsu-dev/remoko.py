# coding: UTF-8

# Packages
import discord
import platform
import random

import os
import subprocess

import binascii
import socket

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

    # Love
    if 'すき' in message.content:
        await message.channel.send(phrases.love)
        print('sent love.')
        return

    # Commands
    if message.content.startswith('remoko'):
        l = message.content.split()[1:]

        # Show Raspberry Pi Status
        if l[0] == 'pi':
            status = piStatus(l)
            await message.channel.send(status)
            print('command pi sent.')

        # Wake on LAN
        elif l[0] == 'wol':
            sendWol(loadenv.ADDRESS, loadenv.IP, 9)

        #Reversi
        elif l[0] == 'reversi':
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

            await message.channel.send (reversi.playReversi(b))

        # The Others
        else:
            await message.channel.send(l)
            await message.channel.send(phrases.invalidCom)
            print('command split test')
        return


client.run(loadenv.TOKEN)
