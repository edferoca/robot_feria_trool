"""
Este archivo guarda los recursos para  enviar mensajes a los 
diferentes dispositvos externos como 
- Telegram 
"""

import telebot


__all__=['send_telegram_msg']


###################
# funcion Telegram
###################
TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)

def send_telegram_msg(texto):
    bot.send_message(906440079,texto,parse_mode="html")