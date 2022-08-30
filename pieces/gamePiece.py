import pygame

class gamePiece(pygame.sprite.Sprite):

    def __init__(self, image, color, position, screenSize, visible):
        super().__init__(self)
        
        self.image = pygame.image.load(image)
        self.color = color
        self.position = position
        self.screenSize = screenSize
        self.width = screenSize(1) / 8
        self.height = screenSize(0) / 8
        self.visible = visible
        
    def drawPiece(self, src, position =None):
        
        if position == None:
            position = self.position
        
        if self.visible:
            self.rect = pygame.Rect((position(0) * self.width, position(1) * self.height), self.width, self.height)
            self