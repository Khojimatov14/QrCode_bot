from environs import Env

env = Env()

BOT_TOKEN = env.str("BOT_TOKEN")
RAILWAY_DOMAIN = env.str("RAILWAY_DOMAIN")
ADMINS = env.list("ADMINS")
