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
#['brook.png', 'bknight.png', 'bbishop.png', 'bqueen.png', 'bking.png']
#['wrook.png', 'wknight.png', 'wbishop.png', 'wqueen.png', 'wking.png']
white_pieces = [rook('white', [0, 0], width, height), rook('white', [4, 0], width, height)]
black_pieces = [rook('black', [7, 7], width, height), rook('black', [4, 7], width, height)]


def drawPieces(src, pieces):
    for piece in pieces:
        piece.draw(src)

def drawBoard(src):
    color_pic = 0
    for row in range(8):
        for column in range(8):
            if color_pic == 0:
                color = white
            if color_pic == 1:
                color = black
            #print(row, column, color)
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


def loop(src):
    done = False
    while not done:
        pygame.display.flip()
        for event in pygame.event.get():
            ...


def main():
    pygame.init()
    src = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Grid')
    clock = pygame.time.Clock()
    clock.tick(50)
    drawBoard(src)
    drawPieces(src, white_pieces)
    drawPieces(src, black_pieces)
    print('white corner rook moves: ', white_pieces[0].getMoves(white_pieces, black_pieces))
    print('white middle rook moves; ', white_pieces[1].getMoves(white_pieces, black_pieces))
    print('black corner rook moves: ', black_pieces[0].getMoves(black_pieces, white_pieces))
    print('black middle rook moves: ', black_pieces[1].getMoves(black_pieces, white_pieces))
    loop(src)


if __name__ == '__main__':
    main()
