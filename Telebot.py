import telebot
from telebot import types
from ride import Ride
bot = telebot.TeleBot("botkey")

need_list=[]
give_list=[]
r=Ride()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    itembtn1 = types.InlineKeyboardButton("need or give ride", callback_data="enter hi")
    itembtn2 = types.InlineKeyboardButton("Just checking", callback_data="check")
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Hi welcome to UTA Rides", reply_markup=markup)


@bot.callback_query_handler(lambda query: query.data.split()[0] == "enter")
def need_or_give(query):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    itembtn1 = types.InlineKeyboardButton("need ride", callback_data="needb")
    itembtn2 = types.InlineKeyboardButton("give ride", callback_data="giveb")
    markup.add(itembtn1, itembtn2)
    bot.reply_to(query.message, "select an option", reply_markup=markup)




@bot.callback_query_handler(lambda query: query.data.split()[0] == "needb")
def needb(query):
    reply_to_send="send message in this formate below\nif need ride: /need[Space]fromAddress,toAddress,aproxDist,date,time\nexample: /need 404,fortworth,20,12,12pm"
    try:
        bot.send_message(query.message.chat.id, reply_to_send)
    except  Exception as e:
        print(e)


@bot.callback_query_handler(lambda query: query.data.split()[0] == "giveb")
def giveb(query):
    reply_to_send="send message in this formate below\nto give ride: /give[Space]fromAddress,toAddress,aproxDist,date,time\nexample: /give 404,fortworth,20,12,12pm"
    try:
        bot.send_message(query.message.chat.id, reply_to_send)
    except  Exception as e:
        print(e)


@bot.message_handler(commands=['need'])
def need_entry(message):
    try:
        det=message.text.strip().split(" ",1)[1].split(",")
        det.append(message.from_user.username)
        need_list.append(det)
        bot.reply_to(message, "entry rigistered"+str(det))
    except Exception as e:
        print(e)
        bot.reply_to(message, "entry not rigistered error:"+str(e))

@bot.message_handler(commands=['give'])
def give_entry(message):
    try:
        det=message.text.strip().split(" ",1)[1].split(",")
        det.append(message.from_user.username)
        give_list.append(det)
        bot.reply_to(message, "entry rigistered"+str(det))
    except Exception as e:
        print(e)
        bot.reply_to(message, "entry not rigistered error"+str(e))


@bot.callback_query_handler(lambda query: query.data.split()[0] == "enter")
def process_callback_enter(query):
    reply_to_send="send message in this formate below\nif need ride: /need[Space]fromAddress,toAddress,aproxDist,date,time\nif give ride: /give[SPACE]fromAddress,toAddress,date,time\nexample: /need 404,fortworth,20,12,12pm"
    try:
        bot.send_message(query.message.chat.id, reply_to_send)
    except  Exception as e:
        print(e)


@bot.callback_query_handler(lambda query: query.data == "check")
def process_callback_check(query):
    try:
        strr="need rides: \n"
        if len(need_list)!=0:
            for i in need_list:
                strr=strr+"@"+str(i[5])+" need ride "+str(i[0])+" --> "+str(i[1])+" dist: "+str(i[2])+" on "+str(i[3])+"th at "+str(i[4])+"\n";
        strr=strr+"================================\ngive rides: \n"
        if len(give_list)!=0:
            for i in give_list:
                strr=strr+"@"+str(i[5])+" will give ride "+str(i[0])+" --> "+str(i[1])+" on "+str(i[3])+"th at "+str(i[4])+"\n";
        bot.send_message(query.message.chat.id, strr)
    except Exception as e:
        print(e)





while 2>1:
    try:
        bot.polling()
    except Exception as e:
        print("error in polling"+str(e))
