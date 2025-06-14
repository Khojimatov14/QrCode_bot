import os
from environs import Env

env = Env()
env.read_env()

if os.getenv("RAILWAY_ENVIRONMENT") is None:  # faqat lokalda ishlasa
    env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
