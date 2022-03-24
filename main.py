import asyncio
import logging
import psycopg2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from handler import kh_handler, shoko_handler, vabi_handler
from config import *
from funcc import rename, db
import buttons


bot = Bot(token=config.TOKEN)
# Диспетчер для бота
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# подключение к бд
conn = psycopg2.connect(host=host,
            user=user,
            password=password,
            database=db_name)
cursor = conn.cursor()
conn.autocommit = True


# Стартовое меню
@dp.message_handler(commands="start")
async def shoko_start(message: types.Message):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(f"""
             INSERT INTO bot_users (user_id,user_name) VALUES ({message.from_user.id},'{message.from_user.first_name}');"""
                           )
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT user_name FROM bot_users WHERE user_id = '{message.from_user.id}';""")
            name = cursor.fetchone()
            name= rename(name)
    except Exception as _ex:
        print(_ex)
    finally:
        if connection:
            connection.close()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='☕Шоколадница'),
                 types.KeyboardButton(text='☕Кофе Хауз'),
                 types.KeyboardButton(text='🍱ВабиСаби'))
    await message.answer(f'{name} выберите от куда хотите заказать доставку:',reply_markup=keyboard)
    return keyboard


@dp.message_handler(text="☕Шоколадница")
async def menu(message: types.Message):
    id = message.from_user.first_name
    name = db(id)
    photo = open('photo/logo/shokologo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍽Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(f'{name} Выберите нужный вам раздел:', reply_markup=keyboard)
    return keyboard


@dp.message_handler(text="☕Кофе Хауз")
async def menu(message: types.Message):
    id = message.from_user.first_name
    name = db(id)
    photo = open('photo/logo/khlogo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍴Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(f'{name} Выберите нужный вам раздел:', reply_markup=keyboard)


@dp.message_handler(text="🍱ВабиСаби")
async def menu(message: types.Message):
    id = message.from_user.first_name
    name = db(id)
    photo = open('photo/logo/vabilogo.jpg', 'rb')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='🍣Меню'),
                types.KeyboardButton(text='Корзина'),
                types.KeyboardButton(text='💬Помощь'))
    await bot.send_photo(message.chat.id, photo=photo)
    await message.answer(f'{name} Выберите нужный вам раздел:', reply_markup=keyboard)


@dp.message_handler(content_types=["text"])
async def menu(message: types.Message):
    id = message.from_user.first_name
    name = db(id)
    if message.text == "🍽Меню":
        cursor.execute('''SELECT * FROM menu_shoko''')
        data = cursor.fetchall()
        await message.answer(f'{name} Выберите нужный раздел меню:', reply_markup=buttons.genmarkup(data))
    elif message.text == "🍴Меню":
        cursor.execute('''SELECT * FROM menu_kh''')
        data = cursor.fetchall()
        await message.answer(f'{name} Выберите нужный раздел меню:', reply_markup=buttons.genmarkup(data))
    elif message.text == "🍣Меню":
        cursor.execute('''SELECT * FROM menu_vabi''')
        data = cursor.fetchall()
        await message.answer(f'{name} Выберите нужный раздел меню:', reply_markup=buttons.genmarkup(data))
    elif message.text == "💬Помощь":
        await message.answer(f"""
{name} Наши контакты:
Почта:blabalbal
Телефон:8-999-99-99
Наш бот:@blablabal""")

def image(a,b):
    photo = open(a,b)
    return photo

@dp.callback_query_handler(text="shoko_soup")
async def shoko_soup(call: types.CallbackQuery):
    await call.message.answer('Какой суп выберете:')
    cursor.execute('''SELECT name FROM shoko_soup''')
    name = cursor.fetchall()
    tom = name[0]
    tom = rename(tom)
    borch  = name[1]
    borch = rename(borch)
    cream = name[2]
    cream = rename(cream)
    cur = name[3]
    cur = rename(cur)
    cur1 = name[4]
    cur1 = rename(cur1)
    cursor.execute('''SELECT price FROM shoko_soup''')
    price = cursor.fetchall()
    #cursor.execute('''SELECT * FROM shoko_soup''')
    data = "Добавить в корзину"
    photo_tom = image("photo/soup/tom.jpg", 'rb')
    photo_borch = open("photo/soup/borch.jpg", 'rb')
    photo_cream = open("photo/soup/grib.jpg", 'rb')
    photo_cur = open("photo/soup/qur2.jpg", 'rb')
    photo_cur1 = open("photo/soup/qur.jpg", 'rb')
    kb = shoko_handler.shoko_basket()
    await call.message.answer_photo(photo_tom, f'{tom}', reply_markup=kb)
    await call.message.answer_photo(photo_borch, f'{borch}', reply_markup=kb)
    await call.message.answer_photo(photo_cream, f'{cream}', reply_markup=kb)
    await call.message.answer_photo(photo_cur, f'{cur}', reply_markup=kb)
    await call.message.answer_photo(photo_cur1, f'{cur1}', reply_markup=kb)
    await call.answer('Какой суп выберете:')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
