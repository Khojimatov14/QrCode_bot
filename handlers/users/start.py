from aiogram import types, F
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import main_keyboard
from loader import dp
from states import UserStates


@dp.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="Sizga qanday QrCode kerak?", reply_markup=main_keyboard)
    await state.set_state(UserStates.select_type)


@dp.callback_query(F.data == "refresh", UserStates())
async def settings(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()
    await call.message.answer(text="Sizga qanday QrCode kerak?", reply_markup=main_keyboard)
    await state.set_state(UserStates.select_type)

