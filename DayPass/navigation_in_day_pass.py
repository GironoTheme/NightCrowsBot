from vision_controll_package import Mouse, Keyboard
from time import sleep


class NavigationInDayPass(Mouse, Keyboard):
    def click_to_day_pass(self):
        self.move_and_click(295, 40)

    def going_through_all_events(self, func):
        sleep(0.5)
        self.move_and_click(440, 330)
        self.scroll_up(20)
        sleep(0.5)
        for i in range(4):
            self.move_and_click(450, 320 + i * 150)
            if func() is True:
                self.click_to_get_all()
            if i == 3:
                self.move(440, 330)
                self.scroll_down(40)
                for i in range(4):
                    self.move_and_click(450, 320 + i * 150)
                    if func() is True:
                        self.click_to_get_all()
                break
        sleep(0.3)
        self.move_and_click(1620, 265)

    def click_to_get_all(self):
        self.move_and_click(1487, 789)
        sleep(1)
        self.move_and_click(955, 622)


navigation_in_day_pass = NavigationInDayPass()
