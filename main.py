from math import *
import pygame
from pieces.rook import rook

black, white, green, red = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
screen_size = [350, 350]
width = screen_size[0] / 8
height = screen_size[1] / 8
white_pieces = [rook('white', (3, 3), screen_size, True)]
black_pieces = []

def loop(src):
    done = False
    piece = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                piece = selectPiece(src)
                moves = None
                if (piece != None):
                    moves = piece.getMoves()
                print(moves)
                redraw(src, white_pieces, black_pieces, moves)
                if (piece != None):
                    movePiece(src, piece)
                redraw(src, white_pieces, black_pieces, moves)
        pygame.display.flip()

def drawPieces(src, pieceList):
    for pieces in pieceList:
        print(pieces.position)
        pieces.drawPiece(src, pieces.position)

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
                # print((x,y))
                pygame.draw.rect(src, color, [width * x, height * y, width, height])
        color_pic += 1
            

def selectPiece(src):
    piece = None
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
    # print(mouse_pos)
    for pieces in white_pieces:
        if(pieces.position == mouse_pos):
            # print(pieces.getMoves())
            piece = pieces
    for pieces in white_pieces:
        if(pieces.position == mouse_pos):
            # print(pieces.getMoves())
            piece = pieces
            
    return piece

def movePiece(src, piece):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
    if (mouse_pos in piece.getMoves()):
        pos = piece.setPosition(mouse_pos)
        print(pos)

def redraw(src, white_pieces, black_pieces, moves =None):
    drawBoard(src, moves)
    drawPieces(src, white_pieces)
    drawPieces(src, black_pieces)

def main():
    pygame.init()
    src = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    redraw(src, white_pieces, black_pieces)
    print("running...")
    loop(src)
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()