from keyboards.default.baliq import baliqlar
from loader import dp
from aiogram import types
from states.kafe import StatesKafe
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=StatesKafe.amount)
async def order(message: types.Message, state: FSMContext):
	amount = message.text
	await state.update_data({
		'amount': amount
	})
	await message.answer("Savatchaga🛒 qo'shildi")
	await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=baliqlar)
	await StatesKafe.product.set()
