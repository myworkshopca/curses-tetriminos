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
# each tetriminos will have 4 characters / units
def paintTetrimino(stdscr, color, type):

    # 9619 - ▓, 9609 - ▉, 9608 - █, 9611 - ▋
    # 9634 - ▢,
    # the character to build each tetrimino
    unit_ch = chr(9609)

    # set the gap between each shape.
    #gap = paint vertical

    offset_x = 10 

    if type == 'square':
        # 2 x 2 tetrimino
        stdscr.addstr(4, 2 + offset_x * 2, unit_ch, color)
        stdscr.addstr(4, 4 + offset_x * 2, unit_ch, color)
        stdscr.addstr(5, 2 + offset_x * 2, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 2, unit_ch, color)
    elif type == 'line':
        # 1 x 4 line
        for x in range(6, 14, 2):
            stdscr.addstr(4, x, unit_ch, color)
    elif type == 't':
        # t shape tetrimino
        stdscr.addstr(4, 4 + offset_x * 3, unit_ch, color)
        stdscr.addstr(5, 2 + offset_x * 3, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 3, unit_ch, color)
        stdscr.addstr(5, 6 + offset_x * 3, unit_ch, color)
    elif type == 'l':
        # l shape tetrimino
        stdscr.addstr(4, 6 + offset_x * 4 + 2, unit_ch, color)
        stdscr.addstr(5, 2 + offset_x * 4 + 2, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 4 + 2, unit_ch, color)
        stdscr.addstr(5, 6 + offset_x * 4 + 2, unit_ch, color)
    elif type == 'lr':
        # l reverse shape tetrimino
        stdscr.addstr(4, 2 + offset_x * 5 + 4, unit_ch, color)
        stdscr.addstr(5, 2 + offset_x * 5 + 4, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 5 + 4, unit_ch, color)
        stdscr.addstr(5, 6 + offset_x * 5 + 4, unit_ch, color)
    elif type == 'z':
        # l shape tetrimino
        stdscr.addstr(4, 2 + offset_x * 6 + 6, unit_ch, color)
        stdscr.addstr(4, 4 + offset_x * 6 + 6, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 6 + 6, unit_ch, color)
        stdscr.addstr(5, 6 + offset_x * 6 + 6, unit_ch, color)
    elif type == 'zr':
        # l shape tetrimino
        stdscr.addstr(4, 4 + offset_x * 7 + 8, unit_ch, color)
        stdscr.addstr(4, 6 + offset_x * 7 + 8, unit_ch, color)
        stdscr.addstr(5, 4 + offset_x * 7 + 8, unit_ch, color)
        stdscr.addstr(5, 2 + offset_x * 7 + 8, unit_ch, color)

# the tetris game will play in a  10 x 20 area
def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(2, 2, 'Painting tetriminos!')

    # initialize color pairs
    bg = -1
    initcolors(bg)

    # paint the bottom border. y = 25
    # 8 for each tetrimino, 7 tetriminos
    # paint vertical borders between each tetrimino.
    for x in range(2, 10 * 6 + 12 + 8 * 2 + 1, 2):
        stdscr.addstr(25, x, chr(9634), curses.color_pair(8))

    start_x = 2
    # paint the vertical borders.
    for i in range(0, 8):
        # calculate the x axis based on index.
        if i == 0:
            x = start_x
        elif i == 1:
            x = start_x + i * 14
        else:
            x = start_x + i * 12 + 2
        # y axis will increase by 1.
        for y in range (4, 25):
            stdscr.addstr(y, x, chr(9634), curses.color_pair(8))

    # paint tetriminos initially
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
