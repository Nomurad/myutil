import os 

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