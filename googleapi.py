from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime
from datetime import *
import pytz
import time
tme = time
from replit import db



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.student-submissions.me.readonly', 'https://www.googleapis.com/auth/classroom.courses.readonly']

'''
caribou, all the 705 stuff, back to the classroom at 88mph
'''

convmonths = ["Janurary","Feburary","March","April","May","June","July","August","September","October","November","December"]



def main():
    global convmonhts
    classes805 = [
        'Homelands Spirit Hawks',
        'Caribou Math Contest',
        '805 Music',
        '805 PE',
        'teCH-eray 805',
        '805 - French, Arts',
        '805 ELC']

    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('duedate/token.json'):
        creds = Credentials.from_authorized_user_file('duedate/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else: 
            os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
            flow = InstalledAppFlow.from_client_secrets_file(
                'duedate/cred.json',SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('duedate/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])


    if not courses:
        print('No courses found.')
    else:
        shortcutday = datetime.now(pytz.timezone('US/Eastern'))
        ymd = {
            'year' : int(shortcutday.strftime("20%y")),
            'month' : int(shortcutday.strftime("%m")),
            'day' : int(shortcutday.strftime("%d"))}
        
        due = []

        print('Google Classroom API running...\nCurrently working on class 805')
        for course in courses:
            try:
                work = service.courses().courseWork().list(courseId=course[u'id']).execute()


                if course['name'] in classes805:

                    assignnum = 0
                    for item in work['courseWork']:
                        
        
                        try:
                            from bot_func import alter
                            ddymd = work['courseWork'][assignnum]['dueDate']

                            formatteddue = "\nDue : " + alter([int(work['courseWork'][assignnum]['dueDate']['month']),int(work['courseWork'][assignnum]['dueDate']['day'])])

                            if ddymd['year'] >= ymd['year'] and ddymd['month'] >= ymd['month'] and ddymd['day'] >= ymd['day']:

                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**"+ str(formatteddue))
                            elif ddymd['year'] > ymd['year']:
                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**"+ str(formatteddue))
                            elif ddymd['year'] >= ymd['year'] and ddymd['month'] > ymd['month']:
                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**"+ str(formatteddue))
                        except:
                            pass

                        assignnum += 1
                else:
                    pass
                    
                    
            except KeyError:
                pass 
        return due      
        
def main2():

    classes705 = [
        '705 Music',
        '705 PE',
        '705 - Cobo- tech',
        '705',
        '705  - Linthwaite (ROTARY) 21/22',
        'Back to the Classroom (at 88 mph) - Part I']

    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('duedate/danieltoken.json'):
        creds = Credentials.from_authorized_user_file('duedate/danieltoken.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
            flow = InstalledAppFlow.from_client_secrets_file(
                'duedate/cred.json',SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('duedate/danieltoken.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    

    if not courses:
        print('No courses found.')
    else:
        shortcutday = datetime.now(pytz.timezone('US/Eastern'))
        ymd = {
            'year' : int(shortcutday.strftime("20%y")),
            'month' : int(shortcutday.strftime("%m")),
            'day' : int(shortcutday.strftime("%d"))}
        
        due = []

        print('Google Classroom API running...\nCurrently working on class 705')
        for course in courses:
            try:
                work = service.courses().courseWork().list(courseId=course[u'id']).execute()


                if course['name'] in classes705:

                    assignnum = 0
                    for item in work['courseWork']:
                        
                        
                
                        try:
                            from bot_func import alter
                            ddymd = work['courseWork'][assignnum]['dueDate']
                            formatteddue = "\nDue : " + alter([int(work['courseWork'][assignnum]['dueDate']['month']),int(work['courseWork'][assignnum]['dueDate']['day'])])
                            if ddymd['year'] >= ymd['year'] and ddymd['month'] >= ymd['month'] and ddymd['day'] >= ymd['day']:
                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**" + str(formatteddue))
                            elif ddymd['year'] > ymd['year']:
                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**" + str(formatteddue))
                            elif ddymd['year'] >= ymd['year'] and ddymd['month'] > ymd['month']:
                                due.append("**" + str(work['courseWork'][assignnum]['title'])+"**"+ str(formatteddue))
                        except:
                            pass

                        assignnum += 1
                else:
                    pass
                    
                    
            except KeyError:
                pass 
                
        return due      
        

#def homework(year,month,day):

