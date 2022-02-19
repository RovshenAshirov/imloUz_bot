import asyncpg
from aiogram import types
from loader import bot, dp, db
from data.config import ADMINS


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    have = False
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
        have = True
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
            
    await message.answer(f"Assalomu alaykum botimizga xush kelibsiz.\n")

    # ADMINGA xabar beramiz
    if have:
        count = await db.count_users()
        msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)



