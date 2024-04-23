import re


def make_valid_name(url: str) -> str:
    pattern = re.compile(r".*//(.*)\..*")
    domen = re.sub(pattern, r"\1", url).replace("/", "--")
    return domen


def add_protocol(url: str) -> str:
    return "https://" + url
