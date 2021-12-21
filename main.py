#FOR ANY ANNOUNCERS, PLEASE ONLY EDIT DUEDATE.PY
#THANK YOU FOR YOUR COOPERATION AND UNDERSTANDING

from discord.ext import commands
import asyncio
import os
from startup import startup
from scheduler import scheduler
import datetime
from datetime import * 
import pytz
import discord
import random
from replit import db
import requests
import time




from os import system
#Start up@
activity = discord.Game(name="$help | $cmd for commands")
bot = commands.Bot(command_prefix="$",activity=activity,status=discord.Status.online, help_command=None)
bot.strip_after_prefix = True
tme = time
print(f"Repl Database keys in use : {db.keys()}")
#bot.remove_command('help')
startup()


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
        embd = discord.Embed(title="COMMANDS", description=str(cmds))
        await ctx.send(embed=embd)


#avatar is to show your's, or someone else's avatar. Ex: $avatar, $avatar @mention, $avatar {id}
@bot.command(aliases=['av'])
async def avatar(ctx, *, avamember: discord.Member = None):
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
        "**Isaac**, your official macho man.\n**James**, wielder of the flying axe <:flyingaxe:884865624914939975>.\n**Daniel**, Hollywood alias 'Daniellus Di'Egro'\n**Christopher**, Eopic kid."
    )
    embd.add_field(
        name='Contributors',
        value=
        "Input your bot ideas in <#839143757748109334> to become a contributor!",
        inline=False)
    await ctx.send(embed=embd)


#help() is for asking for help. Ex: $help
@bot.command(aliases=['Help', 'bothelp'])
async def help(ctx):
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
    responses = ['Hello', 'Hi!', 'Hello!', 'Hi there', 'Hi there!', 'Howdy!', 'Hello!', 'Hi', 'Greetings', 'Salutations', 'Welcome',"Bonjour","Hola","Ciao","Olá","G’day","Privet","你好"]
    await ctx.reply(random.choice(responses), mention_author=False)


#calc() is for calculator
@bot.command()
async def calc(ctx, *args):
    equation = ''
    for item in args:
        equation += str(item)

    try:
        await ctx.send(eval(equation))
    except:
        pass



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
            '`boost`, `bots`, `create`, `emojis`, `events`, `features`', inline = False) #`giveaways`, `icon`, `invite`, `owner`, `members`, `rules`, `staff`',
            #inline=False)
        embed.set_image(
            url=
            r'https://res.cloudinary.com/demo/image/upload/w_350,h_100,e_colorize,co_rgb:000000,r_5/l_text:Montserrat_25:ELC%20Homelands,co_rgb:FFFFFF,g_center/one_pixel.png'
        )
        await ctx.reply(embed=embed, mention_author=False)

    elif args[0] == 'boost':
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
            name='**Here is a list of our Emojis!**\n',
            value=
            f'<:angery:875389778550468648> - Heh\n<:babyisaac:875390321943511100> - Haha chubby\n<:carlbot:857614103232380932> - Tortle\n<:flyingaxe:884865624914939975> - James wields this... beware\n<:gasp:872176337618628648> - *Gasp*\n<:godiedieinawholehole:852669994684514334> - Cmon Aimee\n<:grumpycat:857614180852695080> - l o l\n<:imsuingyoulady:852669995188092959> - Cmon Aimee\n<:ohno:859976978551013396> - Oh no... \n<:ulittlebush:852669975218749460> - Cmon Aimee\n<:why:873303024053928076> - Why\n<:winky:888892068842319953> - One of the first custom emojis in our server!\n<:Wizardhat:909435141288501328> - You\'re a wizard, Harry!\n<:adios:897096452856250389> - Goodbye\n<:disappointed:916513763778252810> - Conan when you tell him you play Genshin\n<:doublepong:911047080007593994> - haha ping go brrr\n',
            inline=False)
        embed.add_field(name='.',value='<:drainedcat:911012930080886804> - No explanation needed**.**\n<:frickkk:917913815713189898> - We all know this feeling\n<:huh:914561577515102268> - *Visible confusion*\n<:invis:896410118797795381> - ...\n<:mydadznutz:909514397905465424> - Crunchy!\n<:mydadznutz2:909515229686276117> - Yum!\n<:omg:916697166146326530> - Isaac\'s pure ricjness\n<:ouch:916704152632045650> - Your face\n<:pensivecowboy:919251960190877729> - No explanation needed\n<a:ohno:914563971170852916> - Oh no...\n<:pixelsadge:919252433299996712> - We all know this feeling\n<:pong:909492236843106355> - haha ping go brrr\n<:pooprollingeyes:914634018111242313> - The emojis that Isabella hates\n<:smuggie:919251740166062100> - l o l\n<:tsktsk:914540098920546316> - tsktsk\n<:wide_daniel:895842460482285628> - Ricj man, but wider')
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
            url=
            r'https://thumbs.dreamstime.com/z/colorful-vector-hand-lettering-banner-spelling-upcoming-events-upcoming-events-hand-drawn-letters-banner-119481161.jpg',
            icon_url=
            r'https://www.springwaternews.ca/wp-content/uploads/2020/12/upcoming-events.jpg'
        )
        embed.add_field(
            name='--',
            value=
            f'<@!235148962103951360> Mod bot\n<@!155149108183695360> Mod Bot\n<@!822488670153474098> $help for more details\n<@!487328045275938828> Fun Bot!\n<@!201503408652419073> Music\n'
        )


#server() is for finding the time. Ex: $time, $clock
@bot.command(aliases=['time'])
async def clock(ctx):
    file = scheduler()

    embed = discord.Embed(title="Time", color=0x808080)
    embed.set_footer(text="Written with python")
    file = discord.File("assets/temp/temp.png", filename="temp.png")
    embed.set_image(url="attachment://temp.png")
    await ctx.reply(file=file, embed=embed, mention_author=False)
    import os
    os.remove(f'assets/temp/temp.png')

#ping() is for people who want to ping the bot
@bot.command()
async def ping(ctx):
    start = tme.time()
    r= requests.head('https://Pinging-bot.isaacchu1.repl.co', timeout=10)
    infoping = f"{(tme.time() - start)*1000} ms"

    embed = discord.Embed(title="Pong!", description = f"Response time : {infoping}")
    embed.set_footer(text="Written with python")
    await ctx.reply(embed=embed, mention_author=False)


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


#poll() is for creating a  poll. Ex: $poll <arg>
@bot.command()
async def poll(ctx, *args):
    if ctx.channel.id == 849714684856238100 or ctx.channel.id == 880096434421125190:
        message = ''
        num = 0
        for item in args:
            message += str(args[num]) + " "
            num += 1
    msg = await ctx.send(f"**{ctx.author}** asks : {message}")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    await ctx.message.delete()


#uniquepoll() is for creating polls with special emojis. Ex: $poll <arg> 
@bot.command()
async def uniquepoll(ctx, *args):
    print(args)
    if ctx.channel.id == 849714684856238100 or ctx.channel.id == 880096434421125190:
        message = ''
        num = -1
        for item in args:
            num += 1
            if len(args) - 2 == num:
                break
            else:
                message += str(args[num]) + " "
    try:
        message = await ctx.send(f"**{ctx.author}** asks : {message}")
        await message.add_reaction(str(args[len(args) - 1]))
        await message.add_reaction(str(args[int(len(args)) - 2]))
        await ctx.message.delete()
    except:
        await ctx.message.delete()
        await message.message.delete()
        await ctx.send(
            "Not a valid format. Format is `$uniquepoll {prompt} {emoji1} {emoji2}`"
        )

#Infection game
@bot.command()
async def infect(ctx, *args):
    if db["infected"] == int(ctx.message.author.id):
        try:
            finlist = int(args[0])
        except:
            userid =list(args[0])
            x = 0
            finlist = ''
            for item in userid:
                if x < 4 or x == len(userid) -1:
                    pass
                else:
                    finlist += str(item)

            finlist = int(finlist)

        db["infected"] =int(finlist)
        channel = bot.get_channel(919281999427043369)
        await channel.send(f'<@!{int(finlist)}> is infected') 
        user = await bot.fetch_user(int(finlist))
        embd = discord.Embed(title = "You have been infected!",description = "Pass on the infection to someone else by typing `$infect {user id}` in an channel in the ELC server. Doing so will also remove the infection from you.\n\nIf you don't know how to get user id:\n\n1.Go to user settings\n2.Click on Advanced\n3.Turn on developer mode\n4.Press the Esc key\n5.Right click a user in the member list on the side and click Copy ID")
        await user.send(embed=embd)
        await ctx.message.delete()
    else:
        await ctx.send("You are not infected!")
        await ctx.message.delete()


@bot.command()
async def resmessage(ctx):
    if ctx.channel.id == 922532597660274739 or ctx.channel.id == 922532805311868999:
        embed = discord.Embed(
            title="Welcome to res room",
            description=
            "<@&907108327962574848> You are in prison because you did something wrong. If you can fix your mistake, fix it before you become a Temporarily Banned Member, kicked or permanently banned. If you cannot, you will suffer either confinement in this prison or receive your due punishment. If you see this message, please fix your mistake in any way you can.\n\n Guidelines :\n 1. What was your mistake\n 2. What will you do so that you won't commit this mistake again? \n 3. Why should you be unmuted?\n\n Answer truthfully. This channel is still moderated, so rules still apply. To resend this message, use command $resmessage"
        )
        await ctx.channel.send(embed=embed)





#MODERATION
modlist_channels = [
    839141157774426142, 846813361177755648, 887097189443207228,
    842823949037076520, 880096434421125190, 909529988200554546
]

#post() is for posting. Ex: $post <arg>
@bot.command()
async def post(ctx, *args):
    message = ''
    num = 0
    for item in args:
        message += str(args[num]) + " "
        num += 1
    message = await ctx.send(message)
    await ctx.message.delete()

#its not here
@bot.command(aliases=["changeday"])
async def setday(ctx, *args):
    if ctx.channel.id in modlist_channels:
        from bot_func import setday
        try:
            set_day = int(args[0])
        except:
            await ctx.send("Not an integer")
            return
        if set_day > 5:
            await ctx.send("Can't set to that day")
        else:
            setday(set_day)
            await ctx.send(f"Changed day to day {set_day}")
    else:
        await ctx.send("You can't do that")



@bot.command()
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if ctx.channel.id in modlist_channels:
        await member.add_roles(role)

@bot.command()
async def react(ctx,*args):
    channel = bot.get_channel(907754572179730433)
    msg = await channel.fetch_message(str(args[0]))
    await msg.add_reaction("✅")

@bot.command(aliases=['reboot','refresh'])
async def restart(ctx):
    if ctx.channel.id in modlist_channels:
        await ctx.send("Restarting...")
        channel = int(ctx.channel.id)
        db["restartctx"] = channel
        system('busybox reboot')
        








###################Start
@bot.event
async def on_ready():

    #Restart command finished ( Messages the user after restart command has completed)
    if db["restartctx"] != 0:
        cnl = db['restartctx']
        channel = bot.get_channel(cnl)
        await channel.send("Restart finished")
        db["restartctx"] = 0
    



    #If you want the bot to do anything when the bot restarts , put it above this comment
    #I got a bit messy underneath this line 


    channel = bot.get_channel(919281999427043369)
    embd = discord.Embed(title = "Connected", description = "Checking for errors...",  color=discord.Color.red())
    embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
    msg = await channel.send(embed=embd)

    bot.remove_command("help")
    #bot.add_command(bot_help)

    #Startup
    global file
    from scheduler import scheduler
    
    #For changing due dates
    from bot_func import cng_due, weatherembed
    from googleapi import main, main2
    


    ###ERROR CHECKING###
    channel = bot.get_channel(919281999427043369)
    infoping = ''  
    des = ''
    reboot = False
    print(db['error'])

    #HTTP Requests
    executiontime = tme.time() 
    try:
        start = tme.time()
        r= requests.head('https://Pinging-bot.isaacchu1.repl.co', timeout=10)
        infoping = f"{(tme.time() - start)*1000} ms"
        des = f"Checking for errors...\n\nPinging passed ...\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
        errormsg = "No"
    except:
        des = 'Error in pinging bot. Priority is low '
        errormsg = "An"
    
    embd = discord.Embed(title = "Connected", description = des,  color=discord.Color.red())
    embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
    await msg.edit(embed=embd)
    

    #Weather API
    executiontime = tme.time() 
    try:
        weatherembed()
        des += f"\n\nWeather API and function passed ...\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
    except:
        des = 'Error in Weather API. Priority is medium - Inform the public about the temporary error'
    embd = discord.Embed(title = "Connected", description = des,  color=discord.Color.red())
    embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
    await msg.edit(embed=embd)


    #PIL Library
    executiontime = tme.time() 
    try:
        file= scheduler()
        des += f"\n\nPIL Library and scheduler function passed...\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
    except:
        reboot = True
        des = 'Error in PIL Library and generating time image. Priority is high during school times'
    
    embd = discord.Embed(title = "Connected", description = des,  color=discord.Color.red())
    embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
    await msg.edit(embed=embd)

    #Google API
    len805 = []
    len705 = []

    try:
        len805 = len(main())
        len705 = len(main2())
        des += f"\n\nGoogle API and duedate function passed.\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
    except:
        reboot = True
        des = ' Error in Google API ( Likely the token ). Priority is high.'

    #Error rebooting
    if reboot == True and db["error"] == False:
        channel = bot.get_channel(919281999427043369)
        await channel.send("<@&879470018809692170> Error in bot. Reboot pending...")
        print("Error in bot. Reboot pending...")
        db["error"] = True
        system("busybox reboot")
    
    #Error bypass ( Due to reboot failure )
    if db['error'] == True and reboot == True:
        channel = bot.get_channel(919281999427043369)
        await channel.send("<@&879470018809692170> Error in bot. Reboot has completed, but the bot still has errors. Running anyways...")

    

    ###ERROR CHECKING### ( Above )


    #CONNECTED MESSAGE#
    if reboot == True:
        pass
    else:
        embd = discord.Embed(title = "Connected", description = des,  color=discord.Color.red())
        embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
        await msg.edit(embed=embd)

        clock = datetime.now(
            pytz.timezone('US/Eastern')).strftime("%m/%d/%y  %H:%M:%S")
        embed = discord.Embed(title='Homelands Bot is Online',
                            description=f"Logged on as {bot.user} as of {clock}",
                            color=discord.Color.green())
        embed.add_field(
            name="Information",
            value=
            f"Day = {db['day']}\n\n<@!{int(db['infected'])}> is infected\n\n{len805} items in the 805 duedates list\n{len705} items in the 705 duedates list\n\n{errormsg} error present pinging 'https://Pinging-bot.isaacchu1.repl.co'.\nResponse time : {infoping}\n\nPIL Library and time generator check...\n"
        )
        embed.set_footer(text="Written with python")
        embed.set_image(url="attachment://temp.png")
        await channel.send(file=file, embed=embed)

    print('Logged on')
    db["error"] = False




    #For scheduling periods
    day = int(db['day'])
    periods = ['09:00', '09:40', '10:20', '12:00', '12:30', '13:10', '13:50']
    holidays = ['10:11', "11:12",'12:20','12:21','12:22','12:23','12:24','12:25','12:26','12:27','12:28','12:29','12:30','1:01','1:02']

    while True:

        channel = bot.get_channel(887095059680477214)
        message = await channel.fetch_message(914295454840258601)
        

        #Import your subjects and periods
        from subjects import dict705, dict805, dict605, sub

        #Find current time
        now_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")

        try:
            os.remove(r'assets/temp/temp.png')
        except:
            pass

        #VARIABLES
        x = datetime.now(pytz.timezone('US/Eastern')).weekday()
        day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        hr = int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H"))

        def refresh():
            print("Updated duedates")
            #Try and except for tempoarary service errors for Google API
            repeat = 0
            while True:
                if repeat > 2:
                    break
                try:
                    #Refresh duedates
                    dueembed = cng_due(main2(), main())
                    return dueembed
                except:
                    repeat += 1
                    pass
        
        #Update weather embed
        #channel= bot.get_channel(922230146038132816)
        #weathermessage = await channel.fetch_message(922231492296445994)
        #await weathermessage.edit(embed=weatherembed())

        #HOLIDAYS
        if datetime.now(
                pytz.timezone('US/Eastern')).strftime("%m:%d") in holidays:
            print("Holiday. Refresh in 2 minutes")
            channel = bot.get_channel(887095059680477214)
            message = await channel.fetch_message(914295454840258601)
            await message.edit(embed=refresh())
            await asyncio.sleep(120)

        #WEEKEND
        elif day_of_the_week[x] not in weekdays:
            print("Weekend. Refresh in 1 minute")
            channel = bot.get_channel(887095059680477214)
            message = await channel.fetch_message(914295454840258601)
            await message.edit(embed=refresh())
            await asyncio.sleep(60)

        #SCHOOL DAY
        
        #School hours
        elif hr >=6 or hr <= 14:
            print("School hours")

            #Scheduler Channel
            channel = bot.get_channel(895778100854546493)


            #Start of the day ( 8:30 )
            if now_time == '08:30':
                file = scheduler()
                embed = discord.Embed(
                    title="Start of school",
                    description=
                    f"It is now period 1. \n\n**605 has {dict605[str(day)]['1']}**\n\n**705 has {dict705[str(day)]['1']}**\n\n**805 has {dict805[str(day)]['1']}**\n"
                )
                embed.add_field(name="Day:", value=day)
                embed.set_footer(text="Written with python")
                file = discord.File("assets/temp/temp.png",
                                    filename="temp.png")
                embed.set_image(url="attachment://temp.png")
                print("Sent period 1")
                msg = await channel.send(file=file, embed=embed)
                await msg.publish()
                await asyncio.sleep(120)

            #Lunchtime
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
                msg = await channel.send(file=file, embed=embed)
                await msg.publish()
                await asyncio.sleep(1800)  #Half an hour

            #End of the day ( 2:30 )
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
                from bot_func import changeday
                nday = changeday(day)

                msg = await channel.send(file=file, embed=embed)
                await msg.publish()

                #Next day time picture
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
                    f"{day_prompt}:\n\n605 has:\n {sub(nday,'605')}\n\n705 has:\n {sub(nday,'705')}\n\n805 has: \n {sub(nday,'805')}"
                )
                embed.add_field(name="Day:", value=nday)
                embed.set_footer(text="Written with python")
                file = discord.File("assets/temp/temp.png",
                                    filename="temp.png")
                embed.set_image(url="attachment://temp.png")
                print("Sent the schdule for the next day")
                msg = await channel.send(file=file, embed=embed)
                await msg.publish()
                await asyncio.sleep(3800)

            #School periods
            elif now_time in periods:
                file = scheduler()
                index = periods.index(now_time)
                index += 2
                embed = discord.Embed(
                    title=f"Period {index}",
                    description=
                    f"It is now period {index}. \n\n**605 has {dict605[str(day)][str(index)]}**\n\n**705 has {dict705[str(day)][str(index)]}**\n\n**805 has {dict805[str(day)][str(index)]}**"
                )
                embed.add_field(name="Day:", value=day)
                embed.set_footer(text="Written with python")
                file = discord.File("assets/temp/temp.png",filename="temp.png")
                embed.set_image(url="attachment://temp.png")
                print(f"Sent school period {index}")
                msg = await channel.send(file=file, embed=embed)
                await msg.publish()

                #Refresh the duedates every period
                cnl = bot.get_channel(887095059680477214)
                message = await cnl.fetch_message(914295454840258601)
                await message.edit(embed=refresh())
                

                await asyncio.sleep(120)
            
            #Non-event periods
            else:
                print("Non-event periods during school day")
                cnl = bot.get_channel(887095059680477214)
                message = await cnl.fetch_message(914295454840258601)
                current_time = datetime.now(
                    pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
                print("Not a vaild period. Checking in approx 5 seconds")
                print(f"Current time : {current_time}")
                if int(list(current_time)[4]) % 3 == 0:
                    cnl = bot.get_channel(887095059680477214)
                    message = await cnl.fetch_message(914295454840258601)
                    await message.edit(embed=refresh())
                await asyncio.sleep(5)
        
        #Off school hours
        else:
            print("School day but off school hours")
            cnl = bot.get_channel(887095059680477214)
            message = await cnl.fetch_message(914295454840258601)
            await message.edit(embed=refresh())
            await asyncio.sleep(180)


#For exceeding API rate limit
try:
    bot.run(os.environ['discordtoken'])
except:
    system('busybox reboot')





#Commentary and Information

#Use this to set up a new token
#file = open('duedate/danieltoken.json', 'r')
#db["token2"] = file.read()
#file.close()
#file = open('duedate/danieltoken.json', 'w')
#file.close()
