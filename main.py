from math import *
import pygame
from pieces.rook import rook
from pieces.bishop import bishop
from pieces.queen import queen
from pieces.knight import knight
from pieces.king import king
from pieces.pawn import pawn

black, white, green, red = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
screen_size = [450, 450]
width = screen_size[0] / 8
height = screen_size[1] / 8
white_pieces = [rook('white', (0, 7), screen_size, True), knight('white', (1, 7), screen_size, True), bishop('white', (2, 7), screen_size, True), queen('white', (3, 7), screen_size, True), king('white', (4, 7), screen_size, True), bishop('white', (5, 7), screen_size, True), knight('white', (6, 7), screen_size, True), rook('white', (7, 7), screen_size, True),
                pawn('white', (4, 6), screen_size, True), ]
black_pieces = [rook('black', (0, 0), screen_size, True), knight('black', (1, 0), screen_size, True), bishop('black', (2, 0), screen_size, True), queen('black', (3, 0), screen_size, True), king('black', (4, 0), screen_size, True), bishop('black', (5, 0), screen_size, True), knight('black', (6, 0), screen_size, True), rook('black', (7, 0), screen_size, True),
                pawn('black', (4, 1), screen_size, True), ]
all_pieces = []
for piece in white_pieces:
    all_pieces.append(piece)
for piece in black_pieces:
    all_pieces.append(piece)

def loop(src):
    done = False
    piece = None
    moves = None
    checkedKing = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                moved = False
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
                if ((piece != None) and (mouse_pos not in piece.getMoves(all_pieces))):
                    moves = None
                    piece = None
                    redraw(src, all_pieces, moves)
                else:
                    if ((piece == None)):
                        piece, moves = getPieceMoves(checkedKing)
                    if (piece != None):
                        moved = movePiece(piece, moves)
                    if (moved):
                        checkedKing, mated = check(piece)
                        if(mated):
                            done = True
                            break
                        checkCapture(piece)
                        moves = None
                        piece = None
                    redraw(src, all_pieces, moves)
                
        pygame.display.flip()
    

def drawPieces(src, pieceList):
    for piece in pieceList:
        piece.drawPiece(src, piece.position)

def drawBoard(src, moves =None):
    color_pic = 0
    for y in range(8):
        for x in range(8):
            if color_pic > 1:
                color_pic = 0
            if color_pic == 0:
                color = white
            elif color_pic == 1:
                color = black
            pygame.draw.rect(src, color, [width * x, height * y, width, height])
            color_pic = 0 if color_pic == 1 else 1
            
            if (moves != None and (x,y) in moves):
                color = green
                pygame.draw.rect(src, color, [width * x, height * y, width, height])
        color_pic += 1
            

def getPieceMoves(checkedKing):
    piece = None
    moves = None
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
    if (checkedKing == None):
        for pieces in all_pieces:
            if((pieces.position == mouse_pos) and (pieces.visible)):
                piece = pieces
                moves = piece.getMoves(all_pieces)
            
    return piece, moves

def movePiece(piece, moves):
    output = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
    if (mouse_pos in moves):
        piece.setPosition(mouse_pos)
        output = True
    
    return output

def checkCapture(movedPiece):
    pieceCaptured = False
    for pieces in all_pieces:
        if ((pieces.position == movedPiece.position) and (pieces.color != movedPiece.color)):
            pieces.setVisible(False)
            pieceCaptured = True
    
    return pieceCaptured

def check(movedPiece):
    checked = False
    checkedKing = None
    mated = False
    
    for piece in all_pieces:
        if (piece.color != movedPiece.color):
            if (piece.position in movedPiece.getMoves(all_pieces)):
                if (type(piece).__name__ == "king"):
                    checked = True
                    checkedKing = piece
    if (checked):
        print("Checked")
        mated = mate(checkedKing)
    else:
        print("Not Checked")
    
    return checkedKing, mated

def mate(king):
    mated = False
    otherMoves = None
    
    for piece in all_pieces:
        startPos = piece.position
        if (piece.color == king.color):
            moves = piece.getMoves(all_pieces)
            for move in moves:
                piece.setPosition(move)

        piece.setPosition(startPos)
    if(king.getMoves(all_pieces) != [] or):
        print(king.getMoves(all_pieces))
        print("Not mate")
    else:
        mated = True
        print("Mate")
        
    return mated

def redraw(src, all_pieces, moves =None):
    drawBoard(src, moves)
    drawPieces(src, all_pieces)

def main():
    pygame.init()
    src = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    redraw(src, all_pieces)
    print("\nRunning...\n")
    loop(src)
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()