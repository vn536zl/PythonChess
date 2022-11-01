
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook


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
      'blackPieces': black_pieces,
      'allPieces': all_pieces
    }
}
