from aiogram import types


async def set_default_commands(bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='Botni ishga tushurish'),
            types.BotCommand(command='bot', description='Yangi botga buyurtma berish!')
        ]
    )
