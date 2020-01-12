import os 
import time
from datetime import datetime
from contextlib import contextmanager

def parse_time(a):
    if 0 < a < 1:
        return f'{a:.3g}秒'
    sec = int(a)
    d = f'{sec // 86400}日'          if sec >= 86400 else ''
    h = f'{sec % 86400 // 3600}時間' if sec >= 3600  else ''
    m = f'{sec % 3600 // 60}分'      if sec >= 60    else ''
    s = f'{sec % 60}秒'
    return d + h + m + s

@contextmanager
def stopwatch(name='anonymous'):
    start = time.time()
    yield lambda: time.time() - start
    elapsed_time = time.time() - start
    isec = int(elapsed_time)
    if isec < 60:
        stime = f'{elapsed_time:.3g}秒'
    else:
        stime = f'{isec}秒 ({parse_time(isec)})'
    print(f'[Stopwatch@{strnow()}] {name}: {stime}')

def strnow(format='%Y/%m/%d %H:%M:%S'):
    return datetime.now().strftime(format)

class Term_Colors(object):
    BLACK     = "\033[30m"
    RED       = "\033[31m"
    GREEN     = "\033[32m"
    YELLOW    = "\033[33m"
    BLUE      = "\033[34m"
    PURPLE    = "\033[35m"
    CYAN      = "\033[36m"
    WHITE     = "\033[37m"
    END       = "\033[0m"
    BOLD      = "\038[1m"
    UNDERLINE = "\033[4m"
    INVISIBLE = "\033[08m"
    REVERCE   = "\033[07m"

    def __init__(self):
        pass

    @classmethod
    def color_print(cls, color, *args):
        # all_args = color + args + self.END
        print(color, *args, end=cls.END+"\n")

if __name__ == "__main__":
    pass