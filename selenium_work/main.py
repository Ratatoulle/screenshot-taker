from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from time import sleep
from selenium_work.url.helper import add_protocol


class ScreenshotTaker:

    def __init__(self):
        self.driver = webdriver.Firefox()

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
