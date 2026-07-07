import os
import time
from datetime import datetime
from functools import wraps
from typing import Callable, Any
def log_operation(func:Callable)->Callable:
    @wraps(func)
    def wrapper(*args,**kwargs)->Any:
        result=func(*args,**kwargs)
        os.makedirs("logs",exist_ok=True)
        with open("logs/function.log","a",encoding="utf-8") as file:
            file.write(f"Timestamp:{datetime.now()}\n" f"Function Name:{func.__name__}\n" f"Arguments:{args[1:]},{kwargs}\n"f"Return Valuse:{result}\n" f"{'-'*40}\n")
        return result
    return wrapper
def execution_time(func:Callable)->Callable:
    @wraps(func)
    def wrapper(*args,**kwargs)->Any:
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        print(f"Execution Time of {func.__name__}:" f"{end_time-start_time:.6f}seconds")
        return result
    return wrapper