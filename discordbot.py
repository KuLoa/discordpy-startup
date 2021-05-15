import discord
import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.content.startswith("/kae"):
        m1 = message.content.replace("/kae ", "")
        m2 = m1.split()
        buy = m2[0]
        sell = m2[1]
        embed = discord.Embed(title="DTC売買", description="", color=000000)
        embed.add_field(name="今は 「買い」　です", value="購入額 : " + buy + "\n売却額" + sell, inline=False)
        embed.set_footer(text="")
        await client.change_presence(activity=discord.Game(name="今は「買い」"))

    if message.content.startswith("/ure"):
        m1 = message.content.replace("/ure ", "")
        m2 = m1.split()
        buy = m2[0]
        sell = m2[1]
        embed = discord.Embed(title="DTC売買", description="", color=000000)
        embed.add_field(name="今は 「売り」　です", value="購入額 : " + buy + "\n売却額" + sell, inline=False)
        embed.set_footer(text="")
        await client.change_presence(activity=discord.Game(name="今は「売り」"))
        
    if message.content == "/stop":
        await client.change_presence(activity=discord.Game(name="何もするな"))
        
client.run(token)
