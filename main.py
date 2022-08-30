from math import *
import pygame
import pieces.gamePiece

black, white = (0, 0, 0), (255, 255, 255)
screen_size = [350, 350]
width = screen_size[0] / 8
height = screen_size[1] / 8

def loop(src):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown()
        pygame.display.flip()

def drawBoard(src):
    color_pic = 0
    for y in range(8):
        for x in range(8):
            if color_pic == 0:
                color = white
            elif color_pic == 1:
                color = black
            pygame.draw.rect(src, color, [width * x, height * y, width, height])
            color_pic = 0 if color_pic == 1 else 1
        color_pic += 1
            

def mouseDown():
    mouse_pos = pygame.mouse.get_pos()
    print("Mouse x: ", floor(mouse_pos[0] / width) + 1, " Mouse y: ", floor(mouse_pos[1] / height) + 1)

def main():
    pygame.init()
    src = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    clock.tick(50)
    drawBoard(src)
    print("running...")
    loop(src)
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()