from datetime import datetime


def log_decorator(func):
    def envelope(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {datetime.now()}')
        return result

    return envelope
