from vision_controll_package import Image
from main_shared_variables import path_to_templates, path_to_screenshots
from time import sleep


class CheckInDungeons(Image):
    def for_enter(self):
        sleep(1)
        self.take_screenshot(path_to_screenshots+"enter_to_dungeon.png", (1830, 1010, 1860, 1040))

        main_color = self.get_main_color(path_to_screenshots+"enter_to_dungeon.png")

        if 90 <= main_color[0] <= 130 and 70 <= main_color[1] <= 110 and 40 <= main_color[2] <= 80:
            return True

        return False

    def usage_time_has_expired(self):
        sleep(1)
        self.take_screenshot(path_to_screenshots + 'usage_time_has_expired.png', (860, 630, 1060, 675))

        return self.matching(path_to_screenshots + 'usage_time_has_expired.png',
                             path_to_templates+'usage_time_has_expired.png')


check_in_dungeons = CheckInDungeons()


