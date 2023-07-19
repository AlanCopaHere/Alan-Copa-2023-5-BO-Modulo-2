import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST = [x for x in range(0, (SCREEN_WIDTH - 10), 2)]
    Y_POS = 20
    SPEED_Y = 20
    SPEED_X = 10
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self, enemy_image):
        self.image = pygame.transform.scale(enemy_image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 544)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.movement_x_for = random.randint(9, 13)
        self.index = 0

    def update(self):
        self.rect.y += self.speed_y
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_direction()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_direction(self):
        self.index += 1
        if self.index >= self.movement_x_for or self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            if self.movement_x == 'left':
                self.index = 0
                self.movement_x = 'right'
            else:
                self.index = 0
                self.movement_x = 'left'
                