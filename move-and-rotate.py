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

    for unit in mino['blocks']:
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(c))

"""
calculate the new yxs for the given mino, type and action.
"""
def calc_mino_yxs(mino, type, action):

    new_mino = {
        'blocks': [],
        'position': 0
    }
    out_bound = False

    if action == 'MOVE_DOWN':
        # we should keep the position.
        new_mino['position'] = mino['position']
        # work on the action: move down.
        # move down is easy, it will only need the y axis to increase by one.
        for unit in mino['blocks']:
            new_mino['blocks'].append([unit[0] + 1, unit[1]]);
            out_bound = (unit[0] + 1) >= 25
    elif action == 'ROTATE':
        # handle the rotate for each tetrimino.
        # For each tetrimino, the rotation will be different.
        # we will create a separate function to handle the ROTATE action.
        new_mino, out_bound = mino_rotate_yxs(mino, type)

    return (new_mino, out_bound)

"""
Rotate the given tetrimino.
Each tetrimino will only rotate toward clockwise direction.

"""
def mino_rotate_yxs(mino, type):

    # the copy method will clone the whole dict object.
    new_mino = mino.copy()
    out_bound = False

    # get the index of the given type.
    index = TETRIMINO_SHAPES.index(type)

    if index == 0:
        # rotate I shape tetrimino.
        # I shape mino only have 2 positions:
        # - horizontal, this is the initial position position = 0
        # - vertical, position = 1
        # we will use the % operator to calc the new position.
        new_mino['position'] = (mino['position'] + 1) % 2
        if new_mino['position'] == 0:
            # rotate the i-shape from vertical to horizontal.
            # we will use the first block as the center to rotate.
            new_mino['blocks'] = []
            # iterate the x axis, start from the x axios of first block
            for x in range(mino['blocks'][0][1],
                    # end number not include
                    mino['blocks'][0][1] + 4 * 2,
                    # takes 2 units for each block
                    2):
                new_mino['blocks'].append([mino['blocks'][0][0], x])

        elif new_mino['position'] == 1:
            # rotate the i-shape from horizontal to vertical.
            # we will use the first block as the center to rotate.
            new_mino['blocks'] = []
            # iterate the y axis, start from the y axios of first block
            for y in range(mino['blocks'][0][0],
                    # end number not include
                    mino['blocks'][0][0] + 4,
                    # takes 1 unit for each block
                    1):
                new_mino['blocks'].append([y, mino['blocks'][0][1]])
                # if any of the y axis greater than 25.
                out_bound = y >= 25
    #elif index == 1:
    #    # rotate O shape tetrimino, nothing should happen.
    #    pass
    elif index == 2:
        # rotate T shape tetrimino.
        # T shape mino has 4 positions:
        # - 0, up, the initial position.
        # - 1, right,
        # - 2, down,
        # - 3, left
        new_mino['position'] = (mino['position'] + 1) % 4
        # get ready the 4 items list for blocks.
        new_mino['blocks'] = [[]] * 4
        # rotate based on the new mino's position
        if new_mino['position'] == 0:
            new_mino['blocks'][0] = mino['blocks'][1]
            new_mino['blocks'][1] = mino['blocks'][3]
            new_mino['blocks'][2] = mino['blocks'][2]
            new_mino['blocks'][3] = [mino['blocks'][2][0], mino['blocks'][2][1] + 2]
        elif new_mino['position'] == 1:
            new_mino['blocks'][0] = mino['blocks'][1]
            new_mino['blocks'][1] = mino['blocks'][3]
            new_mino['blocks'][2] = mino['blocks'][2]
            new_mino['blocks'][3] = [mino['blocks'][2][0] + 1, mino['blocks'][2][1]]
        elif new_mino['position'] == 2:
            new_mino['blocks'][0] = mino['blocks'][1]
            new_mino['blocks'][1] = mino['blocks'][3]
            new_mino['blocks'][2] = mino['blocks'][2]
            new_mino['blocks'][3] = [mino['blocks'][2][0], mino['blocks'][2][1] - 2]
        elif new_mino['position'] == 3:
            new_mino['blocks'][0] = mino['blocks'][1]
            new_mino['blocks'][1] = mino['blocks'][3]
            new_mino['blocks'][2] = mino['blocks'][2]
            new_mino['blocks'][3] = [mino['blocks'][2][0] - 1, mino['blocks'][2][1]]
    else:
        # syntactical else statement, it should never happen.
        pass

    # by default it will return the mino as it is.
    return (new_mino, out_bound)

"""
initialize all units for each tetrimino for the given type.
 characters for building Tetriminos could be found here:
 - http://xahlee.info/comp/unicode_index.html

 each tetrimino is a dictionary. it will have the following structure:
 mino = {
     # blocks will store the coordinates of the 4 blocks for each tetrimino
     "blocks": [],
     # the rotation position, it will have value 0, 1, 2, 3.
     # the initial position is 0
     "position": 0
 }
"""
def init_mino_yxs(type):

    # get the index of the given type.
    index = TETRIMINO_SHAPES.index(type)
    # the mino dict.
    mino = {
        'blocks': [],
        'position': 0
    }

    if index == 0:
        # the i shape in horizental direction.
        mino['blocks'] = [ [4, 6], [4, 8], [4, 10], [4, 12] ]
    elif index == 1:
        # the O shape
        mino['blocks'] = [ [4, 22], [4, 24], [5, 22], [5, 24] ]
    elif index == 2:
        # the t shape
        mino['blocks'] = [ [5, 32], [4, 34], [5, 34], [5, 36] ]
    elif index == 3:
        # the l shape
        mino['blocks'] = [ [4, 48], [5, 44], [5, 46], [5, 48] ]
    elif index == 4:
        # the lr shape
        mino['blocks'] = [ [4, 56], [5, 56], [5, 58], [5, 60] ]
    elif index == 5:
        # the z shape
        mino['blocks'] = [ [4, 68], [4, 70], [5, 70], [5, 72] ]
    else:
        # the zr shape
        mino['blocks'] = [ [4, 82], [4, 84], [5, 82], [5, 80] ]

    return mino

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

    # turn off the default cursor
    curses.curs_set(False)

    # set nodelay mode
    stdscr.nodelay(True)
    stdscr.timeout(600)

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

    # the variable to track all tetriminos.
    # check function init_mino_yxs for the data structure for each mino
    tetriminos = []

    # paint the tetriminos intially
    for t in TETRIMINO_SHAPES:

        index = TETRIMINO_SHAPES.index(t)
        color = TETRIMINO_COLORS[index]
        mino = init_mino_yxs(t)
        tetriminos.append(mino)
        paint_mino(stdscr, mino, t)

    # set the initial action
    action = 'MOVE_DOWN'

    # moving loop.
    while True:
        # let's start with using the keyboard press to conrol the movement.
        key = stdscr.getch()

        # quit if user press q.
        if key == ord('q'):
            break;
        elif key == ord('r'):
            action = 'ROTATE'
        else:
            action = 'MOVE_DOWN'

        # any other key, we will move down one unit for all tetriminos.
        for mino in tetriminos:

            index = tetriminos.index(mino)
            color = TETRIMINO_COLORS[index]
            shape = TETRIMINO_SHAPES[index]

            # calculate the new coordinates for the tetrimino.
            # we will using the the tetrimino's current coordinates to
            # calculate the new coordinates.
            new_mino, out_bound = calc_mino_yxs(mino, shape, action)
            # erase the current tetrimino.
            paint_mino(stdscr, mino, shape, erase=True)

            # check if the new yxs are inside the border.
            if out_bound:
                # set the new yxs to top of the board.
                new_mino= init_mino_yxs(shape)
            # paint the new tetrimino
            paint_mino(stdscr, new_mino, shape)

            # reset the tetrimino list.
            tetriminos[index] = new_mino

curses.wrapper(tetris)
