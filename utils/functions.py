import os
import qrcode
from loader import bot
from data.config import ADMINS
from aiogram.types import FSInputFile
from keyboards import refresh_keyboard


async def send_qrcode(qrcode_text, user_id):
    photo_path = f"utils/qrcodes/{user_id}.png"
    img = qrcode.make(data=qrcode_text, border=1, box_size=50)
    img.save(photo_path)
    await bot.send_photo(chat_id=user_id, photo=FSInputFile(path=photo_path), reply_markup=refresh_keyboard)
    try:
        os.remove(path=photo_path)
    except FileNotFoundError as error:
        await bot.send_message(chat_id=ADMINS[0], text=f"Faylni o'chirishda hatolik yuz berdi!\n\n{error}")