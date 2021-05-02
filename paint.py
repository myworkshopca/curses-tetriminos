import curses

# Tetris page on wikipedia: https://en.wikipedia.org/wiki/Tetris

# initialize colors.
def initcolors(bg_color=-1):

    # initialize the color pair
    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
    #for i in range(0, 20):
        # pair number, foreground color, background color
        #curses.init_pair(i + 1, i, -1)
        curses.init_pair(i + 1, i, bg_color)
        #curses.init_pair(i + 1, i, 8)

# characters for building Tetriminos could be found here:
# - http://xahlee.info/comp/unicode_index.html
#
def paintTetrimino(stdscr, color, type):

    # 9619 - ▓, 9609 - ▉, 9608 - █, 9611 - ▋
    # 9634 - ▢,
    unit_ch = chr(9634)

    if type == 'square':
        # 2 x 2 tetrimino
        stdscr.addstr(5, 2, unit_ch, color)
        stdscr.addstr(5, 4, unit_ch, color)
        stdscr.addstr(6, 2, unit_ch, color)
        stdscr.addstr(6, 4, unit_ch, color)
    elif type == 'line':
        for x in range(2, 10, 2):
            stdscr.addstr(8, x, unit_ch, color)

def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(2, 2, 'Painting tetriminos!')

    # initialize color pairs
    bg = -1
    initcolors(bg)

    paintTetrimino(stdscr, curses.color_pair(4), 'square')
    paintTetrimino(stdscr, curses.color_pair(5), 'line')

    stdscr.getch()

curses.wrapper(tetris)
