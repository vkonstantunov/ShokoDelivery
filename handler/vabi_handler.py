from aiogram import Bot, Dispatcher, executor, types







def vabi_menu():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Smart Закуски", callback_data="test"),
                 types.InlineKeyboardButton(text="Green Меню", callback_data="test"),
                 types.InlineKeyboardButton(text="Основные блюда", callback_data="test"),
                 types.InlineKeyboardButton(text="Пицца", callback_data="test"),
                 types.InlineKeyboardButton(text="Комбо ужин", callback_data="test"),
                 types.InlineKeyboardButton(text="Роллы", callback_data="test"),
                 types.InlineKeyboardButton(text="Суши", callback_data="test"),
                 types.InlineKeyboardButton(text="Теплые роллы", callback_data="test"),
                 types.InlineKeyboardButton(text="Сеты", callback_data="test"),
                 types.InlineKeyboardButton(text="Супы", callback_data="test"),
                 types.InlineKeyboardButton(text="Салаты", callback_data="test"),
                 types.InlineKeyboardButton(text="Закуски поке", callback_data="test"),
                 types.InlineKeyboardButton(text="Лапша и Рис", callback_data="test"),
                 types.InlineKeyboardButton(text="Вегетарианские блюда", callback_data="test"),
                 types.InlineKeyboardButton(text="Гарниры", callback_data="test"),
                 types.InlineKeyboardButton(text="Десерты", callback_data="test"),
                 types.InlineKeyboardButton(text="Напитки", callback_data="test"),
                 types.InlineKeyboardButton(text="Дополнительно", callback_data="test"))
    return keyboard
