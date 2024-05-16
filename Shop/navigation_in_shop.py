from vision_controll_package import Mouse, Keyboard
from Shop.check_in_shop import check_in_shop
from time import sleep


class NavigationInShop(Mouse, Keyboard):
    def movement(self):
        sleep(0.4)
        self._open_an_shop()
        self._click_to_exchange()

        self._buy_scrolls()
        self._buy_summoning_cards()

        self.move_and_click(1870, 45)

    def _buy_scrolls(self):
        self._simple_exchange()

        if check_in_shop.for_scroll_of_weapon():
            self._click_to_scroll_of_weapon()
            self._buy_max()
            self._buy()

        if check_in_shop.for_armor_scroll():
            self._click_to_armor_scroll()
            self._buy_max()
            self._buy()

    def _buy_summoning_cards(self):
        self._summoning()
        cards = check_in_shop.for_mounting()

        for i in range(2):
            if cards[i] is True:
                self.move_and_click(445 + i * 330, 360)
                self._buy()
                self._open_all()

        for el in range(2, 4):
            if cards[el] is True:
                self.move_and_click(445 + (el - 2) * 330, 685)
                self._buy()
                self._open_all()

    def _open_all(self):
        sleep(0.8)
        self.move_and_click(965, 1025)
        sleep(0.4)
        self.move_and_click(965, 1025)

    def _summoning(self):
        self.move_and_click(95, 250)

    def _open_an_shop(self):
        self.move_and_click(1581, 53)

    def _click_to_exchange(self):
        self.move_and_click(340, 125)

    def _simple_exchange(self):
        self.move_and_click(95, 200)

    def _buy_max(self):
        self.move_and_click(873, 703)

    def _buy(self):
        self.move_and_click(1080, 793)
        sleep(0.6)
        self.move_and_click(947, 622)

    def _click_to_scroll_of_weapon(self):
        self.move_and_click(435, 360)

    def _click_to_armor_scroll(self):
        self.move_and_click(759, 360)


navigation_in_shop = NavigationInShop()
