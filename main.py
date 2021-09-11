import math
import sys
import time

import numpy as np
import pygame

game_over = False
SQUARESIZE = 60
ROW_COUNT = 8
COLUMN_COUNT = 8
pygame.init()
width = SQUARESIZE*COLUMN_COUNT
height = SQUARESIZE*ROW_COUNT
size = (width, height)
screen = pygame.display.set_mode(size)
yellow = (255, 232, 5)
purple = (177, 0, 226)
W_PIECE_COUNT = 16
B_PIECE_COUNT = 16
places = {}
YELLOW = (0, 166, 226)
selected = False
selected_piece = ""
turn = 1
creation = 1
WHITE = (255, 255, 255)
admin = True
# jester = input("Would you like to go to admin or game?")
# if jester == "admin":
#     admin = True
white_checked = False
black_checked = False


def create_board():
    global board
    board = np.zeros((8, 8))
    return board


# noinspection PyTypeChecker
def draw_board(placess = ""):
    global creation
    if not placess == "":
        for i in range(0, len(placess), 2):
            print(placess[i], placess[i+1])
            if (not placess[i] % 2 == 0) and (not placess[i+1] % 2 == 0):
                pygame.draw.rect(screen, yellow, ((placess[i + 1] * SQUARESIZE) - SQUARESIZE, (placess[i] * SQUARESIZE) - SQUARESIZE,
                                                  SQUARESIZE, SQUARESIZE))
            if (placess[i] % 2 == 0) and (not placess[i+1] % 2 == 0):
                pygame.draw.rect(screen, purple, ((placess[i + 1] * SQUARESIZE) - SQUARESIZE, (placess[i] * SQUARESIZE) + SQUARESIZE,
                                                  SQUARESIZE, SQUARESIZE))
            if (placess[i] % 2 == 0) and (placess[i+1] % 2 == 0):
                pygame.draw.rect(screen, yellow, ((placess[i + 1] * SQUARESIZE) + SQUARESIZE, (placess[i] * SQUARESIZE) + SQUARESIZE,
                                                  SQUARESIZE, SQUARESIZE))
            if (not placess[i] % 2 == 0) and (placess[i+1] % 2 == 0):
                pygame.draw.rect(screen, purple, ((placess[i + 1] * SQUARESIZE) + SQUARESIZE, (placess[i] * SQUARESIZE) - SQUARESIZE,
                                                  SQUARESIZE, SQUARESIZE))
    if placess == "":
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                if (not r % 2 == 0) and (not c % 2 == 0):
                    pygame.draw.rect(screen, yellow, ((c * SQUARESIZE) - SQUARESIZE, (r * SQUARESIZE) - SQUARESIZE,
                                                      SQUARESIZE, SQUARESIZE))
                    if creation == 1:
                        places["R" + str(r+1) + "C" + str(c+1)] = ""
                if (r % 2 == 0) and (not c % 2 == 0):
                    pygame.draw.rect(screen, purple, ((c * SQUARESIZE) - SQUARESIZE, (r * SQUARESIZE) + SQUARESIZE,
                                                      SQUARESIZE, SQUARESIZE))
                    if creation == 1:
                        places["R" + str(r+1) + "C" + str(c+1)] = ""
                if (r % 2 == 0) and (c % 2 == 0):
                    pygame.draw.rect(screen, yellow, ((c * SQUARESIZE) + SQUARESIZE, (r * SQUARESIZE) + SQUARESIZE,
                                                      SQUARESIZE, SQUARESIZE))
                    if creation == 1:
                        places["R" + str(r+1) + "C" + str(c+1)] = ""
                if (not r % 2 == 0) and (c % 2 == 0):
                    pygame.draw.rect(screen, purple, ((c * SQUARESIZE) + SQUARESIZE, (r * SQUARESIZE) - SQUARESIZE,
                                                      SQUARESIZE, SQUARESIZE))
                    if creation == 1:
                        places["R" + str(r+1) + "C" + str(c+1)] = ""
        creation += 1


black_pawn = pygame.image.load("10.png")
white_pawn = pygame.image.load("11.png")
black_rook = pygame.image.load("20.png")
white_rook = pygame.image.load("21.png")
black_knight = pygame.image.load("30.png")
white_knight = pygame.image.load("31.png")
black_bishop = pygame.image.load("40.png")
white_bishop = pygame.image.load("41.png")
black_queen = pygame.image.load("50.png")
white_queen = pygame.image.load("51.png")
black_king = pygame.image.load("60.png")
white_king = pygame.image.load("61.png")

white_pawn = pygame.transform.scale(white_pawn, (SQUARESIZE, SQUARESIZE))
black_pawn = pygame.transform.scale(black_pawn, (SQUARESIZE, SQUARESIZE))
white_rook = pygame.transform.scale(white_rook, (SQUARESIZE, SQUARESIZE))
black_rook = pygame.transform.scale(black_rook, (SQUARESIZE, SQUARESIZE))
white_knight = pygame.transform.scale(white_knight, (SQUARESIZE, SQUARESIZE))
black_knight = pygame.transform.scale(black_knight, (SQUARESIZE, SQUARESIZE))
white_bishop = pygame.transform.scale(white_bishop, (SQUARESIZE, SQUARESIZE))
black_bishop = pygame.transform.scale(black_bishop, (SQUARESIZE, SQUARESIZE))
white_queen = pygame.transform.scale(white_queen, (SQUARESIZE, SQUARESIZE))
black_queen = pygame.transform.scale(black_queen, (SQUARESIZE, SQUARESIZE))
white_king = pygame.transform.scale(white_king, (SQUARESIZE, SQUARESIZE))
black_king = pygame.transform.scale(black_king, (SQUARESIZE, SQUARESIZE))


def draw_pieces(piece=""):

    if not piece == "":
        if pieces[piece].color == 1:
            if pieces[piece].piece == 1 and pieces[piece].shown:
                screen.blit(white_pawn, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 2 and pieces[piece].shown:

                screen.blit(white_rook, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 3 and pieces[piece].shown:

                screen.blit(white_knight, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                           (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 4 and pieces[piece].shown:

                screen.blit(white_bishop, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                           (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 5 and pieces[piece].shown:

                screen.blit(white_queen, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                          (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 6 and pieces[piece].shown:

                screen.blit(white_king, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
        else:
            if pieces[piece].piece == 1 and pieces[piece].shown:
                screen.blit(black_pawn, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 2 and pieces[piece].shown:
                screen.blit(black_rook, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 3 and pieces[piece].shown:
                screen.blit(black_knight, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                           (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 4 and pieces[piece].shown:
                screen.blit(black_bishop, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                           (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 5 and pieces[piece].shown:
                screen.blit(black_queen, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                          (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
            if pieces[piece].piece == 6 and pieces[piece].shown:
                screen.blit(black_king, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                         (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                pygame.display.update()
    else:
        for x in range(len(pieces)):
            x += 1
            if x <= W_PIECE_COUNT:
                x = str(x)
                piece = "W" + x
                if pieces[piece].piece == 1 and pieces[piece].shown:

                    screen.blit(white_pawn, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 2 and pieces[piece].shown:

                    screen.blit(white_rook, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 3 and pieces[piece].shown:

                    screen.blit(white_knight, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                               (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 4 and pieces[piece].shown:

                    screen.blit(white_bishop, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                               (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 5 and pieces[piece].shown:

                    screen.blit(white_queen, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                              (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 6 and pieces[piece].shown:

                    screen.blit(white_king, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
            if int(x) > W_PIECE_COUNT:
                x -= W_PIECE_COUNT
                x = str(x)
                piece = "B" + x
                if pieces[piece].piece == 1 and pieces[piece].shown:
                    screen.blit(black_pawn, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 2 and pieces[piece].shown:
                    screen.blit(black_rook, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 3 and pieces[piece].shown:
                    screen.blit(black_knight, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                               (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 4 and pieces[piece].shown:
                    screen.blit(black_bishop, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                               (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 5 and pieces[piece].shown:
                    screen.blit(black_queen, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                              (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()
                if pieces[piece].piece == 6 and pieces[piece].shown:
                    screen.blit(black_king, ((pieces[piece].x*SQUARESIZE)-SQUARESIZE,
                                             (pieces[piece].y*SQUARESIZE)-SQUARESIZE))
                    pygame.display.update()

# 1=pawn
# 2=rook
# 3=knight
# 4=bishop
# 5=queen
# 6=king

# Color
# 1= White
# 0= Black


class Piece:
    def __init__(self, x, y, piece, color, name, shown):
        self.x = x
        self.y = y
        self.piece = piece
        self.color = color
        self.name = name
        self.shown = shown
        places["R" + str(y) + "C" + str(x)] = self.name
        x -= 1
        y -= 1

    def move_piece(self, x, y):
        global selected, turn
        places_list = []
        name = self.name
        piece = self.piece
        color = self.color
        new_posx = self.x*SQUARESIZE
        new_posy = self.y*SQUARESIZE
        places["R" + str(y) + "C" + str(x)] = self.name
        places["R" + str(self.y) + "C" + str(self.x)] = ""
        # pieces[name] = Piece(x, y, piece, color, name, True)
        if not math.floor(new_posy/SQUARESIZE) == y and int(new_posx/SQUARESIZE) == x:
            for i in range(SQUARESIZE*(abs(self.y-y))):
                if self.y > y:
                    if new_posy/SQUARESIZE == self.y:
                        for p in range(abs(self.y-y)+1):
                            p = p*-1
                            places_list.append(self.y+p-1)
                            places_list.append(x-1)
                    del pieces[name]
                    pieces[name] = Piece(x, new_posy/SQUARESIZE, piece, color, name, True)
                    draw_board(places_list)
                    draw_pieces(name)
                    new_posy -= 1
                    time.sleep(0.003)
                else:
                    pass
        pieces[name] = Piece(x, y, piece, color, name, True)
        turn += 1
        self.chess_check()
        if self.piece == 6 and not (piece == pieces[places["R" + str(y) + "C" + str(x)]].piece):
            self.chess_check_coords(self.x, self.y)
        selected = False
        draw_board()
        draw_pieces(name)
        pygame.display.update()

    def select(self):
        global selected, selected_piece
        if not admin:
            if self.color == 1:
                if not turn % 2 == 0:
                    if selected:
                        draw_board()
                        pygame.display.update()
                        selected = False

                    pygame.draw.lines(screen, YELLOW, True, [((self.x*SQUARESIZE)-SQUARESIZE,
                                                              (self.y*SQUARESIZE)-SQUARESIZE),
                                                             ((self.x*SQUARESIZE), (self.y*SQUARESIZE)-SQUARESIZE),
                                                             ((self.x*SQUARESIZE), (self.y*SQUARESIZE)),
                                                             ((self.x*SQUARESIZE)-SQUARESIZE, (self.y*SQUARESIZE))], 5)
                    selected_piece = self.name
                    selected = True
            if self.color == 0:
                if turn % 2 == 0:
                    if selected:
                        draw_board()
                        pygame.display.update()
                        selected = False

                    pygame.draw.lines(screen, YELLOW, True,
                                      [((self.x * SQUARESIZE) - SQUARESIZE, (self.y * SQUARESIZE) - SQUARESIZE),
                                       ((self.x * SQUARESIZE), (self.y * SQUARESIZE) - SQUARESIZE),
                                       ((self.x * SQUARESIZE), (self.y * SQUARESIZE)),
                                       ((self.x * SQUARESIZE) - SQUARESIZE, (self.y * SQUARESIZE))], 5)
                    selected_piece = self.name
                    selected = True
        else:
            draw_board()
            pygame.display.update()

            pygame.draw.lines(screen, YELLOW, True,
                              [((self.x * SQUARESIZE) - SQUARESIZE, (self.y * SQUARESIZE) - SQUARESIZE),
                               ((self.x * SQUARESIZE), (self.y * SQUARESIZE) - SQUARESIZE),
                               ((self.x * SQUARESIZE), (self.y * SQUARESIZE)),
                               ((self.x * SQUARESIZE) - SQUARESIZE, (self.y * SQUARESIZE))], 5)
            selected_piece = self.name

            selected = True

    def check(self, x, y):
        if self.piece == 1 and self.color == 1:
            if turn > 2:
                if not places["R" + str(posy) + "C" + str(posx)] == "":
                    if self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        return True
                    elif self.piece == 1 and self.color == 1 and \
                            self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        if self.x == x and self.y - 1 == y:
                            return False
                else:
                    if self.x == x and self.y - 1 == y:
                        return True
            else:
                if not places["R" + str(posy) + "C" + str(posx)] == "":
                    if self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        return True
                    elif self.piece == 1 and self.color == 1 and \
                            self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        if self.x == x and (self.y - 1 == y or self.y - 2 == y):
                            return False
                else:
                    if self.piece == 1 and self.color == 1:
                        if self.x == x and (self.y - 1 == y or self.y - 2 == y):
                            return True
        elif self.piece == 1 and self.color == 0:
            if turn > 2:
                if not places["R" + str(posy) + "C" + str(posx)] == "":
                    if self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        return True
                    elif self.piece == 1 and self.color == 0 and \
                            self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        if self.x == x and self.y + 1 == y:
                            return False
                else:
                    if self.piece == 1 and self.color == 0:
                        if self.x == x and self.y + 1 == y:
                            return True
            else:
                if not places["R" + str(posy) + "C" + str(posx)] == "":
                    if self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        return True
                    elif self.piece == 1 and self.color == 0 and \
                            self.check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                        if self.x == x and (self.y + 1 == y or self.y + 2 == y):
                            return False
                else:
                    if self.piece == 1 and self.color == 0:
                        if self.x == x and (self.y + 1 == y or self.y + 2 == y):
                            return True
        elif self.piece == 2:
            for i in range(abs(self.y-posy)):
                i += 1
                try:
                    if not places["R" + str(self.y - i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y - i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y - i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y - i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue

            for i in range(abs(self.y - posy)):
                i += 1
                try:
                    if not places["R" + str(self.y + i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y + i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y + i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y + i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(abs(self.x - posx)):
                i += 1
                try:
                    if not places["R" + str(self.y) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(abs(self.x - posx)):
                i += 1
                try:
                    if not places["R" + str(self.y) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
        elif self.piece == 3:
            if (self.x == x+2 and self.y - 1 == y) or (self.x == x-2 and self.y - 1 == y) or \
                    (self.x == x+2 and self.y + 1 == y) or (self.x == x-2 and self.y + 1 == y) or \
                    (self.x == x+1 and self.y + 2 == y) or (self.x == x+1 and self.y - 2 == y) or \
                    (self.x == x-1 and self.y + 2 == y) or (self.x == x-1 and self.y - 2 == y):
                return True
        elif self.piece == 4:
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if not places["R" + str(self.y + i) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y + i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y + i) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y + i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if not places["R" + str(self.y - i) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y - i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y - i) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y - i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if not places["R" + str(self.y + i) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y + i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y + i) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y + i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if not places["R" + str(self.y - i) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y - i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y - i) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y - i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
        elif self.piece == 5:
            for i in range(abs(self.y - posy)):
                i += 1
                try:
                    if not places["R" + str(self.y - i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y - i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y - i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y - i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue

            for i in range(abs(self.y - posy)):
                i += 1
                try:
                    if not places["R" + str(self.y + i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y + i == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y + i) + "C" + str(self.x)] == "":
                        if self.x == x and self.y + i == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(abs(self.x - posx)):
                i += 1
                try:
                    if not places["R" + str(self.y) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y) + "C" + str(self.x - i)] == "":
                        if self.x - i == x and self.y == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(abs(self.x - posx)):
                i += 1
                try:
                    if not places["R" + str(self.y) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y == y:
                            if not self.is_same(places["R" + str(posy) + "C" + str(posx)]):
                                return True
                            else:
                                break
                        else:
                            break
                    elif places["R" + str(self.y) + "C" + str(self.x + i)] == "":
                        if self.x + i == x and self.y == y:
                            return True
                        else:
                            continue
                except KeyError:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if (not places["R" + str(self.y + i) + "C" + str(self.x + i)] == KeyError) and \
                            (self.x == x + i and self.y + i == y):
                        return True
                    elif places["R" + str(self.y + i) + "C" + str(self.x + i)] == KeyError:
                        break
                except KeyError:
                    if self.x == x + i and self.y + i == y:
                        return True
                else:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if (not places["R" + str(self.y - i) + "C" + str(self.x + i)] == KeyError) and \
                            (self.x == x + i and self.y - i == y):
                        return True
                    elif places["R" + str(self.y - i) + "C" + str(self.x + i)] == KeyError:
                        break
                except KeyError:
                    if self.x == x + i and self.y - i == y:
                        return True
                else:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if (not places["R" + str(y) + "C" + str(x)] == KeyError) and \
                            (self.x == x - i and self.y == y + i):
                        return True
                    elif places["R" + str(self.y + i) + "C" + str(self.x - i)] == KeyError:
                        break
                except KeyError:
                    if self.x == x - i and self.y == y + i:
                        return True
                else:
                    continue
            for i in range(ROW_COUNT - 1):
                i += 1
                try:
                    if (not places["R" + str(self.y - i) + "C" + str(self.x - i)] == KeyError) and \
                            (self.x == x - i and self.y == y - i):
                        return True
                    elif places["R" + str(self.y - i) + "C" + str(self.x - i)] == KeyError:
                        break
                except KeyError:
                    if self.x == x - i and self.y == y - i:
                        return True
                else:
                    continue
        elif self.piece == 6:
            if (self.x == x + 1 and self.y - 1 == y) or (self.x == x - 1 and self.y - 1 == y) or \
                    (self.x == x + 1 and self.y + 1 == y) or (self.x == x - 1 and self.y + 1 == y) or \
                    (self.x == x and self.y + 1 == y) or (self.x == x + 1 and self.y == y) or \
                    (self.x == x - 1 and self.y == y) or (self.x == x and self.y - 1 == y):
                return True
        else:
            return False

    def is_same(self, piece):
        if self.color == pieces[piece].color:
            return True
        else:
            return False

    def take(self, piece):
        x = pieces[piece].x
        y = pieces[piece].y
        color = pieces[piece].color
        piece_type = pieces[piece].piece
        name = pieces[piece].name
        del pieces[piece]
        pieces[piece] = Piece(x, y, piece_type, color, name, False)
        self.move_piece(x, y)
        if piece_type == 6:
            self.win()
        self.chess_check()
        if self.piece == 6:
            self.chess_check_coords(self.x, self.y)

    def check_pawn(self, piece):
        if self.color == 1:
            if self.x + 1 == pieces[piece].x and self.y - 1 == pieces[piece].y:
                return True
            elif self.x - 1 == pieces[piece].x and self.y - 1 == pieces[piece].y:
                return True
            else:
                return False
        if self.color == 0:
            if self.x + 1 == pieces[piece].x and self.y + 1 == pieces[piece].y:
                return True
            elif self.x - 1 == pieces[piece].x and self.y + 1 == pieces[piece].y:
                return True
            else:
                return False

    def win(self):
        my_font = pygame.font.SysFont("Comic Sans MS", 30)
        if self.color == 0:
            pygame.draw.rect(screen, WHITE, (int((SQUARESIZE * (COLUMN_COUNT / 2)) - SQUARESIZE * 2),
                                             int((SQUARESIZE * (ROW_COUNT / 2) - SQUARESIZE)),
                                             int(SQUARESIZE * (COLUMN_COUNT / 2)), int(SQUARESIZE * (ROW_COUNT / 4))))
            label = my_font.render("Yay! Black Won!", True, (0, 0, 0))
            text_height = label.get_height()
            text_width = label.get_width()
            screen.blit(label, (int(SQUARESIZE * 2 + ((SQUARESIZE * (COLUMN_COUNT / 2)) - text_width) / 2),
                                (int(SQUARESIZE * 2 + ((SQUARESIZE * (COLUMN_COUNT / 2)) - text_height) / 2))))
            pygame.display.update()
            time.sleep(3)
            reset()
        else:
            pygame.draw.rect(screen, WHITE, (int((SQUARESIZE*(COLUMN_COUNT/2))-SQUARESIZE*2),
                                             int((SQUARESIZE*(ROW_COUNT/2)-SQUARESIZE)),
                                             int(SQUARESIZE*(COLUMN_COUNT/2)), int(SQUARESIZE*(ROW_COUNT/4))))
            label = my_font.render("Yay! White Won!", True, (0, 0, 0))
            text_height = label.get_height()
            text_width = label.get_width()
            screen.blit(label, (int(SQUARESIZE*2+((SQUARESIZE*(COLUMN_COUNT/2))-text_width)/2),
                                (int(SQUARESIZE*2+((SQUARESIZE*(COLUMN_COUNT/2))-text_height)/2))))
            pygame.display.update()
            time.sleep(3)
            reset()

    def castle_check(self, piece):
        if self.piece == 6 and pieces[piece].piece == 2 and (self.color == pieces[piece].color):
            for i in range(3):
                i += 1
                if ((self.y == ROW_COUNT and self.x == 5) or (self.y == 1 and self.x == 5)) and \
                        ((pieces[piece].y == ROW_COUNT and pieces[piece].x == COLUMN_COUNT) or
                         (pieces[piece].y == 1 and pieces[piece].x == COLUMN_COUNT)):
                    if places["R" + str(self.y) + "C" + str(self.x + i)] == "" or self.x + i == pieces[piece].x:
                        if self.x + i == pieces[piece].x:
                            return True
                        else:
                            continue
                    else:
                        break
                else:
                    break
            for i in range(4):
                i += 1
                if ((self.y == ROW_COUNT and self.x == 5) or (self.y == 1 and self.x == 5)) and \
                        ((pieces[piece].y == ROW_COUNT and pieces[piece].x == 1) or
                         (pieces[piece].y == 1 and pieces[piece].x == 1)):
                    if places["R" + str(self.y) + "C" + str(self.x - i)] == "" or self.x - i == pieces[piece].x:
                        if self.x - i == pieces[piece].x:
                            return True
                        else:
                            continue
                    else:
                        break
                else:
                    break
        else:
            return False

    def chess_check(self):
        global black_checked, white_checked
        if self.color == 1:
            if self.check(pieces["B5"].x, pieces["B5"].y):
                pass

                black_checked = True
            else:
                pass

        if self.color == 0:
            if self.check(pieces["W5"].x, pieces["W5"].y):
                pass

            else:
                pass

    def chess_check_coords(self, x, y):
        global selected_piece, selected
        if self.color == 1:
            for i in range(18):
                i += 1
                if pieces["B" + str(i)].check(x, y):
                    pass
                else:
                    pass
        if self.color == 0:
            for i in range(18):
                i += 1
                if pieces["W" + str(i)].check(x, y):
                    pass
                else:
                    pass
        selected_piece = ""
        selected = False


board = create_board()
draw_board()
pieces = {"B1": Piece(1, 1, 2, 0, "B1", True), "B2": Piece(2, 1, 3, 0, "B2", True), "B3": Piece(3, 1, 4, 0, "B3", True),
          "B4": Piece(4, 1, 5, 0, "B4", True), "B5": Piece(5, 1, 6, 0, "B5", True), "B6": Piece(6, 1, 4, 0, "B6", True),
          "B7": Piece(7, 1, 3, 0, "B7", True), "B8": Piece(8, 1, 2, 0, "B8", True), "B9": Piece(1, 2, 1, 0, "B9", True),
          "B10": Piece(2, 2, 1, 0, "B10", True), "B11": Piece(3, 2, 1, 0, "B11", True),
          "B12": Piece(4, 2, 1, 0, "B12", True), "B13": Piece(5, 2, 1, 0, "B13", True),
          "B14": Piece(6, 2, 1, 0, "B14", True), "B15": Piece(7, 2, 1, 0, "B15", True),
          "B16": Piece(8, 2, 1, 0, "B16", True), "W1": Piece(1, 8, 2, 1, "W1", True),
          "W2": Piece(2, 8, 3, 1, "W2", True), "W3": Piece(3, 8, 4, 1, "W3", True), "W4": Piece(4, 8, 5, 1, "W4", True),
          "W5": Piece(5, 8, 6, 1, "W5", True), "W6": Piece(6, 8, 4, 1, "W6", True), "W7": Piece(7, 8, 3, 1, "W7", True),
          "W8": Piece(8, 8, 2, 1, "W8", True), "W9": Piece(1, 7, 1, 1, "W9", True),
          "W10": Piece(2, 7, 1, 1, "W10", True), "W11": Piece(3, 7, 1, 1, "W11", True),
          "W12": Piece(4, 7, 1, 1, "W12", True), "W13": Piece(5, 7, 1, 1, "W13", True),
          "W14": Piece(6, 7, 1, 1, "W14", True), "W15": Piece(7, 7, 1, 1, "W15", True),
          "W16": Piece(8, 7, 1, 1, "W16", True)}


def reset():
    global pieces, turn, creation
    creation = 1
    turn = 1
    draw_board()
    pieces = {"B1": Piece(1, 1, 2, 0, "B1", True), "B2": Piece(2, 1, 3, 0, "B2", True),
              "B3": Piece(3, 1, 4, 0, "B3", True),
              "B4": Piece(4, 1, 5, 0, "B4", True), "B5": Piece(5, 1, 6, 0, "B5", True),
              "B6": Piece(6, 1, 4, 0, "B6", True),
              "B7": Piece(7, 1, 3, 0, "B7", True), "B8": Piece(8, 1, 2, 0, "B8", True),
              "B9": Piece(1, 2, 1, 0, "B9", True),
              "B10": Piece(2, 2, 1, 0, "B10", True), "B11": Piece(3, 2, 1, 0, "B11", True),
              "B12": Piece(4, 2, 1, 0, "B12", True), "B13": Piece(5, 2, 1, 0, "B13", True),
              "B14": Piece(6, 2, 1, 0, "B14", True), "B15": Piece(7, 2, 1, 0, "B15", True),
              "B16": Piece(8, 2, 1, 0, "B16", True), "W1": Piece(1, 8, 2, 1, "W1", True),
              "W2": Piece(2, 8, 3, 1, "W2", True), "W3": Piece(3, 8, 4, 1, "W3", True),
              "W4": Piece(4, 8, 5, 1, "W4", True),
              "W5": Piece(5, 8, 6, 1, "W5", True), "W6": Piece(6, 8, 4, 1, "W6", True),
              "W7": Piece(7, 8, 3, 1, "W7", True),
              "W8": Piece(8, 8, 2, 1, "W8", True), "W9": Piece(1, 7, 1, 1, "W9", True),
              "W10": Piece(2, 7, 1, 1, "W10", True), "W11": Piece(3, 7, 1, 1, "W11", True),
              "W12": Piece(4, 7, 1, 1, "W12", True), "W13": Piece(5, 7, 1, 1, "W13", True),
              "W14": Piece(6, 7, 1, 1, "W14", True), "W15": Piece(7, 7, 1, 1, "W15", True),
              "W16": Piece(8, 7, 1, 1, "W16", True)}
    draw_pieces()


while not game_over:
    draw_pieces()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mice = pygame.mouse.get_pressed(3)
            if mice[0]:
                pos = pygame.mouse.get_pos()
                posx = math.ceil(pos[0]/SQUARESIZE)
                posy = math.ceil(pos[1] / SQUARESIZE)
                try:
                    if not places["R" + str(posy) + "C" + str(posx)] == "":
                        if ((not selected) or (not pieces[selected_piece].check(posx, posy)) or
                                pieces[selected_piece].is_same(places["R" + str(posy) + "C" + str(posx)])) and not \
                                pieces[selected_piece].castle_check(places["R" + str(posy) + "C" + str(posx)]):
                            pieces[places["R" + str(posy) + "C" + str(posx)]].select()
                        else:
                            if pieces[selected_piece].castle_check(places["R" + str(posy) + "C" + str(posx)]):
                                if pieces[selected_piece].x < pieces[places["R" + str(posy) + "C" + str(posx)]].x:
                                    pieces[selected_piece].move_piece(pieces[selected_piece].x + 2,
                                                                      pieces[selected_piece].y)
                                    pieces[places["R" + str(posy) + "C" + str(posx)]].move_piece(
                                        pieces[places["R" + str(posy) + "C" + str(posx)]].x - 2,
                                        pieces[places["R" + str(posy) + "C" + str(posx)]].y)
                                else:
                                    pieces[selected_piece].move_piece(pieces[selected_piece].x - 2,
                                                                      pieces[selected_piece].y)
                                    pieces[places["R" + str(posy) + "C" + str(posx)]].move_piece(
                                        pieces[places["R" + str(posy) + "C" + str(posx)]].x + 3,
                                        pieces[places["R" + str(posy) + "C" + str(posx)]].y)
                            elif not pieces[selected_piece].piece == 1:
                                pieces[selected_piece].take(places["R" + str(posy) + "C" + str(posx)])
                            elif pieces[selected_piece].check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                                pieces[selected_piece].take(places["R" + str(posy) + "C" + str(posx)])
                            else:
                                pieces[places["R" + str(posy) + "C" + str(posx)]].select()
                    else:
                        if selected and pieces[selected_piece].check(posx, posy):
                            pieces[selected_piece].move_piece(posx, posy)
                        else:
                            pass
                except KeyError:
                    if not places["R" + str(posy) + "C" + str(posx)] == "":
                        if (not selected) or (not pieces[selected_piece].check(posx, posy)) or \
                                pieces[selected_piece].is_same(places["R" + str(posy) + "C" + str(posx)]):
                            pieces[places["R" + str(posy) + "C" + str(posx)]].select()
                        else:
                            if not pieces[selected_piece].piece == 1:
                                pieces[selected_piece].take(places["R" + str(posy) + "C" + str(posx)])
                            elif pieces[selected_piece].check_pawn(places["R" + str(posy) + "C" + str(posx)]):
                                pieces[selected_piece].take(places["R" + str(posy) + "C" + str(posx)])
                            else:
                                pieces[places["R" + str(posy) + "C" + str(posx)]].select()
                    else:
                        if selected and pieces[selected_piece].check(posx, posy):
                            pieces[selected_piece].move_piece(posx, posy)
                        else:
                            pass
