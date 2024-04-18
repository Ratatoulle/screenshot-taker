from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from .url.helper import add_protocol
from time import sleep

DRIVER = webdriver.Chrome
OPTIONS = webdriver.ChromeOptions


class ScreenshotTaker:

    def __init__(self):
        self.options = OPTIONS()
        self.init_options()
        self.driver = DRIVER(self.options)

    def init_options(self):
        self.options.add_argument("--headless=new")
        self.options.add_argument("--enable-chrome-browser-cloud-management")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def take_from(self, url: str, filename: str, save_path: str, *, sleep_time: int = 10) -> bool:
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
