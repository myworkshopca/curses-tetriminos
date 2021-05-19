import curses

# Tetris page on wikipedia: https://en.wikipedia.org/wiki/Tetris

# define the shapes of tetriminos.
TETRIMINO_SHAPES = ('i', 'o', 't', 'l', 'lr', 'z', 'zr')
# pick the color scheme for tetriminos.
# the value will be the curses color pair id
TETRIMINO_COLORS = (5, 4, 6, 7, 10, 11, 12)

# set the char for each tetrimino.
MINO_CHAR = chr(9609)

"""
Paint the tetrimino for the given mino variable and mino type.
"""
def paint_mino(stdscr, mino, type, erase=False):

    i = TETRIMINO_SHAPES.index(type)
    c = TETRIMINO_COLORS[i]

    # using the python ternary operator to decide
    # what character to use for painting each unit.
    unit_ch = ' ' if erase else MINO_CHAR

    for unit in mino:
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(c))

"""
calculate the new yxs for the given mino, type and action.
"""
def calc_mino_yxs(mino, type, action):

    new_mino = []

    # work on the action: move down.
    for unit in mino:
        new_mino.append([unit[0] + 1, unit[1]]);

    return new_mino

"""
initialize all units for each tetrimino for the given type.
 characters for building Tetriminos could be found here:
 - http://xahlee.info/comp/unicode_index.html

 each tetriminos will have 4 characters / units
"""
def init_mino_yxs(type):

    # get the index of the given type.
    index = TETRIMINO_SHAPES.index(type)

    if index == 0:
        # the I shape in horizental direction.
        return [ [4, 6], [4, 8], [4, 10], [4, 12] ]
    elif index == 1:
        # the O shape
        return [ [4, 22], [4, 24], [5, 22], [5, 24] ]
    elif index == 2:
        # the t shape
        return [ [4, 34], [5, 32], [5, 34], [5, 36] ]
    elif index == 3:
        # the l shape
        return [ [4, 48], [5, 44], [5, 46], [5, 48] ]
    elif index == 4:
        # the lr shape
        return [ [4, 56], [5, 56], [5, 58], [5, 60] ]
    elif index == 5:
        # the z shape
        return [ [4, 68], [4, 70], [5, 70], [5, 72] ]
    else:
        # the zr shape
        return [ [4, 82], [4, 84], [5, 82], [5, 80] ]

# initialize colors.
def init_colors(bg_color=-1):

    # initialize the color pair
    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
    #for i in range(0, 20):
        # pair number, foreground color, background color
        #curses.init_pair(i + 1, i, -1)
        curses.init_pair(i + 1, i, bg_color)
        #curses.init_pair(i + 1, i, 8)

# the tetris game will play in a  10 x 20 area
def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(2, 2, 'Painting tetriminos!')

    # initialize color pairs
    bg = -1
    init_colors(bg)

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

    tetriminos = []
    # paint the tetriminos intially
    for t in TETRIMINO_SHAPES:

        index = TETRIMINO_SHAPES.index(t)
        color = TETRIMINO_COLORS[index]
        mino = init_mino_yxs(t)
        tetriminos.append(mino)
        paint_mino(stdscr, mino, t)

    # moving loop.
    while True:
        # let's start with using the keyboard press to conrol the movement.
        key = stdscr.getch()

        # quit if user press q.
        if key == ord('q'):
            break;

        # any other key, we will move down one unit for all tetriminos.
        for t in tetriminos:
            index = tetriminos.index(t)
            color = TETRIMINO_COLORS[index]
            type = TETRIMINO_SHAPES[index]
            tetriminos[index] = calc_mino_yxs(t, type, 'MOVE_DOWN')
            paint_mino(stdscr, t, type, erase=True)
            paint_mino(stdscr, tetriminos[index], type)

curses.wrapper(tetris)
