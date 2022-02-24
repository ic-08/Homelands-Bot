   #Error check if it isn't during school times

    ###ERROR CHECKING###
    infoping = ''  
    des = ''
    reboot = False

    #Embed
    channel = bot.get_channel(919281999427043369)
    embd = discord.Embed(title = "Connected", description = "Checking for errors...",  color=discord.Color.red())
    embd.set_image(url = 'https://cdn.discordapp.com/attachments/919281999427043369/920113239809994792/download.jpg')
    msg = await channel.send(embed=embd)



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
        if weatherembed() == "Banned": #Rate limited
            des += f"\n\nWeather API and function failed ...\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
        else:
            des += f"\n\nWeather API and function passed ...\nExecution time : {'{:.18f}'.format(tme.time() - executiontime)} seconds"
    except:
        des += '\n\nError in Weather API. Priority is medium - Inform the public about the temporary error'
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