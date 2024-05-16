import gspread


class GoogleSheets:
    """Класс для работы с гугл таблицами"""

    def __init__(self, SPREADSHEET_URL, credentials, num_of_sheet):
        self.SPREADSHEET_URL = SPREADSHEET_URL
        self.credentials = credentials

        self.gs = gspread.service_account(self.credentials)
        self.sh = self.gs.open_by_url(self.SPREADSHEET_URL)
        self.worksheet = self.sh.get_worksheet(num_of_sheet)

    def write_google(self, data):
        """Фуцнкия для записи в гугл таблицу данных\n
        Сюда нужно указать словарь который необходимо записать в таблицу. В таком виде\n
        {Клетка(или диапазон клеток) : значение этой клетки}"""
        for key, value in data.items():
            self.worksheet.update(key, value)

    def get_value_from_cell(self, cell):
        """Функция чтобы получить значение из определенной клетки(или дипазона клеток)
        get_value_from_cell()"""
        value = self.worksheet.get(cell)
        return value


