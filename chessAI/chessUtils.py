# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:08:04 2019

@author: Samarendra
"""
import chessConstants as cc
from LinkedList import Node


def generateDefaultGameBoard():
    board = {}
    
    for i in range(1,9):
        whitepos = (2,i)
        node = Node(cc.PAWN,whitepos,cc.WHITE)
        board[whitepos] = node
        blackpos = (7,i)
        node = Node(cc.PAWN,blackpos,cc.BLACK)
        board[blackpos] = node
    
    white_rook_pos = (1,1)
    node = Node(cc.ROOK,white_rook_pos,cc.WHITE)
    board[white_rook_pos] = node
    
    black_rook_pos = (8,1)
    node = Node(cc.ROOK,black_rook_pos,cc.BLACK)
    board[black_rook_pos] = node
    
    white_knight_pos = (1,2)
    node = Node(cc.KNIGHT,white_knight_pos,cc.WHITE)
    board[white_knight_pos] = node
    
    black_knight_pos = (8,2)
    node = Node(cc.KNIGHT,black_knight_pos,cc.BLACK)
    board[black_knight_pos] = node
    
    white_bishop_pos = (1,3)
    node = Node(cc.BISHOP,white_bishop_pos,cc.WHITE)
    board[white_bishop_pos] = node
    
    black_bishop_pos = (8,3)
    node = Node(cc.BISHOP,black_bishop_pos,cc.BLACK)
    board[black_bishop_pos] = node
    
    white_king_pos = (1,4)
    node = Node(cc.KING,white_king_pos,cc.WHITE)
    board[white_king_pos] = node
    
    black_king_pos = (8,4)
    node = Node(cc.KING,black_king_pos,cc.BLACK)
    board[black_king_pos] = node
    
    white_queen_pos = (1,5)
    node = Node(cc.QUEEN,white_queen_pos,cc.WHITE)
    board[white_queen_pos] = node
    
    black_queen_pos = (8,5)
    node = Node(cc.QUEEN,black_queen_pos,cc.BLACK)
    board[black_queen_pos] = node
    
    white_bishop_pos = (1,6)
    node = Node(cc.BISHOP,white_bishop_pos,cc.WHITE)
    board[white_bishop_pos] = node
    
    black_bishop_pos = (8,6)
    node = Node(cc.BISHOP,black_bishop_pos,cc.BLACK)
    board[black_bishop_pos] = node
    
    white_knight_pos = (1,7)
    node = Node(cc.KNIGHT,white_knight_pos,cc.WHITE)
    board[white_knight_pos] = node
    
    black_knight_pos = (8,7)
    node = Node(cc.KNIGHT,black_knight_pos,cc.BLACK)
    board[black_knight_pos] = node
    
    white_rook_pos = (1,8)
    node = Node(cc.ROOK,white_rook_pos,cc.WHITE)
    board[white_rook_pos] = node
    
    black_rook_pos = (8,8)
    node = Node(cc.ROOK,black_rook_pos,cc.BLACK)
    board[black_rook_pos] = node
    
    return board


def isValidMove(x,y,board):
    
    if x<1 or x>8 :
        return False
    if y<1 or y>8 :
        return False
    if (x,y) in board:
        return False
    return True
    
def isPossibleKillMove(x,y,board,turn):
    if x<1 or x>8 :
        return False
    if y<1 or y>8 :
        return False
    if (x,y) in board and board[(x,y)].color == turn:
        return False
    return True

def isCertainKillMove(x,y,board,turn):
    if (x,y) in board and board[(x,y)].color != turn:
        return True
    return False


        
                            