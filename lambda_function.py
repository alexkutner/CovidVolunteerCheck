RESERVATION_URL = "https://volunteer.covidvaccineseattle.org/RegMobile.aspx"

DEFAULT_VALUE = {'SELECT ONE',
                 'SeattleU Jan 25th through 30th: Washington',
                 'SeattleU Jan 18th through 23rd: Washington',
                 'SeattleU Feb 1st through 6th: Washington',
                 'SeattleU Feb 8th through 13th: Washington',
                 'SeattleU Feb 15th through 20th: Washington'}

import json
import urllib.request
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    contents = urllib.request.urlopen(RESERVATION_URL).read()
    soup = BeautifulSoup(contents, 'html.parser')

    dropdownvalues = soup.find(id='ContentPlaceHolder1_DropDownListOpKey').find_all('option')

    for value in dropdownvalues:
        if value.get_text() not in DEFAULT_VALUE:
            return {
                'statusCode': 200,
                'body': json.dumps('New times found')
            }
    return {
        'statusCode': 404,
        'body': json.dumps('no new resource')
    }
