from Figure import Figure
from King import King
from Queen import Queen
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
import copy
from Pawn import Pawn


class Board():
    figures = []

    last_deleted = 0
    queen_pos = 0
    queen_alliance = 0

    def QueenAdd(self, pos, alliance):
        self.queen_pos = pos
        self.queen_alliance = alliance
        #print('queen add')

    def QueenRemove(self):
        self.removeFigure_pos(self.queen_pos)
        self.addFigure((Pawn(self.queen_pos, self.queen_alliance, 'P' if self.queen_alliance == 'white' else 'p')))
        self.queen_pos = 0
        #print('queen remove')

    def get_last_deleted(self):
        #print('last del', self.last_deleted)
        return self.last_deleted

    def getFigures(self):
        return self.figures

    def removeFigure_pos(self, pos):

        for figure in self.figures:
            if figure.pos == pos:
                # if figure.short == 'k' or figure.short == 'K':
                # return None
                self.figures.remove(figure)
                self.board[figure.getPos()[0]][figure.getPos()[1]] = '_'

    def saveFigure(self, dest):
        if dest == 0:
            self.last_deleted = 0
        else:
            for figure in self.figures:
                if figure.pos == dest:
                    self.last_deleted = figure

    def removeFigure(self, Figure):
        # if Figure.short == 'k' or Figure.short == 'K':
        # return None
        #print(Figure in self.getFigures(),self.is_the_piece_on_the_board_pos(Figure.pos) )

        if Figure in self.getFigures() and self.is_the_piece_on_the_board_pos(Figure.pos):
            self.figures.remove(Figure)
            #print('succesful remove', Figure)
            self.board[Figure.getPos()[0]][Figure.getPos()[1]] = '_'
        else:
            #print('no such figure',Figure, Figure.pos)
            pass

    def addFigure(self, Figure):
        for figure in self.figures:
            if figure.pos == Figure.pos and figure.short == Figure.short:
                #print(figure.pos, Figure,' nije uspio add')
                if Figure.short == 'K' or Figure.short == 'k':
                    if self.board[Figure.getPos()[0]][Figure.getPos()[1]] != Figure.short:
                        self.board[Figure.getPos()[0]][Figure.getPos()[1]] = Figure.short

                return None

        if self.is_the_piece_on_the_board_pos(Figure.pos):
            self.board[Figure.getPos()[0]][Figure.getPos()[1]] = Figure.short
            self.figures.append(Figure)
            #print('uspio add', Figure)

            return Figure
        return None

    def __init__(self):
        self.board = x = [['_' for i in range(8)] for j in range(8)]

        self.addFigure(King([0, 4], 'white', 'K'))
        self.addFigure(King([7, 4], 'black', 'k'))

        self.addFigure(Queen([0, 3], 'white', 'Q'))
        self.addFigure(Queen([7, 3], 'black', 'q'))

        self.addFigure(Bishop([0, 2], 'white', 'B'))
        self.addFigure(Bishop([0, 5], 'white', 'B'))

        self.addFigure(Knight([0, 1], 'white', 'N'))
        self.addFigure(Knight([0, 6], 'white', 'N'))

        self.addFigure(Rook([0, 7], 'white', 'R'))
        self.addFigure(Rook([0, 0], 'white', 'R'))

        self.addFigure(Bishop([7, 2], 'black', 'b'))
        self.addFigure(Bishop([7, 5], 'black', 'b'))

        self.addFigure(Knight([7, 1], 'black', 'n'))
        self.addFigure(Knight([7, 6], 'black', 'n'))

        self.addFigure(Rook([7, 7], 'black', 'r'))
        self.addFigure(Rook([7, 0], 'black', 'r'))

        self.addFigure(Pawn([1, 0], 'white', 'P'))
        self.addFigure(Pawn([1, 1], 'white', 'P'))
        self.addFigure(Pawn([1, 2], 'white', 'P'))
        self.addFigure(Pawn([1, 3], 'white', 'P'))
        self.addFigure(Pawn([1, 4], 'white', 'P'))
        self.addFigure(Pawn([1, 5], 'white', 'P'))
        self.addFigure(Pawn([1, 6], 'white', 'P'))
        self.addFigure(Pawn([1, 7], 'white', 'P'))

        self.addFigure(Pawn([6, 0], 'black', 'p'))
        self.addFigure(Pawn([6, 1], 'black', 'p'))
        self.addFigure(Pawn([6, 2], 'black', 'p'))
        self.addFigure(Pawn([6, 3], 'black', 'p'))
        self.addFigure(Pawn([6, 4], 'black', 'p'))
        self.addFigure(Pawn([6, 5], 'black', 'p'))
        self.addFigure(Pawn([6, 6], 'black', 'p'))
        self.addFigure(Pawn([6, 7], 'black', 'p'))

    def print_board(self):
        for i in range(8):
            print(8 - i, self.board[8 - i - 1])
        print('  - A    B    C    D    E    F    G    H -')

    def getFigure_short(self, short):
        for figure in self.figures:
            if figure.short == short:
                return figure

    def getFigure_pos(self, pos=[]):
        # print(pos, 'trazim fig na ovoj pos')
        # pos[1] = pos[1] - 1
        for figure in self.figures:
            if figure.pos == pos:
                return figure
        # print('none?')
        return None

    def getTile(self, pos):
        if (pos[0] < 7 and pos[0] > 0 and pos[1] < 7 and pos[1] > 0) and self.board[pos[0]][pos[1]] == '_':
            return '_'
        for figure in self.figures:
            if figure.pos == pos:
                return figure
        return '_'

    def is_the_piece_on_the_board(self, pos, mov):
        if (pos[0] + mov[0] < 0 or pos[0] + mov[0] > 7):
            return False
        if (pos[1] + mov[1] < 0 or pos[1] + mov[1] > 7):
            return False
        return True

    def is_the_piece_on_the_board_pos(self, pos, ):
        if (pos[0] < 0 or pos[0] > 7):
            return False
        if (pos[1] < 0 or pos[1] > 7):
            return False
        return True

    def is_black_in_chess_only(self):
        king_pos = self.getFigure_short('k').pos
        moves = []
        figures_chessing = []
        for figure in self.figures:
            if figure.alliance == 'white':
                moves.append([figure, figure.get_legal_moves(self)])
        # print(moves)
        for move1 in moves:
            # print(move1[1], 'mov')
            for move in move1[1]:

                # print(move, 'move')
                if [move1[0].pos[0] + move[0], move1[0].pos[1] + move[1]] == king_pos:
                    # print('ŠAH!')
                    # figures_chessing.append(move1[0])
                    return True

        return False

    def is_black_in_chess(self):
        king_pos = self.getFigure_short('k').pos
        moves = []
        saving_moves = []
        figures_chessing = []
        for figure in self.figures:
            if figure.alliance == 'white':
                moves.append([figure, figure.get_legal_moves(self)])
        # print(moves)
        for move1 in moves:
            # print(move1[0], move1[1], 'mov1')
            for move in move1[1]:

                # print(move, 'move1')
                if [move1[0].pos[0] + move[0], move1[0].pos[1] + move[1]] == king_pos:
                    #print('ŠAH!')
                    figures_chessing.append(move1[0])
                    # self.is_mate_black(figures_chessing)
                    saving_moves = self.get_saving_moves(figures_chessing)

                    # print('saves: ', saving_moves)
        return saving_moves

    def is_mate_black(self, figs):
        # print('figs chessing: ',figs)
        king = self.getFigure_short('k')
        saving_move = []
        if king.get_legal_moves(self) == []:
            ## print('tu smo')
            if len(figs) == 1:
                if figs[0].is_under_attack(self):
                    # nije mat
                    return 0
                    # dali se netko može stat ispred
                    figs = self.getFigures()

                else:
                    # dali se netko može postaviti ispred figure?
                    # print('jesam li uopće tu')
                    black_figs = []
                    for fig in figs:
                        if fig.alliance == 'black':
                            black_figs.append(fig)

                    movs = []

                    for fig in black_figs:
                        movs.append([fig, fig.get_legal_moves(self)])
                    # print()
                    for mov in movs:
                        b1 = copy.deepcopy(self)
                        pos = [mov[0].pos[0], mov[0].pos[1]]
                        mov[0].move([mov[0].pos[0] + mov[1][0], mov[0].pos[1] + mov[1][1]], b1, 0)
                        if b1.get_last_deleted() != 0:
                            # print('addam',b1.get_last_deleted())
                            b1.get_last_deleted()
                            # print('što bi',b1.addFigure(b1.get_last_deleted()))
                        # print(len(b1.getFigures()))
                        if not b1.is_black_in_chess_only():
                            return 0
                        mov[0].pos[0] = pos[0]
                        mov[0].pos[1] = pos[1]

                    print('MATT!!!!!')
                    # exit(0)
                    return 1
            else:
                print('MAT!!!!!!')
                # exit(0)
                return 1

            print('mat')
            # exit(0)
            return 1
        else:
            print('tu sam')
            return 0

    def get_saving_moves(self, figs_chessing):
        # ili kraljevi potezi, ili potezi koji pojedu ili potezi koji blokiraju
        king = self.getFigure_short('k')
        ret = []
        # for move in king.get_legal_moves(self):
        # ret.append([king, [[move[0], move[1]]]])
        fig = figs_chessing[0]
        black_figs = []
        figs = self.getFigures()
        saving_move = []
        for fig in figs:
            if fig.alliance == 'black':
                black_figs.append(fig)

        movs = []

        for fig in black_figs:
            movs.append([fig, fig.get_legal_moves(self)])
        # print('moguci',movs)
        for mov in movs:
            b1 = copy.deepcopy(self)
            pos = [0, 0]
            pos[0] = mov[0].pos[0]
            pos[1] = mov[0].pos[1]
            # print('mov',mov)
            if len(mov[1]) > 0:
                for mov2 in mov[1]:
                    mov[0].pos[0] = pos[0]
                    mov[0].pos[1] = pos[1]

                    mov[0].move([pos[0] + mov2[0], pos[1] + mov2[1]], b1, 0)

                    if not b1.is_black_in_chess_only():
                        ret.append([mov[0], [[mov2[0], mov2[1]]]])
                        # print('saveee',mov[0], mov[0].pos[0] + mov2[0], mov[0].pos[1], 'saving_move')

                    # print(len(b1.getFigures()))
                    if b1.get_last_deleted() != 0:
                        # print('addam',b1.get_last_deleted())
                        b1.addFigure(b1.get_last_deleted())
                        # print('što bi',b1.addFigure(b1.get_last_deleted()))
                    # print(len(b1.getFigures()))
                    mov[0].pos[0] = pos[0]
                    mov[0].pos[1] = pos[1]

        return ret

    def is_white_in_chess(self):
        king_pos = self.getFigure_short('K').pos
        moves = []
        saving_moves = []
        figures_chessing = []
        for figure in self.figures:
            if figure.alliance == 'black':
                moves.append([figure, figure.get_legal_moves(self)])
        for move1 in moves:
            for move in move1[1]:

                if [move1[0].pos[0] + move[0], move1[0].pos[1] + move[1]] == king_pos:
                    #print('ŠAH!')
                    figures_chessing.append(move1[0])
                    #self.is_mate_white(figures_chessing)
                    saving_moves = self.get_saving_moves_white(figures_chessing)

        return saving_moves

    def is_white_in_chess_only(self):
        king_pos = self.getFigure_short('K').pos
        moves = []
        saving_moves = []
        figures_chessing = []
        for figure in self.figures:
            if figure.alliance == 'black':
                moves.append([figure, figure.get_legal_moves(self)])
        # print(moves)
        for move1 in moves:
            # print(move1[0], move1[1], 'mov1')
            for move in move1[1]:

                # print(move, 'move1')
                if [move1[0].pos[0] + move[0], move1[0].pos[1] + move[1]] == king_pos:
                    #print('ŠAH!')
                    # figures_chessing.append(move1[0])
                    # self.is_mate_white(figures_chessing)
                    # saving_moves = self.get_saving_moves(figures_chessing)
                    return True
                    # print('saves: ', saving_moves)
        return False

    def is_mate_white(self, figs):  # mat je ako kralj nema poteza, i figura se nemože napast ili blokirati
        my_figs = []
        boards = []

        i = 0
        # print('mat? board')
        # self.print_board()
        for fig in self.getFigures():
            if fig.alliance == 'white':
                my_figs.append(fig)
        ret = 1
        i = 0
        boards.append(copy.deepcopy(self))
        b1 = boards[i]
        for fig in my_figs:
            movs = fig.get_legal_moves(b1)
            pos = [0, 0]
            pos[0] = fig.pos[0]
            pos[1] = fig.pos[1]
            for move in movs:
                boards.append(copy.deepcopy(self))
                i = i + 1
                b1 = boards[i]
                fig.move([pos[0] + move[0], pos[1] + move[1]], b1,0)
                #print('move3', move, fig)
                b1.print_board()
                if not b1.is_white_in_chess_only():
                    # print('nije mat za potez', fig, move)
                    ret = 0
                fig.pos[0] = pos[0]
                fig.pos[1] = pos[1]
                if b1.get_last_deleted() != 0:
                    b1.addFigure(b1.get_last_deleted())

        if ret == 1:
            print('MAT')
            # exit(0)
            return True

        # king = self.getFigure_short('K')
        # king_moves = king.get_legal_moves(self)
        # print('king moves in chess', king_moves)
        # if len(figs) == 1 and len(king_moves) == 0:
        #     if figs[0].is_under_attack(self):
        #         # nije mat
        #         return 0
        #     else:
        #         # dali se netko može postaviti ispred figure?
        #         print('jesam li uopće tu')
        #         white_figs = []
        #         for fig in figs:
        #             if fig.alliance == 'white':
        #                 white_figs.append(fig)
        #
        #         movs = []
        #
        #         for fig in white_figs:
        #             movs.append([fig, fig.get_legal_moves(self)])
        #         print()
        #         for mov in movs:
        #             b1 = copy.deepcopy(self)
        #             pos = [mov[0].pos[0], mov[0].pos[1]]
        #             mov[0].move([mov[0].pos[0] + mov[1][0], mov[0].pos[1] + mov[1][1]], b1)
        #
        #             if not b1.is_white_in_chess_only():
        #                 return 0
        #             if b1.get_last_deleted() != 0:
        #                 print('addam', b1.get_last_deleted())
        #                 print('što bi', b1.addFigure(b1.get_last_deleted()))
        #             print(len(b1.getFigures()))
        #
        #             mov[0].pos[0] = pos[0]
        #             mov[0].pos[1] = pos[1]
        #
        #         print('MATT!!!!!')
        #         exit(0)
        #         return 1
        #
        # else:
        #     if len(figs) > 1 and len(king_moves) == 0:
        #         print('MATT!!!!')
        #         exit(0)
        #     else:
        #         return 0

    def get_saving_moves_white(self, figs_chessing):
        # ili kraljevi potezi, ili potezi koji pojedu ili potezi koji blokiraju
        king = self.getFigure_short('K')
        ret = []
        # for move in king.get_legal_moves(self):
        # ret.append([king, [[move[0], move[1]]]])
        # fig = figs_chessing[0]
        white_figs = []
        figs = self.getFigures()
        saving_move = []
        for fig in figs:
            if fig.alliance == 'white':
                white_figs.append(fig)

        movs = []

        for fig in white_figs:
            movs.append([fig, fig.get_legal_moves(self)])
        # print('moguci',movs)
        for mov in movs:
            b1 = copy.deepcopy(self)
            pos = [0, 0]
            pos[0] = mov[0].pos[0]
            pos[1] = mov[0].pos[1]
            # print('mov',mov)
            if len(mov[1]) > 0:
                for mov2 in mov[1]:

                    mov[0].move([pos[0] + mov2[0], pos[1] + mov2[1]], b1,0)

                    if not b1.is_white_in_chess_only():
                        ret.append([mov[0], [[mov2[0], mov2[1]]]])
                        # print('saveee whitee',mov[0], mov[0].pos[0] + mov2[0], mov[0].pos[1], 'saving_move')

                    # print(len(b1.getFigures()))
                    if b1.get_last_deleted() != 0:
                        #print('addam',b1.get_last_deleted())
                        b1.addFigure(b1.get_last_deleted())
                        # print('što bi',b1.addFigure(b1.get_last_deleted()))
                    # print(len(b1.getFigures()))
                    mov[0].pos[0] = pos[0]
                    mov[0].pos[1] = pos[1]

        return ret
