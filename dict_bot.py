# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5971673107:AAETMPOOcOdqmTW_DePUds44lNz_1Xhi-dc', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Проверить, что новый функционал не сломал существующий',
    'тикет': 'Определенная задача или багрепорт в сервисе Стартрек',
    'янг': 'Сервис по сбору оценок',
    'кейс': 'Набор шагов, которые нужно выполнить (обычно в кейсе от 1 до 10 шагов).',
    'попап': 'Всплывающее окно.',
    'редирект': 'Перенаправление пользователя на другой адрес.',
    'саджест': 'Выпадающее меню с вариантами значения для выбора.',
    'свайп': 'Специальный жест, движение пальцем по экрану девайса для пролистывания контента, вытягивания шторки и т.п.',
    'скролл': 'Жест, движение сверху вниз для пролистывания списков. Также "скроллить карту" - перемещать карту в произвольном направлении.',
    'тайтл': 'Заголовок чего-либо.',
    'тапахед': '(Десктоп) подсказка в виде слова, которое вы предположительно вводите/хотите ввести.',
'тап': 'Клик пальцем по экрану/кнопке/строке и т.д.',
'тултип': 'Всплывающее окно с названием.',
'ховер': 'Разного рода эффекты (всплывающие подписи, подсказки, плавные переходы, трансформация, ротация, увеличение, смещение и пр.), которые наблюдаются при наведении на них курсора мыши.',
'серп': 'Морда яндекса, страница с результатами поиска.',
'двухфакторная аутентификация': 'Механизм авторизации в Я.Почте с одноразовым паролем.',
'слайдер': 'Превью картинок и видеофайлов с кнопками.',
'сайдбар': 'В Яндекс Диске меню в правой части экрана, при выделении файла в нем доступны функциональные кнопки.',
'днд': 'Метод перемещения файлов путем перетаскивания.',
'статус-бар': 'маленькая информативная панель в верхней части дисплея смартфона, где можно узнать время, заряд аккумулятора и т.д.',
'старт визард': 'Экран, который отображается у запущенного приложения в первый раз после добавления аккаунта.',
'тост': 'Маленькое окошко внизу (на Android) или вверху (на IOS) экрана с краткой информацией для пользователя, появляющееся на несколько секунд.',
'фаб': 'Плавающая кнопка, т.е. с эффектом нависания над остальной частью экрана в моб.почте, в моб.диске.',
'снэк бар': 'Узкая панель, появляющаяся на несколько секунд внизу экрана, с краткой информацией для пользователя.',
'folder list': 'В моб.почте состоит из трех секций: свитчера (переключателя) аккаунтов, списка папок и меток, настройки.',
'топбар': 'Панель вверху экрана приложения на которой находятся функциональные кнопки и название текущего окна приложения.',
'compose': 'Экран написания письма в Яндекс.Почте.',
'ptr': 'Потянуть экран вниз для рефреша страницы.',
'аккаунт менеджер': 'Экран для регистрации/авторизации в приложении.',
'инбокс': 'Папка "Входящие" в почте.',
'корп': 'Корпоративная почта.',
'пдд': 'Почта для доменов.',
'тумблер': 'Переключатель.','
}


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я расшифрую тебе термины асессоров ЯНГа 🤓\nВведи интересующий термин, например, ховер', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
