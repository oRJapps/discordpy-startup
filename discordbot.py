import os
import asyncio
import json
import discord
from server import keep_alive
from discord import message,Embed
import traceback

client = discord.Client(intents=discord.Intents.default())

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(863011085246529576)
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        #announceChannelIds = client.channel.name
        # 入退室通知
        if before.channel is None:
            #await botRoom.send("**" + after.channel.name + "```** に、__" + member.name + "__  が参加しました！```")
            if after.channel.id != 856777019530412103:
                #Invite = await after.channel.create_invite()
                embed = discord.Embed(title=member.name + "が参加しました！",
                                      description="参加チャンネル：[" +
                                      after.channel.name + "]",
                                      color=discord.Colour.green())
                #embed.set_footer(text=Invite.url,url=Invite.url)
                embed.set_thumbnail(url=member.display_avatar.url)
                await botRoom.send(embed=embed)

            else:
                embed = discord.Embed(title="誰かが参加しました！",
                                      description="参加チャンネル：[" +
                                      after.channel.name + "]",
                                      color=discord.Colour.red())
                embed.add_field(
                    name="⚠注意",
                    value="トーク内容にエロ・グロ系が含まれる可能性があるので、参加は中学生以降自己責任です")
                embed.add_field(
                    name="詳細",
                    value=
                    "https://discord.com/channels/739793985471643649/743409631195562037/863580034430533633"
                )
                await botRoom.send(embed=embed)
        elif after.channel is None:
            if before.channel.id != 856777019530412103:
                await botRoom.send("```[" + before.channel.name + "]から、__" +
                                   member.name + "__  が抜けました！```")

        #if before.channel is not None and before.channel.id in announceChannelIds:
        #    await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        #if after.channel is not None and after.channel.id in announceChannelIds:
        #    await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")


#メッセージ監視Bot
@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    CHANNEL_ID = 862362251399004190
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"{message.author.name}の削除メッセージ```{message.content}```")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(os.environ['DISCORD_BOT_TOKEN'])
