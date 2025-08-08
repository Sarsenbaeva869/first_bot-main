from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок
button_profile = KeyboardButton(text="Profile")
button_2 = KeyboardButton(text="Help")
button_3 = KeyboardButton(text="")

# Создание клавиатуры с одной кнопкой в ряду
keyboard_single_row = ReplyKeyboardMarkup(
keyboard=[[button_profile], [button_2], [button_3]],
    resize_keyboard=True, # Изменяет размер клавиатуры под контент
    #one_time_keyboard=True, # Скрывает клавиатуру после использования
    #input_field_placeholder="Выберите действие..." # Подсказка в поле ввода


)


#Создание клавиатуры с несколькими кнопками в ряду
#keyboard_multi_row = ReplyKeyboardMarkup(
##keyboard=[[button_1, button_2], [button_3]],
#resize_keyboard=True
