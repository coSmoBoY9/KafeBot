from loader import dp
from aiogram import types
from keyboards.default.category import cats
from states.kafe import StatesKafe


@dp.message_handler(text="Menu 🍲🍢")
async def get_menu(message: types.Message):
	await message.answer("Xo'sh, buyurtmaga o'tamizmi, sizni issiq taomlarimiz kutmoqda 👨🏻‍🍳🔥", reply_markup=cats)
	await StatesKafe.category.set()