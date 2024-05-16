from PIL import Image as pil
from PIL import ImageEnhance
import pyautogui
from ..shared_variables import path_to_pytesseract
import PIL.ImageGrab
import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = path_to_pytesseract


class Image:
    """Класс для работы с изображениями"""
    def matching(self, main_image_name, template_image_name, need_for_taking_screenshot=False, threshold=0.8,
                 func=None, area_of_screenshot=None):
        """Функция для сравнения 2ух изображений\n
        main_image_name - название основного изображения\n
        template_image_name - названия шаблона для сравнения\n
        need_for_taking_screenshot - нужно ли делать скриншот\n
        threshold - минимальный уровень совпадения 2ух изображений\n
        func - нужно ли возвращать координаты\n
        area_of_screenshot - область в которой нужно сделать скриншот. (указывать как тапл). Если оставить None, то будет сделан скриншот всего экрана
        """

        if need_for_taking_screenshot:
            if area_of_screenshot:
                PIL.ImageGrab.grab(bbox=area_of_screenshot).save(main_image_name)
            else:
                PIL.ImageGrab.grab().save(main_image_name)

        img_rgb = cv2.imread(main_image_name)
        template = cv2.imread(template_image_name)

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if func is None:
            for pt in zip(*loc[::-1]):
                return True
            return False

        for pt in zip(*loc[::-1]):
            return pt
        return False

    def take_screenshot(self, image_name, area_of_screenshot):
        """Функция для создания скриншота\n
        image_name - название изображения скриншота\n
        area_of_screenshot - область скриншота(указывать как тапл)
        """
        if area_of_screenshot:
            PIL.ImageGrab.grab(bbox=area_of_screenshot).save(image_name)
        else:
            PIL.ImageGrab.grab().save(image_name)

    def image_to_string(self, image_name, is_digits):
        """Функция для перевода картники в строку\n
        image_name - название изображения с которого нужно получить текст\n
        is_digits - True если с картинки нужно получить только числа, False если нужно получить еще и текст
        """
        if is_digits is True:
            text = pytesseract.image_to_string(image_name, config='--oem 1 --psm 11 -c tessedit_char_whitelist=0123456789/,.')
            return text
        text = pytesseract.image_to_string(image_name, lang='eng', config='--psm 3')
        return text

    def image_to_string_custom_confing(self, image_name, config):
        """Фуцнкия для получения текста с картинки с использованием своего запроса к Tesseract"""
        text = pytesseract.image_to_string(image_name, config=config)
        return text

    def upscale_image(self, file: str, upscale_multiplier):
        src = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        upscale_multiplier *= 100
        width = int(src.shape[1] * upscale_multiplier / 100)
        height = int(src.shape[0] * upscale_multiplier / 100)
        dsize = (width, height)
        output = cv2.resize(src, dsize)

        cv2.imwrite(file, output)

    def get_main_color(self, file):
        """Функция для получения цвета который чаще всего представлен на картинке\n
        file - название изображения на котором нужно найти цвет
        """
        img = pil.open(file)
        colors = img.getcolors(512)  # put a higher value if there are many colors in your image
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                if c[0] > max_occurence:
                    (max_occurence, most_present) = c
            return most_present
        except TypeError:
            raise Exception("Too many colors in the image")

    @staticmethod
    def delete_all_colors_except_one(file: str, colorMin_list: list, colorMax_list: list):
        """Функция для удаления всех цветов с картинки кроме одного"""
        im = cv2.imread(file)

        colorMin = np.array(colorMin_list, np.uint8)
        colorMax = np.array(colorMax_list, np.uint8)

        RGB  = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        mask = cv2.inRange(RGB, colorMin, colorMax)

        inverse_cachement_mask = cv2.bitwise_not(mask)
        im[inverse_cachement_mask > 0] = [0, 0, 0]

        cv2.imwrite(file, mask)

    @staticmethod
    def get_slider_size(filename):

        pic = cv2.imread(filename)

        gray_image = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

        _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        slider_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(slider_contour)

        return h

    def upscale_contrast(self, file: str, multiply=2.0):
        im = pil.open(file)

        enhancer = ImageEnhance.Contrast(im)
        img_contrast = enhancer.enhance(multiply)

        img_contrast.save(file)

    def find_object_in_area(self, file, area):
        try:
            cords_of_objects = pyautogui.locateOnScreen(image=file, region=area, confidence=0.85)
            return [cords_of_objects.left, cords_of_objects.top]

        except pyautogui.ImageNotFoundException:
            return False


image = Image()

