from math import *
import pygame
from pieces.rook import rook

black, white, green, red = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
screen_size = [350, 350]
width = screen_size[0] / 8
height = screen_size[1] / 8
white_pieces = [rook('white', (1, 1), screen_size, True), rook('white', (7, 1), screen_size, True)]
black_pieces = [rook('black', (7, 4), screen_size, True), rook('black', (1, 4), screen_size, True)]
all_pieces = []
for piece in white_pieces:
    all_pieces.append(piece)
for piece in black_pieces:
    all_pieces.append(piece)

def loop(src):
    done = False
    piece = None
    moves = None
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
                    if (piece == None):
                        piece, moves = getPieceMoves()
                    if (piece != None):
                        moved = movePiece(piece, moves)
                    if (moved):
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
            

def getPieceMoves():
    piece = None
    moves = None
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
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
    print("running...")
    loop(src)
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()