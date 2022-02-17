from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cats = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Baliq 🐠"), KeyboardButton(text="Ichimliklar 🥤")],
		[KeyboardButton(text="Ikkinchi ovqatlar 🍛"), KeyboardButton(text="ORQAGA ↩️")]
	],
	resize_keyboard=True
)