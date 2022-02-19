from aiogram.dispatcher.filters.state import StatesGroup, State


class Advertisement(StatesGroup):
    ad = State()