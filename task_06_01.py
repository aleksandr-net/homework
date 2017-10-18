#!/usr/bin/python3.5
import platform
from functools import wraps


def run_on_linux(func):
    def wrapper(*args, **kwargs):
        if platform.win32_ver() == ('', '', '', '') and platform.mac_ver() == ('', ('', '', ''), ''):
#        if platform.system == 'Linux':
            result = func(*args, **kwargs)
            return result
        else:
            return None
    return wrapper


def run_on_macos(func):
    def wrapper(*args, **kwargs):
        if platform.dist() == ('', '', '') and platform.win32_ver() == ('', '', '', ''):
#        if platform.system == 'Darwin':
            result = func(*args, **kwargs)
            return result
        else:
            return None
    return wrapper


def run_on_windows(func):
    def wrapper(*args, **kwargs):
        if platform.mac_ver() == ('', ('', '', ''), '') and platform.dist() == ('', '', ''):
#        if platform.system == 'Windows':
            result = func(*args, **kwargs)
            return result
        else:
            return None
    return wrapper


@run_on_linux
def func_linux():
    print('Эта функция выполняется только на Linux!')

@run_on_macos
def func_macos():
    print('Эта функция выполняется только на MacOS!')

@run_on_windows
def func_windows():
    print('Эта функция выполняется только на Windows!')

func_linux()
func_macos()
func_windows()
