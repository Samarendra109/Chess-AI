import pygame
import chessConstants as cc
from chessConstants import DefNode
from GameState import GameState
import chessAI



pygame.init()

#set color with rgb
white,black = (255,255,255),(150,150,150)

#Size of squares
size = 80
done = False
clock = pygame.time.Clock()

def drawPiece(piece,gameDisplay):
    x,y = piece.pos
    pieceimg = cc.PIECE_IMG[(piece.color,piece.pType)]
    pieceimg = pygame.transform.scale(pieceimg, (size, size))
    gameDisplay.blit(pieceimg, (size*y,size*x))
    
def drawBoard(gameState,gameDisplay):
    
    for piece in gameState.wList:
        drawPiece(piece,gameDisplay)
    for piece in gameState.bList:
        drawPiece(piece,gameDisplay)
    
    
gameState = GameState.getDefaultGame()
_,gameState = chessAI.getDesiredAction(gameState,3,True,cc.WHITE)

#set display
gameDisplay = pygame.display.set_mode((800,800))

currPiece = None
time = 0
flag = False

def doThread(arg):
    return chessAI.getDesiredAction(arg[0],arg[1],arg[2],arg[3])    

while not done:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            print(pos)
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (size)
            row = pos[1] // (size)
            
            piece = gameState.board.get((row,column),DefNode)
            
            print(piece,currPiece,
                  currPiece.color if currPiece!=None else "")
            if piece != DefNode and piece.color != cc.WHITE:
                currPiece = piece
                
            elif currPiece!=None and currPiece.color == cc.BLACK:
                gameState.board.pop(currPiece.pos,None)
                gameState.board[(row,column)] = currPiece
                currPiece.pos = (row,column)
                time = pygame.time.get_ticks()
                gameState = GameState.getStateFromBoard(gameState.board)
                currPiece = None
                flag = True
        
    
    if pygame.time.get_ticks()-time > 1000 and flag:
        val,gameState = chessAI.getDesiredAction(gameState,3,True,cc.WHITE)
        print("Max ",val)
        flag = False
    
    
    #board length, must be even
    boardLength = 8
    gameDisplay.fill(white)
    
    cnt = 0
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            #check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
            else:
                pygame.draw.rect(gameDisplay, black,[size*z,size*i,size,size])
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1
    
    drawBoard(gameState,gameDisplay)
    
    #Add a nice boarder
    pygame.draw.rect(gameDisplay,black,[size,size,
                                        boardLength*size,boardLength*size],3)
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()