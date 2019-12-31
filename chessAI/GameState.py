# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:20:38 2019

@author: sadash
"""

from LinkedList import Node,LinkedList
import chessConstants as cc
import chessUtils as cu


def generateStateFromMove(piece,tx,ty,board):
    
    x,y = piece.pos
    piece.pos = (tx,ty)
    board.pop((x,y),None)
    prevPiece = board.pop((tx,ty),None)
    board[(tx,ty)] = piece
    
    nState = GameState.getStateFromBoard(board)

    board.pop((tx,ty),None)
    board[(x,y)] = piece
    piece.pos = (x,y)
    if prevPiece != None:
        board[(tx,ty)] = prevPiece
    
    return nState

def getKingMoves(piece,board):
    states = []
    x,y = piece.pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx != 0 or dy != 0:
                tx = x+dx
                ty = y+dy
                if cu.isPossibleKillMove(tx,ty,board,piece.color):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
    return states
                    
def getKnightMoves(piece,board):
    states = []
    x,y = piece.pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx != 0 and dy != 0:
                for flag in [0,1]:
                    tx = x+dx*(1+flag)
                    ty = y+dy*(2-flag)
                    if cu.isPossibleKillMove(tx,ty,board,piece.color):
                        nState = generateStateFromMove(piece,tx,ty,board)
                        states.append(nState)
    return states
                        
def getQueenMoves(piece,board):
    states = []
    x,y = piece.pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx != 0 or dy != 0:
                tx = x+dx
                ty = y+dy
                while cu.isValidMove(tx,ty,board):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
                    tx,ty = tx+dx,ty+dy
                    #print("Queen",tx,ty)
                    
                if cu.isPossibleKillMove(tx,ty,board,piece.color):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
    return states
                    
def getRookMoves(piece,board):
    states = []
    x,y = piece.pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if (dx != 0 or dy != 0) and abs(dx)!=abs(dy):
                tx = x+dx
                ty = y+dy
                while cu.isValidMove(tx,ty,board):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
                    tx,ty = tx+dx,ty+dy
                if cu.isPossibleKillMove(tx,ty,board,piece.color):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
    return states
                    
def getBishopMoves(piece,board):
    states = []
    x,y = piece.pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if (dx != 0 or dy != 0) and abs(dx)==abs(dy):
                tx = x+dx
                ty = y+dy
                while cu.isValidMove(tx,ty,board):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
                    tx,ty = tx+dx,ty+dy
                if cu.isPossibleKillMove(tx,ty,board,piece.color):
                    nState = generateStateFromMove(piece,tx,ty,board)
                    states.append(nState)
    return states
                        
def getPawnMoves(piece,board):
    states = []
    x,y = piece.pos
    
    if piece.color == cc.WHITE:
        
        if cu.isValidMove(x+1,y,board):
            if x+1 == 8:
                piece.pType = cc.QUEEN
            nState = generateStateFromMove(piece,x+1,y,board)
            states.append(nState)
        
        if cu.isCertainKillMove(x+1,y+1,board,piece.color):
            nState = generateStateFromMove(piece,x+1,y+1,board)
            states.append(nState)
        
        if cu.isCertainKillMove(x+1,y-1,board,piece.color):
            nState = generateStateFromMove(piece,x+1,y-1,board)
            states.append(nState)
        
            
    else:
        
        if cu.isValidMove(x-1,y,board):
            if x-1 == 1:
                piece.pType = cc.QUEEN
            nState = generateStateFromMove(piece,x-1,y,board)
            states.append(nState)
            
        if cu.isCertainKillMove(x-1,y+1,board,piece.color):
            nState = generateStateFromMove(piece,x-1,y+1,board)
            states.append(nState)
            
        if cu.isCertainKillMove(x-1,y-1,board,piece.color):
            nState = generateStateFromMove(piece,x-1,y-1,board)
            states.append(nState)
            
    return states
                    

def getStatesUtil(pieceList,board):
    
    states = []
    
    for piece in pieceList:
        if piece.pType == cc.KING:
            states.extend(getKingMoves(piece,board))
        elif piece.pType == cc.KNIGHT:
            states.extend(getKnightMoves(piece,board))
        elif piece.pType == cc.PAWN:
            states.extend(getPawnMoves(piece,board))
        elif piece.pType == cc.QUEEN:
            states.extend(getQueenMoves(piece,board))
        elif piece.pType == cc.ROOK:
            states.extend(getRookMoves(piece,board))
        elif piece.pType == cc.BISHOP:
            states.extend(getBishopMoves(piece,board))
    
    return states

class GameState:
    
    def __init__(self):
        self.board = {}
        self.isWhiteKingAlive = False
        self.isBlackKingAlive = False
        self.wList = LinkedList()
        self.bList = LinkedList()
        
    @classmethod
    def getStateFromBoard(cls,board):
        state = cls()
        for key in board:
            node = Node.getCopiedNode(board[key])
            state.board[key] = node
            if board[key].color == cc.WHITE:
                state.wList.insertNode(node)
                if node.pType == cc.KING:
                    state.isWhiteKingAlive = True
            else:
                state.bList.insertNode(node)
                if node.pType == cc.KING:
                    state.isBlackKingAlive = True
        return state
    
    @classmethod
    def getDefaultGame(cls):
        board = cu.generateDefaultGameBoard()
        return cls.getStateFromBoard(board)
    
    def insertNode(self,node):
        self.board[node.pos] = node
        self.list.insertNode(node)
        
    def deleteNode(self,pos):
        if pos in self.board:
            if self.board[pos].color == cc.WHITE:
                self.wList.deleteNode(self.board[pos])
            else:
                self.bList.deleteNode(self.board[pos])
            self.board.pop(pos,None)
            
    def isTerminalState(self):
        return not (self.isWhiteKingAlive and self.isBlackKingAlive)
            
    def evaluateState(self):
        
        if self.isTerminalState():
            if self.isBlackKingAlive:
                return -cc.INF
            else:
                return cc.INF
        
        val = 0
        for piece in self.wList:
            val += cc.PIECE_VALUE[piece.pType]
        for piece in self.bList:
            val -= cc.PIECE_VALUE[piece.pType]
        return val
    
    def getNextStates(self,turn):
        
        if turn == cc.WHITE:
            return getStatesUtil(self.wList,self.board)
        else:
            return getStatesUtil(self.bList,self.board)
        
        

    
    
