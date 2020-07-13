from Figure import Figure
class Knight():

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

    def get_legal_moves(self,b):
        self.is_defended = False
        legal_moves = []
        # if first or last col

        possible_moves = [[2, -1], [2, 1], [1, 2], [ -1, 2], [-2, 1], [-2, -1], [1, -2],[-1, -2]]
        for move in possible_moves:
            if not b.is_the_piece_on_the_board(self.pos, move):
                continue

            tile = b.getTile([self.pos[0] + move[0], self.pos[1] + move[1]])
            #print('tajlam',tile)
            if tile == '_':
                legal_moves.append(move[:])
            else:
                if tile.alliance != self.alliance:
                    legal_moves.append(move[:])
                else:
                    tile.is_defended = True

        return legal_moves

    def move(self, dest, b, top):
        self.is_defended = False
        move = [0,0]
        legal_moves = self.get_legal_moves(b)
        move[0] = dest[0] - self.pos[0]
        move[1] = dest[1] - self.pos[1]
        #print(dest, self.pos, move, 'konacni move')
        if move in legal_moves:

            if b.getFigure_pos(dest) != None:
                #print('Attacking move')
                b.saveFigure(dest)
                b.removeFigure_pos(dest)
            else:
                #print('normal move')
                b.saveFigure(0)
            b.removeFigure(self)
            self.pos[0] = self.pos[0] + move[0]
            self.pos[1] = self.pos[1] + move[1]
            b.addFigure(self)
            return 1
        #print(self.pos)
        return 0