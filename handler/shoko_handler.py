from aiogram import Bot, Dispatcher, executor, types


def shoko_menu():
    keyboard =types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Постное меню",callback_data="post"),
                 types.InlineKeyboardButton(text="Комбо", callback_data="combo"),
               types.InlineKeyboardButton(text="Завтраки весь день",callback_data="break"),
               types.InlineKeyboardButton(text="Блинчики", callback_data="pan"),
               types.InlineKeyboardButton(text="Салаты", callback_data="salad"),
               types.InlineKeyboardButton(text="Супы", callback_data="soup"),
               types.InlineKeyboardButton(text="Пицца от EAZZYPIZZY", callback_data="pizza"),
               types.InlineKeyboardButton(text="Горячие блюда", callback_data="hot_bl"),
               types.InlineKeyboardButton(text="Сэндвич", callback_data="sandwiches"),
               types.InlineKeyboardButton(text="Десерты", callback_data="desert"),
               types.InlineKeyboardButton(text="Детское меню", callback_data="det"),
               types.InlineKeyboardButton(text="От Шоколадницы с ❤", callback_data="shoko"),
               types.InlineKeyboardButton(text="Дополнительно", callback_data="test"))
    return keyboard

def shoko_sandwiches():
    button = [types.InlineKeyboardButton(text="Ролл Цезарь",callback_data="test"),
                 types.InlineKeyboardButton(text="Ролл с ветчиной и яйцом", callback_data="test"),
               types.InlineKeyboardButton(text="Ролл филадельфия",callback_data="test"),
               types.InlineKeyboardButton(text="Ролл с ростбифом", callback_data="test"),
               types.InlineKeyboardButton(text="Брускетта с крем-сыром и лососем", callback_data="test"),
               types.InlineKeyboardButton(text="Битый авокадо на ремесленном хлебе с яйцом пашот", callback_data="test"),
               types.InlineKeyboardButton(text="Брускетта с тунцом, яйцом и свежими овощами", callback_data="test"),
               types.InlineKeyboardButton(text="Брускетта с ростбифом", callback_data="test"),
               types.InlineKeyboardButton(text="Клаб-сэндвич", callback_data="sandwiches"),
               types.InlineKeyboardButton(text="Баварский бургер", callback_data="test"),
               types.InlineKeyboardButton(text="Веганский бургер", callback_data="test"),
               types.InlineKeyboardButton(text="Сэндвич с нежным ростбифом", callback_data="test"),
               types.InlineKeyboardButton(text="Круассан с лососем и голландским соусом", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_salad():
    button = [types.InlineKeyboardButton(text="Оливье с курице", callback_data="test"),
              types.InlineKeyboardButton(text="Греческий", callback_data="test"),
              types.InlineKeyboardButton(text="Теплый салат с фалафелм и хумусом", callback_data="test"),
              types.InlineKeyboardButton(text="Салат  Пять зеленых овощей", callback_data="test"),
              types.InlineKeyboardButton(text="Страчателла с фермерскими томатами", callback_data="test"),
              types.InlineKeyboardButton(text="Битый авокадо на ремесленном хлебе с яйцом пашот", callback_data="test"),
              types.InlineKeyboardButton(text="Поке с тигровыми креветками", callback_data="test"),
              types.InlineKeyboardButton(text="Поке с слабосаленым лососем", callback_data="test"),
              types.InlineKeyboardButton(text="Цезарь с Курицей", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Цезарь с креветками", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_pan():
    button = [types.InlineKeyboardButton(text="Домашние блинчики", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики Легендарные с шоколадом", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики с маком", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики с крем сыром и томленой вишней", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики с сыром и ветчиной", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики со слабосаленым лососем", callback_data="test"),
              types.InlineKeyboardButton(text="Блинчики с мясом", callback_data="test"),
              types.InlineKeyboardButton(text="Стопка домашних блинов", callback_data="test"),
              types.InlineKeyboardButton(text="Большая Стопка домашних блинов", callback_data="test"),
              types.InlineKeyboardButton(text="Большая порция блинчиков со слабосаленым лососем", callback_data="test"),
              types.InlineKeyboardButton(text="Большая порция блинчиков с мясом", callback_data="test"),
              types.InlineKeyboardButton(text="Большая порция блинчиков с маком", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_soup():
    button1 = types.InlineKeyboardButton(text="В корзину", callback_data="test")
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(button1)
    return keyboard


def shoko_pizza():
    button = [types.InlineKeyboardButton(text="Маргарита", callback_data="test"),
              types.InlineKeyboardButton(text="Ветчина грибы", callback_data="test"),
              types.InlineKeyboardButton(text="Пепперони", callback_data="test"),
              types.InlineKeyboardButton(text="Четыре сыра", callback_data="test"),
              types.InlineKeyboardButton(text="Гавайская", callback_data="test"),
              types.InlineKeyboardButton(text="Курица и грибы", callback_data="test"),
              types.InlineKeyboardButton(text="Страчателла", callback_data="test"),
              types.InlineKeyboardButton(text="Дьявол", callback_data="test"),
              types.InlineKeyboardButton(text="Трюфильная", callback_data="test"),
              types.InlineKeyboardButton(text="Римская Маршмеллоу", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_hot_bl():
    button = [types.InlineKeyboardButton(text="Паровые котлеты", callback_data="test"),
              types.InlineKeyboardButton(text="Диетическая куриная грудка", callback_data="test"),
              types.InlineKeyboardButton(text="Сочный бифштекс с яйцом пашот", callback_data="test"),
              types.InlineKeyboardButton(text="Пельмени с говядиной и зеленью", callback_data="test"),
              types.InlineKeyboardButton(text="Альфредо с курицой", callback_data="test"),
              types.InlineKeyboardButton(text="Паста карбонара", callback_data="test"),
              types.InlineKeyboardButton(text="Паста четыре сыра", callback_data="test"),
              types.InlineKeyboardButton(text="Мясная лазанья", callback_data="test"),
              types.InlineKeyboardButton(text="Гарнир Пюре", callback_data="test"),
              types.InlineKeyboardButton(text="Гарнир Спагетти", callback_data="test"),
              types.InlineKeyboardButton(text="Гарнир Гречка", callback_data="test"),
              types.InlineKeyboardButton(text="Гарнир Киноа", callback_data="test"),
              types.InlineKeyboardButton(text="Гарнир Картофель Фри", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_post():
    button = [types.InlineKeyboardButton(text="Каша со злаками", callback_data="test"),
              types.InlineKeyboardButton(text="Ягодный смузи-боул на кокосовой основе ", callback_data="test"),
              types.InlineKeyboardButton(text="Салат с запеченной свеклой и тыквой", callback_data="test"),
              types.InlineKeyboardButton(text="Салат с печеными овощами и тофу", callback_data="test"),
              types.InlineKeyboardButton(text="Битые огурцы", callback_data="test"),
              types.InlineKeyboardButton(text="Щи из квашеной капусты", callback_data="test"),
              types.InlineKeyboardButton(text="Хумус классический с миксом черри и вяленых томатов", callback_data="test"),
              types.InlineKeyboardButton(text="Хумус с баклажаном,миксом черри и вяленых томатов", callback_data="test"),
              types.InlineKeyboardButton(text="Бургер с растительной котлетой", callback_data="test"),
              types.InlineKeyboardButton(text="Вега ролл", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Гречка с жаренными грибами", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Молодой картофель с жаренными грибами", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Картофельные биточки с грибами", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="РАстительный бифштекс", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Зеленая паста с артишоками", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Чечевица с овощами", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Овощи гриль", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Шоколадно вишневый торт", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Смузи 'Груша-Дыня'", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Смузи 'Киви-Шпинат'", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Смузи 'Облепиха'", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Гречишный чай с зеленым яблоком и мятой", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Персиковый латте на соевой основе", callback_data="sandwiches"),
              types.InlineKeyboardButton(text="Банановый раф с клубникой", callback_data="sandwiches")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_combo():
    button = [types.InlineKeyboardButton(text="Комбо с Баварским бургером", callback_data="test"),
              types.InlineKeyboardButton(text="Комбо с пастой Карбонара", callback_data="test"),
              types.InlineKeyboardButton(text="Комбо с пастой Альфредо", callback_data="test"),
              types.InlineKeyboardButton(text="Комбо с клаб-сэндвичем", callback_data="test"),
              types.InlineKeyboardButton(text="ЗОЖ завтрак", callback_data="test"),
              types.InlineKeyboardButton(text="Комбо обед сытный", callback_data="test"),
              types.InlineKeyboardButton(text="Комбо обед лайт", callback_data="test"),
              types.InlineKeyboardButton(text="Мясная лазанья", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_break():
    button = [types.InlineKeyboardButton(text="Овсяная каша", callback_data="test"),
              types.InlineKeyboardButton(text="Рисовая гречневая на молоке", callback_data="test"),
              types.InlineKeyboardButton(text="Смузи-боул с черникой", callback_data="test"),
              types.InlineKeyboardButton(text="Омлет с сыром и томатами", callback_data="test"),
              types.InlineKeyboardButton(text="Омлет с сыром и ветчиной из птицы и бекона", callback_data="test"),
              types.InlineKeyboardButton(text="Фирменные сырники", callback_data="test"),
              types.InlineKeyboardButton(text="Кокосовые сырники", callback_data="test"),
              types.InlineKeyboardButton(text="Страчателла с томленой вишней", callback_data="test"),
              types.InlineKeyboardButton(text="Сосиски с зеленым горошком", callback_data="test"),
              types.InlineKeyboardButton(text="Шакшука", callback_data="test"),
              types.InlineKeyboardButton(text="Кетозавтрак", callback_data="test"),
              types.InlineKeyboardButton(text="Хашбраун со слабосаленым лососем", callback_data="test"),
              types.InlineKeyboardButton(text="Хашбраун с говяжими колбасками", callback_data="test"),
              types.InlineKeyboardButton(text="Английский завтрак", callback_data="test"),
              types.InlineKeyboardButton(text="Римский бутерброд с яйцом", callback_data="test"),
              types.InlineKeyboardButton(text="Французский завтрак", callback_data="test"),
              types.InlineKeyboardButton(text="Лосось с яйцом пашот и лососем на кунжутной лепешки", callback_data="test"),
              types.InlineKeyboardButton(text="Яйцо бенедикт", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_desert():
    button = [types.InlineKeyboardButton(text="Набор пирожных классика", callback_data="test"),
              types.InlineKeyboardButton(text="Набор пирожных яркий", callback_data="test"),
              types.InlineKeyboardButton(text="Набор рулетов", callback_data="test"),
              types.InlineKeyboardButton(text="Эклер шоколадный", callback_data="test"),
              types.InlineKeyboardButton(text="Брауни", callback_data="test"),
              types.InlineKeyboardButton(text="Штрудель", callback_data="test"),
              types.InlineKeyboardButton(text="Напалеон", callback_data="test"),
              types.InlineKeyboardButton(text="Медовик", callback_data="test"),
              types.InlineKeyboardButton(text="Торт 'Москва'", callback_data="test"),
              types.InlineKeyboardButton(text="Тирамису", callback_data="test"),
              types.InlineKeyboardButton(text="Опера", callback_data="test"),
              types.InlineKeyboardButton(text="Морковный торт", callback_data="test"),
              types.InlineKeyboardButton(text="Красный бархат", callback_data="test"),
              types.InlineKeyboardButton(text="Чизкейк Нью-Йорк", callback_data="test"),
              types.InlineKeyboardButton(text="Десерт Сердце", callback_data="test"),
              types.InlineKeyboardButton(text="ЛЕмонная меренга", callback_data="test"),
              types.InlineKeyboardButton(text="Меренговый рулет с матчей", callback_data="test"),
              types.InlineKeyboardButton(text="Фисташковый рулет с малиной", callback_data="test"),
              types.InlineKeyboardButton(text="Шоколадный Сан-Себастьян", callback_data="test"),
              types.InlineKeyboardButton(text="Мангвый мусс", callback_data="test"),
              types.InlineKeyboardButton(text="Тарталетка с клбуникой", callback_data="test"),
              types.InlineKeyboardButton(text="Тарталетка с голубикой", callback_data="test"),
              types.InlineKeyboardButton(text="Круассан классический", callback_data="test"),
              types.InlineKeyboardButton(text="Круассан миндальный ", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard


def shoko_det():
    button = [types.InlineKeyboardButton(text="dfsdfsdf", callback_data="test"),
              types.InlineKeyboardButton(text="Набор пирожных яркий", callback_data="test"),
              types.InlineKeyboardButton(text="Набор рулетов", callback_data="test"),
              types.InlineKeyboardButton(text="Эклер шоколадный", callback_data="test"),
              types.InlineKeyboardButton(text="Брауни", callback_data="test"),
              types.InlineKeyboardButton(text="Штрудель", callback_data="test"),
              types.InlineKeyboardButton(text="Напалеон", callback_data="test"),
              types.InlineKeyboardButton(text="Медовик", callback_data="test"),
              types.InlineKeyboardButton(text="Торт 'Москва'", callback_data="test"),
              types.InlineKeyboardButton(text="Тирамису", callback_data="test"),
              types.InlineKeyboardButton(text="Опера", callback_data="test"),
              types.InlineKeyboardButton(text="Морковный торт", callback_data="test"),
              types.InlineKeyboardButton(text="Красный бархат", callback_data="test"),
              types.InlineKeyboardButton(text="Чизкейк Нью-Йорк", callback_data="test"),
              types.InlineKeyboardButton(text="Десерт Сердце", callback_data="test"),
              types.InlineKeyboardButton(text="ЛЕмонная меренга", callback_data="test"),
              types.InlineKeyboardButton(text="Меренговый рулет с матчей", callback_data="test"),
              types.InlineKeyboardButton(text="Фисташковый рулет с малиной", callback_data="test"),
              types.InlineKeyboardButton(text="Шоколадный Сан-Себастьян", callback_data="test"),
              types.InlineKeyboardButton(text="Мангвый мусс", callback_data="test"),
              types.InlineKeyboardButton(text="Тарталетка с клбуникой", callback_data="test"),
              types.InlineKeyboardButton(text="Тарталетка с голубикой", callback_data="test"),
              types.InlineKeyboardButton(text="Круассан классический", callback_data="test"),
              types.InlineKeyboardButton(text="Круассан миндальный ", callback_data="test")]

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*button)
    return keyboard
