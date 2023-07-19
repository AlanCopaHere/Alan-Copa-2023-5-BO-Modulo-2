import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT, ENEMY_1, ENEMY_2 

class EnemyManger:
    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.y > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy(self.choice_random_enemy())
            self.enemies.append(enemy)
            
    def choice_random_enemy(self):
        enemy = random.choice([ENEMY_1, ENEMY_2])
        return enemy
        