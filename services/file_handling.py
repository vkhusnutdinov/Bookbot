import os
import sys
from pathlib import Path

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    symbols = {'.', ',', '!', '?', ':', ';'}
    text_page = text[start:] + ' '
    if len(text_page) <= size:
        return text_page, len(text_page)

    for i in range(size, 0, -1):
        if text_page[i - 1] in symbols and text_page[i] not in symbols:
            return text_page[:i], i


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        text, start, i = f.read(), 0, 0
        while start < len(text):
            text_page, size = _get_part_text(text, start, PAGE_SIZE)
            start += size
            i += 1
            book[i] = text_page.lstrip()


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(Path(__file__).parent.parent, os.path.normpath(BOOK_PATH)))
