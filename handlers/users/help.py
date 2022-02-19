from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import ADMINS

from loader import dp

@dp.message_handler(CommandHelp(), user_id=ADMINS)
async def bot_help_admin(message: types.Message):
    text = ("Admin uchun buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/reklama - Reklama yuborish",
            "/number_of_users - Foydalanuvchilar sonini ko'rish")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))