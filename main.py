import os
import requests
import datetime
import names
import time
import random
import threading
from bs4 import BeautifulSoup as bs
import json
import re


from threading import Lock, Thread
from colorama import Fore, Style, init
from collections import defaultdict
from random import randint


init(autoreset=True)


#with open('config.json') as json_data:
    #config = json.load(json_data)


class logger:
    printLock = threading.Lock()

def process():
  initial_number = 7998
  list_of_pids = []
  while True:
    try:

      

      initial_number = initial_number+1
      
      
      
      
      webhooks = []

      url = 'http://www.geminicollectibles.net/productimage.php?product_id=%s' % (initial_number)

      req = requests.get(url)

      soup = bs(req.text, 'lxml')

      image = soup.find('img', attrs={'id':'TinyImage_0'}).get('src')
      if initial_number < 8701:
        if image == None:
          continue
          #make sure it does not put the pid in the list if image is none

        elif initial_number in list_of_pids:
          with logger.printLock:
            print(time.strftime("[%H:%M:%S]") + Style.BRIGHT + Fore.YELLOW + "No new pids")
          continue

        else:
          title = soup.find('title')
          

          initial_number = initial_number

          list_of_pids.append(initial_number)
          print(list_of_pids)


      else:
        initial_number = 7998
        continue


      data = {
          "embeds": [{

              "color": 9616126,
              "footer": {
                  "icon_url": "https://pbs.twimg.com/profile_images/1042255051069304834/vrjcLB8y_400x400.jpg",
                  "text": ('checked out by @copmilk |' + str(time.ctime()))
                },
                "author": {
                "name": "Scraped:",
                },
                "thumbnail": {
                "url": image
                },
                "fields": [
                {
                    "name": "Name",
                    "value": str(title),
                    "inline": False
               },
               {
                 "name": "Pid",
                 "value": initial_number,
                 "inline": False
               }
             ]
           }
         ]
       }






      time.sleep(1.5)
      requests.post(random.choice(webhooks), json=data)
      continue


    except:
      continue


process()
