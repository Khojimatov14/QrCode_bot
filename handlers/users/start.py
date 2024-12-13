from loader import dp
from aiogram import types, F
from states import UserStates
from keyboards import main_keyboard
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart, Command


@dp.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="Sizga qanday QrCode kerak?", reply_markup=main_keyboard)
    await state.set_state(UserStates.select_type)


@dp.callback_query(F.data == "refresh", UserStates())
async def settings(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()
    await call.message.answer(text="Sizga qanday QrCode kerak?", reply_markup=main_keyboard)
    await state.set_state(UserStates.select_type)


@dp.message(Command("bot"))
async def bot_start(message: types.Message):
    await message.answer(text="Assalomu alekum\n\nAgar sizga Telegram bot yaratish hizmati kerak bo'lsa menga yozing! "
                              "Yoki qo'ng'iroq qiling!\n\nTelegram: @khojimatov14\n+998 90-626-66-44")

