from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, автоматически логирует начало и конец выполнения функции,
        а также ее результаты или возникшие ошибки"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n\n"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_message)
                else:
                    print(log_message)
            except Exception as e:
                log_message = f"{func.__name__}  error: {e}. Inputs: {args}{kwargs}\n\n"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_message)
                else:
                    print(log_message)
                raise Exception(log_message)
        return inner
    return decorator
