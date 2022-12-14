# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'баг': 'некорректная работа программы, вызванная ошибкой в программном коде или дизайне продукта',
    'регресс': 'Проверка на наличие багов, вызванных изменениями в приложении. \nПроверить, что новый функционал не сломал существующий',
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
'тумблер': 'Переключатель.',
    'пальма': 'Система управления тестовой документацией и тестированием',
    'мок': 'Объекты, которые заменяют реальный объект в условиях теста. Объект-заглушка, реализующий заданный аспект моделируемого ПО',
    'репозиторий': 'Это хранилище кода и истории его изменений',
    'git': 'Это консольная утилита, для отслеживания и ведения истории изменения файлов, в проекте, система управления версиями кода',
    'черный ящик': 'Тестировщику не известно как устроена тестируемая система',
    'белый ящик': 'Тестировщику известны все детали реализации тестируемой системы',
    'серый ящик': 'Тестировщику известно только некоторые особенности устройства тестируемой системы',
    'спецификация': 'Детальное описание того, как должно работать ПО.',
    'баг репорт': 'Документ, описывающий ситуацию или последовательность действий приведшую к некорректной работе объекта тестирования, с указанием причин и ожидаемого результата',
    'валидация': 'Определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, требованиям к системе',
    'верификация': 'Процесс оценки системы или её компонентов с целью определения удовлетворяют ли результаты текущего этапа разработки условиям, сформированным в начале этого этапа',
    'тестирование': 'Процесс проверки соответствия заявленных к продукту требований и реально реализованной функциональности, осуществляемый путем наблюдения за его работой в искусственно созданных ситуациях и на ограниченном наборе тестов, выбранных определенным образом',
    'qa': 'Совокупность мероприятий, охватывающих все технологические этапы разработки, выпуска и эксплуатации программного обеспечения',
    'ошибка': 'Действие, которое порождает неправильный результат',
    'cбой': 'Несоответствие фактического результата работы компонента или системы ожидаемому результату',
    'ux': 'Ощущение, испытываемое пользователем во время использования цифрового продукта',
    'ui': 'Это инструмент, позволяющий осуществлять взаимодействие «пользователь — приложение»',
    'тест-дизайн': 'Это этап процесса тестирования ПО, на котором проектируются и создаются тестовые случаи (тест кейсы)',
    'тест-план': 'Это документ, описывающий весь объем работ по тестированию, а также оценки рисков с вариантами их разрешения',
    'чек-лист': 'Это документ, описывающий что должно быть протестировано',
    'тест-кейс': 'Это артефакт, описывающий совокупность шагов, конкретных условий и параметров, необходимых для проверки реализации тестируемой функции или её части',
    'приоритет багов': 'Важность той или иной ошибки в ПО,: \nTrivial — косметическая малозаметная проблема.\nMinor — очевидная, незначительная проблема.\nMajor — значительная проблема.\nCritical — проблема, нарушающая работу c ключевыми функциями ПО.\nBlocker — проблема, нарушающая функционирование ПО.',
}


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я расшифрую тебе термины асессоров ЯНГа 🤓\nВведи интересующий термин, например, приоритет багов', # текст сообщения
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
