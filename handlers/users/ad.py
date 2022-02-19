import asyncio

from states.advertisement import Advertisement
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot
from utils.photograph import photo_link

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def do_ad(message: types.Message):
    await message.answer("Reklamangizni yuboring:")
    await Advertisement.ad.set()
    

@dp.message_handler(state=Advertisement.ad)
@dp.message_handler(content_types="photo", state=Advertisement.ad)
async def answer_ad(message: types.Message, state: FSMContext):
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        if message.content_type == "photo":
            photo = message.photo[-1]
            link = await photo_link(photo)
            try:
                await bot.send_photo(chat_id=user_id, photo=link, caption=message.caption)
            except:
                pass
        else:
            try:
                await bot.send_message(chat_id=user_id, text=message.text)
            except:
                pass
        await asyncio.sleep(0.05)
    await state.finish()
    await message.answer("Reklama foydalanuvchilarga yuborildi!")

