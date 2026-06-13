import sys
import asyncio
import logging
from aiohttp import web
from loader import dp, bot
import middlewares, filters, handlers
from middlewares import ThrottlingMiddleware
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data.config import WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


# WEBHOOK
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)
    dp.update.middleware.register(ThrottlingMiddleware())


async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()


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


# POLLING
# async def main():
#     dp.update.middleware.register(ThrottlingMiddleware())
#
#     await bot.delete_webhook(drop_pending_updates=True)
#
#     await asyncio.gather(
#         on_startup_notify(bot=bot),
#         set_default_commands(bot=bot))
#
#     try:
#         await dp.start_polling(bot)
#     except asyncio.CancelledError:
#         logging.info("Bot to‘xtatilmoqda...")
#     finally:
#         await bot.session.close()
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#                         stream=sys.stdout)
#
#     try:
#         asyncio.get_event_loop().run_until_complete(main())
#     except KeyboardInterrupt:
#         logging.info("Bot foydalanuvchi tomonidan to‘xtatildi")
