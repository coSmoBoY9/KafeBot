from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

baliqlar = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Sazan (300g)"), KeyboardButton(text="Sudak (300g)")],
		[KeyboardButton(text="Sous 300ml"), KeyboardButton(text="ORQAGA ↩️")]
	],
	resize_keyboard=True
)