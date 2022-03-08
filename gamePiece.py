import pygame


class gamePiece(pygame.sprite.Sprite):
    def __init__(self, color, position, image, width, height):
        super().__init__()

        self.color = color
        self.position = position
        self.rect = pygame.Rect((position[0] * width), (position[1] * height), width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, src):
        src.blit(self.image, self.rect)

    def getMoves(self):
        raise NotImplementedError("Implement getMoves!")

