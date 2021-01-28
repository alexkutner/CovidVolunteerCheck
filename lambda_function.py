# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

DEFAULT_VALUE = {'SELECT ONE',
                 'SeattleU Jan 25th through 30th: Washington',
                 'SeattleU Jan 18th through 23rd: Washington',
                 'SeattleU Feb 1st through 6th: Washington',
                 'SeattleU Feb 8th through 13th: Washington'}

import json
import urllib.request
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    contents = urllib.request.urlopen("https://volunteer.covidvaccineseattle.org/RegMobile.aspx").read()
    soup = BeautifulSoup(contents, 'html.parser')

    dropdownvalues = soup.find(id='ContentPlaceHolder1_DropDownListOpKey').find_all('option')

    for value in dropdownvalues:
        if value.get_text() not in DEFAULT_VALUE:
            return {
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }
            print('we found one!')

    return {
        'statusCode': 404,
        'body': json.dumps('no new resource')
    }
