from vision_controll_package import Windows
from DayPass.get_rewards import get_rewards
from Gift.get_gifts import get_gifts
from Dungeons.dungeon_farming import dungeon_farming
from Shop.buy import buy
windows = Windows()


def launch(hwnd):
    get_gifts.get()

    get_rewards.get()

    dungeon_farming.farming()

    buy.buy()


windows.switch_windows(launch)


