import os
import telebot
import requests
import json
import csv
import io


# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('db827ac1')
bot_id = os.getenv('5652864232:AAFKKpMExXR9cH17akEcexSthhFRQOJgxB8')

bot = telebot.TeleBot('5652864232:AAFKKpMExXR9cH17akEcexSthhFRQOJgxB8')

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    
    bot.reply_to(message, 'Getting movie info...')
    
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    movie_name=(message.text).replace('/movie ','')
    movie_name_csv=(message.text).replace('/movie ','')
    
    url1='http://www.omdbapi.com/?apikey=db827ac1&t='+movie_name
    responce=requests.get(url1)
    print(responce.text)
    abcd=json.loads(responce.text)
    efgh="  Movie Name :"+str(abcd["Title"])+"\n "+"Year :"+str(abcd["Year"])+"\n"+" Released :"+str(abcd["Released"])+"\n"+" imdbRating :"+str(abcd["imdbRating"]+"\n"+str(abcd["Poster"]))
    print(efgh)
    bot.send_message(message.chat.id,efgh)
    


      
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    movie_name=(message.text).replace('/export ','')
    
    movie_name_csv=(message.text).replace('/export ','')+'.csv'
    
    url2='http://www.omdbapi.com/?apikey=db827ac1&t='+movie_name
    responce = requests.get(url2)
    
    abcd=json.loads(responce.text)
    efgh="  Movie Name :"+str(abcd["Title"])+"\n "+"Year :"+str(abcd["Year"])+"\n"+" Released :"+str(abcd["Released"])+"\n"+" imdbRating :"+str(abcd["imdbRating"])
    print(efgh)
    row1=["Movie Name",str(abcd["Title"])]
    row2=["Year :",str(abcd["Year"])]
    row3=[" Released :",str(abcd["Released"])]
    row4=[" imdbRating :",str(abcd["imdbRating"])]
    
    
    
    filename = movie_name_csv

    with open(filename, 'w+') as csvfile :
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(row1)
        csvwriter.writerow(row2)
        csvwriter.writerow(row3)
        csvwriter.writerow(row4)


        

    pqr=open(filename,'r')
    bot.send_document(message.chat.id,document=pqr)
    
    
    

    

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
