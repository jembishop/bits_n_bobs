import curses
import logging
from curses import wrapper

logger = logging.getLogger(__file__)
hdlr = logging.FileHandler(__file__ + ".log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

## Step 1 progress down the tree to work out the final selection function
## Step two compute the new selection and replace current selection with it if valid.
# Selection actions
def move_right(text, start, end):
    return start + 1, end + 1


def move_left(text, start, end):
    return start - 1, end - 1


def find_right(text, start, end):
    substring = "jem"
    ind = text[end:].find(substring) + end
    if ind > 0:
        start, end = ind, ind+len(substring)
    return start, end

def find_left(text, start, end):
    substring = "jem"
    ind = text[:start].rfind(substring)
    if ind > 0:
        start, end = ind, ind+len(substring)
    return start, end

def valid_selection(selection):
    for i in selection:
        if i < 0:
            return False
    return True


keymap = {"k": move_right, "j": move_left, "f":find_right, "d":find_left}


def main(stdscr):
    stdscr.clear()
    selection = (0, 1)
    logger.info("STARTING")
    text = ""
    mode = "N"
    while True:
        # logger.info(f"SELECTION: {selection}")
        c = stdscr.getch()
        if c == ord("i"):
           logging.info("SHIFT")
           mode = "I"
        if mode == "I":
            stdscr.insnstr(0, selection[1], chr(c))
            selection = move_left(text, *selection)
            continue
        action = keymap.get(chr(c))
        if not action:
            continue
        next_selection = action(text, *selection)
        if valid_selection(next_selection):
            selection = next_selection
        for index in range(len(text)):
            if index in range(*selection):
                stdscr.chgat(0, index, 1, curses.A_REVERSE)
            else:
                stdscr.chgat(0, index, 1, curses.A_NORMAL)


wrapper(main)
