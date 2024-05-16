from pathlib import Path


def find_path_to_folder(folder):
    for root_path in Path(f'{disk_with_tesseract}:\\').glob(f'**\\{folder}\\'):
        return root_path


name_of_window = 'NIGHT CROWS'
disk_with_tesseract = 'C'

path_to_tesseract = f"{find_path_to_folder('tesseract')}\\tesseract.exe"

path_to_screenshots = f"{find_path_to_folder('NightCrowsBot')}\\Images\\screenshots\\"
path_to_templates = f"{find_path_to_folder('NightCrowsBot')}\\Images\\templates\\"
path_to_json = f"{find_path_to_folder('NightCrowsBot')}\\Jsons\\"

limit_for_calculating_best_price = 200000
purchase_limit = 50000
percent_of_difference = 15

min_balance = 1000000

list_of_orders = None

