from aiogram import Bot, Dispatcher, executor, types







def kh_menu():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Постное меню", callback_data="test"),
                 types.InlineKeyboardButton(text="Комбо", callback_data="test"),
                 types.InlineKeyboardButton(text="Завтраки весь день", callback_data="test"),
                 types.InlineKeyboardButton(text="Блинчики", callback_data="test"),
                 types.InlineKeyboardButton(text="Салаты", callback_data="test"),
                 types.InlineKeyboardButton(text="Супы", callback_data="test"),
                 types.InlineKeyboardButton(text="Пицца", callback_data="test"),
                 types.InlineKeyboardButton(text="Горячие блюда", callback_data="test"),
                 types.InlineKeyboardButton(text="Сэндвич", callback_data="test"),
                 types.InlineKeyboardButton(text="Десерты", callback_data="test"),
                 types.InlineKeyboardButton(text="Детское меню", callback_data="test"),
                 types.InlineKeyboardButton(text="Дополнительно", callback_data="test"))
    return keyboard

