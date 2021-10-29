from app import bot, dp
from config import admin_id

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
   await bot.send_message(chat_id=admin_id, text="Salom Raxmatjon bot ishga tushdi")
word = ['Roma', 'Raxmatjon', 'roma', 'raxmatjon', 'Rahmatjon', 'rahmatjon', 'Juventus', 'Yuventus', 'Juve', 'Yuve', 'ufo607', 'ufo 607', 'ufo_607', 'Ufo607', 'Ufo_607', 'Ufo 607', 'Roma Borz', 'roma Borz', 'roma borz']
neg = ['Barcelona', 'Barselona', 'barcelona', 'barselona', 'barca', 'barsa', 'Barca', 'Barsa', 'Real', 'Real Madrid', 'real', 'real madrid','realmadrid', 'RealMadrid']
@dp.message_handler()
async def echo(message: Message):
   count = 0
   chat_id = message["from"]["id"]
   text = message.text
   if text in word:
      await bot.send_message(chat_id=chat_id, text=f"'{text}' best of the best")
   elif text in neg:
      await bot.send_message(chat_id=chat_id, text=f"'{text}' bad of the bad")
   else:
      await bot.send_message(chat_id=chat_id, text=text)
