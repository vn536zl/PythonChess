from math import *
import pygame

from pieces.GamePiece import GamePiece
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook


black, white, green = (0, 0, 0), (255, 255, 255), (0, 150, 0),
pygame.init()

info = pygame.display.Info()
screen_size = [info.current_w/2, info.current_h/2]
white_pieces = [Rook('white', (0, 7), True), Knight('white', (1, 7), True),
                Bishop('white', (2, 7), True), Queen('white', (3, 7), True),
                King('white', (4, 7), True), Bishop('white', (5, 7), True),
                Knight('white', (6, 7), True), Rook('white', (7, 7), True),
                Pawn('white', (4, 6), True), ]
black_pieces = [Rook('black', (0, 0), True), Knight('black', (1, 0), True),
                Bishop('black', (2, 0), True), Queen('black', (3, 0), True),
                King('black', (4, 0), True), Bishop('black', (5, 0), True),
                Knight('black', (6, 0), True), Rook('black', (7, 0), True),
                Pawn('black', (4, 1), True), ]
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
            vidInfo = pygame.display.Info()
            size = [(vidInfo.current_w), (vidInfo.current_h)]
            board_size = [(2 * size[0]) / 3, size[1]]
            width = board_size[0]/8
            height = board_size[1]/8

            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.VIDEORESIZE:
                size = list(event.size)
                board_size = [(2 * size[0]) / 3, size[1]]
                draw(src, all_pieces, board_size, moves)

            if event.type == pygame.MOUSEBUTTONUP:
                moved = False
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))
                if ((piece is not None) and (mouse_pos not in piece.getMoves(all_pieces))):
                    moves = None
                    piece = None
                    draw(src, all_pieces, board_size)
                else:
                    if ((piece is None)):
                        piece, moves = getPieceMoves(checkedKing, possibleMoves, mouse_pos)
                    if (piece is not None):
                        moved = movePiece(piece, moves, mouse_pos)
                    if (moved):
                        checkCapture(piece)
                        checkedKing, mated, possibleMoves = KingChecked(piece)
                        if (mated):
                            done = True
                            break
                        moves = None
                        piece = None
                    draw(src, all_pieces, board_size, moves)

        pygame.display.flip()


def drawPieces(src, pieceList, size):
    for piece in pieceList:
        piece.setSize(size)
        piece.drawPiece(src, piece.position)


def drawBoard(src, size, moves=None):
    color_pic = 0
    width = size[0] / 8
    height = size[1] / 8

    for y in range(8):
        for x in range(8):
            color = None
            if color_pic > 1:
                color_pic = 0
            if color_pic == 0:
                color = white
            elif color_pic == 1:
                color = black
            pygame.draw.rect(src, color, [width * x, height * y, width, height])
            color_pic = 0 if color_pic == 1 else 1

            if (moves is not None and (x, y) in moves):
                s = pygame.Surface((width, height))
                s.set_alpha(100)
                s.fill(green)
                src.blit(s, (width * x, height * y))
        color_pic += 1


def getPieceMoves(checkedKing, possibleMoves, mouse_pos):
    piece = None
    moves = []
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


def movePiece(piece, moves, mouse_pos):
    output = False
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


def KingChecked(movedPiece):
    print(type(movedPiece))
    checked = False
    checkedKing = None
    mated = False
    possibleMoves = None

    for piece in all_pieces:
        if (piece.color != movedPiece.color):
            if (piece.position in movedPiece.getMoves(all_pieces)):
                if (type(piece).__name__ == "King"):
                    checked = True
                    checkedKing = piece
    if (checked):
        print("Checked")
        mated, possibleMoves = KingMated(checkedKing, movedPiece)
    else:
        print("Not Checked")

    return checkedKing, mated, possibleMoves


def checkOtherMoves(King, movedPiece):
    possibleMoves = {}
    posit = 0

    for piece in all_pieces:
        if (piece.color == King.color):
            movesPerPiece = []
            moves = piece.getMoves(all_pieces)
            for move in moves:
                if (move == movedPiece.position):
                    movesPerPiece.append(move)
                if (move in movedPiece.getMoves(all_pieces)):
                    originalPos = piece.position
                    piece.setPosition(move)
                    if (King.position not in movedPiece.getMoves(all_pieces)):
                        movesPerPiece.append(move)
                    piece.setPosition(originalPos)
            key = (type(piece).__name__) + " " + str(posit)
            possibleMoves.update({key: movesPerPiece})
            posit += 1

    return possibleMoves


def KingMated(King: GamePiece, movedPiece):
    mated = False

    possibleMoves = checkOtherMoves(King, movedPiece)

    if (King.getMoves(all_pieces) != [] or possibleMoves != {}):
        key = type(King).__name__ + " " + str(King.position[0])
        possibleMoves.update({key: King.getMoves(all_pieces)})
        print(possibleMoves)
        print("Not mate")
    else:
        mated = True
        print("Mate")

    return mated, possibleMoves


def draw(src, all_pieces, size, moves=None):
    drawBoard(src, size, moves)
    drawPieces(src, all_pieces, size)


def main():
    src = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    draw(src, all_pieces, [(2*screen_size[0])/3, screen_size[1]])
    print("\nRunning...\n")
    loop(src)
    pygame.quit()


if __name__ == "__main__":
    main()
