from math import *
import pygame
from pieces.bishop import bishop
from pieces.king import king
from pieces.knight import knight
from pieces.pawn import pawn
from pieces.queen import queen
from pieces.rook import rook

black, white, green, red = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
pygame.init()

info = pygame.display.Info()
screen_size = [info.current_w/1.5, info.current_h/2]
board_size = [(3*screen_size[0])/4, screen_size[1]]
info_size = [screen_size[0]/4, screen_size[1]]
width = board_size[0] / 8
height = board_size[1] / 8
white_pieces = [rook('white', (0, 7), board_size, True), knight('white', (1, 7), board_size, True),
                bishop('white', (2, 7), board_size, True), queen('white', (3, 7), board_size, True),
                king('white', (4, 7), board_size, True), bishop('white', (5, 7), board_size, True),
                knight('white', (6, 7), board_size, True), rook('white', (7, 7), board_size, True),
                pawn('white', (4, 6), board_size, True), ]
black_pieces = [rook('black', (0, 0), board_size, True), knight('black', (1, 0), board_size, True),
                bishop('black', (2, 0), board_size, True), queen('black', (3, 0), board_size, True),
                king('black', (4, 0), board_size, True), bishop('black', (5, 0), board_size, True),
                knight('black', (6, 0), board_size, True), rook('black', (7, 0), board_size, True),
                pawn('black', (4, 1), board_size, True), ]
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
    possibleMoves = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.VIDEORESIZE:
                redraw(src, all_pieces, moves)

            if event.type == pygame.MOUSEBUTTONUP:
                moved = False
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
                if ((piece is not None) and (mouse_pos not in piece.getMoves(all_pieces))):
                    moves = None
                    piece = None
                    redraw(src, all_pieces, moves)
                else:
                    if ((piece is None)):
                        piece, moves = getPieceMoves(checkedKing, possibleMoves)
                    if (piece is not None):
                        moved = movePiece(piece, moves)
                    if (moved):
                        checkedKing, mated, possibleMoves = kingChecked(piece)
                        if (mated):
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


def drawBoard(src, moves=None):
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

            if (moves is not None and (x, y) in moves):
                color = green
                pygame.draw.rect(src, color, [width * x, height * y, width, height])
        color_pic += 1


def getPieceMoves(checkedKing, possibleMoves):
    piece = None
    moves = []
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
    if (checkedKing is None):
        for pieces in all_pieces:
            if ((pieces.position == mouse_pos) and (pieces.visible)):
                piece = pieces
                moves = piece.getMoves(all_pieces)
    elif (checkedKing is not None):
        for pieces in all_pieces:
            if ((pieces.position == mouse_pos) and (pieces.visible)):
                for pieceKey, possMoves in possibleMoves.items():
                    testToKey = type(pieces).__name__ + " " + str(pieces.position[0])
                    if (testToKey == pieceKey):
                        for pieceMoves in pieces.getMoves(all_pieces):
                            if pieceMoves in possMoves:
                                piece = pieces
                                moves.append(pieceMoves)

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


def kingChecked(movedPiece):
    checked = False
    checkedKing = None
    mated = False
    possibleMoves = None

    for piece in all_pieces:
        if (piece.color != movedPiece.color):
            if (piece.position in movedPiece.getMoves(all_pieces)):
                if (type(piece).__name__ == "king"):
                    checked = True
                    checkedKing = piece
    if (checked):
        print("Checked")
        mated, possibleMoves = kingMated(checkedKing, movedPiece)
    else:
        print("Not Checked")

    return checkedKing, mated, possibleMoves


def checkOtherMoves(king, movedPiece):
    possibleMoves = {}

    for piece in all_pieces:
        if (piece.color == king.color):
            movesPerPiece = []
            moves = piece.getMoves(all_pieces)
            for move in moves:
                if (move == movedPiece.position):
                    movesPerPiece.append(move)
                if (move in movedPiece.getMoves(all_pieces)):
                    originalPos = piece.position
                    piece.setPosition(move)
                    if (king.position not in movedPiece.getMoves(all_pieces)):
                        movesPerPiece.append(move)
                    piece.setPosition(originalPos)
            key = (type(piece).__name__) + " " + str(piece.position[0])
            possibleMoves.update({key: movesPerPiece})

    return possibleMoves


def kingMated(king, movedPiece):
    mated = False

    possibleMoves = checkOtherMoves(king, movedPiece)

    if (king.getMoves(all_pieces) != [] or possibleMoves != {}):
        key = type(king).__name__ + " " + str(king.position[0])
        possibleMoves.update({key: king.getMoves(all_pieces)})
        print(possibleMoves)
        print("Not mate")
    else:
        mated = True
        print("Mate")

    return mated, possibleMoves


def redraw(src, all_pieces, moves=None):
    drawBoard(src, moves)
    drawPieces(src, all_pieces)


def main():
    print(info)
    src = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    redraw(src, all_pieces)
    print("\nRunning...\n")
    loop(src)
    pygame.quit()


if __name__ == "__main__":
    main()
