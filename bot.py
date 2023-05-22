import sys
import time
import datetime
import telepot
import requests
import bs4
from bs4 import BeautifulSoup

#Insert here your bot token
bot = telepot.Bot('insert here your bot token')

#Insert here your chat id
chat_id = 'insert here your account id'

#Taking from the text files the last news you received
id_file = open("id_file.txt","r")
id_post=(id_file.read())
id_file.close()

#Taking from the text files the team you choose
team_file = open("my_team.txt","r")
team=(team_file.read())
team_file.close()
team_url = team.rstrip('\n')


base_url="https://www.bbc.com/sport/football/teams/"
final_url= base_url + team_url

#Web scraping the next news
page = requests.get(final_url)
page_code = BeautifulSoup(page.content, 'html.parser')
section = page_code.find("main", {"id": "main-content"})
listUl = section.find_all("ul")
get_link=listUl[0].find('a').get('href')

#Comparing the next news and the last news
feed_link = "https://www.bbc.com/" + get_link 
link_prev = id_post.rstrip('\n')
if feed_link == link_prev:
        compare = 0
else:
    compare = 1
    id_file = open('id_file.txt', 'r+')
    id_file.truncate(0)
    id_file.close()
    id_file = open("id_file.txt","w")
    id_file.write(str(feed_link))
    id_file.close()
    bot.sendMessage(chat_id,feed_link)
