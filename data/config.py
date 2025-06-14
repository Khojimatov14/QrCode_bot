import os
from environs import Env

env = Env()
env.read_env()

if os.getenv("production") is None:
    env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
