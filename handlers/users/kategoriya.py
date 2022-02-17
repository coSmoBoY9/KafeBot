from cgitb import text
from loader import dp
from aiogram import types
from keyboards.default.baliq import baliqlar
from states.kafe import StatesKafe


@dp.message_handler(text="Baliq 🐠", state=StatesKafe.category)
async def get_fish(message: types.Message):
	await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=baliqlar)
	await StatesKafe.next()
