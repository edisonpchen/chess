import pygame
import time
import sys

board = [['  ' for i in range(8)] for i in range(8)]

## Creates a chess piece class that shows what team a piece is on, what type of piece it is and whether or not it can be killed by another selected piece.
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image

bp = Piece('b', 'p', 'pieces/bP.png')
wp = Piece('w', 'p', 'pieces/wP.png')
bk = Piece('b', 'k', 'pieces/bK.png')
wk = Piece('w', 'k', 'pieces/wK.png')
br = Piece('b', 'r', 'pieces/bR.png')
wr = Piece('w', 'r', 'pieces/wR.png')
bb = Piece('b', 'b', 'pieces/bB.png')
wb = Piece('w', 'b', 'pieces/wB.png')
bq = Piece('b', 'q', 'pieces/bQ.png')
wq = Piece('w', 'q', 'pieces/wQ.png')
bkn = Piece('b', 'kn', 'pieces/bN.png')
wkn = Piece('w', 'kn', 'pieces/wN.png')
