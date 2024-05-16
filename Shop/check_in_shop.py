from vision_controll_package import Image
from main_shared_variables import path_to_screenshots, path_to_templates
from time import sleep


class CheckInShop(Image):
    def for_scroll_of_weapon(self):
        sleep(1)
        self.take_screenshot(path_to_screenshots+'scroll_of_weapon.png', (354, 348, 394, 428))

        return self.matching(path_to_templates + 'scroll_of_weapon.png', path_to_screenshots + 'scroll_of_weapon.png')

    def for_armor_scroll(self):
        sleep(1)
        self.take_screenshot(path_to_screenshots+'armor_scroll.png', (682, 348, 717, 428))

        return self.matching(path_to_templates+'armor_scroll.png', path_to_screenshots+'armor_scroll.png')

    def for_mounting(self):
        sleep(1)
        cards = []

        for we in range(2):
            self.take_screenshot(path_to_screenshots+f'mounting{we}.png',
                                 (355 + we * 325, 310, 400 + we * 325, 415))

            cards.append(self.matching(path_to_screenshots + f'mounting{we}.png',
                                       path_to_templates + f'mounting{we}.png'))

        for ste in range(2):
            self.take_screenshot(path_to_screenshots+f'mounting{ste+2}.png',
                                 (355 + ste * 325, 655, 400 + ste * 325, 775))

            cards.append(self.matching(path_to_screenshots+f'mounting{ste+2}.png',
                                       path_to_templates+f'mounting{ste+2}.png'))

        return cards


check_in_shop = CheckInShop()




