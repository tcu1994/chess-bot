from Figure import Figure
import copy
class King():

    def __init__(self, pos, alliance, short,):
        self.pos = pos
        self.alliance = alliance
        self.short = short
        self.possible_moves = [[1, 1], [0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]

    def is_under_attack(self,b):
        figs = b.getFigures()
        opp_figs = []
        for fig in figs:
            if fig.alliance != self.alliance:
                opp_figs.append(fig)

        for fig in opp_figs:
            for move in fig.get_legal_moves(b):
                if [fig.pos[0] + move[0], fig.pos[1] + move[1]] == self.pos:
                    return 1

        return 0
    def getPos(self):
        return self.pos

    def get_legal_moves(self, b):
        #print('getam legalne od', self.short, ' od pozicije', self.pos[0], self.pos[1])
        #b.print_board()
        legal_moves = []

        self.possible_moves = [[1, 1], [0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]

        for move in self.possible_moves:
            if not b.is_the_piece_on_the_board(self.pos, move):
                continue

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            if b.is_the_piece_on_the_board(self.pos, move):

                if tile == '_':
                    legal_moves.append(move[:])
                else:
                    if tile.alliance != self.alliance :
                        legal_moves.append(move[:])
                    else:
                        tile.is_defended = True


        pos = [0,0]
        pos[0] = self.pos[0]
        pos[1] = self.pos[1]


        figures = b.getFigures()
        opposite_figures = []
        for figure in figures:
            if figure.alliance != self.alliance:
                opposite_figures.append(figure)

        opposite_moves = []
        for figure in opposite_figures:
            moves = []
            if figure.short == 'K' or figure.short == 'k':
                moves.append(figure.get_legal_moves_short(b))

            else:
                moves.append(figure.get_legal_moves(b))
                if figure.short == 'P':
                    moves[0].append([1, -1])
                    moves[0].append([1, 1])
                    if [1,0] in moves[0]:
                        moves[0].remove([1,0])
                    if [2,0] in moves[0]:
                        moves[0].remove([2,0])
                if figure.short == 'p':
                    moves[0].append([-1, -1])
                    moves[0].append([-1, 1])
                    if [-1,0] in moves[0]:
                        moves[0].remove([-1,0])
                    if [-2,0] in moves[0]:
                        moves[0].remove([-2,0])

            #print(moves, 'moves of ', figure)
            if moves != [[]]:
                for i,move in enumerate(moves[0]):
                    #print([figure, [figure.pos[0] + move[0], figure.pos[1] + move[1]]], 'move')
                    opposite_moves.append([figure, [figure.pos[0] + move[0], figure.pos[1] + move[1]]])

        if self.short == 'K' and not b.is_white_in_chess_only():
            #print(self.pos,b.getFigure_pos([0,7]),b.getFigure_pos([0,5]), b.getFigure_pos([0,6]) is None)
            if self.pos == [0,4] and b.getFigure_pos([0,7]) != 'None' and  b.getFigure_pos([0,5]) is None and b.getFigure_pos([0,6]) is None:
                if b.getFigure_pos([0,7]).short == 'R':
                    #print('ADDAN ROKADA')
                    legal_moves.append([0,2])

            if self.pos == [0,4] and b.getFigure_pos([0,0]) is not  None and  b.getFigure_pos([0,3]) is None and b.getFigure_pos([0,2]) is None and b.getFigure_pos([0,1]) is None:
                if b.getFigure_pos([0,0]).short == 'R':
                    #print('ADDAN ROKADA')
                    legal_moves.append([0,-3])














        #print(opposite_moves, 'opp move')
        #print(legal_moves, 'leg')
        legal_moves0 = copy.deepcopy(legal_moves)
        for move in legal_moves:
            for opp_move in opposite_moves:
                val =[self.pos[0] + move[0], self.pos[1] + move[1]]
                #print(val, opp_move, 'KINGARA')

                if opp_move[1] == val:
                    #print(self.short,' king ipak nemoze', val, move)
                    if move in legal_moves0:
                        legal_moves0.remove(move)
                if (b.getFigure_pos(val) != None) and (b.getFigure_pos(val).is_defended):
                    #print(val, 'je branjena, king nemoze tu')
                    if move in legal_moves0:
                        legal_moves0.remove(move)
                opp_king = b.getFigure_short('k' if self.alliance == 'white' else 'K')

                if abs(opp_king.pos[0] - val[0]) < 2 and abs(opp_king.pos[1] - val[1]) < 2:
                    #print('kings cant be that close')
                    if move in legal_moves0:
                        legal_moves0.remove(move)
        #print('king leg', legal_moves)
        return legal_moves0



    def get_legal_moves_short(self, b):
        legal_moves = []
        possible_moves = [[1, 1], [0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]

        for move in possible_moves:
            if not b.is_the_piece_on_the_board(self.pos, move):
                continue

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])

            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])

        return legal_moves
    def move(self, dest,b, top):

        legal_moves = self.get_legal_moves(b)
        move = [0,0]

        move[0] = dest[0] - self.pos[0]
        move[1] = dest[1] - self.pos[1]



        if move in legal_moves:
            if b.getFigure_pos(dest) != None:
                #print('Attacking move')
                b.saveFigure(dest)
                b.removeFigure_pos(dest)
            else:
                b.saveFigure(0)


            b.removeFigure(self)
            #pos = [0,0]
            #pos[0] = self.pos[0]
            #pos[1] = self.pos[1]
            self.pos[0] = self.pos[0] + move[0]
            self.pos[1] = self.pos[1] + move[1]
            b.addFigure(self)

            if self.short == 'K':
                if move == [0, 2] and top == 1:
                    rook = b.getFigure_pos([0, 7])
                    print('rokada', rook)
                    rook.castle(b,0)
                if move == [0, -3] and top == 1:
                    rook = b.getFigure_pos([0, 0])
                    print('rokada', rook)
                    rook.castle(b, 1)

            if self.short == 'k':
                if move == [0, 2] and top == 1:
                    rook = b.getFigure_pos([7, 7])
                    print('rokada', rook)
                    rook.castle(b,0)
                if move == [0, -3] and top == 1:
                    rook = b.getFigure_pos([7, 0])
                    print('rokada', rook)
                    rook.castle(b, 1)

            return 1
        else: return 0