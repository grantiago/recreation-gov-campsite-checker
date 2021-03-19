#!/usr/bin/env python3

import argparse
import json
import logging
import sys
from datetime import datetime, timedelta
from dateutil import rrule
from itertools import count, groupby

import requests
from fake_useragent import UserAgent
from datetime import date 
today = date.today()
year = today.year
#permit = '234623' #mfs
#zone = '377' #
myStart = '-05-28' # mfs permit start note the hypen -
permitEnd = '09-03'
newYears = "-12-21"
zulu = 'T00:00:00.000Z&'
yearEnd = f"{year}{newYears}{zulu}"


BASE_URL = "https://www.recreation.gov"
AVAILABILITY_ENDPOINT = "/api/permits/"
#AVAILABILITY_ENDPOINT = "/api/camps/availability/campground/"

#MAIN_PAGE_ENDPOINT = "/api/camps/campgrounds/"

INPUT_DATE_FORMAT = "%Y-%m-%d"
ISO_DATE_FORMAT_REQUEST = "%Y-%m-%dT00:00:00.000Z"
headers = {"User-Agent": UserAgent().random}
def valid_date(s):
    try:
        return datetime.strptime(s, INPUT_DATE_FORMAT)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
        
def format_date(date_object, format_string=ISO_DATE_FORMAT_REQUEST):
    """
    This function doesn't manipulate the date itself at all, it just
    formats the date in the format that the API wants.
    """
    date_formatted = datetime.strftime(date_object, format_string)
    return date_formatted
def site_date_to_human_date(date_string):
    date_object = datetime.strptime(date_string, ISO_DATE_FORMAT_RESPONSE)
    return format_date(date_object, format_string=INPUT_DATE_FORMAT)
# she is searching campgrounds not campsites
def send_request(url, params):
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code != 200:
        raise RuntimeError(
            "failedRequest",
            "ERROR, {} code received from {}: {}".format(
                resp.status_code, url, resp.text
            ),
        )
    return resp.json()
park_id = 232448 #tuolomne meadows
div = '/divisions/'
tail = 'commercial_acct=false&is_lottery=false'
api_data = []
'''
https://www.recreation.gov/api/permits/
234624/divisions/
378/availability?
start_date=2021-03-17T06:00:00.000Z&
end_date=2021-12-31T00:00:00.000Z&
commercial_acct=false&is_lottery=false
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d", action="store_true", help="Debug log level")
    parser.add_argument("--start-date", required=True, help="Start date [YYYY-MM-DD]")
    parser.add_argument("--end-date", required=True, help="End date [YYYY-MM-DD]. Best to set it to yyyy-12-31 for next available return.")
    parser.add_argument("--permit", required=True, help="The permit # mfs = 234623 Selway = 234624", type=int)
    args = parser.parse_args()
# argparse replaces '-' in your argument names with underscores when naming the variables
#print(args.start_date)
#print(args.start_date + zulu)
#print(args.end_date)
#print(args.permit)

if args.permit == 234623:
  zone = 377
# print("mfs ")
#  print(zones)
else :
  zone = 378
# print("selway 378")
#  print(zones)
url = "{}{}{}{}{}/availability?".format(BASE_URL, AVAILABILITY_ENDPOINT, args.permit, div, zone)
startd = ('start_date=' + args.start_date + zulu)
endd = ('end_date=' + args.end_date + zulu)
params=(startd + endd + tail)
resp = send_request(url, params)
api_data.append(resp)
#print(api_data)
print(json.dumps(api_data, indent = 3)) 