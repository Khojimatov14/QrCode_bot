from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip", default="localhost")

WEBHOOK_URL = env.str("WEBHOOK_URL", default="")
WEBHOOK_PATH = "/webhook"
WEBAPP_HOST = env.str("WEBAPP_HOST", default="0.0.0.0")
WEBAPP_PORT = env.int("WEBAPP_PORT", default=8080)

