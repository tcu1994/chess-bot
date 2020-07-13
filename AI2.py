import copy
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
import ctypes  # An included library with Python install.
class AI2():
    def __init__(self):
        self.positions = 0
    def calculate(self, b, saves = None, forbidden_move = None):
        import time
        start_time = time.time()
        self.positions = 0
        alpha = -200
        beta = 200
        maxEval = -200

        if saves:
            legal_moves = saves





        else:

            #eval = 0
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
                    dest = [pos[0] + move[0], pos[1] + move[1]]
                    move_figure[0].move(dest, b1, 0)
                    if not b1.is_black_in_chess_only():
                        eval = self.calculate_white_move(b1, alpha, beta)
                        #eval = self.evaluate_position(b1.getFigures())
                        self.positions = self.positions + 1
                        maxEval = max(maxEval, eval)
                        alpha = max(alpha, maxEval)
                        evals_movs.append([move_figure[0], dest])
                        evals.append(eval)
                    else:
                        pass
                    move_figure[0].pos[0] = pos[0]
                    move_figure[0].pos[1] = pos[1]
                    if len(evals) > 1 and (evals[-1] > evals[-2]) and b1.get_last_deleted() != 0:
                        #print('search',b1.get_last_deleted().pos[0], b1.get_last_deleted().pos[1])
                        b1.addFigure(b1.get_last_deleted())
                    if True:
                        if b1.get_last_deleted() != 0:
                            b1.addFigure(b1.get_last_deleted())
                    if beta < alpha:
                        print('break na razini 0',alpha,beta)
                        break
                        pass
            if beta < alpha:
                break
                pass
        #if b.queen_pos != 0:
            #b.QueenRemove()
        print(len(boards))

        print(evals_movs)
        print(evals)
        #b.print_board()
        print(len(b.getFigures()))
        if len(evals_movs) == 0 and b.is_black_in_chess_only():
            ctypes.windll.user32.MessageBoxW(0, "MAT", "ŠAH", 1)
            exit(0)
        if len(evals_movs) == 0 and not b.is_black_in_chess_only():
            ctypes.windll.user32.MessageBoxW(0, "STALEMATE", "ŠAH", 1)
            exit(0)
        print('konacni move',evals_movs[np.argmax(evals)][0], evals_movs[np.argmax(evals)][1])
        print('positions: ', self.positions)
        end_time = time.time()
        time = end_time - start_time
        print('positions/s :', self.positions / time)
        return evals_movs[np.argmax(evals)][0].move(evals_movs[np.argmax(evals)][1], b, 1)


    def evaluate_position(self,figures):
        eval = 0
        pawnEvalWhite = [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
            [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
            [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
            [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
            [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
            [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
        knightEval = [
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
            [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
            [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
            [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
            [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
            [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        ]
        bishopEvalWhite = [
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
            [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
            [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
            [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
            [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        ]
        rookEvalWhite = [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
        ]
        evalQueen = [
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
            [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
            [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
            [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        ]
        kingEvalWhite = [

            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
            [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
        ]
        for figure in figures:
            if figure.alliance == 'white':
                if figure.short == 'P':



                    eval = eval - 1


                    eval = eval + pawnEvalWhite[7 - figure.pos[1]][figure.pos[0]]



                if figure.short == 'N':
                    eval = eval - 3


                    eval = eval + knightEval[7 - figure.pos[1]][figure.pos[0]]


                if figure.short == 'B':

                    eval = eval - 3.5


                    eval = eval + bishopEvalWhite[7 - figure.pos[1]][figure.pos[0]]



                if figure.short == 'R':
                    eval = eval - 6


                    eval = eval + bishopEvalWhite[7 - figure.pos[1]][figure.pos[0]]

                if figure.short == 'Q':
                    eval = eval - 9


                    eval = eval + evalQueen[7 - figure.pos[1]][figure.pos[0]]

                if figure.short == 'K':
                    eval = eval - 100




                    eval = eval + kingEvalWhite[7 - figure.pos[1]][figure.pos[0]]
            else:
                if figure.short == 'p':
                    eval = eval + 1
                    eval = eval + list(reversed(pawnEvalWhite))[7 - figure.pos[1]][figure.pos[0]]
                if figure.short == 'n':
                    eval = eval + 3
                    eval = eval + knightEval[7 - figure.pos[1]][figure.pos[0]]
                if figure.short == 'b':
                    eval = eval + 3.5
                    eval = eval + list(reversed(bishopEvalWhite))[7 - figure.pos[1]][figure.pos[0]]
                if figure.short == 'r':
                    eval = eval + 6
                    eval = eval + list(reversed(rookEvalWhite))[7 - figure.pos[1]][figure.pos[0]]
                if figure.short == 'q':

                    eval = eval + 9
                    eval = eval + evalQueen[7 - figure.pos[1]][figure.pos[0]]
                if figure.short == 'k':
                    eval = eval + 100
                    eval = eval + list(reversed(kingEvalWhite))[7 - figure.pos[1]][figure.pos[0]]





















        return eval

    def calculate_white_move(self,b, alpha, beta):
        minEval = 200
        #eval = 0
        figures = b.getFigures()
        #print(len(figures), 'len')
        legal_moves = []
        for figure in figures:
            if figure.alliance == 'white':
                legs = figure.get_legal_moves(b)
                legal_moves.append([figure, legs])
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
                    move_figure[0].move(dest, b1,0)
                    if not b1.is_white_in_chess_only():
                        #print(move_figure[0], pos[0], pos[1], move, 'legalan potez')
                        eval = self.calculate_black_move(b1, alpha, beta)
                        #eval = self.evaluate_position(b1.getFigures())
                        self.positions = self.positions + 1
                        minEval = min(minEval, eval)
                        beta = min(beta, minEval)

                        #eval = calculate_white_move(b1)
                        # b1.print_board()
                        # print(len(b1.getFigures()))
                        # print(b1.getFigures())
                        # print(eval, 'eval je a dest je ', dest)
                        #evals_movs.append([move_figure[0], dest])
                        evals.append(eval)
                    else:
                        pass

                    move_figure[0].pos[0] = pos[0]
                    move_figure[0].pos[1] = pos[1]
                    if len(evals) > 1 and (evals[-1] < evals[-2]) and b1.get_last_deleted() != 0:
                        #print('search',b1.get_last_deleted().pos[0], b1.get_last_deleted().pos[1])
                        b1.addFigure(b1.get_last_deleted())
                    if True:
                        if b1.get_last_deleted() != 0:
                            b1.addFigure(b1.get_last_deleted())
                    if beta < alpha:
                        print('break na razini 1', alpha, beta, eval)
                        break
                        pass
            if beta < alpha:
                break
                pass

        #print(len(boards))

        #print(evals_movs, evals)
        #print(evals[0])
        #b.print_board()
        if len(evals) == 0:
            evals.append(100)
        if b1.queen_pos != 0:
            b1.QueenRemove()
        #print(len(b.getFigures()))
        #print('konacni move',evals_movs[np.argmin(evals)][0], evals_movs[np.argmin(evals)][1])
        #return evals[np.argmin(evals)]
        return minEval


    def calculate_black_move(self,b, alpha, beta):
        maxEval = -200
        #eval = 0
        figures = b.getFigures()
        # print(len(figures), 'len')
        legal_moves = []
        for figure in figures:
            if figure.alliance == 'black':
                legs = figure.get_legal_moves(b)
                legal_moves.append([figure, legs])
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
                    # print('radim move', move, move_figure[0], pos)
                    dest = [pos[0] + move[0], pos[1] + move[1]]
                    move_figure[0].move(dest, b1, 0)
                    if not b1.is_black_in_chess_only():
                        # print(move_figure[0], pos[0], pos[1], move, 'legalan potez')
                        eval = self.evaluate_position(b1.getFigures())
                        #eval = self.calculate_white_move2(b1, alpha, beta)
                        self.positions = self.positions + 1
                        maxEval = max(maxEval, eval)
                        alpha = max(alpha, maxEval)

                # eval = calculate_white_move(b1)
                        # b1.print_board()
                        # print(len(b1.getFigures()))
                        # print(b1.getFigures())
                        # print(eval, 'eval je a dest je ', dest)
                        # evals_movs.append([move_figure[0], dest])
                        evals.append(eval)
                    else:
                        # print(move_figure[0], move, 'otpao')
                        pass

                    move_figure[0].pos[0] = pos[0]
                    move_figure[0].pos[1] = pos[1]
                    if len(evals) > 1 and (evals[-1] > evals[-2]) and b1.get_last_deleted() != 0:
                        # print('search',b1.get_last_deleted().pos[0], b1.get_last_deleted().pos[1])
                        b1.addFigure(b1.get_last_deleted())
                    if True:
                        if b1.get_last_deleted() != 0:
                            b1.addFigure(b1.get_last_deleted())
                    if beta < alpha:
                        break
                        print('break na razini 2', alpha, beta)
                        pass
            if beta < alpha:
                break
                pass

        #print(len(boards))

        # print(evals_movs, evals)
        # print(evals[0])
        # b.print_board()
        if len(evals) == 0:
            evals.append(-100)
        if b1.queen_pos != 0:
            b1.QueenRemove()
        #print(len(b.getFigures()))
        # print('konacni move',evals_movs[np.argmin(evals)][0], evals_movs[np.argmin(evals)][1])
        #return evals[np.argmax(evals)]
        return maxEval


    def calculate_white_move2(self,b, alpha, beta):
        eval = 0
        minEval = 200
        figures = b.getFigures()
        # print(len(figures), 'len')
        legal_moves = []
        for figure in figures:
            if figure.alliance == 'white':
                legs = figure.get_legal_moves(b)
                legal_moves.append([figure, legs])
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
                    # print('radim move', move, move_figure[0], pos)
                    dest = [pos[0] + move[0], pos[1] + move[1]]
                    move_figure[0].move(dest, b1,0)
                    if not b1.is_white_in_chess_only():
                        # print(move_figure[0], pos[0], pos[1], move, 'legalan potez')
                        eval = self.evaluate_position(b1.getFigures())
                        self.positions = self.positions + 1
                        minEval = min(minEval, eval)
                        beta = min(beta, minEval)
                        # eval = calculate_white_move(b1)
                        # b1.print_board()
                        # print(len(b1.getFigures()))
                        # print(b1.getFigures())
                        # print(eval, 'eval je a dest je ', dest)
                        # evals_movs.append([move_figure[0], dest])
                        evals.append(eval)
                    else:
                        # print(move_figure[0], move, 'otpao')
                        pass

                    move_figure[0].pos[0] = pos[0]
                    move_figure[0].pos[1] = pos[1]
                    if len(evals) > 1 and (evals[-1] < evals[-2]) and b1.get_last_deleted() != 0:
                        # print('search',b1.get_last_deleted().pos[0], b1.get_last_deleted().pos[1])
                        b1.addFigure(b1.get_last_deleted())
                    if True:
                        if b1.get_last_deleted() != 0:
                            b1.addFigure(b1.get_last_deleted())
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break

        #print(len(boards))

        # print(evals_movs, evals)
        # print(evals[0])
        # b.print_board()
        if len(evals) == 0:
            evals.append(100)
        if b1.queen_pos != 0:
            b1.QueenRemove()
        #print(len(b.getFigures()))
        # print('konacni move',evals_movs[np.argmin(evals)][0], evals_movs[np.argmin(evals)][1])
        return evals[np.argmin(evals)]