# import middlewares, filters, handlers
# import asyncio
# import logging
# import sys
# from utils.notify_admins import on_startup_notify
# from utils.set_bot_commands import set_default_commands
# from loader import dp, bot
# from middlewares import ThrottlingMiddleware
#
#
# async def main():
#     await on_startup_notify()
#     await set_default_commands()
#     dp.update.middleware.register(ThrottlingMiddleware())
#     try:
#         await bot.delete_webhook(drop_pending_updates=True)
#         await dp.start_polling(bot)
#     finally:
#         await bot.session.close()
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())


import middlewares, filters, handlers
import asyncio
import logging
import sys
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import dp, bot
from middlewares import ThrottlingMiddleware
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

# 🔐 Webhook sozlamalari (sizning NGROK domeningiz asosida)
WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = "https://2f66-90-156-165-215.ngrok-free.app"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = "0.0.0.0"  # barcha IP'lar uchun ochiq
WEBAPP_PORT = 3000       # ngrok orqali yo'naltirilgan port

# 🚀 Bot ishga tushganda:
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    await on_startup_notify()
    await set_default_commands()
    dp.update.middleware.register(ThrottlingMiddleware())
    print(f"Webhook set to: {WEBHOOK_URL}")

# 🛑 Bot to‘xtaganda:
async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()
    print("Webhook removed and session closed.")

# 🌐 Web-serverni ishga tushirish
async def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    setup_application(app, dp, bot=bot)
    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    web.run_app(main(), host=WEBAPP_HOST, port=WEBAPP_PORT)


