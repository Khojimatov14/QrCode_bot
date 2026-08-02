import io
import asyncio
import qrcode
from loader import bot
from aiogram.types import BufferedInputFile
from keyboards import refresh_keyboard


def _generate_qr_bytes(qrcode_text: str) -> bytes:
    img_buf = io.BytesIO()
    img = qrcode.make(data=qrcode_text, border=2, box_size=10)
    img.save(img_buf, format="PNG")
    return img_buf.getvalue()


async def send_qrcode(qrcode_text, user_id):
    photo_bytes = await asyncio.to_thread(_generate_qr_bytes, qrcode_text)
    photo = BufferedInputFile(file=photo_bytes, filename=f"qrcode_{user_id}.png")
    await bot.send_photo(chat_id=user_id, photo=photo, reply_markup=refresh_keyboard)