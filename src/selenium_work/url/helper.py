import re


def get_domen_name(url: str) -> str:
    pattern = re.compile(r".*/(.*)\..*")
    domen = re.sub(pattern, r"\1", url)
    return domen


def add_protocol(url: str) -> str:
    return "https://" + url
