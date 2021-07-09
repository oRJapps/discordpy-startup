import discord
from discord import message
import os
import traceback


token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(863009355115528192)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        #announceChannelIds = client.channel.name

        # 退室通知
        if before.channel is None:
             await botRoom.send("**" + after.channel.name + "```** に、__" + member.name + "__  が参加しました！```")
        elif after.channel is None:
             await botRoom.send("**" + before.channel.name + "```** から、__" + member.name + "__  が抜けました！```")
        #if before.channel is not None and before.channel.id in announceChannelIds:
        #    await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")

        #if after.channel is not None and after.channel.id in announceChannelIds:
        #    await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")

#メッセージ監視Bot
@client.event
async def on_message_delete(message):
    if message.author.bot:
        return

    CHANNEL_ID = 8862362251399004190
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"{message.author.name}の削除メッセージ```{message.content}```")
    
