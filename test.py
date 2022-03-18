   #Variables
    from bot_func import cng_due
    from googleapi import main,main2
    from scheduler import scheduler
    
    day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    channel = bot.get_channel(919281999427043369)
    periods = ['09:00', '09:40', '10:20', '12:00', '12:30', '13:10', '13:50']
    holidays = ['03:15','03:16','03:17','03:18','03:19','03:20']

    if not t1.is_alive():
        sys.exit()

    import asyncio
    
    #Import your subjects and periods
    from subjects import dict705, dict805, dict605, sub
    #CUrrent time
    now_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")
    try:
        os.remove(r'assets/temp/temp.png')
    except:
        pass

    #VARIABLES
    hr = int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H"))
    x = datetime.now(pytz.timezone('US/Eastern')).weekday()
    day = int(db['day'])
    

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
    
    

    #Update the weather embed every 4 minutes
    if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%M")) % 4 == 0:
        from bot_func import weatherembed
        channel = bot.get_channel(922230146038132816)
        message = await channel.fetch_message(922231492296445994)
        try:
            await message.edit(embed=weatherembed())
        except:
            pass

    #HOLIDAYS
    if datetime.now(
            pytz.timezone('US/Eastern')).strftime("%m:%d") in holidays:
        print("Holiday. Refresh in 2 minutes")
        cnl = bot.get_channel(887095059680477214)
        message = await cnl.fetch_message(914295454840258601)
        await message.edit(embed=refresh())
        await asyncio.sleep(120)

    #WEEKEND
    elif day_of_the_week[x] not in weekdays:
        print("Weekend. Refresh in 1 minute")
        cnl = bot.get_channel(887095059680477214)
        message = await cnl.fetch_message(914295454840258601)
        await message.edit(embed=refresh())
        await asyncio.sleep(60)



    #SCHOOL DAY
    
    #School hours
    

    elif hr >=6 and hr <= 14:

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
            await asyncio.sleep(3800)

            #Announce the person who is infected


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
            print("Not a vaild period")
            if int(list(datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S"))[4]) % 3 == 0:
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