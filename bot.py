import time
import random
import telepot
import json
import sys
import re
from time import sleep


from telepot.loop import MessageLoop


def handle(msg):
    chat_id= msg['chat']['id']
    command = msg['text']
    
    dict = bot.getChat(chat_id)
    
    print(dict)
    print(msg)
    dictmsg = msg['from']
    ##print(dictmsg['first_name'])
    ##print(dict['first_name'])

    print ('Got Command: %s'%command)
    #bot.sendMessage(chat_id,"Halo Kak " + dict['first_name'])
    check = command.find('Indi')
    check1 = command.find('indi')
    if check >=0 or check1 >=0:
        result= command.find('paket indihome')
        result2= command.find('paket fit')
        result3= command.find('paket phoenix')
        result4= command.find('paket single play')
        result5= command.find('odp')
        result6= command.find('paket sky')
        result7= command.find('karyawan')
        result8= command.find('pacar')
        result9= command.find('halo')
        result10= command.find('streamix')
        #result11= command.find('sky')
        result12=command.find('kenal')
        result13=command.find('lagi apa')
        result14= command.find('lagi ngapain')
        result15=command.find('keyword')
        
    

        if result >= 0:
            bot.sendMessage(chat_id,str('Silahkan Kak '+dictmsg['first_name'] ))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/mb5G1Z2'))
        if result2 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/mHyTFLr'))

        if result3 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/MMmYz8V'))
            
        if result4 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/q9hcKCG'))
            
        if result5 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/VtVbkGC'))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/v1Rg70V'))

        if result6 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/rfYwvNH'))

        if result7 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini harganya Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/bJCMthx'))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/Kw7651n'))

        if result8 >= 0:
            bot.sendMessage(chat_id,str('HAH pacar?'))
            bot.sendMessage(chat_id,str('Kak '+ dictmsg['first_name']+' bisa aja deh'))
            
        if result9 >= 0:
            bot.sendMessage(chat_id,str('Iyaa sayang'))

        if result10 >= 0:
            bot.sendMessage(chat_id,str('Silahkan, ini Kak ' +dictmsg['first_name']))
            bot.sendPhoto(chat_id=chat_id,photo=('https://ibb.co/F4bH2Jj'))

        if result12 >=0:
            bot.sendMessage(chat_id,str('Kenal ? Siapa tuh Kak ' +dictmsg['first_name']))

        if result13 >=0:
            bot.sendMessage(chat_id,str('Bales chat Kakak ' +dictmsg['first_name'] + ' dong'))

        if result14 >=0:
            bot.sendMessage(chat_id,str('Bales chat Kakak ' +dictmsg['first_name'] + ' dong'))

        if result15 >=0:
            bot.sendMessage(chat_id,str('Halo kak ' +dictmsg['first_name'] + ' untuk menggunakan bot ini terdapat beberapa keyword yang digunakan yaitu paket indihome, paket fit, paket phoenix, paket single play, odp, paket sky, karyawan, pacar, halo, streamix, kenal, lagi apa, lagi ngapain, keyword'))      
                
            
                
#bot = telepot.Bot(token api)               
bot = telepot.Bot('966720987:AAEcdEXwHjKddxpWF-R97Ns-ZB3UC9EZWfM')

MessageLoop(bot,handle).run_as_thread()
print ('I am Listening....')

while 1:
    time.sleep(10)
