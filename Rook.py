from Figure import Figure
class Rook():

    def __init__(self, pos, alliance, short):
        self.pos = pos
        self.alliance = alliance
        self.short = short

        self.is_defended = False

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
        self.is_defended = False
        legal_moves = []

        # for 4 dimensions
        move = [0, 0]
        while True:
            move[0] = move[0] + 1
            #print(self.pos, move)
            if not b.is_the_piece_on_the_board(self.pos, move):
                break

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            #p3#rint('tile rook', tile)
            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                    break
                else:
                    tile.is_defended = True
                    break
        #print(legal_moves)
        move = [0, 0]
        while True:
            move[1] = move[1] + 1
            if not b.is_the_piece_on_the_board(self.pos, move):
                break

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            #print('tile rook', tile)
            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                    break
                else:
                    tile.is_defended = True
                    break
        #print(legal_moves ,' roook')
        move = [0, 0]
        while True:
            move[0] = move[0] - 1
            if not b.is_the_piece_on_the_board(self.pos, move):
                break

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            #print('tile rook', tile)

            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                    break
                else:
                    tile.is_defended = True
                    break
        #print(legal_moves)
        move = [0, 0]
        while True:
            move[1] = move[1] - 1
            if not b.is_the_piece_on_the_board(self.pos, move):
                break

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            #print('tile rook', tile)
            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                    break
                else:
                    tile.is_defended = True
                    break

        return legal_moves


    def castle(self,b, long):
        if self.alliance == 'white':
            if long == 0:
                b.removeFigure(self)
                self.pos[0] = 0
                self.pos[1] = 5
                b.addFigure(self)
            else:
                b.removeFigure(self)
                self.pos[0] = 0
                self.pos[1] = 2
                b.addFigure(self)
        else:
            if long == 0:
                b.removeFigure(self)
                self.pos[0] = 7
                self.pos[1] = 5
                b.addFigure(self)
            else:
                b.removeFigure(self)
                self.pos[0] = 7
                self.pos[1] = 2
                b.addFigure(self)


    def move(self, dest, b, top):
        legal_moves = self.get_legal_moves(b)

        move = [0, 0]

        #print(legal_moves)


        move[0] = dest[0] - self.pos[0]
        move[1] = dest[1] - self.pos[1]
        #print(dest, self.pos, move, 'konacni move')
        if move in legal_moves:

            if b.getFigure_pos(dest) != None:
                #print('Attacking move')
                b.saveFigure(dest)
                b.removeFigure_pos(dest)
            else:
                b.saveFigure(0)



            b.removeFigure(self)
            self.pos[0] = self.pos[0] + move[0]
            self.pos[1] = self.pos[1] + move[1]
            b.addFigure(self)
        #print(self.pos)
        return 1