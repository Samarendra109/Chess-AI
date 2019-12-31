# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:09:52 2019

@author: Samarendra
"""
from pygame import image



WHITE = "white"
BLACK = "black"

def flip(turn):
    if turn == WHITE:
        return BLACK
    return WHITE

QUEEN = 'queen'
KING = 'king'
ROOK = 'rook'
BISHOP = 'bishop'
KNIGHT = 'knight'
PAWN = 'pawn'

class DefNode:
    color = 'Nothing'
    pType = 'Nothing'

INF = 90500

PIECE_VALUE = {
        QUEEN : 90,
        KING : 90000,
        ROOK : 50,
        BISHOP : 30,
        KNIGHT : 30,
        PAWN : 10
        }

WHITE_KING_IMG = image.load("images/white_king.png")
BLACK_KING_IMG = image.load("images/black_king.png")

WHITE_BISHOP_IMG = image.load("images/white_bishop.png")
BLACK_BISHOP_IMG = image.load("images/black_bishop.png")

WHITE_KNIGHT_IMG = image.load("images/white_knight.png")
BLACK_KNIGHT_IMG = image.load("images/black_knight.png")

WHITE_ROOK_IMG = image.load("images/white_rook.png")
BLACK_ROOK_IMG = image.load("images/black_rook.png")

WHITE_PAWN_IMG = image.load("images/white_pawn.png")
BLACK_PAWN_IMG = image.load("images/black_pawn.png")

WHITE_QUEEN_IMG = image.load("images/white_queen.png")
BLACK_QUEEN_IMG = image.load("images/black_queen.png")

PIECE_IMG ={
        (WHITE,KING) : WHITE_KING_IMG,
        (BLACK,KING) : BLACK_KING_IMG,
        (WHITE,BISHOP) : WHITE_BISHOP_IMG,
        (BLACK,BISHOP) : BLACK_BISHOP_IMG,
        (WHITE,ROOK) : WHITE_ROOK_IMG,
        (BLACK,ROOK) : BLACK_ROOK_IMG,
        (WHITE,PAWN) : WHITE_PAWN_IMG,
        (BLACK,PAWN) : BLACK_PAWN_IMG,
        (WHITE,QUEEN) : WHITE_QUEEN_IMG,
        (BLACK,QUEEN) : BLACK_QUEEN_IMG,
        (WHITE,KNIGHT) : WHITE_KNIGHT_IMG,
        (BLACK,KNIGHT) : BLACK_KNIGHT_IMG,
        }


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            