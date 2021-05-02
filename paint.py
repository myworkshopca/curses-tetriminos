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
        # 1 x 4 line
        for x in range(2, 10, 2):
            stdscr.addstr(8, x, unit_ch, color)
    elif type == 't':
        # t shape tetrimino
        stdscr.addstr(10, 4, unit_ch, color)
        stdscr.addstr(11, 2, unit_ch, color)
        stdscr.addstr(11, 4, unit_ch, color)
        stdscr.addstr(11, 6, unit_ch, color)
    elif type == 'l':
        # l shape tetrimino
        stdscr.addstr(13, 6, unit_ch, color)
        stdscr.addstr(14, 2, unit_ch, color)
        stdscr.addstr(14, 4, unit_ch, color)
        stdscr.addstr(14, 6, unit_ch, color)
    elif type == 'lr':
        # l reverse shape tetrimino
        stdscr.addstr(16, 2, unit_ch, color)
        stdscr.addstr(17, 2, unit_ch, color)
        stdscr.addstr(17, 4, unit_ch, color)
        stdscr.addstr(17, 6, unit_ch, color)
    elif type == 'z':
        # l shape tetrimino
        stdscr.addstr(19, 2, unit_ch, color)
        stdscr.addstr(19, 4, unit_ch, color)
        stdscr.addstr(20, 4, unit_ch, color)
        stdscr.addstr(20, 6, unit_ch, color)
    elif type == 'zr':
        # l shape tetrimino
        stdscr.addstr(22, 4, unit_ch, color)
        stdscr.addstr(22, 6, unit_ch, color)
        stdscr.addstr(23, 4, unit_ch, color)
        stdscr.addstr(23, 2, unit_ch, color)

def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(2, 2, 'Painting tetriminos!')

    # initialize color pairs
    bg = -1
    initcolors(bg)

    paintTetrimino(stdscr, curses.color_pair(4), 'square')
    paintTetrimino(stdscr, curses.color_pair(5), 'line')
    paintTetrimino(stdscr, curses.color_pair(6), 't')
    paintTetrimino(stdscr, curses.color_pair(7), 'l')
    # 8 is white, 9 is grey, we want some colorful thing...
    paintTetrimino(stdscr, curses.color_pair(10), 'lr')
    paintTetrimino(stdscr, curses.color_pair(11), 'z')
    paintTetrimino(stdscr, curses.color_pair(12), 'zr')

    stdscr.getch()

curses.wrapper(tetris)
