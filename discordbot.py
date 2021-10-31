#API https://apexlegendsapi.com
import discord
import os
import sys
import json
import requests
from discord.ext import commands
from discord.ext import tasks

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@tasks.loop(seconds=90)
async def map_ro():
    base_url = "https://api.mozambiquehe.re/maprotation?version=2&auth="
    endpoint = "API-KEY HERE"
    session = requests.Session()
    req = session.get(base_url+endpoint)
    req.close()
    res = json.loads(req.text)
    c_bmap_name = res["battle_royale"]["current"]["map"]
    c_bmap_timer = res["battle_royale"]["current"]["remainingMins"]
    n_bmap_name = res["battle_royale"]["next"]["map"]
    await client.change_presence(activity=discord.Game(name=f"{c_bmap_name}=={c_bmap_timer}min=>{n_bmap_name}"))

@client.event
async def on_ready():
    map_ro.start()
  
@client.event
async def on_message(message):
    if message.content.startswith("/kae"):
        m1 = message.content.replace("/kae ", "")
        m2 = m1.split()
        buy = m2[0]
        sell = m2[1]
        embed = discord.Embed(title="DTC売買", description="", color=000000)
        embed.add_field(name="今は 「買い」　です", value="購入額 : " + buy + "\n売却額 : " + sell, inline=False)
        embed.set_footer(text="")
        await message.channel.send(embed=embed)
        await client.change_presence(activity=discord.Game(name="今は「買い」"))

    if message.content.startswith("r/ure"):
        m1 = message.content.replace("/ure ", "")
        m2 = m1.split()
        buy = m2[0]
        sell = m2[1]
        embed = discord.Embed(title="DTC売買", description="", color=000000)
        embed.add_field(name="今は 「売り」　です", value="購入額 : " + buy + "\n売却額 : " + sell, inline=False)
        embed.set_footer(text="")
        await message.channel.send(embed=embed)
        await client.change_presence(activity=discord.Game(name="今は「売り」"))
        
    if message.content == "/stop":
        await client.change_presence(activity=discord.Game(name="何もするな"))
        
         if message.content == "&map":
        base_url = "https://api.mozambiquehe.re/maprotation?version=2&auth="
        endpoint = "API-KEY HERE"
        session = requests.Session()
        req = session.get(base_url+endpoint)
        req.close()
        res = json.loads(req.text)
        #bpubs
        c_bmap_name = res["battle_royale"]["current"]["map"]
        c_bmap_timer = res["battle_royale"]["current"]["remainingMins"]
        n_bmap_name = res["battle_royale"]["next"]["map"]
        #apubs
        c_amap_name = res["arenas"]["current"]["map"]
        c_amap_timer = res["arenas"]["current"]["remainingMins"]
        n_amap_name = res["arenas"]["next"]["map"]
        #branked
        c_brmap_name = res["ranked"]["current"]["map"]
        #aranked
        c_armap_name = res["arenasRanked"]["current"]["map"]
        c_armap_timer = res["arenasRanked"]["current"]["remainingMins"]
        n_armap_name = res["arenasRanked"]["next"]["map"]
        embed=discord.Embed(title="Apex Map Timer", color=0x00bfff)
        embed.add_field(name=f"カジュアル：バトロワ", value=f"**{c_bmap_name}**=={c_bmap_timer}min=>**{n_bmap_name}**", inline=False)
        embed.add_field(name=f"カジュアル：アリーナ", value=f"**{c_amap_name}**=={c_amap_timer}min=>**{n_amap_name}**", inline=False)
        embed.add_field(name=f"ランク：バトロワ", value=f"**{c_brmap_name}**", inline=False)
        embed.add_field(name=f"ランク：アリーナ", value=f"**{c_armap_name}**=={c_armap_timer}min=>**{n_armap_name}**", inline=False)
        embed.set_footer(text="Created by Tomo")
        await message.channel.send(embed=embed)
        
client.run(token)
