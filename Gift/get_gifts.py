from vision_controll_package import Image
from main_shared_variables import path_to_templates, path_to_screenshots
from Gift.navigation_in_gift import navigation_in_gift
from time import sleep


class GetGifts(Image):
    def get(self):
        #if self._check_for_gift():
        navigation_in_gift.open_an_gift()

    def _check_for_gift(self):
        sleep(1)
        #self.take_screenshot(path_to_templates + 'gift_icon.png', (1671, 19, 1680, 27))
        return self.matching(path_to_templates + 'gift_icon.png',
                             template_image_name=path_to_screenshots + 'gift_icon.png',
                             need_for_taking_screenshot=True, area_of_screenshot=(1671, 19, 1680, 27))


get_gifts = GetGifts()


