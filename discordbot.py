import discord
import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.content == "/kae":
        await client.change_presence(activity=discord.Game(name="今買え"))
        
    if message.content == "/ure":
        await client.change_presence(activity=discord.Game(name="今売れ"))
        
client.run(token)
