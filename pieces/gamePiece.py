import pygame

class gamePiece(pygame.sprite.Sprite):

    def __init__(self, image, color, position, screenSize, visible):
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.color = color
        self.position = position
        self.screenSize = screenSize
        self.width = screenSize[0] / 8
        self.height = screenSize[1] / 8
        self.visible = visible
        
    def drawPiece(self, src, position):
        if self.visible:
            self.rect = pygame.Rect((position[0] * self.width), (position[1] * self.height), self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            src.blit(self.image, self.rect)
            
    def getMoves(self):
        raise NotImplementedError("Please implement getMoves")
    
    def setPosition(self):
        raise NotImplementedError("Please implement setPosition")
    
    def setVisible(self):
        raise NotImplementedError("Please implement setVisible")