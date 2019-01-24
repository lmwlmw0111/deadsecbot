import asyncio
import discord
import json
import urllib
import os
import sys

client = discord.Client()

token = "NTMyOTI2NjEyNDQ3MTY2NDY0.DxnOJQ.mYp5x31DTstmHGPvxpXxDKGyCwM"

@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="!명령어 를 채팅창에!", type=1))

@client.event


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("!명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = 'DEADSEC 디스코드 명령어',
            description = '채팅창에 명령어를 입력하면 해당 명령에 대한 정보를 알려줍니다!',
            colour = 0x00ff00
        )

        embed.set_footer(text = '명령어는 추가될 수 있습니다!')
        embed.add_field(name = '!안내서', value = '기본안내서의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!바이백', value = '바이백 문서의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!스킬', value = '스킬 플랜 문서의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!srp', value = 'SRP 규정 문서의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!인텔', value = '인텔 사이트의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!캐피탈', value = '캐피탈 규정 문서의 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!얼라이언스', value = '얼라이언스 홈페이지 링크를 불러옵니다.',inline = False)
        embed.add_field(name = '!브레이브', value = '브레이브 멈블 사이트 링크를 불러옵니다.',inline = False)
        await client.send_message(channel,embed=embed)

    elif message.content.startswith('!안내서'):
        embed = discord.Embed(title='기본안내서 링크입니다!', description='https://docs.google.com/document/d/1k4daY8_pTnd21GJNFBfun_xfQgA0yu4WTqhwjZ8qG4A/edit', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!바이백'):
        embed = discord.Embed(title='바이백 문서 링크입니다!', description='https://docs.google.com/spreadsheets/d/1q1z7S085qp_J6opfozCv3rb7DgB-ApcUYSS4J0ubo2g/edit?ouid=104471863279176496179&usp=sheets_home&ths=true', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!스킬'):
        embed = discord.Embed(title='스킬 플랜 문서 링크입니다!', description='https://docs.google.com/document/d/1l7PZeyaaQCvgka3jN7jV7lzQRKHW3p4N6JR81mwTZMA/edit', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!srp'):
        embed = discord.Embed(title='SRP 규정 문서 링크입니다!', description='https://docs.google.com/document/d/19C6wbknOBGvpw1EUl9k2f0GeFVpNpfXGY_1NYEXoS9w/edit', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!인텔'):
        embed = discord.Embed(title='인텔 사이트 링크입니다!', description='http://intelmap.xyz', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!캐피탈'):
        embed = discord.Embed(title='캐피탈 규정 문서 링크입니다!', description='https://docs.google.com/document/d/1N_PYbDXed4I-17yfq9nbsbElZOqjnCLEUA-axe-zpEg/edit', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!얼라이언스'):
        embed = discord.Embed(title='얼라이언스 홈페이지 링크입니다!', description='https://auth.walka.space', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
    
    elif message.content.startswith('!브레이브'):
        embed = discord.Embed(title='브레이브 멈블 사이트 주소입니다!', description='https://mumble.bravecollective.com/', color=0x00ff00)
        await client.send_message(message.channel, embed=embed)


client.run(token)

