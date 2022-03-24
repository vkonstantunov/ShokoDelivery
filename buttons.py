from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_users = KeyboardButton('Пользователи')
menu = KeyboardButton('Меню')
basket = KeyboardButton('Добавить в корзину')
replykb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(menu)
replykb1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(basket)




def genmarkup(data): # передаём в функцию data

    markup = InlineKeyboardMarkup() # создаём клавиатуру
    markup.row_width = 1 # кол-во кнопок в строке
    for i in data: # цикл для создания кнопок
        markup.add(InlineKeyboardButton(i[1], callback_data=i[2]))
    return markup #возвращаем клавиатуру


def basket(data):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    for i in data:  # цикл для создания кнопок
        markup.add(InlineKeyboardButton(i[1], callback_data=i[2]))
    return markup  # возвращаем клавиатуру
