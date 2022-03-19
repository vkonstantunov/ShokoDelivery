import logging

import keyboard as keyboard
from aiogram import Bot, Dispatcher, executor, types
import botadmin
from handler import kh_handler,shoko_handler,vabi_handler
import sqlite3

bot = Bot(token=botadmin.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



# Стартовое меню
@dp.message_handler(commands="start")
async def shoko_start(message: types.Message):
    try:
        conn = sqlite3.connect('shokobot.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO test VALUES("{message.from_user.id}","{message.from_user.first_name}")')
        conn.commit()
    except Exception as e:
        print(e)
        conn = sqlite3.connect('shokobot.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO test VALUES("{message.from_user.id}")')
        conn.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='☕Шоколадница'),
                 types.KeyboardButton(text='☕Кофе Хауз'),
                 types.KeyboardButton(text='🍱ВабиСаби'))
    await message.answer('Выберите от куда хотите заказать доставку:',reply_markup=keyboard)
    return keyboard




@dp.message_handler(text="☕Шоколадница")
async def menu(message: types.Message):
    photo = open('photo/logo/shokologo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍽Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите нужный вам раздел:', reply_markup=keyboard)
    return keyboard


@dp.message_handler(text="☕Кофе Хауз")
async def menu(message: types.Message):
    photo = open('photo/logo/khlogo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍴Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Данное заведение в разработке')



@dp.message_handler(text="🍱ВабиСаби")
async def menu(message: types.Message):
    photo = open('photo/logo/vabilogo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍣Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(message.chat.id, photo=photo)
    await message.answer('Данное заведение в разработке')



@dp.message_handler(content_types=["text"])
async def menu(message: types.Message):
    if message.text == "🍽Меню":
        keyboard = shoko_handler.shoko_menu()
        await message.answer('Выберите действие:', reply_markup=keyboard)
        return keyboard
    elif message.text == "🍴Меню":
        keyboard = kh_handler.kh_menu()
        await message.answer('Выберите действие:', reply_markup=keyboard)
        return keyboard
    elif message.text == "🍣Меню":
        keyboard = vabi_handler.vabi_menu()
        await message.answer('Выберите действие:', reply_markup=keyboard)
        return keyboard
    elif message.text == "💬Помощь":
        await message.answer("""
Наши контакты:
Почта:blabalbal
Телефон:8-999-99-99
Наш бот:@blablabal""")

@dp.callback_query_handler(text="sandwiches")
async def shoko_sandwiches(call: types.CallbackQuery):
    kb = shoko_handler.shoko_sandwiches()
    await call.message.answer("Какой сэндвич вам по вкусу?", reply_markup=kb)

@dp.callback_query_handler(text="salad")
async def shoko_salad(call: types.CallbackQuery):
    kb = shoko_handler.shoko_salad()
    await call.message.answer("Какой Салат вам по вкусу?", reply_markup=kb)

@dp.callback_query_handler(text="pan")
async def shoko_pan(call: types.CallbackQuery):
    kb = shoko_handler.shoko_pan()
    await call.message.answer("Какие блинчики вы любите?", reply_markup=kb)

@dp.callback_query_handler(text="soup")
async def shoko_soup(call: types.CallbackQuery):
    photo = open('photo/soup/qur.jpg', 'rb')
    photo1 = open('photo/soup/grib.jpg', 'rb')
    photo2 = open('photo/soup/tom.jpg', 'rb')
    photo3 = open('photo/soup/borch.jpg', 'rb')
    kb = shoko_handler.shoko_soup()
    await call.message.answer_photo(photo, """
Куриный суп с лапшой 300гр
Цена: 300р""", reply_markup=kb)
    await call.message.answer_photo(photo1, 'Крем-Суп с шампиньонами',reply_markup=kb)
    await call.message.answer_photo(photo2, 'Том ям с креветками и кальмаром', reply_markup=kb)
    await call.message.answer_photo(photo3, 'Борщ с говядиной', reply_markup=kb)


@dp.callback_query_handler(text="pizza")
async def shoko_pizza(call: types.CallbackQuery):
    kb = shoko_handler.shoko_pizza()
    await call.message.answer("Какой суп вам по вкусу?", reply_markup=kb)



@dp.callback_query_handler(text="hot_bl")
async def shoko_hot_bl(call: types.CallbackQuery):
    kb = shoko_handler.shoko_hot_bl()
    await call.message.answer("Как дома", reply_markup=kb)


@dp.callback_query_handler(text="post")
async def shoko_post(call: types.CallbackQuery):
    kb = shoko_handler.shoko_post()
    await call.message.answer("Для тех кто держит пост", reply_markup=kb)


@dp.callback_query_handler(text="combo")
async def shoko_combo(call: types.CallbackQuery):
    kb = shoko_handler.shoko_combo()
    await call.message.answer("Выгодно", reply_markup=kb)


@dp.callback_query_handler(text="break")
async def shoko_break(call: types.CallbackQuery):
    kb = shoko_handler.shoko_break()
    await call.message.answer("Их можно заказать целый день", reply_markup=kb)


@dp.callback_query_handler(text="desert")
async def shoko_desert(call: types.CallbackQuery):
    kb = shoko_handler.shoko_desert()
    await call.message.answer("Ммм как вкусно", reply_markup=kb)


@dp.callback_query_handler(text="test")
async def shoko_test(call: types.CallbackQuery):
    await call.message.answer("Функция корзины в разработке......")



if __name__ == '__main__':
    executor.start_polling(dp)
