from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    sms_text = State()
    sms_number = State()
    email_text = State()
    email_subject = State()
    email_address = State()
    call = State()
    wifi_password = State()
    wifi_name = State()
    wifi_type = State()
    link = State()
    text = State()
    select_type = State()