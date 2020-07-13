import copy
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import ctypes  # An included library with Python install.
def calculate(b, saves = None, forbidden_move = None):



    if saves:
        legal_moves = saves





    else:

        eval = 0
        figures = b.getFigures()
        #print(len(figures), 'len')
        legal_moves = []
        for figure in figures:
            if figure.alliance == 'black':
                legs = figure.get_legal_moves(b)
                if figure.short == 'k':
                    if forbidden_move in legs:
                        #print('deletam', forbidden_move)
                        legs.remove(forbidden_move)
                legal_moves.append([figure, legs])


        # for figure in figures:
        #     if figure.alliance == 'black':
        #         moves = []
        #         pos= [0,0]
        #         pos[0] = figure.pos[0]
        #         pos[1] = figure.pos[1]
        #         b1 = copy.deepcopy(b)
        #         moves1 = figure.get_legal_moves(b1)
        #         for move in moves1:
        #             b1 = copy.deepcopy(b)
        #             figure.pos[0] = pos[0]
        #             figure.pos[1] = pos[1]
        #             figure.move([pos[0] + move[0], pos[1] + move[1]], b1)
        #             if not b1.is_black_in_chess_only():
        #                 moves.append(move)
        #                 print(figure,pos[0],pos[1], move, 'legalan potez')
        #             else:
        #                 print(figure, move, 'otpao')
        #             figure.pos[0] = pos[0]
        #             figure.pos[1] = pos[1]
        #             if b1.get_last_deleted() != 0:
        #                 b1.addFigure(b1.get_last_deleted())
        #         legal_moves.append([figure, moves])


    #print(legal_moves, 'OVO SU SVI')
    evals = []
    evals_movs = []
    boards = []

    for move_figure in legal_moves:
        if move_figure[1] != []:
            for move in move_figure[1]:
                boards.append(copy.deepcopy(b))

    i = 0
    for move_figure in legal_moves:

        pos = [move_figure[0].pos[0], move_figure[0].pos[1]]
        if move_figure[1] != []:
            for move in move_figure[1]:
                move_figure[0].pos[0] = pos[0]
                move_figure[0].pos[1] = pos[1]
                b1 = boards[i]
                i = i + 1
                #print('radim move', move, move_figure[0], pos)
                dest = [pos[0] + move[0], pos[1] + move[1]]
                move_figure[0].move(dest, b1)
                if not b1.is_black_in_chess_only():
                    #print(move_figure[0], pos[0], pos[1], move, 'legalan potez')
                    eval = evaluate_position(b1.getFigures())
                    # b1.print_board()
                    # print(len(b1.getFigures()))
                    # print(b1.getFigures())
                    # print(eval, 'eval je a dest je ', dest)
                    evals_movs.append([move_figure[0], dest])
                    evals.append(eval)
                else:
                    #print(move_figure[0], move, 'otpao')
                    pass

                move_figure[0].pos[0] = pos[0]
                move_figure[0].pos[1] = pos[1]
                if len(evals) > 1 and (evals[-1] > evals[-2]) and b1.get_last_deleted() != 0:
                    #print('search',b1.get_last_deleted().pos[0], b1.get_last_deleted().pos[1])
                    b1.addFigure(b1.get_last_deleted())
                if True:
                    if b1.get_last_deleted() != 0:
                        b1.addFigure(b1.get_last_deleted())

    print(len(boards))

    print(evals_movs, evals)
    #print(evals[0])
    #b.print_board()
    print(len(b.getFigures()))
    if len(evals_movs) == 0 and b.is_black_in_chess_only():
        ctypes.windll.user32.MessageBoxW(0, "MAT", "ŠAH", 1)
        exit(0)
    if len(evals_movs) == 0:
        ctypes.windll.user32.MessageBoxW(0, "STALEMATE", "ŠAH", 1)
        exit(0)
    print('konacni move',evals_movs[np.argmax(evals)][0], evals_movs[np.argmax(evals)][1])
    return evals_movs[np.argmax(evals)][0].move(evals_movs[np.argmax(evals)][1], b)


def evaluate_position(figures):
    eval = 0
    for figure in figures:
        if figure.alliance == 'white':
            if figure.short == 'P':
                eval = eval - 1
            if figure.short == 'N':
                eval = eval - 3
            if figure.short == 'B':
                eval = eval - 3.5
            if figure.short == 'R':
                eval = eval - 6
            if figure.short == 'Q':
                eval = eval - 9
            if figure.short == 'K':
                eval = eval - 100
        else:
            if figure.short == 'p':
                eval = eval + 1
            if figure.short == 'n':
                eval = eval + 3
            if figure.short == 'b':
                eval = eval + 3.5
            if figure.short == 'r':
                eval = eval + 6
            if figure.short == 'q':
                eval = eval + 9
            if figure.short == 'k':
                eval = eval + 100

    return eval