import pygame
from Board import Board
import math
from AI2 import *
import os
pygame.init()
print(os.environ['PATH'])
display_width = 400
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ŠAH')

black = (100,100,100)
white = (255,255,255)


saves = []
def render_img(x,y, name):
    render = pygame.image.load(name)
    gameDisplay.blit( render, (x,y))
    return render

run = True
gameDisplay.fill(white)
rects = []
color = white
def draw_rects():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = white
            else:
                color = black
            #print(i * 50, j * 50, color)
            rect = pygame.draw.rect(gameDisplay, color, (j * 50, i * 50, 50, 50))
            pygame.display.update()
            rects.append(rect)

def black_to_move(saves = None, forbidden_move = None):
    AI22 = AI2()
    return AI22.calculate(board, saves, forbidden_move)








board = Board()
def draw_board():
    draw_rects()
    figures = board.getFigures()
    print(len(figures))
    for figure in figures:
        name = ''
        if figure.short == 'k':
            name = 'images/bking.png'
        if figure.short == 'q':
            name = 'images/bqueen.png'
        if figure.short == 'p':
            name = 'images/bpawn.png'
        if figure.short == 'b':
            name = 'images/bbishop.png'
        if figure.short == 'n':
            name = 'images/bknight.png'
        if figure.short == 'r':
            name = 'images/brook.png'
        if figure.short == 'K':
            name = 'images/wking.png'
        if figure.short == 'Q':
            name = 'images/wqueen.png'
        if figure.short == 'R':
            name = 'images/wrook.png'
        if figure.short == 'B':
            name = 'images/wbishop.png'
        if figure.short == 'N':
            name = 'images/wknight.png'
        if figure.short == 'P':
            name = 'images/wpawn.png'

        if figure.short == board.board[figure.pos[0]][figure.pos[1]]:
            render_img( figure.pos[1] * 50, 350 - figure.pos[0] * 50, name)
        if figure.short == 'Q':
            print('QUEEN ON ', figure.pos)

    pygame.display.update()

flag = 0
figure = None
draw_board()
while run:
    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            #print('klik')
            # Set the x, y postions of the mouse click
            x, y = event.pos

            for rect in rects:

                if rect.collidepoint(x, y):

                    #print('kolko ide u ovo')
                    #print('clicked on tile ',7-  math.trunc(y  / 50), math.trunc(x / 50))
                    if not board.getFigure_pos([7-  math.trunc(y  / 50), math.trunc(x / 50)]):
                        if figure is None:
                            break
                        else:
                            #draw_board()
                            if len(saves) > 0:
                                if [figure, [[7 - math.trunc(y / 50) - figure.pos[0], math.trunc(x / 50) - figure.pos[1]]]] in saves:
                                    #print('radim move tu3')
                                    pos = [figure.pos[0], figure.pos[1]]

                                    print('tu se vrti')
                                    ret = figure.move([7 - math.trunc(y / 50), math.trunc(x / 50)], board, 1)
                                    #print('ret', ret)
                                    if board.is_white_in_chess_only():
                                        print('nemere taj potez')
                                        figure.pos[0] = pos[0]
                                        figure.pos[1] = pos[1]
                                        if board.get_last_deleted() != 0:
                                            board.addFigure(board.get_last_deleted())
                                        break
                                    if ret == 0:
                                        #print('breakno')
                                        break
                                else:
                                    break
                            else:
                                #print('radim move tu4')
                                pos = [figure.pos[0], figure.pos[1]]
                                if [7 - math.trunc(y / 50) - figure.pos[0], math.trunc(x / 50) - figure.pos[1]] not in figure.get_legal_moves(board):
                                    break
                                else:
                                    ret = figure.move([7 - math.trunc(y / 50), math.trunc(x / 50)], board,1)
                                if board.is_white_in_chess_only():
                                    print('nemere taj potez')
                                    figure.pos[0] = pos[0]
                                    figure.pos[1] = pos[1]
                                    if board.get_last_deleted() != 0:
                                        board.addFigure(board.get_last_deleted())
                                    break
                                #print('ret', ret)
                                if ret == 0:
                                    #print('breakno')
                                    break
                            draw_board()
                            saves = board.is_black_in_chess()
                            ret = 0
                            while ret == 0  or isinstance(ret,list):
                                forbidden_move = None
                                ret = black_to_move(saves, forbidden_move)
                                print(ret, isinstance(ret, list))
                                if isinstance(ret, list):
                                    #print('tada')
                                    ret = black_to_move(saves, ret)
                            draw_board()

                            saves = board.is_white_in_chess()
                            if board.is_white_in_chess_only() and saves == []:
                                ctypes.windll.user32.MessageBoxW(0, "MAT", "ŠAH", 1)
                                exit(0)
                            print(saves, ' saves white')
                            board.print_board()
                            #for fig in board.getFigures():
                                #if fig.alliance== 'white':
                                    #print(fig, fig.is_defended)

                            break

                    else:

                        figure2 = board.getFigure_pos([7 - math.trunc(y / 50), math.trunc(x / 50)])
                        if figure2.alliance == 'black':
                            if len(saves) > 0:
                                #print('lala,',[figure, [[7 - math.trunc(y / 50)- figure.pos[0], math.trunc(x / 50)- figure.pos[1]]]], saves)
                                if [figure, [[7 - math.trunc(y / 50) - figure.pos[0], math.trunc(x / 50) - figure.pos[1]]]] in saves:
                                    #print('radim move tu2')

                                    pos = [figure.pos[0], figure.pos[1]]
                                    ret = figure.move([7 - math.trunc(y / 50), math.trunc(x / 50)], board, 1)
                                    if board.is_white_in_chess_only():
                                        print('nemere taj potez')
                                        figure.pos[0] = pos[0]
                                        figure.pos[1] = pos[1]
                                        if board.get_last_deleted() != 0:
                                            board.addFigure(board.get_last_deleted())
                                        break
                                    #print('ret', ret)
                                    if ret == 0:
                                        #print('breakno')
                                        break
                            else:
                                #3print('radim move tu')
                                if figure is None:
                                    break

                                pos = [figure.pos[0], figure.pos[1]]
                                if [7 - math.trunc(y / 50) - figure.pos[0], math.trunc(x / 50) - figure.pos[1]] not in figure.get_legal_moves(board):
                                    break
                                else:
                                    ret = figure.move([7 - math.trunc(y / 50), math.trunc(x / 50)], board,1)
                                if board.is_white_in_chess_only():
                                    print('nemere taj potez')
                                    figure.pos[0] = pos[0]
                                    figure.pos[1] = pos[1]
                                    if board.get_last_deleted() != 0:
                                        board.addFigure(board.get_last_deleted())
                                    break
                                #print('ret', ret)
                                if ret == 0:
                                    #print('breakno')
                                    break
                            draw_board()
                            saves = board.is_black_in_chess()
                            ret = 0
                            while ret == 0 or isinstance(ret,list):
                                forbidden_move = None
                                ret = black_to_move(saves, forbidden_move)
                                print(ret, isinstance(ret, list))
                                if isinstance(ret, list):
                                    #print('tada')
                                    ret = black_to_move(saves, ret)
                            draw_board()
                            saves = board.is_white_in_chess()
                            if board.is_white_in_chess_only() and saves == []:
                                ctypes.windll.user32.MessageBoxW(0, "MAT", "ŠAH", 1)
                                exit(0)
                            print(saves, ' saves white')
                            board.print_board()
                            #for fig in board.getFigures():
                                #print(fig, fig.is_defended)

                            break
                        else:
                            figure = figure2
                            if flag == 1:
                                pygame.time.delay(1000)
                                draw_board()
                                flag = 2

                            elif flag == 0:
                                if saves:
                                    #print('saves', saves)
                                    saves0 = []
                                    for save in saves:
                                        if save[0].pos[0] == figure.pos[0] and save[0].pos[1] == figure.pos[1]:
                                            saves0.append(save)
                                    for save in saves0:
                                        #print(save)
                                        flag = 1
                                        rect = pygame.draw.rect(gameDisplay, (200, 200, 200), (
                                        (figure.pos[1] + save[1][0][1]) * 50 + 12, (7 - (figure.pos[0] + save[1][0][0])) * 50 + 12,
                                        25, 25))
                                        pygame.display.update()
                                else:
                                    moves = copy.deepcopy(figure.get_legal_moves(board))
                                    moves1 = copy.deepcopy(figure.get_legal_moves(board))
                                    b1 = copy.deepcopy(board)
                                    print(moves)
                                    for move in moves1:
                                        pos = [0, 0]
                                        pos[0] = figure.pos[0]
                                        pos[1] = figure.pos[1]
                                        print(move, pos)
                                        figure.move([move[0] + pos[0], move[1] + pos[1]], b1, 0)
                                        if b1.is_white_in_chess_only():
                                            print('mov removan')
                                            moves.remove(move)
                                        figure.pos[0] = pos[0]
                                        figure.pos[1] = pos[1]
                                        if b1.get_last_deleted() != 0:
                                            b1.addFigure(b1.get_last_deleted())

                                    for move in moves:
                                        #print(((figure.pos[1] + move[1] ), ( 7- (figure.pos[0] +move[0]))))
                                        flag = 1
                                        pos = [0,0]
                                        pos[0] = figure.pos[0]
                                        pos[1] = figure.pos[1]


                                        rect = pygame.draw.rect(gameDisplay, (200,200,200), ((figure.pos[1] + move[1] )* 50 + 12, (7- (figure.pos[0] +move[0])) * 50 + 12, 25, 25))
                                        pygame.display.update()




                            else:
                                flag = 0
                                break




pygame.quit()
quit()
