from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from time import sleep
from url.helper import get_domen_name, add_protocol

DRIVER = webdriver.Chrome
OPTIONS = webdriver.ChromeOptions


class ScreenshotTaker:

    def __init__(self):
        self.driver = DRIVER()
        self.options = OPTIONS()
        self.init_options()

    def init_options(self):
        self.options.add_argument("--headless")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def take_from(self, url: str, filename: str, save_path: str, *, sleep_time: int = 5) -> bool:
        try:
            self.driver.get(url)
        except InvalidArgumentException:
            try:
                url = add_protocol(url)
                self.driver.get(url)
            except (InvalidArgumentException, WebDriverException):
                print(f"URL {url} is invalid")
                return False
        sleep(sleep_time)
        return self.driver.get_screenshot_as_file(save_path + filename + ".png")


urls = [
    "https://vk.com",
    "https://youtube.com",
    "https://rbc.ru",
    "https://ura.news",
]

with ScreenshotTaker() as taker:
    for url in urls:
        filename = get_domen_name(url)
        if taker.take_from(url, filename, "png/", sleep_time=0):
            print(f"Screenshot for {url} was successfully taken!")
