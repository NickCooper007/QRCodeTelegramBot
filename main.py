from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pq
from config import token
import keep_alive

bot = Bot(token=token)
dp = Dispatcher(bot)

answers = []


@dp.message_handler(commands=['start'])
async def starter(msg: types.Message):
  await msg.answer(
    'Hello this is a QR Code Generator in telegram \nSend me a text and i can create a QR code'
  )


@dp.message_handler()
async def send_text_based_qr(msg: types.Message):
  await msg.answer('your text is received')

  qr_code = pq.create(msg.text)
  qr_code.png('code.png', scale=6)

  with open('code.png', 'rb') as photo:
    await bot.send_photo(msg.chat.id, photo)
    await bot.send_message(
      msg.chat.id, 'Your QR Code is created \nYou can send me another text')


keep_alive.keep_alive()
executor.start_polling(dp)
