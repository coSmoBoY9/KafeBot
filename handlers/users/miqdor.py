from loader import dp
from aiogram import types
from keyboards.default.amount import miqdorlar
from states.kafe import StatesKafe


@dp.message_handler(text="Sazan (300g)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/dD5k1PQ", caption = "Sazan (300g)\n\nNarxi: 45000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()