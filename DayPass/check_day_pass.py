from vision_controll_package import Image
from main_shared_variables import path_to_screenshots, path_to_templates
from time import sleep


class DayPass(Image):
    def icon(self):
        sleep(1)
        # self.take_screenshot(path_to_screenshots+'day_pass_icon.png', (316, 18, 325, 26))
        # self.take_screenshot(path_to_templates+'gift_icon.png', (1671, 19, 1680, 27))
        return self.matching(path_to_templates + 'day_pass_icon.png',
                             template_image_name=path_to_screenshots + 'day_pass_icon.png',
                             need_for_taking_screenshot=True, area_of_screenshot=(316, 18, 325, 26))

    def get_all(self):
        return self.matching(path_to_templates + 'get_all.png',
                             template_image_name=path_to_screenshots + 'get_all.png',
                             need_for_taking_screenshot=True, area_of_screenshot=(1579, 771, 1587, 7796))


day_pass = DayPass()

