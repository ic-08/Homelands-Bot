cmd_dict = {

}
import datetime
from datetime import datetime
import pytz



def search(cmd):
    if cmd == 'CMD_GET_ALL':
        return cmd_dict

def changeday(day):

    file1 = open("day.py", "w")
    if day == 5:
        day = 1
        x = "day = " + str(day)
    else:
        day += 1
        x = "day = " + str(day)
    file1.write(x)
    file1.close()
    
    return day

def setday(day):
    file1 = open("day.py", "w")
    x = "day = " + str(day)
    file1.write(x)
    file1.close()
    return day

def cng_due(due705,due805):
    import discord
    final705 = ''
    final805 = ''

    for item in due705:
        final705 += str(item) + "\n\n"

    for item in due805:
        final805 += str(item) + "\n\n"

    embed = discord.Embed(
        title = "Due Dates", 
        color = 0x808080)
    #805 Homework
    embed.add_field(name = "-------------- 805 --------------", value = "\n" + final805,  inline = False)
    
    #705 Homework 
    embed.add_field(name = "-------------- 705 --------------", value = "\n"+ final705, inline = False)
    
    #General ( Applies to all )
    embed.add_field(name = "General", value = "**HAVE YOUR PARENTS FILL OUT YOUR COVID SCREENING SHEET EVERY MORNING**", inline = False)
    timenow = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
    daynow = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d")
    embed.set_footer(text=f"Written with Python. Updated {daynow} {timenow}") #lmao ops
    return embed


##### FOR THE GOOGLEAPI ONLY #####
def alter(dat):
    convmonths = ["Janurary","Feburary","March","April","May","June","July","August","September","October","November","December"]
    bigmonths = [1,3,5,6,7,9,10,12]

    if dat[1] == 1 and dat[0] not in bigmonths:
        if dat[0] >= 2:
            dueday = str(convmonths[dat[0]-2]) +" "+ "31" 
        else:
            dueday = str(convmonths[11]) +" "+ "31"
    
    if dat[1] == 1 and dat[0] == 3:
        year = int(datetime.now(pytz.timezone('US/Eastern').strftime("20%y"))) % 4
        if year == 0:
            dueday = convmonths[dat[0]-2] +" "+ "28"
        else:
            dueday = convmonths[dat[0]-2] +" "+ "29"

    elif dat[1] == 1 and dat[0] in bigmonths:
        if dat[0] >= 2:
            dueday = str(convmonths[dat[0]-2]) +" "+ "30" 
        else:
            dueday = str(convmonths[11]) +" "+ "30"

    
    else:
        dueday = str(convmonths[dat[0]-1]) +" "+ str(dat[1]-1)
    return dueday

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

