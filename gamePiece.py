import pygame


class gamePiece(pygame.sprite.Sprite):
    def __init__(self, color, position, image, width, height, visible):
        super().__init__()

        self.color = color
        self.width = width
        self.height = height
        self.position = position
        self.imageFile = image
        self.visible = visible
        self.image = pygame.image.load(self.imageFile)

    def draw(self, src, position):
        if self.visible:
            self.rect = pygame.Rect((position[0] * self.width), (position[1] * self.height), self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            src.blit(self.image, self.rect)

    def getMoves(self):
        raise NotImplementedError("Implement getMoves!")

    def setPosition(self):
        raise NotImplementedError("Implement setPosition")

    def setVisible(self):
        raise NotImplementedError("Implement setVisible")


