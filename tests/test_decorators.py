import re
from typing import Any

import pytest

from src.decorators import log


@log('log.txt')
def log_decorator_error() -> None:
    """Тестируем декоратор log при возникновении ошибки c выводом в файл"""
    raise ValueError("Ошибка")


@log()
def log_decorator_ok() -> None:
    """Тестируем декоратор log c выводом в консоль"""
    pass


def test_log_decorator_1() -> None:
    """Тестируем декоратор log, при возникновении ошибки при записи в файл"""
    with pytest.raises(Exception, match=re.escape('log_decorator_error  error: Ошибка. Inputs: (){}\n\n')):
        log_decorator_error()


def test_log_decorator_2(capsys: Any) -> None:
    """Тестируем декоратор log, при возникновении ошибки при записи в консоль"""
    log_decorator_ok()
    captured = capsys.readouterr()
    assert captured.out == 'log_decorator_ok ok\n\n\n'
