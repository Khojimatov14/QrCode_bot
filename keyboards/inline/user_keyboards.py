from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Text", callback_data="text"),
            InlineKeyboardButton(text="🔗 Link", callback_data="link"),
        ],
        [
            InlineKeyboardButton(text="📶 Wi-Fi", callback_data="wifi"),
            InlineKeyboardButton(text="📞 Call", callback_data="call"),
        ],
        [
            InlineKeyboardButton(text="📧 Email", callback_data="email"),
            InlineKeyboardButton(text="✉️ SMS", callback_data="sms"),
        ],
    ]
)

wifi_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="WPA", callback_data="WPA"),
            InlineKeyboardButton(text="WPA2", callback_data="WPA2"),
        ],
        [
            InlineKeyboardButton(text="WPA3", callback_data="WPA3"),
            InlineKeyboardButton(text="WEP", callback_data="WEP"),
        ]
    ]
)

refresh_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="♻️ Yangilash", callback_data="refresh")
        ]
    ]
)