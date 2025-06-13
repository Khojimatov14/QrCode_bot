from loader import dp
from aiogram import F
from utils import send_qrcode
from states import UserStates
from keyboards import wifi_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

# Text
@dp.callback_query(F.data == "text", UserStates.select_type)
async def text_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Textni kiriting...")
    await state.set_state(UserStates.text)
    await call.answer()


@dp.message(UserStates.text)
async def text_qrcode2(message: Message):
    await send_qrcode(qrcode_text=message.text, user_id=message.from_user.id)


# Link
@dp.callback_query(F.data == "link", UserStates.select_type)
async def link_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Linkni kiriting...")
    await state.set_state(UserStates.link)
    await call.answer()


@dp.message(UserStates.link)
async def link_qrcode2(message: Message):
    await send_qrcode(qrcode_text=message.text, user_id=message.from_user.id)


# Wi-Fi
@dp.callback_query(F.data == "wifi", UserStates.select_type)
async def wifi_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Himoya turini tanlang!", reply_markup=wifi_keyboard)
    await state.set_state(UserStates.wifi_type)
    await call.answer()


@dp.callback_query(UserStates.wifi_type)
async def wifi_qrcode2(call: CallbackQuery, state: FSMContext):
    await state.update_data(wifi_type=call.data)
    await call.message.edit_text(text="Wi-Fi nomini kiriting...")
    await state.set_state(UserStates.wifi_name)
    await call.answer()


@dp.message(UserStates.wifi_name)
async def wifi_qrcode3(message: Message, state: FSMContext):
    await state.update_data(wifi_name=message.text)
    await message.answer(text="Wi-Fi parolini kiriting...")
    await state.set_state(UserStates.wifi_password)


@dp.message(UserStates.wifi_password)
async def wifi_qrcode4(message: Message, state: FSMContext):
    data = await state.get_data()
    wifi_type = data.get("wifi_type", "Noma'lum")
    wifi_name = data.get("wifi_name", "Noma'lum")
    wifi_text = f"WIFI:T:{wifi_type};S:{wifi_name};P:{message.text};;"
    await send_qrcode(qrcode_text=wifi_text, user_id=message.from_user.id)


# call
@dp.callback_query(F.data == "call", UserStates.select_type)
async def call_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Telefon raqamni kiriting...")
    await state.set_state(UserStates.call)
    await call.answer()


@dp.message(UserStates.call)
async def call_qrcode2(message: Message):
    await send_qrcode(qrcode_text=f"tel:{message.text}", user_id=message.from_user.id)


# Email
@dp.callback_query(F.data == "email", UserStates.select_type)
async def email_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Email manzilini kiriting...")
    await state.set_state(UserStates.email_address)
    await call.answer()


@dp.message(UserStates.email_address)
async def email_qrcode2(message: Message, state: FSMContext):
    await state.update_data(email_address=message.text)
    await message.answer(text="Email mavzusini kiriting...")
    await state.set_state(UserStates.email_subject)


@dp.message(UserStates.email_subject)
async def email_qrcode3(message: Message, state: FSMContext):
    await state.update_data(email_subject=message.text)
    await message.answer(text="Email matnini kiriting...")
    await state.set_state(UserStates.email_text)


@dp.message(UserStates.email_text)
async def email_qrcode4(message: Message, state: FSMContext):
    data = await state.get_data()
    email_address = data.get("email_address", "Noma'lum")
    email_subject = data.get("email_subject", "Noma'lum")
    email_text = f"mailto:{email_address}?subject={email_subject}&body={message.text}"
    await send_qrcode(qrcode_text=email_text, user_id=message.from_user.id)


# SMS
@dp.callback_query(F.data == "sms", UserStates.select_type)
async def sms_qrcode(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Telefon raqamni kiriting...")
    await state.set_state(UserStates.sms_number)
    await call.answer()


@dp.message(UserStates.sms_number)
async def sms_qrcode2(message: Message, state: FSMContext):
    await state.update_data(sms_number=message.text)
    await message.answer(text="SMS xabar matnini kiriting...")
    await state.set_state(UserStates.sms_text)


@dp.message(UserStates.sms_text)
async def sms_qrcode3(message: Message, state: FSMContext):
    data = await state.get_data()
    sms_number = data.get("sms_number", "Noma'lum")
    sms_text = f"SMSTO:{sms_number}:{message.text}"
    await send_qrcode(qrcode_text=sms_text, user_id=message.from_user.id)