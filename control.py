#FOR ANY ANNOUNCERS, PLEASE ONLY EDIT DUEDATE.PY
#THANK YOU FOR YOUR COOPERATION AND UNDERSTANDING

from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive

keep_alive()
from scheduler import scheduler
import datetime
from datetime import *
import pytz
import time
import discord
import random
import bot_func
from bot_func import search
from discord.utils import get


#Start up@
bot = commands.Bot(command_prefix='$')
activity = discord.Game(name="$help | $cmd for commands")
bot = commands.Bot(command_prefix="$",activity=activity,status=discord.Status.online)
bot.strip_after_prefix = True



## BELOW USED FOR BOT ##
def separate_str(string):
    building_word = ''
    word_list = []
    if string != '()' and string != "":
        for char in string:
            if char != " " and char != "(" and char != ")" and char != ",":
                building_word += char
            else:
                word_list.append(building_word)
                building_word = ''
    return word_list



### BOT'S COMMAND LIST BELOW! ###
### ALPHABETICAL ORDER PLEASE ###
'''

Notice: Before each command, there SHOULD be a comment detailing the command and how to use it.
For example:
#test() is for testing. Ex: $test, $ttt
'''


#_8ball is for 'determining the future' (not really). Ex: $_8ball <prompt>, $8ball <prompt>, $8b <prompt>
@bot.command(aliases=['8ball', '8b'])
async def _8ball(ctx,
                 *args):  #unfortunally, async def 8ball(): returned an error
    #list of predictions to (randomly) choose from
    predictions = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later.',
        'Better not tell you now.', 'Cannot predict now.',
        'Concentrate and ask again.', "Don't count on it.", 'My reply is no.',
        'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
    ]

    if str(args) != '()':
        msg = random.choice(predictions)
    else:
        msg = 'No prompt given. Try `$8ball <prompt>`'

    await ctx.send(msg)


#cmd() is for getting a list of cmds. For now it is a list, aiming to build a list like Dank Memer
@bot.command(aliases=['command', 'cmds', 'commands', 'com'])
async def cmd(ctx, *args):
    if str(args) != '()':
        pass  #for looking up a specific cmd
    else:
        await ctx.send('`$cmd <optional: specific command>`')
        cmds = ''

        #For each pair in the dictionary of commands
        for pair in bot.all_commands.items():
            cmds += f"`{pair[0]}`, "

        #Create an embed with all the Commands
        embd = discord.Embed(title="COMMANDS", description = str(cmds))
        await ctx.send(embed=embd)    

#avatar is to show your's, or someone else's avatar. Ex: $avatar, $avatar @mention, $avatar {id}
@bot.command(aliases=['av'])
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember == None:
        avamember = await bot.fetch_user(ctx.author.id)
    elif avamember is int:
        avamember = await bot.fetch_user(avamember)
    userAvatarUrl = avamember.avatar_url
    embd = discord.Embed(title="Avatar")
    embd.set_image(url=userAvatarUrl)
    await ctx.send(embed=embd)

#https://www.i2symbol.com/symbols/corner link to unicode characters for stuff like this: └
#see Dank Memer pls help to see more


#credits is to show credits. Ex: $credits
@bot.command(aliases=['credit', 'contributors', 'developers', 'dev', 'devs'])
async def credits(ctx):
    embd = discord.Embed(title="CREDITS", color=discord.Color.teal())
    embd.add_field(
        name='Developers',
        value=
        "**Isaac**, your official macho man.\n**James**, wielder of the flying axe <:flyingaxe:884865624914939975>.\n**Daniel**, Hollywood alias 'Daniellus Di'Egro'."
    )
    embd.add_field(
        name='Contributors',
        value=
        "Input your bot ideas in <#839143757748109334> to become a contributor!",
        inline=False)
    await ctx.send(embed=embd)
#hi james hi #hold up, gotta go for now


#help() is for asking for help. Ex: $help
@commands.command(aliases=['help'])
async def bot_help(ctx):
    embd = discord.Embed(
        title='Homelands Bot Help',
        description=
        "**Hi! Welcome to the Homelands Bot Help Manual**\nI am proud to be part of the Homeland's community!I can currently do a few things, altough by the start of school, I will be providing support, such as reminders, fun games, homework support, and more!\n Have fun and **GO HOMELANDS**!",
        color=discord.Color.blue())

    embd.set_footer(text="Written with Python.")
    embd.set_image(
        url=
        'https://cdn.discordapp.com/attachments/842823949037076520/879383578742517780/unknown.png'
    )
    embd.add_field(name='Prefix', value='`$`', inline=False)
    embd.add_field(name='Commands',
                   value='`$cmd` for more info.',
                   inline=False)
    embd.add_field(
        name='Peel Link',
        value=
        '[www.peelschools.org](https://www.peelschools.org/Pages/default.aspx)',
        inline=True)
    embd.add_field(
        name='School Holidays',
        value=
        '[Holidays](https://www.peelschools.org/calendar/Documents/School%20Year%20Calendar%202021-2022%20Regular%20Elementary%20and%20Secondary%20chart.pdf)',
        inline=True)

    await ctx.send(embed=embd)


#hi() is for saying hello. Ex: $hi, $hello
@bot.command(aliases=[
    'hello', 'hi!', 'hello!', 'hi there', 'Hi there', 'Hi there!', 'Howdy!',
    'howdy!', 'Hello', 'Hello!', 'Hi!', 'Hi'
])
async def hi(ctx):
    await ctx.reply('Hello!', mention_author=False)


#report() is for reporting a user. Ex: $report {args}
@bot.command(aliases=['rpt'])
async def report(ctx, *args):
    channel = bot.get_channel(846813361177755648)
    txt = ''
    for item in args:
        txt += str(item)
        txt += ' '
    await channel.send(f" <@!{ctx.author.id}> reports {txt}")
    await ctx.send(f'<@!{ctx.author.id}>, your request has been received.')


#server() is for server details. Ex: $server
@bot.command()
async def server(ctx, *args):
    if len(args) == 0:
        embed = discord.Embed(
            title="Server Information",
            description=
            f'ELC Homelands is a server is for texting, homework help (Covering all subjects) , reminders and more. With a wide community of **{ctx.guild.member_count}** members, we wish to provide you with the best school server experience.',
            color=0x808080)
        embed.set_author(name="Homelands Bot",
                         url='https://www.peelschools.org/Pages/default.aspx',
                         icon_url="https://www.microcad.ca/images/pdsb.png")
        embed.set_footer(
            text="$server [keyword] • Use !server for a list of keywords!")
        embed.add_field(
            name='Main Features',
            value=
            "• Texting\n• Reminders\n• Homework Help\n• A welcoming community\n• Fun!\n• A well-moderated chat!"
        )
        embed.add_field(
            name='Actions',
            value=
            '`boost`, `bots`, `create`, `emojis`, `events`, `features`, `giveaways`, `icon`, `invite`, `owner`, `members`, `rules`, `staff`',
            inline=False)
        embed.set_image(
            url=
            r'https://res.cloudinary.com/demo/image/upload/w_350,h_100,e_colorize,co_rgb:000000,r_5/l_text:Montserrat_25:ELC%20Homelands,co_rgb:FFFFFF,g_center/one_pixel.png'
        )
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'boost':
        print("hi")
        embed = discord.Embed(title="Server Boost", color=0x808080)
        embed.set_author(name="Homelands Bot",
                         url='https://www.peelschools.org/Pages/default.aspx',
                         icon_url="https://www.microcad.ca/images/pdsb.png")
        embed.add_field(
            name='--',
            value=
            f'Boost us to get even more perks! You can sleep knowing you are cool and have your own hoisted role! <:sunglasses:887516435742593075>'
        )
        embed.add_field(
            name='Booster Only Perks',
            value=
            f"• You'll be the most awesomeness\n• Access to make an autoresponse or autoreact when someone pings you!",
            inline=False)
        embed.set_footer(
            text="$server [keyword] • Use !server for a list of keywords!")
        embed.set_image(
            url=r'https://i.ytimg.com/vi/ZyX7U78keu0/maxresdefault.jpg')
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'bots':
        embed = discord.Embed(
            title="Server Bots",
            description=
            "We have bots that provide useful features!\n\nHere's a list of them and what they do below:",
            color=0x808080)
        embed.set_author(name="Homelands Bot",
                         url='https://www.peelschools.org/Pages/default.aspx',
                         icon_url="https://www.microcad.ca/images/pdsb.png")
        embed.add_field(
            name='--',
            value=
            f'<@!235148962103951360> Mod bot\n<@!155149108183695360> Mod Bot\n<@!822488670153474098> $help for more details\n<@!487328045275938828> Fun Bot!\n<@!201503408652419073> Music\n'
        )
        embed.set_footer(
            text="$server [keyword] • Use !server for a list of keywords!")
        embed.set_image(
            url=
            r'https://bs-uploads.toptal.io/blackfish-uploads/blog/post/seo/og_image_file/og_image/21026/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png'
        )
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'create':
        embed = discord.Embed(
            title="Server Bots",
            description=
            "We have bots that provide useful features!\n\nHere's a list of them and what they do below:",
            color=0x808080)
        embed.set_author(name="Homelands Bot",
                         url='https://www.peelschools.org/Pages/default.aspx',
                         icon_url="https://www.microcad.ca/images/pdsb.png")
        server = bot.get_guild(839135669712060486)
        format = "%a, %d %b %Y | %H:%M:%S %ZEDT"
        server_creation = server.created_at.strftime(format)
        embed.add_field(name='--', value=f'{server_creation}')
        embed.set_footer(
            text="$server [keyword] • Use !server for a list of keywords!")
        embed.set_image(
            url=
            r'https://www.gematsu.com/wp-content/uploads/2021/05/PS-Discord_05-03-21.jpg'
        )
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'emojis':
        embed = discord.Embed(title="Server Emojis",
                              description="Emojis here",
                              color=0x808080)
        embed.set_author(name="Homelands Bot",
                         url='https://www.peelschools.org/Pages/default.aspx',
                         icon_url="https://www.microcad.ca/images/pdsb.png")
        embed.add_field(
            name='--',
            value=
            'Isaac and James are so cool and smart <:wink:891113149728698368>')
        embed.add_field(
            name='**Here is a list of our Emojis!**\n',
            value=
            f'<:angery:875389778550468648> - Heh\n<:babyisaac:875390321943511100> - Very cute emoji\n<:carlbot:857614103232380932> - Tortle\n<:flyingaxe:884865624914939975> - James uses this\n<:gasp:872176337618628648> - *Gasp*\n<:godiedieinawholehole:852669994684514334> - Cmon Aimee\n<:grumpycat:857614180852695080> - l o l\n<:imsuingyoulady:852669995188092959> - Cmon Aimee\n<:ohno:859976978551013396> - Oh no... \n<:ulittlebush:852669975218749460> - Cmon Aimee\n<:why:873303024053928076> - Why\n<:winky:888892068842319953> - One of the first custom emojis in our server!',
            inline=False)
        embed.set_footer(
            text="$server [keyword] • Use !server for a list of keywords!")
        embed.set_image(
            url=
            r'https://user-images.githubusercontent.com/3952718/89732919-2ddf3e00-da52-11ea-9ea5-59df51a6c25e.png'
        )
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'events':
        embed = discord.Embed(
            title="Server Events",
            description="All events that we host will be here!",
            color=0x808080)
        embed.set_author(
            name="Homelands Bot",
            url=r'https://thumbs.dreamstime.com/z/colorful-vector-hand-lettering-banner-spelling-upcoming-events-upcoming-events-hand-drawn-letters-banner-119481161.jpg',
            icon_url=r'https://www.springwaternews.ca/wp-content/uploads/2020/12/upcoming-events.jpg')
        embed.add_field(
            name='--',
            value=
            f'<@!235148962103951360> Mod bot\n<@!155149108183695360> Mod Bot\n<@!822488670153474098> $help for more details\n<@!487328045275938828> Fun Bot!\n<@!201503408652419073> Music\n'
        )


#server() is for finding the time. Ex: $time, $clock
@bot.command(aliases=['clock'])
async def time(ctx):
    file = scheduler()

    embed = discord.Embed(title="Time", color=0x808080)
    embed.set_footer(text="Written with python")
    file = discord.File("assets/temp/temp.png", filename="temp.png")
    embed.set_image(url="attachment://temp.png")
    await ctx.reply(file=file, embed=embed, mention_author=False)
    import os
    os.remove(f'assets/temp/temp.png')


#rev() is for reversing a sentence. Ex: $rev <arg>
@bot.command()
async def rev(ctx, *args):
    s = ''
    for item in args:
        s += str(item)
        s += ' '
    stringlength = len(s)
    rev_sentence = s[stringlength::-1]
    await ctx.reply(rev_sentence, mention_author=False)


#poll() is for creating a anonymous poll. Ex: $poll <arg>
@bot.command()
async def poll(ctx, *args):
    subject = args[0]
    args = list(args)
    args.pop(0)
    x = ""
    for item in args:
        x += str(item)
        x += " "
    embed = discord.Embed(title="Poll!", color=0x808080)
    embed.add_field(name=subject, value=x)
    embed.set_footer(text="Written with python")
    await ctx.send(embed=embed)


#vote() is for creating a anonymous voting. Ex: $vote <arg>
@bot.command()
async def vote(ctx, *args):

    x = ""
    for item in args:
        x += str(item)
        x += " "
    embed = discord.Embed(title="Poll!", description=x, color=0x808080)
    embed.set_footer(text="Written with python")
    await ctx.send(embed=embed)





#Start
@bot.event
async def on_ready():
    bot.remove_command("help")
    bot.add_command(bot_help)

    #Bot is online
    time = datetime.now(pytz.timezone('US/Eastern')).strftime("%m/%d/%y  %H:%M:%S")
    channel = bot.get_channel(842122582848438302)
    embed = discord.Embed(
        title='Homelands Bot is Online',
        description=f"Logged on as <@!822488670153474098> as of {time}",
        color=discord.Color.green())
    embed.set_footer(text="Written with python")
    message = await channel.fetch_message(893225406969303061)
    await message.edit(embed=embed)
    print('Logged on')

    #For changing due dates
    from duedate import cng_date
    embed = cng_date()
    channel = bot.get_channel(887095059680477214)
    message = await channel.fetch_message(888786030893858837)
    await message.edit(embed=embed)

    #For changing events
    from events import events
    embed = events()
    channel = bot.get_channel(856654803408650282)
    message = await channel.fetch_message(890978759786766367)
    await message.edit(embed=embed)

    #Define announcment channel
    ctx = bot.get_channel(895778100854546493)

    #For scheduling periods
    from day import day
    
    global file
    periods = ['09:00', '09:40', '10:20', '12:00', '12:30', '13:10','13:50'] 
    holidays = ['10:11']

    while True:
        #Import your subjects and periods
        from subjects import dict705, dict805, sub

        #Find current time
        now_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")
        try:
            os.remove(r'assets/temp/temp.png')
        except:
            pass



        #Check if it is the weekend
        x = datetime.now(pytz.timezone('US/Eastern')).weekday()
        day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        if day_of_the_week[x] == 'Saturday' or day_of_the_week[x] == 'Sunday':
            print("It is the weekend. Re-trying in 1 hour")
            print(f'Today is {day_of_the_week[x]}')
            await asyncio.sleep(3600)

        #Check if it is a holiday
        elif datetime.now(
                pytz.timezone('US/Eastern')).strftime("%m:%d") in holidays:
            print("It is a holiday. Re-trying in 1 hour")
            await asyncio.sleep(3600)
        
        #Check if it is during off-school times
        elif int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) >= 19 or int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) < 6:
            if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) == 17:
                file = scheduler()

                #Prompt in the scheduling.
                if day_of_the_week[x] == "Friday":
                    day_prompt = "Monday"
                else:
                    day_prompt = "Tomorrow"

                #Privious day schedule 
                embed = discord.Embed(
                    title=f"Good Afternoon!",
                    description=
                    f"{day_prompt}:\n\n705 has:\n {sub(day,'705')}\n\n805 has: \n {sub(day,'805')}"
                )
                embed.add_field(name="Day:", value=day)
                embed.set_footer(text="Written with python")
                file = discord.File("assets/temp/temp.png",
                                    filename="temp.png")
                embed.set_image(url="attachment://temp.png")
                print("Sent the schdule for the next day")
                await ctx.send(file=file, embed=embed)
                await asyncio.sleep(3800)

            else:
                print("Off duty times 3 p.m. to 6 a.m. . Re-trying in 30 minutes")
                await asyncio.sleep(1800)

        #School periods
        elif now_time in periods:
            file = scheduler()
            index = periods.index(now_time)
            index += 2
            embed = discord.Embed(
                title=f"Period {index}",
                description=
                f"It is now period {index}. \n\n**705 has {dict705[str(day)][str(index)]}**\n\n**805 has {dict805[str(day)][str(index)]}**"
            )
            embed.add_field(name="Day:", value=day)
            embed.set_footer(text="Written with python")
            file = discord.File("assets/temp/temp.png",
                                filename="temp.png")
            embed.set_image(url="attachment://temp.png")
            print(f"Sent school period {index}")
            await ctx.send(file=file, embed=embed)
            await asyncio.sleep(120)

        #Event periods

        #Start of day
        elif now_time == '08:30':
            file = scheduler()
            embed = discord.Embed(
                title="Start of school",
                description=
                f"It is now period 1. \n\n**705 has {dict705[str(day)]['1']}**\n\n**805 has {dict805[str(day)]['1']}**\n"
            )
            embed.add_field(name="Day:", value=day)
            embed.set_footer(text="Written with python")
            file = discord.File("assets/temp/temp.png",
                                filename="temp.png")
            embed.set_image(url="attachment://temp.png")
            print("Sent period 1")
            await ctx.send(file=file, embed=embed)
            await asyncio.sleep(120)

        #Lunch
        elif now_time == '11:00':
            file = scheduler()
            embed = discord.Embed(title="Lunchtime",
                                  description="Time for lunch! 😋")
            embed.add_field(name="Day:", value=day)
            embed.set_footer(text="Written with python")
            file = discord.File("assets/temp/temp.png",
                                filename="temp.png")
            embed.set_image(url="attachment://temp.png")
            print("Sent lunch")
            await ctx.send(file=file, embed=embed)
            await asyncio.sleep(1800)  #Half an hour

        #End of day
        elif now_time == '14:30':
            file = scheduler()
            embed = discord.Embed(title="End of school",
                                  description="Have a nice day!")
            embed.add_field(name="Day:", value=day)
            embed.set_footer(text="Written with python")
            file = discord.File("assets/temp/temp.png",
                                filename="temp.png")
            embed.set_image(url="attachment://temp.png")

            #Change the day
            file1 = open("day.py", "w")
            x = "day = " + str(day+1)
            if day == 5:
                x = "day = 1"
            file1.write(x)
            file1.close()
            
            await ctx.send(file=file, embed=embed)
            await asyncio.sleep(3600)

        else:
            print("Not a vaild period. Checking in approx 5 seconds")
            print(datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M"))
            await asyncio.sleep(5)


bot.run(os.environ['.env'])

#Control updated 2021-10-10