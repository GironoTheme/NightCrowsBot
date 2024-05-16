import telebot


class Telegram:
    """Класс для работы с тг"""
    def __init__(self):
        self.TG_USER_ID = 123
        self.TG_API_KEY = 123
        self.BOT = telebot.TeleBot(self.TG_API_KEY)

    def send_message(self, msg):
        """Функция для отпправки сообщения в тг"""
        self.BOT.send_message(self.TG_USER_ID, msg)
