import pygame
import sys


class GamePiece(pygame.sprite.Sprite):

    def __init__(self, image, color, position, visible, moves):
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.color = color
        self.position = position
        self.visible = visible
        self.moves = moves
        self.width = 0
        self.height = 0
        self.all_pieces = []
        self.name = type(self).__name__
        self.id = type(self).__name__ + str(position[0]) + str(position[1])

    def loadPieces(self, all_pieces):
        for piece in all_pieces:
            if (piece.getVisible()):
                self.all_pieces.append(piece)

    def drawPiece(self, src, position):
        if (self.visible) and (self.width + self.height != 0):
            self.rect = pygame.Rect((position[0] * self.width), (position[1] * self.height), self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            src.blit(self.image, self.rect)
        elif self.width + self.height == 0:
            print("Set the width and height")
            
    def getMoves(self):
        raise NotImplementedError("Please implement getMoves")

    def setPosition(self, selectedPos):
        self.position = selectedPos
        if (sys._getframe(1).f_code.co_name == "movePiece"):
            self.moves += 1

    def setVisible(self, visible):
        self.visible = visible
    
    def setSize(self, size):
        self.width = size[0]/8
        self.height = size[1]/8

    def setMove(self, num):
        self.moves = num

    def getPosition(self):
        return self.position

    def getVisible(self):
        return self.visible

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getID(self):
        return self.id
