from os import stat
from loader import dp
from aiogram import types
from states.kafe import StatesKafe
from keyboards.default.asosiy import menu
from keyboards.default.category import cats
from keyboards.default.baliq import baliqlar
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.category)
async def back_cat(message: types.Message, state: FSMContext):
	await message.answer("Sahifani tanlang 😊", reply_markup=menu)
	await state.finish()


@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.product)
async def back_prod(message: types.Message):
	await message.answer("Taomlarga o'tish uchun sahifani tanlang...", reply_markup=cats)
	await StatesKafe.category.set()


@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.amount)
async def back_amount(message: types.Message):
	await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=baliqlar)
	await StatesKafe.product.set()


@dp.message_handler(text="Bosh Sahifa 🏠", state=StatesKafe.amount)
async def back_amount(message: types.Message, state: FSMContext):
	await message.answer("Buyurtma berishni boshlaymizmi?", reply_markup=menu)
	await state.finish()