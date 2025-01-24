import telebot
from telebot import types
import sqlite3
import os

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
DATABASE_PATH = os.environ.get('DATABASE_PATH', "reminders.db")

telebot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
connect_db = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
cur = connect_db.cursor()
# # cur.execute(
# #     '''
# #     INSERT INTO reminder (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         text TEXT
# #     )
# #     '''
# # )
# connect_db.commit()


@telebot.message_handler(commands=['start'])
def start(message):
    container = types.InlineKeyboardMarkup(row_width=1)
    menu_button_1 = types.InlineKeyboardButton(
        'Задать напоминание',
        callback_data='set_a_reminder'
        )
    menu_button_2 = types.InlineKeyboardButton(
        'Посмотреть напоминания',
        callback_data='view_reminders'
    )
    container.add(menu_button_1, menu_button_2)
    telebot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name}, я бот напоминалка,'
        f' вот что я умею: ', reply_markup=container
    )


@telebot.callback_query_handler(func=lambda x: x.data)
def menu_button_1(callback_data):
    if callback_data.data == 'set_a_reminder':
        telebot.send_message(
            callback_data.message.chat.id, "Введите текст напоминания:"
        )
        telebot.register_next_step_handler(
            callback_data.message, save_reminder
        )
    elif callback_data.data == 'view_reminders':
        view_reminders(callback_data.message)


def save_reminder(message):
    try:
        reminder_text = message.text
        cur.execute(
                "INSERT INTO reminder (text) VALUES (?)",
                (reminder_text,)
        )
        connect_db.commit()
        telebot.send_message(message.chat.id, "Напоминание сохранено!")
    except sqlite3.Error as e:
        telebot.send_message(message.chat.id, f"Ошибка базы данных: {e}")
    except Exception as e:
        telebot.send_message(message.chat.id, f"Ошибка: {e}")


def view_reminders(message):
    try:
        cur.execute("SELECT text FROM reminder")
        reminders = cur.fetchall()
        if reminders:
            reminder_text = "\n".join([r[0] for r in reminders])
            telebot.send_message(message.chat.id,
                                 f"Ваши напоминания:\n{reminder_text}")
        else:
            telebot.send_message(
                message.chat.id, "У вас пока нет напоминаний."
            )
    except Exception as e:
        telebot.send_message(message.chat.id, f"Ошибка: {e}")


telebot.polling(non_stop=True, timeout=123)
connect_db.close()
