import time
import keyboard as kb


class Keyboard:
    """Класс для работы с клавиатурой"""

    def __init__(self):
        self.TYPE_INTERVAL = 0.1

    def hold_down_button(self, button, clamping_time):
        """Функция для зажатия клавиши"""
        kb.press(button)
        time.sleep(clamping_time)
        kb.release(button)

    def press_button(self, button):
        """Фуцнкия для нажатия клавиши\n
        button - клавиша
        """
        kb.press(button)

    def esc(self):
        """Функция для нажатия клавиши esc"""
        kb.press('esc')

    def type(self, text):
        """Функция для того чтобы напечатать текст"""
        kb.write(str(text))


keyboard = Keyboard()

