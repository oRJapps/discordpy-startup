import discord
from discord import message
from discord import Embed
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
        botRoom = client.get_channel(863011085246529576)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        #announceChannelIds = client.channel.name

        # 入退室通知
        if before.channel is None:
             #await botRoom.send("**" + after.channel.name + "```** に、__" + member.name + "__  が参加しました！```")
             if after.channel.id != 856777019530412103:
                 embed=discord.Embed(title="[VC:"+after.channel.name+"]" + member.name +"が参加しました！",description="一般ボイスチャンネル",color=discord.Colour.green())
                 await botRoom.send(embed=embed)
                 Invite = await after.channel.create_invite()
                 await botRoom.send(Invite.url)
             else:
                embed=discord.Embed(title="[VC:"+after.channel.name+"]" + "誰かが参加しました！",description="Not一般ボイスチャンネル",color=discord.Colour.red())
                embed.add_field(name="⚠注意",value="トーク内容にエロ・グロ系が含まれる可能性があるので、参加は中学生以降自己責任です")
                await botRoom.send(embed=embed)

        elif after.channel is None:
            if before.channel.id != 856777019530412103:
             await botRoom.send("```[" + before.channel.name + "]から、__" + member.name + "__  が抜けました！```")
            else:
                return
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
client.run(token)
