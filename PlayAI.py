from Board import Board
from King import *
from AI import *

b = Board()

b.print_board()

while True:
    inp = input('white to move:')
    col = inp[1]
    if col == 'a':
        col = 0
    if col == 'b':
        col = 1
    if col == 'c':
        col = 2
    if col == 'd':
        col = 3
    if col == 'e':
        col = 4
    if col == 'f':
        col = 5
    if col == 'g':
        col = 6
    if col == 'h':
        col = 7

    col2 = inp[4]
    if col2 == 'a':
        col2 = 0
    if col2 == 'b':
        col2 = 1
    if col2 == 'c':
        col2 = 2
    if col2 == 'd':
        col2 = 3
    if col2 == 'e':
        col2 = 4
    if col2 == 'f':
        col2 = 5
    if col2 == 'g':
        col2 = 6
    if col2 == 'h':
        col2 = 7

    figure = b.getFigure_pos([int(inp[2]) - 1, col])
    if figure.short != inp[0]:
        print('illegal move!')
    else:
        ret = figure.move([int(inp[5]) - 1, col2], b)
        if ret == 0:
            print('illegal move!')

    b.is_black_in_chess()

    print('black to move.')
    calculate(b)
    b.print_board()