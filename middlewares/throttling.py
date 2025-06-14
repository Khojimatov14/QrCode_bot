import time
from aiogram import BaseMiddleware, types

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, default_rate: float = 0.5) -> None:
        self.default_rate = default_rate
        self.users_data = {}

    async def __call__(self, handler, event: types.Update, data: dict):
        user_id = None

        # Foydalanuvchi ID'ni aniqlash
        if event.message:
            user_id = event.message.from_user.id
        elif event.callback_query:
            user_id = event.callback_query.from_user.id

        # Agar foydalanuvchi aniqlanmasa, o'tkazib yuborish
        if not user_id:
            return await handler(event, data)

        now = time.time()
        user_data = self.users_data.get(user_id, {"last": 0.0})

        if now - user_data["last"] < self.default_rate:
            # Throttle qilish
            if event.message:
                await event.message.reply("<b>So'rov ko'payib ketdi!</b>")
            elif event.callback_query:
                await event.callback_query.answer("So'rov ko'payib ketdi!", show_alert=False)
            return  # Javob qaytmaslik

        # Agar throttle bo'lmasa, davom etish
        self.users_data[user_id] = {"last": now}
        return await handler(event, data)
