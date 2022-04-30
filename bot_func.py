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
    dueday = ''
    convmonths = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
    bigmonths = [1, 3, 5, 6, 7, 9, 10, 12 ] 

    try:
        x = bigmonths.index(int(dat[0]))
        if dat[1] == 1:
            if dat[0] >= 2:
                dueday = str(convmonths[dat[0]-2]) +" "+ "30" 
            else:
                dueday = str(convmonths[11]) +" "+ "30"
    except ValueError:
        if dat[1] == 1:
            if dat[0] >= 2:
                dueday = str(convmonths[dat[0]-2]) +" "+ "31" 
            else:
                dueday = str(convmonths[11]) +" "+ "31"

                
    if dueday != '':
        return dueday

    
    if dat[1] == 1 and dat[0] == 3:
        year = int(datetime.now(pytz.timezone('US/Eastern').strftime("20%y"))) % 4
        if year == 0:
            dueday = convmonths[dat[0]-2] +" "+ "28"
        else:
            dueday = convmonths[dat[0]-2] +" "+ "29"
    
    else:
        dueday = str(convmonths[dat[0]-1]) +" "+ str(dat[1]-1)
        
    return dueday



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

#Convert second time to real life time
def findday(second,*args):
    second = second - 14400 #Change to Toronto timezone
    try:
        temp = args[0]
        return datetime.fromtimestamp(second).strftime("%H:%M:%S")
    except:
        return datetime.fromtimestamp(second).strftime("%A, %B %d, %Y %H:%M:%S")

#Create a weather embed
def weatherembed():
    try:
        base_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=43.523365520378476&lon=-79.66657897048847&exclude=&appid=00690130308a127174f58a7a073c7ca7'
        response = requests.get(base_url)
        x = response.json()
        current = x['current']
        hourly = x['hourly']
    except:
        base_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=43.523365520378476&lon=-79.66657897048847&exclude=&appid=c60c87b8057579c58bf1b21e7bbdf86b'
        response = requests.get(base_url)
        x = response.json()
    
    try:
        current = x['current']
        hourly = x['hourly']
        currentmod = ''
    except:
        return "Banned"

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

    embed.add_field(name="Hourly", value = "--\n\n",inline = False)

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

    
    embed.add_field(name="Daily", value = "--\n\n",inline = False)
    
    days = 0
    for item in x['daily']:
        if days > 5:
            break
        days += 1
        daily = ''
        daily += f"Sunrise : {findday(item['sunrise'],True)}"
        daily += f"\nSunset : {findday(item['sunset'],True)}"
        daily += f"\nMoonrise : {findday(item['moonrise'],True)}"
        daily += f"\nMoonset : {findday(item['moonset'],True)}"
        daily += f"\nMax: {round(item['temp']['max']-273.15,4)}°C"
        daily += f"\nMin: {round(item['temp']['min']-273.15,4)}°C"
        daily += f"\nMorning: {round(item['temp']['morn']-273.15,4)}°C"
        daily += f"\nEvening: {round(item['temp']['eve']-273.15,4)}°C"
        daily += f"\nNight: {round(item['temp']['night']-273.15,4)}°C\n\nFeels like  :"
        daily += f"\nMorning: {round(item['feels_like']['morn']-273.15,4)}°C"
        daily += f"\nEvening: {round(item['feels_like']['eve']-273.15,4)}°C"
        daily += f"\nNight: {round(item['feels_like']['night']-273.15,4)}°C"
        daily += f"\nHumidity : {item['humidity']}%"
        daily += f"\nUVI : {item['uvi']}"
        daily += f"\nDescription :\n"
        daily += item['weather'][0]['main'] + "-"
        daily += item['weather'][0]['description'] 

        embed.add_field(name=datetime.fromtimestamp(item['dt']-18000).strftime("%B %d\n %H:%M:%S"), value = daily) 

    try:
        temp = x['alerts']
        embed.add_field(name="Alerts", value = f"Start time : {findday(x['alerts'][0]['start'])}\nEnd time : {findday(x['alerts'][0]['end'])}\n\n Alert : {x['alerts'][0]['description']}")
    except:
        embed.add_field(name="Alerts", value = f"No alerts at this time")

    timenow = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
    daynow = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d")
    embed.set_footer(text=f"Written with Python. Updated {daynow} {timenow}")

    print("Updated weather")
    return embed