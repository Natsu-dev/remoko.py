# coding: UTF-8

# Packages
import discord
from discord.ext import commands
import platform
import random

import binascii
import socket

# Custom Libraries
import loadenv
import phrases
import reversi

# '<OS name> <version>をプレイ中'
client = discord.Client(activity=discord.Game(
    name=platform.system() + ' ' + platform.release()))

bot = commands.Bot(command_prefix='>')

class MyBot(commands.Bot):

    async def on_ready(self):
        print('USER: ' + self.user.name)
        print('ID: ' + self.user.id)
        print('ready...')

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

        # Wake on LAN
        if l[0] == 'wol':
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
