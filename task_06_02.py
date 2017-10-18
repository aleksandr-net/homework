#!/usr/bin/python3.5
import time

def pause(p_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(p_time)
            return func(*args, **kwargs)
    
        return wrapper
    return decorator
