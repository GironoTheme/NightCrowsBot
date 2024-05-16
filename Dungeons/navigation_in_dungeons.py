from vision_controll_package import Mouse, Keyboard
from Dungeons.check_in_dungeons import check_in_dungeons
from time import sleep


class NavigationInDungeons(Mouse, Keyboard):
    def movement(self):
        self._click_to_dungeons_icon()
        self._busting_dungeons()

    def _click_to_dungeons_icon(self):
        self.move_and_click(1875, 50)
        self.move_and_click(1730, 245)
        sleep(0.5)

    def _busting_dungeons(self):
        self.move_and_click(120, 125)

        self._simple_dungeons()
        self._special_dungeons()

    def _simple_dungeons(self):
        for i in range(4):
            self.move_and_click(120, 250 + i * 180)
            self._enter_to_dungeon()

    def _enter_to_dungeon(self):
        if check_in_dungeons.for_enter():
            self.move_and_click(1790, 1030)
            sleep(0.3)
            self.move_and_click(1065, 675)

            self._auto_farming()
            self._check_time()

    def _auto_farming(self):
        sleep(15)
        self.move_and_click(1865, 770)

    def _special_dungeons(self):
        self.move_and_click(340, 125)
        self._enter_to_dungeon()

    def _check_time(self):
        while True:
            sleep(1200)
            if check_in_dungeons.usage_time_has_expired() is True:
                self.move_and_click(955, 650)
                sleep(0.4)
                self._click_to_dungeons_icon()
                break


navigation_in_dungeons = NavigationInDungeons()



