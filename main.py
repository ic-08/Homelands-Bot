#FOR ANY ANNOUNCERS, PLEASE ONLY EDIT DUEDATE.PY
#THANK YOU FOR YOUR COOPERATION AND UNDERSTANDING
import discord
from discord.ext import commands, tasks
import os
from scheduler import scheduler
import datetime
from datetime import * 
import pytz
import random
from replit import db
import requests
import time
import sys
from threading import Thread
import json
import asyncio

#Start up@
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name="$help | $cmd for commands")
bot = commands.Bot(command_prefix="$",activity=activity,status=discord.Status.online, help_command=None,intents=intents)
bot.help_command = None
bot.strip_after_prefix = True
tme = time
print(f"Repl Database keys in use : {db.keys()}")
for key in db.keys():
    print(f"{key} : {db[str(key)]}")
          
#bot.remove_command('help')

#Bot status check
async def b_status():
    global x
    while True:
        try:
            r = requests.get('https://Pinging-bot.isaacchu1.repl.co/status',timeout=10)
            x = r.json()
            if x[0]['status'] != 'ONLINE':
                print("Bot offline")
                print("Rebooting") 
                print(f"Bot status : {x[0]['status']}")
                await bot.close()
                sys.exit()
            else:
                await asyncio.sleep(5)
        except:
            pass

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
#https://www.i2symbol.com/symbols/corner link to unicode characters for stuff like this: └
#see Dank Memer pls help to see more
'''

Notice: Before each command, there SHOULD be a comment detailing the command and how to use it.
For example:
#test() is for testing. Ex: $test, $ttt
@bot.command()
'''

@bot.command()
async def test(ctx):
    for item in bot.users:
        if not item.bot:
            print(item.id)
            await ctx.send(item.id)
            await ctx.send(item)

#_9ball is for 'determining the future' (not really). Ex: $_9ball <prompt>, $9ball <prompt>, $9 <prompt>


@bot.command(aliases=['9ball', '9b'])
async def _9ball(ctx,*args):  #unfortunally, async def 8ball(): returned an error
    #list of predictions to (randomly) choose from
    predictions = [
        "Don't count on it.", 'My reply is no.',
        'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
    ]

    if str(args) != '()':
        msg = random.choice(predictions)
    else:
        msg = 'No prompt given. Try `$9ball <prompt>`'

    await ctx.send(msg)

#_8ball is for 'determining the future' (not really). Ex: $_8ball <prompt>, $8ball <prompt>, $8b <prompt>


@bot.command(aliases=['8ball', '8b'])
async def _8ball(ctx,*args):  #unfortunally, async def 8ball(): returned an error
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

#_7ball is for 'determining the future' (not really). Ex: $_7ball <prompt>, $7ball <prompt>, $7b ( Jeopardised version of 8 ball) <prompt>


@bot.command(aliases=['7ball', '7b'])
async def _7ball(ctx,*args):  #unfortunally, async def 7ball(): returned an error
    #list of predictions to (randomly) choose from
    predictions = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
    ]

    if str(args) != '()':
        msg = random.choice(predictions)
    else:
        msg = 'No prompt given. Try `$7ball <prompt>`'

    await ctx.send(msg)
    
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



#cmd() is for getting a list of cmds. For now it is a list, aiming to build a list like Dank Memer


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

#report() is for reporting users : Ex: $report Someone deleted the report commands




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
        "**Hi! Welcome to the Homelands Bot Help Manual**\nI am proud to be part of the Homeland's community!I can currently do a few things, altough you can check my current commands by typing `$help`. Homelands bot aims to provide support, such as reminders, fun games, homework support, and more!\n Have fun and **GO HOMELANDS**!",
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




#server() is for server details. Ex: $server


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
        infectedembed = discord.Embed(title = "Infection", description = f"The infection has been passed on to '<@!{int(finlist)}>")
        await channel.send(embed=infectedembed)
        
        user = await bot.fetch_user(int(finlist))
        embd = discord.Embed(title = "You have been infected!",description = "Pass on the infection to someone else by typing `$infect {user id}` in an channel in the ELC server. Doing so will also remove the infection from you.\n\nIf you don't know how to get user id:\n\n1.Go to user settings\n2.Click on Advanced\n3.Turn on developer mode\n4.Press the Esc key\n5.Right click a user in the member list on the side and click Copy ID")
        await user.send(embed=embd)
        await ctx.message.delete()
    else:
        await ctx.send("You are not infected!")
        await ctx.message.delete()









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


@bot.command()
async def report(ctx,*args):
    channel = bot.get_channel(846813361177755648)
    report = ''
    for message in args:
        report += message + " "
    await channel.send(f"{ctx.author.mention} reports : {report}")
    await ctx.send(f"{ctx.author.mention}, your request has been received. The admins will look over your case.\nKeep in mind : For the best response time, include the perpetrator, reason for report, and message link if valid to make your requests quicker")

#ping() is for people who want to ping the bot


@bot.command()
async def ping(ctx):
    start_time = time.time()
    await ctx.send("** **")
    embed = discord.Embed(title="Pong!", description = f"Response time : \n\nLatency :{bot.latency * 1000} ms\nDiscord API :{time.time() - start_time * 1000} ms")
    embed.set_footer(text="Written with python")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed, mention_author=False)


#rev() is for reversing a sentence. Ex: $rev <arg>


@bot.command()
async def rev(ctx, *args):
    s = ''
    potty_words = [
    "faggot",
    "bastard",
    "whore",
    "nigger",
    "nigga",
    "bitch",
    "cunt",
    "asshole",
    "motherfucker",
    "twat",
    "fag",
    "fuck",
    "hoe",
    "slut",
    "dick" 
    ]
    for item in args:
        if item not in potty_words:
          s += str(item)
          s += ' '
    stringlength = len(s)
    rev_sentence = s[stringlength::-1]

    for item in rev_sentence.split(' '):
        if item in potty_words:
            await ctx.reply("No potty words please")
            break
    
    if item not in potty_words:
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
async def resmessage(ctx):
    if ctx.channel.id == 923714584462884894 or ctx.channel.id == 923020245512384512:
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
async def post(ctx,*args):

    message = ''
    num = 0
    for item in args:
        message += str(args[num]) + " "
        num += 1
    await ctx.send("Ping role (Type id). Or type something random or 'None' to ping no roles")
    
    response = await bot.wait_for('message')
    await ctx.channel.purge(limit=2)
    if response.content.lower() == 'none':
        message = await ctx.send(message)
    else:
        try:
            message = await ctx.send(f"<@&{response.content}> {message}")
        except:
            message = await ctx.send(message)
        
        # actions which should happen if the person responded with 'no' or something els
    #await prompt.message.delete()
    #await response.message.delete()
    
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
    await ctx.message.delete()                                          





@bot.command(aliases=['reboot','refresh'])
async def restart(ctx):
    if ctx.channel.id in modlist_channels:
        await ctx.send("Restarting...")
        channel = int(ctx.channel.id)
        db["restartctx"] = str(channel) + " " + str(tme.time())
        sys.exit()
        



@bot.event
async def on_ready():

    #Restart command finished ( Messages the user after restart command has completed)
    restartvalue = db['restartctx']
    if restartvalue != 0:

        #Infection game
        if restartvalue == "reboot":
            from random import choice
            randomuser = choice(bot.users)

            channel = bot.get_channel(839135669712060490)
            await channel.send(f"<@!{int(db['infected'])}> was infected at the end of the week.")

            db['infected'] = int(randomuser.id)

            user = await bot.fetch_user(int(db['infected']))

            embd = discord.Embed(title = "You have been infected with hehehehaw!",description = "Pass on the hehehehaw to someone else by typing `$infect {user id}` in an channel in the ELC server. Doing so will also remove the hehehehaw from you.\n\nIf you don't know how to get user id:\n\n1.Go to user settings\n2.Click on Advanced\n3.Turn on developer mode\n4.Press the Esc key\n5.Right click a user in the member list on the side and click Copy ID")
            await user.send(embed=embd)
            db["restartctx"] = 0
        else:
            cnl = db['restartctx']
            cnl = cnl.split()
            channel = bot.get_channel(int(cnl[0]))
            embd = discord.Embed(title = "Connected",
                                 description = f"Restart finished.\nExecuted in {tme.time() - float(cnl[1])}", 
                                 color=discord.Color.green())
            
            await channel.send(embed=embd)
            db["restartctx"] = 0

    channel = bot.get_channel(919281999427043369)
    #CONNECTED MESSAGE#
    clock = datetime.now(
        pytz.timezone('US/Eastern')).strftime("%m/%d/%y  %H:%M:%S")
     
    await channel.send(embed=discord.Embed(
        title='Homelands Bot is Online',
        description=f"Logged on as {bot.user} as of {clock}",
        color=discord.Color.green()))
    
    print('Logged on')
    global idling_time
    idling_time = 0
    background_task.start()
    scheduling.start()
    global nested
    await asyncio.create_task(b_status())




@tasks.loop(seconds=5)
async def scheduling():

    
    global idling_time
    global time_status
    if idling_time != 0:
        idling_time -= 5
    else:
        
        #Scheduling for school
        from scheduler import scheduler
        from subjects import dict705, dict805, dict605, sub
        day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        channel = bot.get_channel(919281999427043369)
        periods = ['09:00', '09:40', '10:20', '12:00', '12:30', '13:10', '13:50']
        holidays = ['03:15','03:16','03:17','03:18','03:19','03:20']
        now_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")
        hr = int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H"))
        x = datetime.now(pytz.timezone('US/Eastern')).weekday()
        day = int(db['day'])

        
        try:
            os.remove(r'assets/temp/temp.png')
        except:
            pass
        
        #Non-school days
        if datetime.now(
                pytz.timezone('US/Eastern')).strftime("%m:%d") in holidays or day_of_the_week[x] not in weekdays:
            time_status = "Holiday. Refresh in a minute."
            idling_time = 60
    
        #School days
                    
        #School hours
        elif hr >=6 and hr <= 14:
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
                idling_time = 600
    
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
                idling_time = 600
                
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
    
                #Time
                file = scheduler()
    
                #Prompt in the scheduling.
                if day_of_the_week[x] == "Friday":
                    day_prompt = "Monday"
                else:
                    day_prompt = "Tomorrow"
    
                #Send the schedule for tomorrow
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
                idling_time = 9000
    
    
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
                idling_time = 1500
            else:
                time_status = "School hours"
        else:
            time_status = "School day but off school hours"
            idling_time = 60


@tasks.loop(seconds=60) 
async def background_task():
    
    from startup import timeupdate
    if timeupdate() == 'restart':
        sys.exit()
    global x
    global time_status
    try:
        print(f"Bot status : {x[0]['status']}\n")
        print(time_status)
    except:
        pass
    
    #Variables
    from bot_func import cng_due
    from googleapi import main,main2
    from bot_func import weatherembed
    
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
    
    

    #Update the weather and duedate embed every 4 and 1 minute(s)
    cnl = bot.get_channel(887095059680477214)
    message = await cnl.fetch_message(914295454840258601)
    try:
        await message.edit(embed=refresh())
    except:
        pass
    if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%M")) % 4 == 0:
        
        channel = bot.get_channel(922230146038132816)
        message = await channel.fetch_message(922231492296445994)
        try:
            await message.edit(embed=weatherembed())
        except:
            pass



if __name__ == "__main__":

    #Start
    from startup import run
    t = Thread(target=run)
    t.daemon = True
    t.start()

            
    asyncio.get_event_loop().run_until_complete(bot.start(os.environ['discordtoken'],reconnect=True))
    
    sys.exit()






