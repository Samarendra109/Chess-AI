# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:20:38 2019

@author: sadash
"""

from chessConstants import INF,flip


def alphaBetaPruning(gameState,iteration,isMax,turn,alpha,beta):
    
    if iteration == 0:
        return gameState.evaluateState(),gameState
    
    if gameState.isTerminalState():
        return gameState.evaluateState(),gameState
    
    maxVal,minVal = -INF,INF
    finalState = None
    
    if isMax:
        
        for state in gameState.getNextStates(turn):     
            val,_ = getDesiredAction(state,iteration-1,False,flip(turn))
            maxVal = max(val,maxVal)
            alpha = max(alpha,maxVal)
            if maxVal == val:
                finalState = state
            #if iteration == 4:
             #   print(val,end=" ")
            if alpha >= beta:
                break
        
        #if iteration == 4:
         #   print("")
        
        return maxVal,finalState
    
    else:
        
        for state in gameState.getNextStates(turn):
            val,_ = getDesiredAction(state,iteration-1,True,flip(turn))
            minVal = min(val,minVal)
            beta = min(minVal,beta)
            if minVal == val:
                finalState = state
            if alpha >= beta:
                break
                
        return minVal,finalState
                
def getDesiredAction(gameState,iteration,isMax,turn):
    alpha,beta = -INF,INF
    return alphaBetaPruning(gameState,iteration,isMax,turn,alpha,beta)        

'''
-----------------------
def alphaBetaPruning(gameState,iteration,isMax,turn,alpha,beta):
    
    if iteration == 0:
        return gameState.evaluateState(),gameState
    
    fState = gameState
    if isMax:
        bestVal = -INF
        for state in gameState.getNextStates(turn):
            nTurn = cc.BLACK if turn == cc.WHITE else cc.WHITE
            val,_ = alphaBetaPruning(state,iteration-1,False,nTurn,alpha,beta)
            bestVal = max(val,bestVal)
            alpha = max(alpha,bestVal)
            fState = state if bestVal==val else fState
            if beta <= alpha:
                break
            
    else:
        bestVal = INF
        for state in gameState.getNextStates(turn):
            nTurn = cc.BLACK if turn == cc.WHITE else cc.WHITE
            val,_ = alphaBetaPruning(state,iteration-1,True,nTurn,alpha,beta)
            bestVal = min(val,bestVal)
            beta = min(bestVal,beta)
            fState = state if bestVal==val else fState
            if beta <= alpha:
                break
            
    return bestVal,fState
        

def getDesiredAction(gameState,iteration,isMax,turn):
    alpha,beta = -INF,INF
    return alphaBetaPruning(gameState,iteration,isMax,turn,alpha,beta)
---------------------

def getDesiredAction(gameState,iteration,isMax,turn):
    
    if iteration == 0:
        return gameState.evaluateState(),gameState
    
    if gameState.isTerminalState():
        return gameState.evaluateState(),gameState
    
    maxVal,minVal = -INF,INF
    finalState = None
    
    if isMax:
        
        for state in gameState.getNextStates(turn):     
            val,_ = getDesiredAction(state,iteration-1,False,flip(turn))
            maxVal = max(val,maxVal)
            if maxVal == val:
                finalState = state
            if iteration == 4:
                print(val,end=" ")
        
        if iteration == 4:
            print("")
        
        return maxVal,finalState
    
    else:
        
        for state in gameState.getNextStates(turn):
            val,_ = getDesiredAction(state,iteration-1,True,flip(turn))
            minVal = min(val,minVal)
            if minVal == val:
                finalState = state
                
        return minVal,finalState
 
''' 
    

























