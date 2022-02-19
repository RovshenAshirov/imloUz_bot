from aiogram import types
from data.config import ADMINS
from loader import dp, db

@dp.message_handler(text="/number_of_users", user_id=ADMINS)
async def see_user(message: types.Message):
    users = await db.select_all_users()
    await message.answer(f"Bot foydalanuvchilari soni:  {len(users)}")
