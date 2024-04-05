from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver import Firefox
from time import sleep
import os

png_path = "png/"


def safe_mkdir(path: str):
    try:
        os.mkdir(path)
    except (FileExistsError, FileNotFoundError):
        print(f"Couldn't create {path}.\n"
              "Directory already created or no parent directory.")


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
        except InvalidArgumentException:
            print("Invalid URL")
    safe_mkdir(save_path)
    sleep(sleep_time)
    result = driver.get_screenshot_as_file(save_path + filename + ".png")
    return result


urls = [
    "https://vk.com",
    "https://74.ru",
    "https://youtube.com",
    "https://habr.com",
]

delay = 0

driver = webdriver.Firefox()

for url in urls:
    filename = get_domen_name(url)
    take_screenshot_from(url, driver, filename, png_path)

driver.quit()