
# Import Piece definition
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook

Pawn('white', (4, 6), True)
Pawn('black', (4, 1), True)

white_pieces = [Rook('white', (0, 7), True), Knight('white', (1, 7), True),
                Bishop('white', (2, 7), True), Queen('white', (3, 7), True),
                King('white', (4, 7), True), Bishop('white', (5, 7), True),
                Knight('white', (6, 7), True), Rook('white', (7, 7), True)]
black_pieces = [Rook('black', (0, 0), True), Knight('black', (1, 0), True),
                Bishop('black', (2, 0), True), Queen('black', (3, 0), True),
                King('black', (4, 0), True), Bishop('black', (5, 0), True),
                Knight('black', (6, 0), True), Rook('black', (7, 0), True)]

for i in range(8):
    black_pieces.append(Pawn('black', (i, 1), True))
    white_pieces.append(Pawn('white', (i, 6), True))

all_pieces = []
black_defaults = []
white_defaults = []
for piece in white_pieces:
    all_pieces.append(piece)
    white_defaults.append({'Name': piece.getID(), 'Visibility': piece.getVisible(), 'Position': piece.getPosition()})
for piece in black_pieces:
    all_pieces.append(piece)
    black_defaults.append({'Name': piece.getID(), 'Visibility': piece.getVisible(), 'Position': piece.getPosition()})

config = {
    'app': {
        'env': 'dev',
        'title': 'PyChess'
    },

    'screenSize': [550, 450],

    'color': {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'green': (0, 150, 0)
    },

    'pieces': {
        'whitePieces': white_pieces,
        'whiteDefaults': white_defaults,
        'blackPieces': black_pieces,
        'blackDefaults': black_defaults,
        'allPieces': all_pieces
    }
}
