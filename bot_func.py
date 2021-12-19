cmd_dict = {

}
import datetime
from datetime import datetime
import pytz
from replit import db
import requests
import os
import discord

#Search for commands
def search(cmd):
    if cmd == 'CMD_GET_ALL':
        return cmd_dict

#Change to the next sequential day
def changeday(day):
    if day == 5:
        day = 1
        db["day"] = int(day)
    else:
        day += 1
        db["day"] = int(day)

    return day

#Set a day to a value
def setday(day):
    db["day"] = int(day)
    return day

#Create a embed for due dates
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



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

#Convert second time to real life time
def findday(second):
    second = second - 18000
    return datetime.fromtimestamp(second).strftime("%A, %B %d, %Y %H:%M:%S")

#Create a weather embed
def weatherembed():
    base_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=43.523365520378476&lon=-79.66657897048847&exclude=minutely,daily,alerts&appid=e8667dca125b603f58a42482dbe11cdc'
    response = requests.get(base_url)
    x = response.json()
    current = x['current']
    hourly = x['hourly']
    currentmod = ''

    currentmod += f"Sunrise today : {findday(current['sunrise'])}"
    currentmod += f"\nSunset today : {findday(current['sunset'])}"
    currentmod += f"\nTemperature : {round(current['temp']-273.15,4)}°C"
    currentmod += f"\nFeels like : {round(current['feels_like']-273.15,4)}°C"
    currentmod += f"\nHumidity : {current['humidity']}%"
    currentmod += f"\nUVI : {current['uvi']}"
    currentmod += f"\nDescription : "
    currentmod += current['weather'][0]['main'] + "-"
    currentmod += current['weather'][0]['description']

    embed = discord.Embed(title='Weather',description=f"**Current**\n\n{findday(current['dt'])}\n\n{currentmod}")
    embed.set_image(url = "https://media.discordapp.net/attachments/922230146038132816/922239336169230386/rain-umbrella-vancouver-weather.jpg?width=1198&height=4")

    hours = 0
    for item in hourly:
        if hours > 11:
            break
        hours += 1
        final = ''
        final += f"\nTemperature : {round(item['temp']-273.15,4)}°C"
        final += f"\nFeels like : {round(item['feels_like']-273.15,4)}°C"
        final += f"\nHumidity : {item['humidity']}%"
        final += f"\nUVI : {item['uvi']}"
        final += f"\nDescription :\n"
        final += item['weather'][0]['main'] + "-"
        final += item['weather'][0]['description'] 
        embed.add_field(name=datetime.fromtimestamp(item['dt']-18000).strftime("%B %d\n %H:%M:%S"), value = final)
    timenow = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
    daynow = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d")
    embed.set_footer(text=f"Written with Python. Updated {daynow} {timenow}")
    
    return embed