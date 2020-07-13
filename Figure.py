class Figure():
    def __init__(self, pos, alliance,short):
        self.pos = pos
        self.alliance = alliance
        self.short = short
        self.is_defended = False

    def move(self, dest, b, top):
        pass
    def is_under_attack(self,b):
        figs = b.getFigures()
        opp_figs = []
        for fig in figs:
            if fig.alliance != self.alliance:
                opp_figs.append(fig)

        for fig in opp_figs:
            for move in fig.get_legal_moves():
                if [fig.pos[0] + move[0], fig.pos[1] + move[1]] == self.pos:
                    return 1

        return 0
