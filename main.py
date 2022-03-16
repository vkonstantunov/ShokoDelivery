import logging
from aiogram import Bot, Dispatcher, executor, types

import botadmin
import kb

bot = Bot(token=botadmin.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Стартовое меню
@dp.message_handler(commands="start")
async def shoko_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='Меню'),
                 types.KeyboardButton(text='Помощь'),
                 types.KeyboardButton(text='Корзина'))
    await message.answer("Выберите действие:", reply_markup=keyboard)

    return keyboard


@dp.message_handler(text="Главное меню")
async def shoko_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text='Меню'),
                 types.KeyboardButton(text='Помощь'),
                 types.KeyboardButton(text='Корзина'))
    await message.answer("Выберите действие:", reply_markup=keyboard)

    return keyboard


@dp.message_handler(text="Меню")
async def shoko_menu(message: types.Message):
    keyboard = kb.shoko_m()
    keyboard1 = kb.shoko_s()

    await message.answer("Выберите действие:", reply_markup=keyboard)
    await message.answer("Выберите действие:", reply_markup=keyboard1)


@dp.message_handler(text="Корзина")
async def shoko_basket(message: types.Message):
    keyboard1 = kb.shoko_s()
    await message.answer("Выберите действие:", reply_markup=keyboard1)


@dp.message_handler(text="Помощь")
async def shoko_help(message: types.Message):
    keyboard = kb.shoko_h()
    await message.answer("Выберите действие:", reply_markup=keyboard)


@dp.message_handler(text="Наши контакты")
async def shoko_help(message: types.Message):
    await message.answer("Наша почта: help@shoko.ru")
    await message.answer("Наша телефон: 8-999-99-99-99")
    await message.answer("Наш бот для обратной связи:@shoko_delevery_bot")


# Обработка напитков
@dp.callback_query_handler(text="drinks")
async def shoko_drinks(call: types.CallbackQuery):
    keyboard = kb.shoko_dr()
    await call.message.answer("Какие напитки интересуют?", reply_markup=keyboard)
    await call.answer()


# Обработка супов
@dp.callback_query_handler(text="soup")
async def shoko_soup(call: types.CallbackQuery):
    keyboard = kb.shoko_sp()
    await call.message.answer("Какой суп интересует?", reply_markup=keyboard)
    await call.answer()


# Обработка горячих напитков
@dp.callback_query_handler(text="hot_drinks")
async def shoko_drinks_hot(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_hot()
    await call.message.answer("Какие напитки интересуют?", reply_markup=keyboard)
    await call.answer()


# Кофе
@dp.callback_query_handler(text="coffee")
async def shoko_drinks_coffee(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_hot_coffee()
    await call.message.answer("Какой кофе интресует?", reply_markup=keyboard)
    await call.answer()


# Чай
@dp.callback_query_handler(text="tea")
async def shoko_drinks_coffee(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_hot_tea()
    await call.message.answer("Какой чай интересует?", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="cold_drinks")
async def shoko_drinks_tea(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_cold()
    await call.message.answer("Какие напитки интересуют?", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="juice")
async def shoko_drinks_juice(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_cold_juice()
    await call.message.answer("Какой сок интересует?", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="lemonade")
async def shoko_drinks_lemonade(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_cold_lemonade()
    await call.message.answer("Какой лимонад интересует?", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="smoothie")
async def shoko_drinks_smoothie(call: types.CallbackQuery):
    keyboard = kb.shoko_dr_cold_smoothie()
    await call.message.answer("Какое смузи интересует?", reply_markup=keyboard)
    await call.answer()

#Научился бро обновлять гит)

if __name__ == '__main__':
    executor.start_polling(dp)
