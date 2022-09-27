import telebot
from telebot import types
from requests import get
buy=[0,0,0]
bot=telebot.TeleBot('1480500018:AAGyEekow7WFuNqtNrx4VyEShwpu_Fjjmx8')

buttons=[]
usrs=[]
dict={417081307: [0, 2, 0]}

def check_user(id):
    if id not in usrs:
        usrs.append(id)
        dict[id]=[0,0,0]


#add_name_many_cash_photo
#change_number_many
#delete_number
@bot.message_handler(commands=['start'])
def welcome(message):
    check_user(message.chat.id)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    item1 = types.KeyboardButton("Изменить Адресс отправки")
    item2 = types.KeyboardButton("Изменить Адресс назначения")
    item3 = types.KeyboardButton("Старт")
    markup1.add(item1,item2,item3)
    bot.send_message(message.chat.id, "",parse_mode='html', reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def send(message):
    if message.text=="Изменить Адресс отправки":
        bot.send_message(message.chat.id,"Введите адресс отправки")








bot.polling(none_stop=True)
