import os
from enum import Enum

def clear_console(message = "Press Enter to continue..."):
    input(message)
    os.system('cls' if os.name=='nt' else 'clear')

class Return(Enum):
    EXIT = 0
    BACK = 1

def CallbackOption(message = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            if message:
                clear_console(message)
            else:
                clear_console()
        return wrapper
    if callable(message):
        func, message = message, None
        return decorator(func)
    return decorator

def CallbackSubMenu(func):
    def wrapper(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        func(*args, **kwargs)
    return wrapper

