import discord
import datetime
import calendar

client = discord.Client()

@client.event
async def on_ready():
    print("System is ready for use.")
    await client.change_presence(activity=discord.Game(name='稼働中！'))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(r"\help"):
        embed = discord.Embed(title="HELP", description="", color=000000)
        embed.add_field(name="できること", value="・今日開講される科目のシラバス表示\n・科目を指定してシラバスを表示", inline=False)
        embed.set_footer(text="")
        await message.channel.send(embed=embed)

    if message.content.startswith(r"\today"):
        await message.channel.send("本日開講される科目のシラバスを表示します")

        today = datetime.date.today().weekday()
        weekday = calendar.day_name[today]

        if today == 0: #Mon
            embed = discord.Embed(title="syllabus")
            embed.add_field(name=weekday, value="1限目 保健体育IIA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0036&year=2020&lang=ja"
                                              "\n2限目 実験実習IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0052&year=2020&lang=ja"
                                              "\n3限目 同上"
                                              "\n4限目 課題学習時間", inline=False)
            await message.channel.send(embed=embed)

        if today == 1:
            embed = discord.Embed(title="syllabus")
            embed.add_field(name=weekday, value="1限目 プログラミングIIA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0051&year=2020&lang=ja"
                                              "\n2限目 微分積分IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0040&year=2020&lang=ja"
                                              "\n3限目 線形代数IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0038&year=2020&lang=ja"
                                              "\n4限目 なし", inline=False)
            await message.channel.send(embed=embed)

        if today == 2:
            embed = discord.Embed(title="syllabus")
            embed.add_field(name=weekday, value="1限目 化学IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0044&year=2020&lang=ja"
                                              "\n2限目 電気磁気学IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0047&year=2020&lang=ja"
                                              "\n3限目 英語IIIA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0032&year=2020&lang=ja"
                                              "\n4限目 課題学習時間", inline=False)
            await message.channel.send(embed=embed)

        if today == 3:
            embed = discord.Embed(title="syllabus")
            embed.add_field(name=weekday, value="1限目 英語IVA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0034&year=2020&lang=ja"
                                              "\n2限目 微分積分IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0040&year=2020&lang=ja"
                                              "\n3限目 物理学IIA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0042&year=2020&lang=ja"
                                              "\n4限目 HR", inline=False)
            await message.channel.send(embed=embed)

        if today == 4:
            embed = discord.Embed(title="syllabus")
            embed.add_field(name=weekday, value="1限目 電気回路IA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0049&year=2020&lang=ja"
                                              "\n2限目 国語IIA\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0028&year=2020&lang=ja"
                                              "\n3限目 歴史A\n     https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=12&subject_id=0030&year=2020&lang=ja"
                                              "\n4限目 課題学習時間", inline=False)
            await message.channel.send(embed=embed)



client.run("NzgwOTgzNjgxMTk1MDQ5MDI2.X73Buw.HznTw64Ol3hX7njXIn8YysxiyuA")
