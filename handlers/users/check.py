from aiogram import types
from loader import dp
from utils.transliterate import to_cyrillic, to_latin
from utils.checkWord import checkWord

@dp.message_handler()
async def check(message: types.Message):
    msg = message.text
    latin = False
    if msg.isascii():
        msg = to_cyrillic(msg)
        latin = True
    result = checkWord(msg)
    if result['available']:
        if latin:
            msg = to_latin(msg)
            await message.answer(f'✅ {msg}')
        else:
            await message.answer(f'✅ {msg}')

    else:
        if latin:
            msg = to_latin(msg)
            matches = []
            for matche in result['matches']:
                matches.append(to_latin(matche))
            response = f'❌ {msg}'
            for matche in matches:
                response += f'\n✅ {matche}'
            await message.answer(response)
        else:
            response = f'❌ {msg}'
            for matche in result['matches']:
                response += f'\n✅ {matche}'
            await message.answer(response)
