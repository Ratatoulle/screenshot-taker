from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from selenium.webdriver import Firefox
from time import sleep
import os

def get_domen_name(url: str) -> str:
    import re
    pattern = re.compile(r".*/(.*)\..*")
    domen = re.sub(pattern, r"\1", url)
    return domen


def add_protocol(url: str) -> str:
    return "https://" + url


def take_screenshot_from(url: str, driver: Firefox, filename: str, save_path: str, *, sleep_time: int = 5) -> bool:
    try:
        driver.get(url)
    except InvalidArgumentException:
        try:
            url = add_protocol(url)
            driver.get(url)
        except (InvalidArgumentException, WebDriverException):
            print(f"URL {url} is invalid")
            return False
    # safe_mkdir(save_path)
    sleep(sleep_time)
    return driver.get_screenshot_as_file(save_path + filename + ".png")

driver = webdriver.Firefox()

driver.quit()
