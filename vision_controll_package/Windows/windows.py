import win32gui
import win32com.client
import win32con
from ..shared_variables import name_of_window


class Windows:
    """Класс для работы с окнами"""

    def __init__(self):
        self.NAME_OF_WINDOW = name_of_window

    def switch_windows(self, func):
        """Функция для переключения окон\n
        func - функция которую нужно выполнять после переключения окна
        """
        shell = win32com.client.Dispatch("WScript.Shell")

        windows_list = self.__find_windows()

        if len(windows_list) > 0:
            for window in windows_list:
                for i in range(3):
                    shell.SendKeys('%')
                win32gui.ShowWindow(window, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(window)

                func(window)

    def __find_windows(self):
        def __is_toplevel(hwnd):
            return win32gui.GetParent(hwnd) == 0 and win32gui.IsWindowVisible(hwnd)

        hwnd_list = []

        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd) if __is_toplevel(hwnd) else None, hwnd_list)

        lst_processes = [hwnd for hwnd in hwnd_list if self.NAME_OF_WINDOW in win32gui.GetWindowText(hwnd)]

        if lst_processes:
            return lst_processes
        else:
            return None

