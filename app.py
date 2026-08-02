import os
import sys
import asyncio
import logging
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from loader import dp, bot
import middlewares, filters, handlers
from middlewares import ThrottlingMiddleware
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

# Environment sozlamalari
WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "").rstrip("/")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")

if not WEBHOOK_URL and WEBHOOK_HOST:
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", os.getenv("WEBAPP_PORT", 8080)))


async def on_startup_polling():
    dp.update.middleware.register(ThrottlingMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def on_startup_webhook(app):
    logging.info(f"Webhook o'rnatilmoqda: {WEBHOOK_URL}")
    dp.update.middleware.register(ThrottlingMiddleware())
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def on_shutdown_webhook(app):
    await bot.delete_webhook()
    await bot.session.close()


def run_webhook():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    app.on_startup.append(on_startup_webhook)
    app.on_shutdown.append(on_shutdown_webhook)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)


async def run_polling():
    await on_startup_polling()
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logging.info("Bot to‘xtatilmoqda...")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    if WEBHOOK_URL:
        logging.info(f"Bot Webhook rejimida ishga tushmoqda. Port: {WEBAPP_PORT}")
        run_webhook()
    else:
        logging.info("Bot Long-Polling rejimida ishga tushmoqda...")
        asyncio.run(run_polling())

