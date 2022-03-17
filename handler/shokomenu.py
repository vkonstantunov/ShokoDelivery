from aiogram import types
from handler import shoko_handler



class SHOKOMENU():

    @dp.callback_query_handler(text="sandwiches")
    async def shoko_sandwiches(call: types.CallbackQuery):
        kb = shoko_handler.shoko_sandwiches()
        await call.message.answer("Кокой сэндвич вам по вкусу?", reply_markup=kb)

    @dp.callback_query_handler(text="salad")
    async def shoko_salad(call: types.CallbackQuery):
        kb = shoko_handler.shoko_salad()
        await call.message.answer("Какой Салат вам по вкусу?", reply_markup=kb)

    @dp.callback_query_handler(text="pan")
    async def shoko_pan(call: types.CallbackQuery):
        kb = shoko_handler.shoko_pan()
        await call.message.answer("Какой Салат вам по вкусу?", reply_markup=kb)

    @dp.callback_query_handler(text="test")
    async def shoko_test(call: types.CallbackQuery):
        await call.message.answer("Функция корзины корзины в разработке......")
