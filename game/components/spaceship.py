import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH


class SpaceShip(Sprite):
    SPACESHIP_WIDTH = 60
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH // 2
    Y_POS = 500
    SPEED = 15

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()  # Al instanciar el metodo get_rect() tenemos acceso a varias funcionalidades
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = "player"
        self.shooting_time = random.randint(30, 50)

    def update(self, user_input, game):
        self.shoot(game.bullet_manager)
        # Diagonalmente hacia la izquierda y arriba
        if user_input[pygame.K_UP] and user_input[pygame.K_LEFT]:
            if self.rect.top > SCREEN_HEIGHT // 2 and self.rect.left > -self.SPACESHIP_WIDTH:
                self.rect.x -= self.SPEED
                self.rect.y -= self.SPEED
            elif self.rect.top < SCREEN_HEIGHT // 2 and self.rect.left > -self.SPACESHIP_WIDTH:
                self.rect.x -= self.SPEED - 10
            else:
                self.rect.x = SCREEN_WIDTH
        # Diagonalmente hacia la izquierda y abajo
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_LEFT]:
            if self.rect.bottom < SCREEN_HEIGHT and self.rect.left > 0:
                self.rect.x -= self.SPEED
                self.rect.y += self.SPEED
            elif self.rect.bottom > SCREEN_HEIGHT and self.rect.left > -self.SPACESHIP_WIDTH:
                self.rect.x -= self.SPEED - 10
            else:
                self.rect.x = SCREEN_WIDTH

        # Diagonalmente hacia la derecha y arriba
        elif user_input[pygame.K_UP] and user_input[pygame.K_RIGHT]:
            if self.rect.top > SCREEN_HEIGHT // 2 and self.rect.right < (SCREEN_WIDTH + self.SPACESHIP_WIDTH):
                self.rect.x += self.SPEED
                self.rect.y -= self.SPEED
            elif self.rect.top < SCREEN_HEIGHT // 2 and self.rect.right < (SCREEN_WIDTH + self.SPACESHIP_WIDTH):
                self.rect.x += self.SPEED - 10
            else:
                self.rect.x = -self.SPACESHIP_WIDTH 
        # Diagonalmente hacia la derecha y abajo
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT]:
            if self.rect.bottom < SCREEN_HEIGHT and self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SPEED
                self.rect.y += self.SPEED
            elif self.rect.bottom > SCREEN_HEIGHT and self.rect.right < (SCREEN_WIDTH + self.SPACESHIP_WIDTH):
                self.rect.x += 5
            else:
                self.rect.x = -self.SPACESHIP_WIDTH

        # Movimientos rectilineos
        elif user_input[pygame.K_LEFT]:
            # si la parte izqueirda de la nave esta dentro del
            if self.rect.left > -self.SPACESHIP_WIDTH: 
                self.rect.x -= self.SPEED
            else:
                self.rect.x = SCREEN_WIDTH
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right < (SCREEN_WIDTH + self.SPACESHIP_WIDTH):
                self.rect.x += self.SPEED
            else:
                self.rect.x = -self.SPACESHIP_WIDTH
        elif user_input[pygame.K_UP]:
            if self.rect.top > SCREEN_HEIGHT // 2:
                self.rect.y -= self.SPEED
        elif user_input[pygame.K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time -= random.randint(30, 50)
