from aiogram import types


def shoko_m():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Постное меню', callback_data='lean_menu'),
        types.InlineKeyboardButton(text='Комбо', callback_data='combo'),
        types.InlineKeyboardButton(text='Завтрак', callback_data='breakfast'),
        types.InlineKeyboardButton(text='Салаты', callback_data='salad'),
        types.InlineKeyboardButton(text='Супы', callback_data='soup'),
        types.InlineKeyboardButton(text='Горячие', callback_data='hot'),
        types.InlineKeyboardButton(text='Сэндвичи', callback_data='sandwich'),
        types.InlineKeyboardButton(text='Детское', callback_data='childrens_menu'),
        types.InlineKeyboardButton(text='Десерты', callback_data='desserts'),
        types.InlineKeyboardButton(text='Тест', callback_data='test'),
        types.InlineKeyboardButton(text='Напитки', callback_data='drinks'),
    )
    return keyboard


def shoko_s():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='Главное меню'),
                 types.KeyboardButton(text='Помощь‍'),
                 types.KeyboardButton(text='Корзина'))
    return keyboard


def shoko_h():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='Наши контакты'),
                 types.KeyboardButton(text='Обратная связь'),
                 types.KeyboardButton(text='Главное меню'))
    return keyboard


def shoko_dr():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Горячие напитки', callback_data='hot_drinks'),
        types.InlineKeyboardButton(text='Холодные напитки', callback_data='cold_drinks'))
    return keyboard


#Горячие напитки
def shoko_dr_hot():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Кофе', callback_data='coffee'),
        types.InlineKeyboardButton(text='Чай', callback_data='tea'))
    return keyboard


#Кофе
def shoko_dr_hot_coffee():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Капучино Мега 300мл', callback_data='cappuccino300'),
        types.InlineKeyboardButton(text='Капучино Мега 500мл', callback_data='cappuccino500'),
        types.InlineKeyboardButton(text='Американо Мега 300мл', callback_data='americano300'),
        types.InlineKeyboardButton(text='Американо Мега 500мл', callback_data='americano500'),
        types.InlineKeyboardButton(text='Латте', callback_data='latte'))
    return keyboard


#Чай
def shoko_dr_hot_tea():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Черный чай 500мл', callback_data='black_tea'),
        types.InlineKeyboardButton(text='Зеленой чай 500мл', callback_data='green_tea'),
        types.InlineKeyboardButton(text='Облепиховый 500мл', callback_data='americano300'),
        types.InlineKeyboardButton(text='Фруктовый 500мл', callback_data='sea_buckthorn_tea'),
        types.InlineKeyboardButton(text='Чай Матча 300мл', callback_data='matcha_tea'))
    return keyboard


#Холодные напитки
def shoko_dr_cold():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Свежевыжатые соки', callback_data='juice'),
        types.InlineKeyboardButton(text='Лимонады', callback_data='lemonade'),
        types.InlineKeyboardButton(text='Смузи', callback_data='smoothie'))
    return keyboard


def shoko_dr_cold_juice():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Яблочный', callback_data='apple_juice'),
        types.InlineKeyboardButton(text='Апельсиновый', callback_data='orange_juice'),
        types.InlineKeyboardButton(text='Морковный', callback_data='carrot_juice'))
    return keyboard


def shoko_dr_cold_lemonade():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Домашний лимонад', callback_data='homemade_lemonade'),
        types.InlineKeyboardButton(text='Мохито', callback_data='mojito'),
        types.InlineKeyboardButton(text='Морс', callback_data='morse'))
    return keyboard


def shoko_dr_cold_smoothie():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Смузи манго чиа', callback_data='mango_smoothie'),
        types.InlineKeyboardButton(text='Смузи клубника мята', callback_data='strawberry_smoothie'),
        types.InlineKeyboardButton(text='Ласси', callback_data='lassi_smoothie'))
    return keyboard


def shoko_sp():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text='Борщ', callback_data='borsch_soup'),
        types.InlineKeyboardButton(text='Крем-суп', callback_data='cream_soup'),
        types.InlineKeyboardButton(text='Куриный суп', callback_data='chicken_soup'),
        types.InlineKeyboardButton(text='Том ям', callback_data='tom_yam_soup'))
    return keyboard



