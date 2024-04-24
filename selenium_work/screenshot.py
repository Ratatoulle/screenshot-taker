from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from .url.helper import add_protocol
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

DRIVER = webdriver.Remote
OPTIONS = webdriver.ChromeOptions

se_port = os.environ.get("SE_PORT")
se_host = os.environ.get("SE_HOST")

IN_CONTAINER = True


def take_from(url: str, *, sleep_time: int = 10) -> bytes | bool:
    options = OPTIONS()
    options.add_argument("--headless=new")
    if IN_CONTAINER:
        driver = DRIVER(options=options, command_executor=f"http://{se_host}:{se_port}")
    else:
        driver = DRIVER(options=options)
    try:
        driver.get(url)
    except InvalidArgumentException:
        try:
            url = add_protocol(url)
            driver.get(url)
        except (InvalidArgumentException, WebDriverException):
            return False
        sleep(sleep_time)
        image = driver.get_screenshot_as_png()
        if not image:
            return False
        else:
            return image
    finally:
        driver.close()
        driver.quit()
