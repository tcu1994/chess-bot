from Figure import Figure
class Pawn():

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

        move = [0, 0]

        if self.alliance == 'white':
            move = [1, 0]
            if b.is_the_piece_on_the_board(self.pos, move):
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                #print(tile, self.pos + move)
                if tile == '_':
                    legal_moves.append(move[:])

            if self.pos[0] == 1:
                move = [2, 0]
                tile0 = b.getTile([self.pos[0] + move[0] - 1, self.pos[1] + move[1]])
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                if tile == '_' and tile0 == '_':
                    legal_moves.append(move[:])

            move = [1, 1]
            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            if tile != '_':
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                elif isinstance(tile, Figure):
                    tile.is_defended = True

            move = [1, -1]
            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            if tile != '_':
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                elif isinstance(tile, Figure):
                    tile.is_defended = True

            #print(legal_moves)
        else:
            move = [-1, 0]
            if b.is_the_piece_on_the_board(self.pos, move):
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                #print(tile, self.pos + move)
                if tile == '_':
                    legal_moves.append(move[:])

            if self.pos[0] == 6:
                move = [-2, 0]
                tile0 = b.getTile([self.pos[0] + move[0] + 1, self.pos[1] + move[1]])
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                if tile == '_' and tile0 == '_':
                    legal_moves.append(move[:])

            move = [-1, -1]
            if b.is_the_piece_on_the_board(self.pos, move):
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                if tile != '_':
                    if tile.alliance != self.alliance:
                        legal_moves.append(move[:])
                    elif isinstance(tile, Figure):
                        tile.is_defended = True

            move = [-1, 1]
            if b.is_the_piece_on_the_board(self.pos, move):
                tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
                #print('blabla',[self.pos[0] + move[0], self.pos[1] + move[1]],tile)

                if tile != '_':
                    if tile.alliance != self.alliance:
                        #print('jel tu')
                        legal_moves.append(move[:])
                elif isinstance(tile, Figure):
                        tile.is_defended = True

        return legal_moves


    def move(self, dest, b, top):
        move = [0,0]
        legal_moves = self.get_legal_moves(b)
        move[0] = dest[0] - self.pos[0]
        move[1] = dest[1] - self.pos[1]
        #print(dest, self.pos, move, 'konacni move')
        #print(legal_moves, 'leg moves pawn')
        if move in legal_moves:

            if b.getFigure_pos(dest) != None:
                #print('Attacking move')
                b.saveFigure(dest)
                b.removeFigure_pos(dest)


            else:
                #print('normal move')
                b.saveFigure(0)
            b.removeFigure_pos(self.pos)
            self.pos[0] = self.pos[0] + move[0]
            self.pos[1] = self.pos[1] + move[1]
            b.addFigure(self)
        if self.pos[0] == 7 and self.alliance == 'white' or self.pos[0] == 0 and self.alliance == 'black':
            #inp = input('Choose promotion figure; Q, R, B, N:')
            b.removeFigure_pos(self.pos)
            from Queen import Queen
            if self.alliance == 'white':
                b.addFigure(Queen(self.pos, 'white', 'Q'))
                if top == 0:
                    b.QueenAdd(self.pos, 'white')
            else:
                b.addFigure(Queen(self.pos, 'black', 'q'))
                if top == 0:
                    b.QueenAdd(self.pos, 'black')
        return 1