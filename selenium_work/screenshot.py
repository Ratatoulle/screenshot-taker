from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from .url.helper import add_protocol
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

IN_CONTAINER = False

if IN_CONTAINER:
    DRIVER = webdriver.Remote
else:
    DRIVER = webdriver.Chrome

OPTIONS = webdriver.ChromeOptions

se_port = os.environ.get("SE_PORT")
se_host = os.environ.get("SE_HOST")


def take_from(url: str, *, sleep_time: int = 10) -> bytes | bool:
    options = OPTIONS()
    options.add_argument("--headless=new")
    if IN_CONTAINER:
        driver = DRIVER(options=options, command_executor=f"http://{se_host}:{se_port}")
    else:
        driver = DRIVER(options=options)
    if "https://" not in url and "http://" not in url:
        url = add_protocol(url)
    try:
        driver.get(url)
        sleep(sleep_time)
        image = driver.get_screenshot_as_png()
    finally:
        # driver.close()
        driver.quit()
    return image
