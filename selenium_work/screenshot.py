from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from .url.helper import add_protocol
from time import sleep

DRIVER = webdriver.Chrome
OPTIONS = webdriver.ChromeOptions

def take_from(url: str, *, sleep_time: int = 10) -> bytes | bool:
    options = OPTIONS()
    options.add_argument("--headless=new")
    options.add_argument("--enable-chrome-browser-cloud-management")
    driver = DRIVER(options)
    try:
        driver.get(url)
    except InvalidArgumentException:
        try:
            url = add_protocol(url)
            driver.get(url)
        except (InvalidArgumentException, WebDriverException):
            print(f"URL {url} is invalid")
            return False
    sleep(sleep_time)
    return driver.get_screenshot_as_png()
