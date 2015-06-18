#!/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import subprocess
from time import sleep
def sendmessage(title, message):
   # cmd=['osascript','-e','\'display','notification','\"hello\"', 'with','title','\"kill\"\''];
    cmd=['notify',message]
    subprocess.Popen(cmd).wait()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[1].text
    sendmessage("Score", score)
    sleep(60)
