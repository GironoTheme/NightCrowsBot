from vision_controll_package import Mouse, Keyboard
from time import sleep


class NavigationInGift(Mouse, Keyboard):
    def open_an_gift(self):
        self.move_and_click(1653, 46)
        self._going_through_gifts()

    def _going_through_gifts(self):
        for _ in range(5):
            self.move_and_click(458, 334)
            sleep(0.5)
            self.click()

            self._proclamation()

            self.move_and_click(458, 334)
            sleep(0.5)
            self.click()

            self.scroll_down(7)

        for i in range(4):
            self.move_and_click(458, 334 + i * 140)
            self.click()
            self._proclamation()

        self.press_button('esc')

    def _proclamation(self):
        self._get_achievements()

        self._daily_attendance(555)
        self._daily_attendance(700)

    def _get_achievements(self):
        self.move_and_click(905, 596)
        sleep(0.3)
        self.move_and_click(1533, 384)

        self.move_and_click(1300, 596)
        sleep(0.3)
        self.move_and_click(1533, 384)

    def _daily_attendance(self, y_cords):
        for i in range(7):
            self.move_and_click(750 + i * 120, y_cords)
            sleep(0.2)
            self.move_and_click(1533, 384)


navigation_in_gift = NavigationInGift()


