import pygame
from rook import rook

# var's
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
green = (0, 255, 0)
window_size = [350, 350]
width = window_size[0] / 8
height = window_size[1] / 8
margin = 5
# ['brook.png', 'bknight.png', 'bbishop.png', 'bqueen.png', 'bking.png']
# ['wrook.png', 'wknight.png', 'wbishop.png', 'wqueen.png', 'wking.png']
white_pieces = [rook('white', [0, 0], width, height, True), rook('white', [4, 0], width, height, True)]
black_pieces = [rook('black', [7, 7], width, height, True), rook('black', [4, 7], width, height, True)]
selectedPieces = []


def drawPieces(src, pieces):
    for piece in pieces:
        # print(piece.getPosition())
        piece.draw(src, piece.position)


def drawBoard(src):
    color_pic = 0
    for row in range(8):
        for column in range(8):
            if color_pic == 0:
                color = white
            if color_pic == 1:
                color = black
            # print(row, column, color)
            pygame.draw.rect(src,
                             color,
                             [width * column,
                              height * row,
                              width,
                              height])

            color_pic = 0 if color_pic == 1 else 1

        color_pic += 1


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, pos, width, height):
        super().__init__()

        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.image = pygame.image.load('1x/' + image)
        self.image = pygame.transform.scale(self.image, (width, height))


def mouseDown(mouseLoc):
    selected_piece = None
    friends = []
    enemies = []

    white_locations = [[], []]
    for piece in white_pieces:
        white_locations[0].append(piece.position)
        white_locations[1].append(piece)

    black_locations = [[], []]
    for piece in black_pieces:
        black_locations[0].append(piece.position)
        black_locations[1].append(piece)
    # print('white: ', white_locations, 'black: ', black_locations)

    for i in range(len(white_locations[0])):
        if mouseLoc == white_locations[0][i]:
            selected_piece = white_locations[1][i]
            enemies = black_pieces
            friends = white_pieces
    for i in range(len(black_locations[0])):
        if mouseLoc == black_locations[0][i]:
            selected_piece = black_locations[1][i]
            enemies = white_pieces
            friends = black_pieces

    if selected_piece is not None:
        moves = selected_piece.getMoves(friends, enemies)
        return moves, selected_piece
    else:
        return None, None


def redraw(src, moves):
    drawBoard(src)
    drawPieces(src, white_pieces)
    drawPieces(src, black_pieces)

    if (moves is None) or (len(moves) > 2):
        return None

    for i in range(len(moves[0])):
        pygame.draw.rect(src,
                         green,
                         [width * moves[0][i][0],
                          height * moves[0][i][1],
                          width,
                          height])

    for i in range(len(moves[1])):
        pygame.draw.rect(src,
                         green,
                         [width * moves[1][i][0],
                          height * moves[1][i][1],
                          width,
                          height])


def loop(src):
    global selectedPieces, selectedPiece
    done = False
    moves = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = round(pos[0] // width)
                row = round(pos[1] // height)
                mouseLoc = [col, row]
                if moves is None:
                    # print('moves is none')
                    moves, selectedPiece = mouseDown(mouseLoc)
                elif (mouseLoc in moves[0]) or (mouseLoc in moves[1]):
                    # print('mouseLoc is in moves')
                    selectedPiece.setPosition(mouseLoc)
                    selectedPiece.draw(src, selectedPiece.position)
                    moves = None
                elif (moves is not None) and (mouseLoc not in moves):
                    # print('moves not none mouse location not in moves')
                    moves, selectedPiece = mouseDown(mouseLoc)

                if selectedPiece is not None:
                    if selectedPiece.color == 'black':
                        for piece in white_pieces:
                            if selectedPiece.position == piece.position:
                                piece.setVisable(False)
                    else:
                        for piece in black_pieces:
                            if selectedPiece.position == piece.position:
                                piece.setVisable(False)

                # print(moves)
                redraw(src, moves)

        pygame.display.flip()


def main():
    pygame.init()
    src = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    drawBoard(src)
    drawPieces(src, white_pieces)
    drawPieces(src, black_pieces)

    loop(src)
    pygame.quit()


if __name__ == '__main__':
    main()
