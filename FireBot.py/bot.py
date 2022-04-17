import discord
from discord.ext import commands
from discord.ext.commands import bot
from Cybernator import Paginator as pag
import asyncio
from discord import Activity, ActivityType
import datetime
import random
import json
import DiscordUtils
bot = commands.Bot(command_prefix=">",intents=discord.Intents.all())
bot.remove_command("help")
pref = ">" #текущий префикс

#=====Тестовые команды=====



#==========команды==========

@bot.command() #команда p!help (++)
async def help(ctx):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if sett[str(ctx.guild.id)]['language'] == "RU" or sett[str(ctx.guild.id)]['language'] == "None":
        #страница 1
        embedRU1 = discord.Embed(title='Помощь(Страница 1/7)',description="Информация(5):",color=0x0000CD)
        embedRU1.add_field(name=f'`{pref}help` <страница(1/6)> :',value="Получить помощь",inline=False)
        embedRU1.add_field(name=f'`{pref}info` <пользователь> :',value="Узнать информацию о пользователе",inline=False)
        embedRU1.add_field(name=f'`{pref}avatar` <пользователь> :',value="Автар пользователя")
        embedRU1.add_field(name=f'`{pref}bot_info` :',value="Информация о боте",inline=False)
        embedRU1.add_field(name=f'`{pref}serverinfo` :',value="Информация о сервере",inline=False)
        embedRU1.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedRU1.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 2
        embedRU2 = discord.Embed(title='Помощь(Страница 2/7)',description="Модерация(6):",color=0xFF0000)
        embedRU2.add_field(name=f'`{pref}mute` <@пользоватетель> <время> <s-сек,m-минуты...(s,m,h,d)> <причина> :',value="Зумутить пользователя на время",inline=False)
        embedRU2.add_field(name=f'`{pref}unemute` <@пользователь> <причина> :',value="Размьютить пользователя",inline=False)
        embedRU2.add_field(name=f'`{pref}kick` <@пользователь> <причина> :',value="Выгнать пользователя с сервера",inline=False)
        embedRU2.add_field(name=f'`{pref}ban` <@пользователь> <причина> :',value="Забанить пользователя на сервере",inline=False)
        embedRU2.add_field(name=f'`{pref}unban` <@пользователь> <причина> :',value="Разбанить пользователя на сервере(В разработке)",inline=False)
        embedRU2.add_field(name=f'`{pref}clear` <кол-во сообщений> :',value="Удалить сообщения",inline=False)
        embedRU2.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedRU2.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 3
        embedRU3 = discord.Embed(title='Помощь(Страница 3/7)',description="Рейтинг(2):",color=0x9370DB)
        embedRU3.add_field(name=f'`{pref}rank` <@пользоватетель> :',value="Посмотреть уровень пользователя",inline=False)
        embedRU3.add_field(name=f'`{pref}top` :',value="Посмотреть топ по уровням",inline=False)
        embedRU3.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedRU3.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 4
        embedRU4 = discord.Embed(title='Помощь(Страница 4/7)',description="Экономика(4):",color=0xFFFF00)
        embedRU4.add_field(name=f'`{pref}daily` :',value="Получить ежедневные монетки(от 1000 до 2000)",inline=False)
        embedRU4.add_field(name=f'`{pref}slot` <ставка> :',value="Поиграть в слот машину(в разработке)",inline=False)
        embedRU4.add_field(name=f'`{pref}balance` <@пользователь> :',value="Узнать баланс пользователя",inline=False)
        embedRU4.add_field(name=f'`{pref}pay` <@пользователь> <кол-во монет>:',value="Перевести монеты пользователю",inline=False)
        embedRU4.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=b997178ce22df11aa6b5a6221c16aec4&n=13&exp=1")
        embedRU4.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 5
        embedRU5 = discord.Embed(title='Помощь(Страница 5/7)',description="Магазин(4):",color=0x4B0082)
        embedRU5.add_field(name=f'`{pref}shop` :',value="Открыть магазин",inline=False)
        embedRU5.add_field(name=f'`{pref}addshop` <@роль> <стоимость> :',value="Добавить в магазин роль",inline=False)
        embedRU5.add_field(name=f'`{pref}removeshop` <@роль> :',value="Удалить роль из магазина",inline=False)
        embedRU5.add_field(name=f'`{pref}buy` <@роль> :',value="Купить роль из магазина",inline=False)
        embedRU5.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedRU5.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 6
        embedRU6 = discord.Embed(title='Помощь(Страница 6/7)',description="Настройки(4):",color=0x4B0082)
        embedRU6.add_field(name=f'`{pref}settings_audit_log_channel` :',value="Задать канал аудита",inline=False)
        embedRU6.add_field(name=f'`{pref}settings_voice_room` :',value="Задать канал для создания приватное голосовой комнаты",inline=False)
        embedRU6.add_field(name=f'`{pref}current_settings` :',value="Посмотреть текущие настройки",inline=False)
        embedRU6.add_field(name=f'`{pref}language` <язык> :',value="Задать язык бота",inline=False)
        embedRU6.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Settings_app_icon.png")
        embedRU6.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 7
        embedRU7 = discord.Embed(title='Помощь(Страница 7/7)',description="Мини-игры(2):",color=0x4B0082)
        embedRU7.add_field(name=f'`{pref}tictactoe <@1-ый игрок> <@2-ой игрок> :` :',value="Начать игру крестики-нолики",inline=False)
        embedRU7.add_field(name=f'`{pref}place <Номер клетки от 1 до 9>` :',value="Поставить крестик/нолик в клетку",inline=False)
        embedRU7.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Settings_app_icon.png")
        embedRU7.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)

        embeds = [embedRU1,embedRU2,embedRU3,embedRU4,embedRU5,embedRU6,embedRU7]
        message = await ctx.send(embed=embedRU1)
        page = pag(bot, message , only=ctx.author, use_more=False, embeds=embeds, footer=False,use_exit=True, delete_message=True, timeout=300)
        await page.start()

    if sett[str(ctx.guild.id)]['language'] == "USA":
        #страница 1
        embedEN1 = discord.Embed(title='help',description="page:1/6:",color=0x0000CD)
        embedEN1.add_field(name="Information(5):",value="1234",inline=False)
        embedEN1.add_field(name=f'`{pref}help` <page(1/6)> :',value="Get help",inline=False)
        embedEN1.add_field(name=f'`{pref}info` <user> :',value="information about the user",inline=False)
        embedEN1.add_field(name=f'`{pref}avatar` <user> :',value="users avatar")
        embedEN1.add_field(name=f'`{pref}bot_info` :',value="Information about the bot",inline=False)
        embedEN1.add_field(name=f'`{pref}serverinfo` :',value="Server Information",inline=False)
        embedEN1.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedEN1.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 2
        embedEN2 = discord.Embed(title='help',description="page:2/6:",color=0xFF0000)
        embedEN2.add_field(name="Moderation(6):",value="1234",inline=False)
        embedEN2.add_field(name=f'`{pref}mute` <@user> <time> <s-secons,m-minutes...(s,m,h,d)> <Reason> :',value="Mute the user",inline=False)
        embedEN2.add_field(name=f'`{pref}unemute` <@user> <Reason> :',value="Unmute the user",inline=False)
        embedEN2.add_field(name=f'`{pref}kick` <@user> <Reason> :',value="Kick the user off the server",inline=False)
        embedEN2.add_field(name=f'`{pref}ban` <@user> <Reason> :',value="Ban a user on the server",inline=False)
        embedEN2.add_field(name=f'`{pref}unban` <@user> <Reason> :',value="Unban the user on the server(In development)",inline=False)
        embedEN2.add_field(name=f'`{pref}clear` <Number of messages> :',value="Delete Messages",inline=False)
        embedEN2.set_thumbnail(url="https://yt3.ggpht.com/a/AATXAJwx3XT9TvQoeKlcl_afK_98BaQcADRPnGEc-EseuQ=s900-c-k-c0xffffffff-no-rj-mo")
        embedEN2.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 3
        embedEN3 = discord.Embed(title='help',description="page:3/6:",color=0x9370DB)
        embedEN3.add_field(name="Rating(2):",value="1234",inline=False)
        embedEN3.add_field(name=f'`{pref}rank` <@user> :',value="View User level",inline=False)
        embedEN3.add_field(name=f'`{pref}top` :',value="View the top by level",inline=False)
        embedEN3.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedEN3.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 4
        embedEN4 = discord.Embed(title='help',description="page:4/6:",color=0xFFFF00)
        embedEN4.add_field(name="Economy(4):",value="1234",inline=False)
        embedEN4.add_field(name=f'`{pref}daily` :',value="Get daily coins(from 1000 to 2000)",inline=False)
        embedEN4.add_field(name=f'`{pref}slot` <Bid> :',value="Play a slot machine(in development)",inline=False)
        embedEN4.add_field(name=f'`{pref}balance` <@user> :',value="Find out the user's balance",inline=False)
        embedEN4.add_field(name=f'`{pref}pay` <@user> <Number of coins>:',value="Transfer coins to the user",inline=False)
        embedEN4.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=b997178ce22df11aa6b5a6221c16aec4&n=13&exp=1")
        embedEN4.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 5
        embedEN5 = discord.Embed(title='help',description="page:5/6:",color=0x4B0082)
        embedEN5.add_field(name="Shop(4):",value="1234",inline=False)
        embedEN5.add_field(name=f'`{pref}shop` :',value="Open a shop",inline=False)
        embedEN5.add_field(name=f'`{pref}addshop` <@role> <cost> :',value="Add a role to the shop",inline=False)
        embedEN5.add_field(name=f'`{pref}removeshop` <@role> :',value="Remove a role from the shop",inline=False)
        embedEN5.add_field(name=f'`{pref}buy` <@role> :',value="Buy a role from the shop",inline=False)
        embedEN5.set_thumbnail(url="https://cdn.discordapp.com/avatars/803326017069514753/9ac368efda049a55aaf11acaa8b908cb.webp?size=1024")
        embedEN5.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 6
        embedEN6 = discord.Embed(title='help',description="page:6/6:",color=0x4B0082)
        embedEN6.add_field(name="Settings(4):",value="1234",inline=False)
        embedEN6.add_field(name=f'`{pref}settings_audit_log_channel <channel>` :',value="Set audit_log_channel",inline=False)
        embedEN6.add_field(name=f'`{pref}settings_voice_room` <voice channel id>:',value="Set a channel to create a private voice room",inline=False)
        embedEN6.add_field(name=f'`{pref}current_settings` :',value="View current settings",inline=False)
        embedEN6.add_field(name=f'`{pref}language` <language> :',value="set the language of the bot",inline=False)
        embedEN6.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Settings_app_icon.png")
        embedEN6.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        #страница 7
        embedEN7 = discord.Embed(title='help',description="page:7/7:",color=0x4B0082)
        embedEN7.add_field(name="Mini-games(2):",value="1234",inline=False)
        embedEN7.add_field(name=f'`{pref}tictactoe <@1st player> <@2nd player> :` :',value="Start the Tic-tac-toe game",inline=False)
        embedEN7.add_field(name=f'`{pref}place <Cell number from 1 to 9>` :',value="Put a cross / zero in the cell",inline=False)
        embedEN7.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Settings_app_icon.png")
        embedEN7.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)

        embeds = [embedEN1,embedEN2,embedEN3,embedEN4,embedEN5,embedEN6,embedEN7]
        message = await ctx.send(embed=embedEN1)
        page = pag(bot, message , only=ctx.author, use_more=False, embeds=embeds, footer=False,use_exit=True, delete_message=True, timeout=300)
        await page.start()

@bot.command() #команда p!say (++)
@commands.has_permissions(manage_messages=True)
async def say(ctx,arg = None):
    if arg == None:
        return
    text = ' '.join(ctx.message.content.split(' ')[1:])
    await ctx.send(text)

@bot.command() #аватар p!avatar
async def avatar(ctx,member:discord.Member = None):
    if member == ctx.author or member == None:
        emb = discord.Embed(title=f'Аватар **{ctx.message.author}**',color=0xFFFF00)
        emb.set_image(url=ctx.message.author.avatar_url)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f'Аватар **{member}**',color=0xFFFF00)
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)

@bot.command() #команда p!bug (+++)
async def bug(ctx,arg = None):
    if arg == None:
        return
    text = ' '.join(ctx.message.content.split(' ')[1:])
    emb = discord.Embed(title="Репорт бага",color=0xFFFF00)
    emb.add_field(name="Пользователь:",value=f'{ctx.message.author.mention}({ctx.message.author.display_name}) ID:{ctx.message.author.id}')
    emb.add_field(name="Сервер:",value=f'{ctx.guild} ID:{ctx.guild.id}')
    emb.add_field(name="Описание бага:",value=text)
    emb.set_thumbnail(url=ctx.message.author.avatar_url)
    for guild in bot.guilds:
        bug_report_channel = discord.utils.get(bot.get_all_channels(), guild__id = 803668344694636545, id = 813074238533140521) #Канал Баг-репортов
    await bug_report_channel.send(embed=emb)
    emb = discord.Embed(title='Успешно!',color=0x00FF00)
    emb.add_field(name="Отчёт о баге был отправлен!",value="✅",inline=False)
    await ctx.send(embed=emb)

@bot.command() #команда p!ping (++)
async def ping(ctx):
    emb = discord.Embed(title=f'Ping',description=f'Pong! {round(bot.latency*1000)} ms',color=0xFFFF00)
    await ctx.send(embed=emb)

@bot.command() #команда p!serverinfo (++)
async def serverinfo(ctx):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if sett[str(ctx.guild.id)]['language'] == "RU" or sett[str(ctx.guild.id)]['language'] == "None":
        if ctx.guild.verification_level == "none":
            verification_level1 = "Отсутствует"
        elif ctx.guild.verification_level == "low":
            verification_level1 = "Низкий"
        elif ctx.guild.verification_level == "medium":
            verification_level1 = "Средний"
        elif ctx.guild.verification_level == "high":
            verification_level1 = "Высокий"
        else:
            verification_level1 = "Очень высокий"
        emb = discord.Embed(title=f'**Информация о сервере {ctx.guild}**',color=0x00FFFF)
        emb.add_field(name="Участники:",value=f'<:member_total:817014515006570546> Всего: {ctx.guild.member_count}\n<:members:817014577304174612> Людей: {ctx.guild.member_count}\n<:bots:817014615266295829> Ботов: {ctx.guild.member_count}')
        emb.add_field(name="Каналы:",value=f'<:channel_total:817014683764654140> Всего: **{int(len(ctx.guild.channels)) + int(len(ctx.guild.voice_channels))}**\n<:text_channels:817014735504932894>  Текстовых: **{str(len(ctx.guild.channels))}**\n<:voice_channels:817015566388297739> Голосовых: **{str(len(ctx.guild.voice_channels))}**')
        emb.add_field(name="Владелец:",value=ctx.guild.owner)
        emb.add_field(name="Регион:",value=ctx.guild.region)
        emb.add_field(name="Уровень проверки:",value=verification_level1)
        emb.add_field(name="Кол-во ролей",value=str(len(ctx.guild.roles)))
        emb.add_field(name="Дата создания:",value=ctx.guild.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"))
        emb.add_field(name="ID:",value=ctx.guild.id,inline=False)
        emb.set_thumbnail(url=ctx.guild.icon_url)
        emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=emb)

    if sett[str(ctx.guild.id)]['language'] == "USA":
        emb = discord.Embed(title=f'**Server Information {ctx.guild}**',color=0x00FFFF)
        emb.add_field(name="Owner:",value=ctx.guild.owner,inline=False)
        emb.add_field(name="Region:",value=ctx.guild.region,inline=False)
        emb.add_field(name="Number of members:",value=ctx.guild.member_count,inline=False)
        emb.add_field(name="Channels: ",value=f'Text channels - {str(len(ctx.guild.channels))}\nVoice channels - {str(len(ctx.guild.voice_channels))}')
        emb.add_field(name="Number of roles",value=str(len(ctx.guild.roles)),inline=False)
        emb.add_field(name="Date of creation:",value=ctx.guild.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.add_field(name="ID:",value=ctx.guild.id,inline=False)
        emb.set_thumbnail(url=ctx.guild.icon_url)
        emb.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=emb)

@bot.command() #команда p!bot_info (+)
async def bot_info(ctx):
    emb = discord.Embed(title=f'**Печенька#9215**',description=f'Привет! Меня зовут Печенька\n\nМой префикс `{pref}`. Пропиши `{pref}help` чтобы узнать больше о моих функциях',color=0x00FFFF)
    emb.add_field(name="Сборка:",value="Alpha 1.6.4.0 (28.09.21 20:54)",inline=True)
    emb.add_field(name="Создатель:",value="<:flamy_grief:892464875908005888> flamy grief#4767",inline=True)
    emb.add_field(name="Полезные ссылки:",value="[Сервер поддержки](https://discord.gg/fks937cBv9)\n[Пригласить](https://discord.com/api/oauth2/authorize?client_id=803326017069514753&permissions=1610608119&scope=bot)\n[Веб-сайт(скоро!)](http://FireBot.xyz)",inline=False)
    emb.set_thumbnail(url="https://cdn.discordapp.com/avatars/760230155150426146/9b41fdd70c6439ee202d74df8ec3c28b.webp?size=1024")
    await ctx.send(embed=emb)

#Команды модерации:

@bot.command() #команда p!mute <пользователь> <время в минутах> <причина> (+)
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member:discord.Member = None,time:int = None,timeT:str = None,reason = "Причина не указана"):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if member == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите пользователя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if member == ctx.message.author:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Вы не можете замьютить себя!!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if time == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите время!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    muterole = discord.utils.get(ctx.guild.roles,name='Muted')
    if not muterole:
        for guild in bot.guilds:
            muterole4 = await guild.create_role(name="Muted",color=0x808080) #Создание роли Muted если её нет
            muterole = discord.utils.get(ctx.guild.roles,name='Muted')
    await member.add_roles(muterole)
    await member.move_to(None)
    if timeT == "None":
        timetomute = time * 60
        time_name = "Минуты(у)"
    elif timeT == "s":
        timetomute = time * 1
        time_name = "Секунды(у)"
    elif timeT == "m":
        timetomute = time * 60
        time_name = "Минуты(у)"
    elif timeT == "h":
        timetomute = time * 60 * 60
        time_name = "Час(а)"
    elif timeT == "d":
        timetomute = time * 60 * 60 * 24
        time_name = "Дня(ей)"
    await asyncio.sleep(timetomute)
    emb = discord.Embed(title='Мут',color=0x808080)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name='Время',value=f'{time} {time_name}',inline=False)
    await ctx.send(embed=emb)
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    emb = discord.Embed(title='Авто-Анмут',color=0x808080)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value="Время вышло",inline=False)
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    await member.remove_roles(muterole)
    await ctx.send(embed=emb)

@bot.command() #команда p!Unmute <пользователь> (+)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member = None):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if member == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите пользователя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    muterole = discord.utils.get(ctx.guild.roles,name='Muted')
    emb = discord.Embed(title='Анмут',color=0x00FF00)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    await ctx.send(embed=emb)
    await member.remove_roles(muterole)

@bot.command() #команда p!kick <пользователь> <причина> (+)
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member = None,reason = "Причина не указана"):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if member == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите пользователя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if member == ctx.message.author:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Вы не можете кикнуть себя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    emb = discord.Embed(title='кик',color=0xFFA500)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    await member.kick()
    await ctx.send(embed=emb)

@bot.command() #команда p!ban <пользователь> <причина> (+)
@commands.has_permissions(ban_members = True)
async def ban(ctx,member:discord.Member = None,reason = "Причина не указана"):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if member == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите пользователя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if member == ctx.message.author:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Вы не можете забанить себя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    emb = discord.Embed(title='Бан',color=0x8B0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    await member.ban(reason=reason)
    await ctx.send(embed=emb)

@bot.command() #команда p!clear <кол-во> (+)
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=10):
    deleted = await ctx.message.channel.purge(limit=amount + 1)

#доп команды:

@bot.event #статус бота ()
async def on_ready():
    print("Бот запустился")
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game(f'{pref}help | На {str(len(bot.guilds))} сервере(ах)'))

@bot.event #авто роль
async def on_member_join(member):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if sett[str(ctx.guild.id)]['autorole'] != "None":
        for guild in bot.guilds:
            role = discord.utils.get(guild.roles, id=sett[str(ctx.guild.id)]['autorole'])
            await member.add_roles(role)
    if sett[str(ctx.guild.id)]['joinchannel'] != "None":
        for guils in bot.guilds:
            channel = discord.utils.get(guild.text_channels, id=sett[str(guild.id)]['joinchannel'])
            await channel.send(f'{member.mention} добро пожаловать на сервер!')

@bot.event #голосовая комната (+)
async def on_voice_state_update(member,before,after):
    with open('settings.json','r') as f:
        sett = json.load(f)
    for guild in bot.guilds:
        if not str(guild.id) in sett:
            sett[str(ctx.guild.id)] = {}
            sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
            sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
            sett[str(ctx.guild.id)]['Vcc_category'] = "None"
            sett[str(ctx.guild.id)]['language'] = "None"
            with open('settings.json','w') as f:
                json.dump(sett,f)
            with open('settings.json','r') as f:
                sett = json.load(f)
            return
        if sett[str(guild.id)]['Voice_create_channel'] == "None":
            return
        if after.channel.id == sett[str(guild.id)]['Voice_create_channel']: #айди гч
            for guild in bot.guilds:
                maincategory = discord.utils.get(guild.categories, id=sett[str(guild.id)]['Vcc_category']) #название категории
                channel2 = await guild.create_voice_channel(name=f'канал {member.display_name}',category = maincategory)
                await channel2.set_permissions(member,connect=True,mute_members=True,move_members=True,manage_channels=True)
                await member.move_to(channel2)
                def check(x,y,z):
                    return len(channel2.members) == 0
                await bot.wait_for('voice_state_update',check=check)
                await channel2.delete()

@bot.event #уровень (+) + проверка на наличие запрещённых слов
async def on_message(message):
    if message.author.bot == True:
        return
    ban_msg = ["дурак","дебил","лох"]
    for i in ban_msg: #проверка на наличие запрещённых слов
        if i in message.content:
            await message.delete()
            await message.channel.send(message.author.mention + " НЕ МАТЕРИСЬ!")
            return
    with open('lvl.json','r') as f:
        users = json.load(f)
    with open('settings.json','r') as f:
        sett = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
            users[user]['experience'] = 0
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
        users[user]['experience'] += exp
    async def add_lvl(users,user):
        exp = users[user]['exp']
        lvl = users[user]['lvl']
        if exp >= lvl * 10:
            lvl = lvl + 1
            await message.channel.send(f'Поздравляем {message.author.mention} ты достиг {lvl} уровня !')
            users[user]['exp'] = 0
            users[user]['lvl'] = lvl
    await update_data(users,str(message.author.id))
    await add_exp(users,str(message.author.id),1)
    await add_lvl(users,str(message.author.id))
    await bot.process_commands(message)
    with open('lvl.json','w') as f:
        json.dump(users,f)

@bot.command() #команда p!rank (+)
async def rank(ctx,memberrank:discord.Member = None):
    if memberrank == ctx.author or memberrank == None:
        with open('lvl.json','r') as f:
            users = json.load(f)
        emb = discord.Embed(description=f'Ранг пользователя ***{ctx.author}***')
        emb.add_field(name="Уровень:",value=users[str(ctx.author.id)]["lvl"])
        emb.add_field(name="Опыт:",value=f'{users[str(ctx.author.id)]["exp"]}/{users[str(ctx.author.id)]["lvl"]*10}')
        await ctx.send(embed=emb)
    else:
        with open('lvl.json','r') as f:
            users = json.load(f)
        emb = discord.Embed(description=f'Ранг пользователя ***{member}***')
        emb.add_field(name="Уровень:",value=users[str(member.id)]["lvl"])
        emb.add_field(name="Опыт:",value=f'{users[str(member.id)]["exp"]}/{users[str(member.id)]["lvl"]*10}')
        await ctx.send(embed=emb)

def get_top_experience(users1):
    users = []
    for k, v in users1.items():
        users.append(ExperienceCount(k, v['experience']))
    return sorted(users, key=lambda x: x.experience, reverse=True)

with open('lvl.json','r') as f:
        users1 = json.load(f)
class ExperienceCount:

    def __init__(self, user, experience):
        self.user = user
        self.experience = experience

    def __repr__(self):
        return f'<@{self.user}> | Уровень: {self.experience // 10} | Опыт: {self.experience} '

leaderboard = get_top_experience(users1)
a = get_top_experience(users1)

@bot.command()
async def top(ctx):
    if len(users1) == 1:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name=f'<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}', value="=", inline=False)
        await ctx.send(embed=embed)
    elif len(users1) == 2:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}\n<:rank_silver:817465034372284496> **#2.** {leaderboard[1]}', value="=", inline=False)
        await ctx.send(embed=embed)
    elif len(users1) == 3:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}\n<:rank_silver:817465034372284496> **#2.** {leaderboard[1]}\n<:rank_bronze:817465251834232932> **#3.** {leaderboard[2]}', value="=", inline=False)
        await ctx.send(embed=embed)
    elif len(users1) == 4:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}\n<:rank_silver:817465034372284496> **#2.** {leaderboard[1]}\n<:rank_bronze:817465251834232932> **#3.** {leaderboard[2]}\n**#4.** {leaderboard[3]}', value="=", inline=False)
        await ctx.send(embed=embed)
    elif len(users1) == 5:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}\n<:rank_silver:817465034372284496> **#2.** {leaderboard[1]}\n<:rank_bronze:817465251834232932> **#3.** {leaderboard[2]}\n**#4.** {leaderboard[3]}\n**#5.** {leaderboard[4]}', value="=", inline=False)
        await ctx.send(embed=embed)
    elif len(users1) > 5:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='<:rank_gold:817464941773848650> **#1.** {leaderboard[0]}\n<:rank_silver:817465034372284496> **#2.** {leaderboard[1]}\n<:rank_bronze:817465251834232932> **#3.** {leaderboard[2]}\n**#4.** {leaderboard[3]}\n**#5.** {leaderboard[4]}\n**...**', value="=", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Топ рейтинга участников', description='за всё время', color=0xff5555)
        embed.add_field(name='**Нет пользователей**', value="Возможно ОШИБКА", inline=False)
        await ctx.send(embed=embed)    

@bot.command() #команда p!info (++)
async def info(ctx,member:discord.Member = None):
    with open('settings.json','r') as f:
        sett = json.load(f)
    if sett[str(ctx.guild.id)]['language'] == "RU" or sett[str(ctx.guild.id)]['language'] == "None":
        if member == None or member == ctx.message.author:
            with open('lvl.json','r') as f:
                users = json.load(f)
            if ctx.message.author.raw_status == "online":
                status1 = "<:online:817015687095517224> В сети"
            elif ctx.message.author.raw_status == "idle":
                status1 = "<:idle:817015721052733480> Не активен"
            elif ctx.message.author.raw_status == "dnd":
                status1 = "<:dnd:817015759750037504> Не беспокоить"
            else:
                status1 = "<:offline:817015805954883594> Не в сети"
            if ctx.message.author.id == 760230155150426146:
                emb = discord.Embed(title=f'**Информация о :white_check_mark: {ctx.message.author.display_name}**',description="Информация(в разработке)",color=0x00FFFF)
                emb.add_field(name="Основная информация:",value="1234",inline=False)
                emb.add_field(name="Имя пользователя:",value=ctx.message.author,inline=False)
                emb.add_field(name="Статус:",value=status1,inline=False)
                emb.add_field(name="Пользовательский статус:",value=ctx.message.author.activity)
                if ctx.message.author.bot == True:
                    bot1 = "Да"
                else:
                    bot1 = "Нет"
                emb.add_field(name="Бот:",value=bot1,inline=False)
                emb.add_field(name="Лучшая роль", value=ctx.message.author.top_role,inline=False)
                emb.add_field(name="Присоединился:",value=ctx.message.author.joined_at,inline=False)
                emb.add_field(name="Дата регистрации:",value=ctx.message.author.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
                emb.add_field(name="Рейтинг:",value=leaderboard[0] or leaderboard[1] or leaderboard[2] or leaderboard[3] or leaderboard[4],inline=True)
                emb.add_field(name="Уровень:",value=users[str(ctx.message.author.id)]["lvl"],inline=True)
                emb.add_field(name="Опыт:",value=f'{users[str(ctx.message.author.id)]["exp"]}/{users[str(ctx.message.author.id)]["lvl"]*10}(Всего:{users[str(ctx.message.author.id)]["experience"]})',inline=True)
                emb.add_field(name="ID:",value=ctx.message.author.id,inline=False)
                emb.set_thumbnail(url=ctx.message.author.avatar_url)
                emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=emb)
            else:
                discord.Embed(title=f'**Информация о {ctx.message.author.display_name}**',description="Информация(в разработке)",color=0x00FFFF)
                emb.add_field(name="Основная информация:",value="1234",inline=False)
                emb.add_field(name="Имя пользователя:",value=ctx.message.author,inline=False)
                emb.add_field(name="Статус:",value=status1,inline=False)
                emb.add_field(name="Пользовательский статус:",value=ctx.message.author.activity)
                if ctx.message.author.bot == True:
                    bot1 = "Да"
                else:
                    bot1 = "Нет"
                emb.add_field(name="Бот:",value=bot1,inline=False)
                emb.add_field(name="Лучшая роль", value=ctx.message.author.top_role,inline=False)
                emb.add_field(name="Присоединился:",value=ctx.message.author.joined_at,inline=False)
                emb.add_field(name="Дата регистрации:",value=ctx.message.author.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
                emb.add_field(name="Рейтинг:",value=leaderboard[0] or leaderboard[1] or leaderboard[2] or leaderboard[3] or leaderboard[4],inline=True)
                emb.add_field(name="Уровень:",value=users[str(ctx.message.author.id)]["lvl"],inline=True)
                emb.add_field(name="Опыт:",value=f'{users[str(ctx.message.author.id)]["exp"]}/{users[str(ctx.message.author.id)]["lvl"]*10}(Всего:{users[str(ctx.message.author.id)]["experience"]})',inline=True)
                emb.add_field(name="ID:",value=ctx.message.author.id,inline=False)
                emb.set_thumbnail(url=ctx.message.author.avatar_url)
                emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=emb)
        else:
            with open('lvl.json','r') as f:
                users = json.load(f)
            emb = discord.Embed(title=f'**Информация о {member}**',description="Информация(в разработке)",color=0x00FFFF)
            emb.add_field(name="Основная информация:",value="1234",inline=False)
            emb.add_field(name="Имя пользователя:",value=member.display_name,inline=False)
            emb.add_field(name="Статус:",value=member.status,inline=False)
            emb.add_field(name="Пользовательский статус:",value=f'{member.raw_status}')
            if member.bot == True:
                bot1 = "Да"
            else:
                bot1 = "Нет"
            emb.add_field(name="Бот:",value=bot1,inline=False)
            emb.add_field(name="Лучшая роль", value=member.top_role,inline=False)
            emb.add_field(name="Присоединился:",value=member.joined_at,inline=False)
            emb.add_field(name="Дата регистрации:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.add_field(name="Рейтинг:",value=leaderboard[0] or leaderboard[1] or leaderboard[2] or leaderboard[3] or leaderboard[4],inline=True)
            emb.add_field(name="Уровень:",value=users[str(member.id)]["lvl"],inline=True)
            emb.add_field(name="Опыт:",value=f'{users[str(member.id)]["exp"]}/{users[str(member.id)]["lvl"]*10}(Всего:{users[str(member.id)]["experience"]})',inline=True)
            emb.add_field(name="ID:",value=member.id,inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_footer(text=f"Вызвано:{member}",icon_url=member.avatar_url)
            await ctx.send(embed=emb)

    if sett[str(ctx.guild.id)]['language'] == "USA":
        if member == None or member == ctx.message.author:
            with open('lvl.json','r') as f:
                users = json.load(f)
            emb = discord.Embed(title=f'**Information about {ctx.message.author}**',description="Information(in development)",color=0x00FFFF)
            emb.add_field(name="Basic information:",value="1234",inline=False)
            emb.add_field(name="User Name:",value=ctx.message.author.display_name,inline=False)
            emb.add_field(name="Status:",value=ctx.message.author.status,inline=False)
            emb.add_field(name="User Status:",value=f'{ctx.message.author.raw_status}')
            if ctx.message.author.bot == True:
                bot1 = "YES"
            else:
                bot1 = "NO"
            emb.add_field(name="Bot:",value=bot1,inline=False)
            emb.add_field(name="The best role", value=ctx.message.author.top_role,inline=False)
            emb.add_field(name="Joined:",value=ctx.message.author.joined_at,inline=False)
            emb.add_field(name="Registration date:",value=ctx.message.author.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.add_field(name="Rating:",value=leaderboard[0] or leaderboard[1] or leaderboard[2] or leaderboard[3] or leaderboard[4],inline=True)
            emb.add_field(name="Level:",value=users[str(ctx.message.author.id)]["lvl"],inline=True)
            emb.add_field(name="Experience:",value=f'{users[str(ctx.message.author.id)]["exp"]}/{users[str(ctx.message.author.id)]["lvl"]*10}(Total exp:{users[str(ctx.message.author.id)]["experience"]})',inline=True)
            emb.add_field(name="ID:",value=ctx.message.author.id,inline=False)
            emb.set_thumbnail(url=ctx.message.author.avatar_url)
            emb.set_footer(text=f"Caused by:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            with open('lvl.json','r') as f:
                users = json.load(f)
            emb = discord.Embed(title=f'**Information about {member}**',description="Информация(в разработке)",color=0x00FFFF)
            emb.add_field(name="Basic information:",value="1234",inline=False)
            emb.add_field(name="User Name:",value=member.display_name,inline=False)
            emb.add_field(name="Status:",value=member.status,inline=False)
            emb.add_field(name="User Status:",value=f'{member.raw_status}')
            if member.bot == True:
                bot1 = "YES"
            else:
                bot1 = "NO"
            emb.add_field(name="Bot:",value=bot1,inline=False)
            emb.add_field(name="The best role", value=member.top_role,inline=False)
            emb.add_field(name="Joined:",value=member.joined_at,inline=False)
            emb.add_field(name="Registration date:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.add_field(name="Rating:",value=leaderboard[0] or leaderboard[1] or leaderboard[2] or leaderboard[3] or leaderboard[4],inline=True)
            emb.add_field(name="Level:",value=users[str(member.id)]["lvl"],inline=True)
            emb.add_field(name="Experience:",value=f'{users[str(member.id)]["exp"]}/{users[str(member.id)]["lvl"]*10}(Total exp:{users[str(member.id)]["experience"]})',inline=True)
            emb.add_field(name="ID:",value=member.id,inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_footer(text=f"Caused by:{member}",icon_url=member.avatar_url)
            await ctx.send(embed=emb)

@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name, 
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)

@bot.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(bot.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(bot.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                
                await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

queue = []
mr = random.randint(1000,2000) #рандомные деньги

#Команды экономики  -\-\-\-

@bot.command() #команда p!daily (каждые 12 часов) (+)
async def daily(ctx):
    with open('economy.json','r') as f:
        money = json.load(f)

    if not str(ctx.author.id) in money:
        money[str(ctx.author.id)] = {}
        money[str(ctx.author.id)]['Money'] = 0
        with open('economy.json','w') as f:
            json.dump(money,f)
        with open('economy.json','r') as f:
            money = json.load(f)
    if not str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'***{ctx.author}*** Вы получили {mr} монет!')
        await ctx.send(embed=emb)
        money[str(ctx.author.id)]['Money'] += mr
        queue.append(str(ctx.author.id))
        with open('economy.json','w') as f:
            json.dump(money,f)
        await asyncio.sleep(43200) #12 часов
        queue.remove(str(ctx.author.id))
    if str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'***{ctx.author}*** Вы уже получили свои монеты сегодня!')
        await ctx.send(embed=emb)

@bot.command() #команда p!balance (+)
async def balance(ctx,member:discord.Member = None):
    if member == ctx.author or member == None:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У ***{ctx.author}*** {money[str(ctx.author.id)]["Money"]} монет')
        await ctx.send(embed=emb)
    else:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У ***{member}*** {money[str(member.id)]["Money"]} монет')
        await ctx.send(embed=emb)


    if role == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите роль!",value="❌",inline=False)
        await ctx.send(embed=emb)
    with open('shop.json','r') as f:
        shop = json.load(f)
    if not str(role.id) in shop[str(ctx.guild.id)]:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Этой роли нет в магазине!",value="❌",inline=False)
        await ctx.send(embed=emb)
    if str(role.id) in shop[str(ctx.guild.id)]:
        emb = discord.Embed(title='Успешно!',color=0x00FF00)
        emb.add_field(name="Роль была удалена из магазина",value="✅",inline=False)
        await ctx.send(embed=emb)
        del shop[str(ctx.guild.id)][str(role.id)]
    with open('shop.json','w') as f:
        json.dump(shop,f)


    if role == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите укажите роль!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('shop.json','r') as f:
        shop = json.load(f)
    with open('economy.json','r') as f:
        money = json.load(f)
    if str(role.id) in shop[str(ctx.guild.id)]:
        if shop[str(ctx.guild.id)][str(role.id)]['Cost'] > money[str(ctx.author.id)]['Money']:
            emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
            emb.add_field(name="У вас недостаточно денег!",value="❌",inline=False)
            await ctx.send(embed=emb)
            return
        if shop[str(ctx.guild.id)][str(role.id)]['Cost'] <= money[str(ctx.author.id)]['Money']:
            if not role in ctx.author.roles:
                emb = discord.Embed(title='Успешно!',color=0x00FF00)
                emb.add_field(name="Вы купили роль!",value="✅",inline=False)
                await ctx.send(embed=emb)
                for i in shop[str(ctx.guild.id)]:
                    if i == str(role.id):
                        buy = discord.utils.get(ctx.guild.roles,id = int(i))
                        await ctx.author.add_roles(buy)
                        money[str(ctx.author.id)]['Money'] -= shop[str(ctx.guild.id)][str(role.id)]['Cost']
            else:
                emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
                emb.add_field(name="У вас уже есть эта роль!",value="❌",inline=False)
                await ctx.send(embed=emb)
    with open('shop.json','w') as f:
        json.dump(shop,f)

@bot.command() #команда p!add shop (добавить роль на продажу) (+)
async def addshop(ctx,role:discord.Role = None,cost:int = None):
    if role == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите роль!:",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if cost == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите стоимость!:",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('shop.json','r') as f:
        shop = json.load(f)
    if str(role.id) in shop:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Эта роль уже есть в магазине:",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if not str(role.id) in shop:
        shop[str(role.id)] = {}
        shop[str(role.id)]['Cost'] = cost
        emb = discord.Embed(title='Успешно!',color=0x00FF00)
        emb.add_field(name="Роль добавлена в магазин:",value="✅",inline=False)
        await ctx.send(embed=emb)
    with open('shop.json','w') as f:
        json.dump(shop,f)

@bot.command() #команда p!shop (+)
async def shop(ctx):
    with open('shop.json','r') as f:
        shop = json.load(f)
    emb1 = discord.Embed(title="Магазин")
    emb_counter = 0
    emb1 = discord.Embed(title="Магазин")
    for role in shop:
        emb1.add_field(name=f'Цена: {shop[role]["Cost"]}',value=f'<@&{role}>',inline=False)
        emb_counter = emb_counter + 1
    await ctx.send(embed=emb1)
    print(emb_counter)

@bot.command() #команда p!removeshop (+)
async def removeshop(ctx,role:discord.Role = None):
    if role == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите роль!",value="❌",inline=False)
        await ctx.send(embed=emb)
    with open('shop.json','r') as f:
        shop = json.load(f)
    if not str(role.id) in shop:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Этой роли нет в магазине!",value="❌",inline=False)
        await ctx.send(embed=emb)
    if str(role.id) in shop:
        emb = discord.Embed(title='Успешно!',color=0x00FF00)
        emb.add_field(name="Роль была удалена из магазина",value="✅",inline=False)
        await ctx.send(embed=emb)
        del shop[str(role.id)]
    with open('shop.json','w') as f:
        json.dump(shop,f)

@bot.command() #команда p!buy (+)
async def buy(ctx,role:discord.Role = None):
    if role == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите укажите роль!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('economy.json','r') as f:
        money = json.load(f)
    if str(role.id) in money["shop"]:
        if money['shop'][str(role.id)]['Cost'] > money[str(ctx.author.id)]['Money']:
            emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
            emb.add_field(name="У вас недостаточно денег!",value="❌",inline=False)
            await ctx.send(embed=emb)
            return
        if money['shop'][str(role.id)]['Cost'] <= money[str(ctx.author.id)]['Money']:
            if not role in ctx.author.roles:
                emb = discord.Embed(title='Успешно!',color=0x00FF00)
                emb.add_field(name="Вы купили роль!",value="✅",inline=False)
                await ctx.send(embed=emb)
                for i in money['shop']:
                    if i == str(role.id):
                        buy = discord.utils.get(ctx.guild.roles,id = int(i))
                        await ctx.author.add_roles(buy)
                        money[str(ctx.author.id)]['Money'] -= money['shop'][str(role.id)]['Cost']
            else:
                emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
                emb.add_field(name="У вас уже есть эта роль!",value="❌",inline=False)
                await ctx.send(embed=emb)
    with open('economy.json','w') as f:
        json.dump(money,f)

@bot.command() #команда p!pay (+)
async def pay(ctx,member:discord.Member = None,arg:int = None):
    if member == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите пользователя!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if member == ctx.message.author:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Вы не можете отправить монеты себе!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    if arg == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите кол-во монет!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('economy.json','r') as f:
        money = json.load(f)
    if money[str(ctx.author.id)]['Money'] >= arg:
        emb = discord.Embed(description=f'{ctx.author} подарил {member} {arg} монет!')
        money[str(ctx.author.id)]['Money'] -= arg
        money[str(member.id)]['Money'] += arg
        await ctx.send(embed=emb)
    else:
        await ctx.send("У вас недостаточно денег!")
    with open('economy.json','w') as f:
        json.dump(money,f)

#Команды настроек

@bot.command() #настройки p!settings
@commands.has_permissions(administrator=True)
async def settings_audit_log_channel(ctx,channel_set:discord.TextChannel = None):
    if channel_set == None:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Укажите канал!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('settings.json','r') as f:
            sett = json.load(f)
    if not str(ctx.guild.id) in sett: #запись настроек
        sett[str(ctx.guild.id)] = {}
        sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
        sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
        sett[str(ctx.guild.id)]['Vcc_category'] = "None"
        sett[str(ctx.guild.id)]['language'] = "None"
        sett[str(ctx.guild.id)]['autorole'] = "None"
        sett[str(ctx.guild.id)]['joinchannel'] = "None"
        with open('settings.json','w') as f:
            json.dump(sett,f)
        with open('settings.json','r') as f:
            sett = json.load(f)
    sett[str(ctx.guild.id)]['audit_log_channel'] = channel_set.id
    emb = discord.Embed(title="Успешно",color=0x00FF00)
    emb.add_field(name="Канал аудита:",value=channel_set)
    await ctx.send(embed=emb)
    with open('settings.json','w') as f:
        json.dump(sett,f)
    emb = discord.Embed(title="Успешно",color=0x00FF00)
    emb.add_field(name="Теперь это канал аудита!",value=f'ID: {channel_set.id}')
    if str(ctx.guild.id) in sett: #система аудита
        if sett[str(ctx.guild.id)]['audit_log_channel'] != "None":
            channel = bot.get_channel(sett[str(ctx.guild.id)]['audit_log_channel'])
            await channel.send(embed=emb)
    with open('settings.json','w') as f:
        json.dump(sett,f)

@bot.command() #текущие настройки
@commands.has_permissions(administrator=True)
async def current_settings(ctx):
    with open('settings.json','r') as f:
            sett = json.load(f)
    if not str(ctx.guild.id) in sett: #запись настроек
        sett[str(ctx.guild.id)] = {}
        sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
        sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
        sett[str(ctx.guild.id)]['Vcc_category'] = "None"
        sett[str(ctx.guild.id)]['language'] = "None"
        sett[str(ctx.guild.id)]['autorole'] = "None"
        sett[str(ctx.guild.id)]['joinchannel'] = "None"
        with open('settings.json','w') as f:
            json.dump(sett,f)
        with open('settings.json','r') as f:
            sett = json.load(f)
    if sett[str(ctx.guild.id)]['language'] == "RU": #язык
        Lang1 = ":flag_ru: Русский(RU)"
    elif sett[str(ctx.guild.id)]['language'] == "USA":
        Lang1 = ":flag_us: English(USA)"
    else:
        Lang1 = f'Не указан({pref}language <язык>)'
    if sett[str(ctx.guild.id)]["audit_log_channel"] == "None": #Аудит
        Audit_channel_visual = f'Не указан ({pref}settings_audit_log_channel <Канал>)'
    else:
        Audit_channel_visual = f'<#{sett[str(ctx.guild.id)]["audit_log_channel"]}>'
    if sett[str(ctx.guild.id)]['Voice_create_channel'] == "None":
        Voice_create_channel_visual = f'Не указан ({pref}settings_voice_room <ID канала>)'
    else:
        Voice_create_channel_visual = sett[str(ctx.guild.id)]['Voice_create_channel']
    emb = discord.Embed(title=f'Настройки сервера ***{ctx.guild}***',description="Текущие настройки:",color=0x000000)
    emb.add_field(name="Канал аудита:",value=f'{Audit_channel_visual}',inline=False)
    emb.add_field(name="ID Канала для создания голосового канала:",value=Voice_create_channel_visual,inline=False)
    emb.add_field(name="Язык:",value=f'{Lang1}',inline=False)
    await ctx.send(embed=emb)

@bot.command() #смена языков
@commands.has_permissions(administrator=True)
async def language(ctx,language:str = None):
    if language == None:
        emb = discord.Embed(title='Языки:',color=0x808080)
        emb.add_field(name="RU - ",value=":flag_ru: (RU)",inline=False)
        emb.add_field(name="USA - ",value=":flag_us: (USA)",inline=False)
        await ctx.send(embed=emb)
        return
    with open('settings.json','r') as f:
            sett = json.load(f)
    if not str(ctx.guild.id) in sett: #запись настроек
        sett[str(ctx.guild.id)] = {}
        sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
        sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
        sett[str(ctx.guild.id)]['Vcc_category'] = "None"
        sett[str(ctx.guild.id)]['language'] = "None"
        sett[str(ctx.guild.id)]['autorole'] = "None"
        sett[str(ctx.guild.id)]['joinchannel'] = "None"
        with open('settings.json','w') as f:
            json.dump(sett,f)
        with open('settings.json','r') as f:
            sett = json.load(f)
    if language == "RU" or language == "USA":
        sett[str(ctx.guild.id)]['language'] = language
        if language == "RU":
            emb = discord.Embed(title="Успешно",color=0x00FF00)
            emb.add_field(name="Язык бота теперь:",value=f':flag_ru: Русский(RU)')
        if language == "USA":
            emb = discord.Embed(title="Successful",color=0x00FF00)
            emb.add_field(name="The bot's language is now:",value=f':flag_us: English(USA)')
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title='ОШИБКА',color=0xFF0000)
        emb.add_field(name="Язык указан неверно!",value="❌",inline=False)
        await ctx.send(embed=emb)
        return
    with open('settings.json','w') as f:
            json.dump(sett,f)

@bot.command() #Создание и настройка гк
@commands.has_permissions(administrator=True)
async def settings_voice_room(ctx,Voice_create_chann:discord.VoiceChannel = None):
    if Voice_create_chann == None:
        emb = discord.Embed(title="Ошибка",color=0xFF0000)
        emb.add_field(name="Укажите id голосового канала!",value="❌")
        await ctx.send(embed=emb)
        return
    with open('settings.json','r') as f:
        sett = json.load(f)
    if not str(ctx.guild.id) in sett: #запись настроек
        sett[str(ctx.guild.id)] = {}
        sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
        sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
        sett[str(ctx.guild.id)]['Vcc_category'] = "None"
        sett[str(ctx.guild.id)]['language'] = "None"
        sett[str(ctx.guild.id)]['autorole'] = "None"
        sett[str(ctx.guild.id)]['joinchannel'] = "None"
        with open('settings.json','w') as f:
            json.dump(sett,f)
        with open('settings.json','r') as f:
            sett = json.load(f)
    sett[str(ctx.guild.id)]['Voice_create_channel'] = Voice_create_chann.id
    sett[str(ctx.guild.id)]['Vcc_category'] = Voice_create_chann.category.id
    emb = discord.Embed(title="Успешно",color=0x00FF00)
    emb.add_field(name="Канал для создания голосовой комнаты:",value=f':loud_sound: {Voice_create_chann}')
    await ctx.send(embed=emb)
    with open('settings.json','w') as f:
        json.dump(sett,f)

@bot.command()
@commands.has_permissions(administrator=True)
async def settings_autorole(ctx,role:discord.Role = None):
    if role == None:
        emb = discord.Embed(title="Ошибка",color=0xFF0000)
        emb.add_field(name="укажите роль или None для отключения",value="❌")
        await ctx.send(embed=emb)
        return
    with open('settings.json','r') as f:
        sett = json.load(f)
    if not str(ctx.guild.id) in sett: #запись настроек
        sett[str(ctx.guild.id)] = {}
        sett[str(ctx.guild.id)]['audit_log_channel'] = "None"
        sett[str(ctx.guild.id)]['Voice_create_channel'] = "None"
        sett[str(ctx.guild.id)]['Vcc_category'] = "None"
        sett[str(ctx.guild.id)]['language'] = "None"
        sett[str(ctx.guild.id)]['autorole'] = "None"
        sett[str(ctx.guild.id)]['joinchannel'] = "None"
        with open('settings.json','w') as f:
            json.dump(sett,f)
        with open('settings.json','r') as f:
            sett = json.load(f)
    if role == "None":
        sett[str(ctx.guild.id)]['autorole'] = "None"
    else:
        sett[str(ctx.guild.id)]['autorole'] = role.id
        emb = discord.Embed(title="Успешно",color=0x00FF00)
        emb.add_field(name="Роль при входе на сервер:",value=f'<@&{role.id}>')
        await ctx.send(embed=emb)
    with open('settings.json','w') as f:
        json.dump(sett,f)
#Команды игры p!tictacoe (Крестики-нолики)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Сейчас очередь <@" + str(player1.id) + ">")
        elif num == 2:
            turn = player2
            await ctx.send("Сейчас очередь <@" + str(player2.id) + ">")
    else:
        await ctx.send("Игра уже в процессе Закончите данную игру чтобы начать новую!")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    if mark == ":regional_indicator_x:":
                        winer = player1.mention
                        p = player1
                    else:
                        winer = player2.mention
                        p = player2
                    emb = discord.Embed(title=f'**Победил {winer}**({mark})',description="За победу начислено 100 монет",color=0x00FFFF)
                    await ctx.send(embed=emb)
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Ничья!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Обязательно выберите целое число от 1 до 9 (включительно)!")
        else:
            await ctx.send("Сейчас не твоя очередь!")
    else:
        await ctx.send("Пожалуйста, начните новую игру с помощью команды `p!tictactoe.`")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Пожалуйста, укажите 2 игрока для этой команды!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Пожалуйста, н�� забудьте упомянуть/пингануть игроков!")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Пожалуйста, введите позицию, которую вы хотели бы отметить!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Пожалуйста, не забудьте ввести целое число!")

#Команды музыки

#C:/Users/Алексей/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Алексей/Desktop/печенька.py/bot.py

bot.run('ODAzMzI2MDE3MDY5NTE0NzUz.YA8Jpw.gM1sAgQzF5L_c7s-DFnTX_NQzHU')