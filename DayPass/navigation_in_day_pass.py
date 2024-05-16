from vision_controll_package import Mouse, Keyboard
from time import sleep


class NavigationInDayPass(Mouse, Keyboard):
    def click_to_day_pass(self):
        self.move_and_click(295, 40)

    def going_through_all_events(self, func):
        for i in range(3):
            self.move_and_click(450, 320 + i * 150)
            if func():
                self.click_to_get_all()

        sleep(0.3)
        self.move_and_click(1580, 265)

    def click_to_get_all(self):
        self.move_and_click(1487, 789)
        sleep(1)
        self.move_and_click(955, 622)


navigation_in_day_pass = NavigationInDayPass()
