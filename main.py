# Python libraries
from math import *
import pygame

# external configfile
from app_constanst import config

# Show Environment
print('Environment:', config['app']['env'])

# Get colors and starting screen size
black, white, green = config['color']['black'], config['color']['white'], config['color']['green']
screen_size = config['screenSize']

# Get pieces and type
white_pieces = config['pieces']['whitePieces']
white_defaults = config['pieces']['whiteDefaults']
black_pieces = config['pieces']['blackPieces']
black_defaults = config['pieces']['blackDefaults']
all_pieces = config['pieces']['allPieces']


def onReset():

    for piece in all_pieces:
        if piece.getColor() == "black":
            for setting in black_defaults:
                print(setting['Name'])
                if (piece.getID() == setting['Name']):
                    piece.setVisible(setting['Visibility'])
                    piece.setPosition(setting['Position'])
                    piece.setMove(0)
        if piece.getColor() == "white":
            for setting in white_defaults:
                print(setting['Name'])
                if (piece.getID() == setting['Name']):
                    piece.setVisible(setting['Visibility'])
                    piece.setPosition(setting['Position'])
                    piece.setMove(0)

    main()


# Set game piece size and give piece all available pieces
def drawPieces(src: pygame.Surface, size: list, castle: bool, kingPiece):
    for piece in all_pieces:
        piece.loadPieces(all_pieces)
        piece.setSize(size)
        if (castle):
            kingX, kingY = kingPiece.getPosition()
            if (piece.getName() == "Rook" and piece.getColor() == kingPiece.getColor()):
                if (piece.getPosition() == (kingX + 1, kingY)):
                    piece.setPosition((kingX - 1, kingY))
                elif (piece.getPosition() == (kingX - 1, kingY)):
                    piece.setPosition((kingX + 1, kingY))

        piece.drawPiece(src, piece.getPosition())


# Draw the game board
def drawBoard(src: pygame.Surface, size: list, moves: list = None):
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


# Get all the moves each piece is able to make
def getPieceMoves(turn: int, mouse_pos: tuple, checkedKing=None, possibleMoves: dict = None):
    returnedPiece = None
    moves = []

    if (turn % 2 == 0):
        teamsPieces = black_pieces
    else:
        teamsPieces = white_pieces

    if (checkedKing is None):
        for piece in teamsPieces:
            if ((piece.getPosition() == mouse_pos) and (piece.getVisible())):
                returnedPiece = piece
                moves = piece.getMoves()
    elif (checkedKing is not None):
        for piece in teamsPieces:
            if ((piece.getPosition() == mouse_pos) and (piece.getVisible())):
                for pieceKey, possMoves in possibleMoves.items():
                    testToKey = piece.getID()
                    if (testToKey == pieceKey):
                        for pieceMoves in piece.getMoves():
                            if pieceMoves in possMoves:
                                piece = piece
                                moves.append(pieceMoves)

    return returnedPiece, moves


# Function for moving game pieces
def movePiece(piece, moves: list, mouse_pos: tuple):
    output = False
    castle = False
    returnedPiece = None

    if (mouse_pos in moves):
        piece.setPosition(mouse_pos)
        if (piece.getName() == "King"):
            if (mouse_pos[0] == 1 or mouse_pos[0] == 6):
                castle = True
                returnedPiece = piece
        output = True

    return output, castle, returnedPiece


def checkCapture(movedPiece):
    pieceCaptured = False

    for piece in all_pieces:
        if ((piece.getPosition() == movedPiece.getPosition()) and (piece.getColor() != movedPiece.getColor())):
            piece.setVisible(False)
            pieceCaptured = True
        elif (movedPiece.getName() == "Pawn"):
            pawnX, pawnY = movedPiece.getPosition()
            if (piece.getName() == "Pawn" and piece.getColor() != movedPiece.getColor() and piece.moves == 1):
                if ((piece.getPosition() == (pawnX, pawnY - 1) and piece.getColor() == "white") or (
                        piece.getPosition() == (pawnX, pawnY + 1) and piece.getColor() == "black")):
                    piece.setVisible(False)
                    pieceCaptured = True

    return pieceCaptured


# Check other pieces for move when checked
def checkOtherMoves(king):
    possibleMoves = {}

    for friendPiece in all_pieces:
        if (friendPiece.getColor() == king.getColor()):
            movesPerPiece = []
            moves = friendPiece.getMoves()
            for move in moves:
                originalPos = friendPiece.getPosition()
                friendPiece.setPosition(move)
                allEnemyMoves = []
                for enemyPieces in all_pieces:
                    if ((enemyPieces.getColor() != king.getColor()) and (
                            friendPiece.getPosition() != enemyPieces.getPosition())):
                        enemyMoves = enemyPieces.getMoves()
                        for enemyMove in enemyMoves:
                            allEnemyMoves.append(enemyMove)
                if (king.getPosition() not in allEnemyMoves):
                    movesPerPiece.append(move)
                friendPiece.setPosition(originalPos)

            key = friendPiece.getID()
            possibleMoves.update({key: movesPerPiece})

    return possibleMoves


# Check if king in check
def KingChecked(movedPiece):
    checked = False
    checkedKing = None
    mated = False
    possibleMoves = None

    for piece in all_pieces:
        if (piece.getColor() != movedPiece.getColor()):
            if (piece.getPosition() in movedPiece.getMoves()):
                if (piece.getName() == "King"):
                    checked = True
                    checkedKing = piece
    if (checked):
        mated, possibleMoves = KingMated(checkedKing)

    return checkedKing, mated, possibleMoves


# Check if mate
def KingMated(king):
    mated = False

    possibleMoves = checkOtherMoves(king)
    totalVal = []
    for val in possibleMoves.values():
        totalVal += val

    if (totalVal == []):
        mated = True

    return mated, possibleMoves


# Single function for drawing board and pieces on screen
def draw(src: pygame.Surface, size: list, castle: bool = None, kingPiece=None, moves: list = None):
    drawBoard(src, size, moves)
    drawPieces(src, size, castle, kingPiece)


def gameEnd(src: pygame.Surface):
    width, height = src.get_size()

    surface = pygame.Surface((width, height))
    surface.fill((150, 0, 0))
    retryButton = pygame.draw.rect(surface, black, [width / 2.6, height / 2, width / 4, height / 6], border_radius=3)

    gameOverText = pygame.font.SysFont('impact', int(40 * height / 550)).render("Game Over!", True, black)
    gameOverRect = gameOverText.get_rect(center=(width / 2, height / 3))
    retryText = pygame.font.SysFont('impact', int(25 * height / 550)).render("Retry?", True, white)
    retryRect = retryText.get_rect(center=retryButton.center)

    surface.blit(retryText, retryRect)
    surface.blit(gameOverText, gameOverRect)
    src.blit(surface, (0, 0))

    return retryButton


# Main loop for pygame events
def loop(src: pygame.Surface):
    done = False
    piece = None
    moves = None
    ended = False
    checkedKing = None
    possibleMoves = None
    turn = 1
    doDraw = True
    castle = False
    movedPiece = None
    retryButton = None

    while (not done):
        for event in pygame.event.get():
            vidInfo = pygame.display.Info()
            size = [(vidInfo.current_w), (vidInfo.current_h)]
            board_size = [(2 * size[0]) / 3, size[1]]
            width = board_size[0] / 8
            height = board_size[1] / 8

            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.VIDEORESIZE:
                size = list(event.size)
                board_size = [(2 * size[0]) / 3, size[1]]
                if (doDraw):
                    draw(src, board_size, moves)
                else:
                    gameEnd(src)

            if event.type == pygame.MOUSEBUTTONUP:
                moved = False
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = (floor(mouse_pos[0] / width), floor(mouse_pos[1] / height))

                if (ended):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    topLeft = retryButton.topleft
                    topRight = retryButton.topright[0]
                    bottomLeft = retryButton.bottomleft[1]

                    if (topLeft[0] < mouseX < topRight and topLeft[1] < mouseY < bottomLeft):
                        onReset()

                if ((piece is not None) and (mouse_pos not in piece.getMoves())):
                    moves = None
                    piece = None
                else:
                    if ((piece is None)):
                        piece, moves = getPieceMoves(turn, mouse_pos, checkedKing, possibleMoves)
                    if (piece is not None):
                        moved, castle, movedPiece = movePiece(piece, moves, mouse_pos)
                    if (moved):
                        checkCapture(piece)
                        checkedKing, mated, possibleMoves = KingChecked(piece)
                        if (mated):
                            print("Ended")
                            retryButton = gameEnd(src)
                            ended = True
                            doDraw = False
                            break
                        moves = None
                        piece = None
                        turn += 1
                if (doDraw):
                    draw(src, board_size, castle, movedPiece, moves)

        pygame.display.flip()


# main function setting defaults
def main():

    pygame.init()

    src = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption(config['app']['title'])

    clock = pygame.time.Clock()
    clock.tick(50)

    draw(src, [(2 * screen_size[0]) / 3, screen_size[1]])
    print("Running...\n")
    loop(src)

    pygame.quit()


# Start game
if __name__ == "__main__":
    main()
