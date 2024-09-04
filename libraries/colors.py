try:
    # To install colorama isn't
    # needed if you aren't a developper.
    from colorama import Fore

    """Colorama colors:"""

    COL_RED = Fore.RED
    COL_CYAN = Fore.CYAN
    COL_BLUE = Fore.BLUE
    COL_GREEN = Fore.GREEN
    COL_YELLOW = Fore.YELLOW

    COL_RESET = Fore.RESET

except:
    COL_RED = ""
    COL_CYAN = ""
    COL_BLUE = ""
    COL_GREEN = ""
    COL_YELLOW = ""
    COL_RESET = ""

"""RGB 1 colors:"""

LIGHT_RED = (1, 0.5, 0.5)
RED = (1, 0, 0)
DARK_RED = (0.5, 0, 0)

LIGHT_GREEN = (0.5, 1, 0.5)
GREEN = (0, 1, 0)
DARK_GREEN = (0, 0.5, 0)

LIGHT_BLUE = (0, 0.1, 1)
BLUE = (0, 0.25, 1)
DARK_BLUE = (0, 0, 0.5)

LIGHT_GREY = (0.75, 0.75, 0.75)
GREY = (0.5, 0.5, 0.5)
DARK_GREY = (0.25, 0.25, 0.25)

LIGHT_YELLOW = (1, 1, 0)
YELLOW = (1, 1, 0)
DARK_YELLOW = ()

LIGHT_VIOLET = ()
VIOLET = (1, 0, 1)
DARK_VIOLET = ()

LIGHT_CYAN = (0, 1, 1)
CYAN = (0, 1, 1)
DARK_CYAN = ()

LIGHT_ORANGE = ()
ORANGE = ()
DARK_ORANGE = ()

LIGHT_PINK = ()
PINK = ()
DARK_PINK = ()

WHITE = (1, 1, 1)
BLACK = (0, 0, 0)

#LIGHT_ = ()
# = ()
#DARK_ = ()