from aiogram.dispatcher.filters.state import State, StatesGroup


class StatesKafe(StatesGroup):
	category = State()
	product = State()
	amount = State()