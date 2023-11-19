import unittest
import pygame
from unittest.mock import patch
# from Main import game

class TestSum(unittest.TestCase):

    def setUp(self): 
       pygame.init()
       self.screen = pygame.display.set_mode((600, 500))
       pygame.display.set_caption('Shoot The Enemy')
       self.clock = pygame.time.Clock()
       self.text = pygame.font.Font(None, 36)
       self.game_over = False
       self.enemies = []
       self.bullets = []
       self.score = 0

    def tearDown(self):
        pygame.quit()

    # pygame.event.get()
    def test_initialize_game(self):
        self.assertEqual(self.screen.get_size(), (600, 500))
        self.assertEqual(pygame.display.get_caption()[0], 'Shoot The Enemy')
        self.assertIsNotNone(self.clock)
        self.assertIsNotNone(self.text)
        self.assertFalse(self.game_over)
        self.assertListEqual(self.enemies, [])
        self.assertListEqual(self.bullets, [])
        self.game_surface = pygame.image.load('2D.jpg').convert()
        self.wording = self.text.render('Shoot Them', True, 'purple')
        self.enemy_enter = pygame.image.load('enemy.jpg').convert()
        self.hero_entry = pygame.image.load('hero.jpg').convert()
        self.bullets = pygame.image.load('bullet1.png').convert()
        self.explosion = pygame.image.load('explosion.png').convert()
        self.assertIsNotNone(self.explosion)
        self.heart = pygame.image.load('heart.png').convert()
        pygame.quit()

     
    def draw_explosion(self, x,y):
        self.game = self.Game()
        explosion = []
        x = 0
        y = 0
        self.draw_explosion(x, y)
        explosion = pygame.image.load('explosion.png').convert()
        self.screen.blit(explosion, (x, y - explosion.get_height()))
        explosion_duration = 20
        explosion = self.game.draw_explosion()
        for explosion_info in explosions:
            pass

        new_bullets = []
        for bullet_pos in self.bullets:
            bullet_hit = False
            for enemy in enemies:
                if pygame.Rect(bullet_pos[0], bullet_pos[1], self.bullet.get_width(), self.bullet.get_height()).colliderect(
                        pygame.Rect(enemy[0], enemy[1], self.enemy_enter.get_width(), self.enemy_enter.get_height())):
                    self.draw_explosion(enemy[0], enemy[1])  # Draw explosion at enemy position
                    bullet_hit = True
                    score += 1
                    enemies.remove(enemy)
                    break
            if not bullet_hit:
                self.screen.blit(self.bullet, (bullet_pos[0], bullet_pos[1]))
                bullet_pos[1] -= 20
            if bullet_pos[1] > 0:
                new_bullets.append(bullet_pos)
        bullets = new_bullets

        # Update explosion animations
        new_explosions = []
        for explosion_info in explosions:
            if explosion_info[1] < explosion_duration:
                self.draw_explosion(explosion_info[0], explosion_info[2])
                explosion_info[1] += 1
                new_explosions.append(explosion_info)
        explosions = new_explosions

    def test_restart_game(self):
        global lives, game_over, enemies, bullets, score, hero_position
        lives = 3

        def restart_game():
            global lives, game_over, enemies, bullets, score, hero_position
            lives = 3
            game_over = False
            enemies.clear()
            bullets.clear()
            score = 0
            hero_position = 500


        self.game_over = False
        self.enemies.clear()
        self.bullets.clear()
        self.score = 0
        self.hero_position = 500


    def test_enemy_spawning(self):
        global enemy_spawn_interval, enemy_spawn_counter, enemies
        enemy_spawn_interval = 60
        enemy_spawn_counter = 60
        enemies = []

        for _ in range(60):
    #   self.game_loop()
            self.assertEqual(len(self.enemies), 0)

            new_enemies = []
        for enemy in enemies:
            enemy[1] += 2
            if enemy[1] < 500:
                self.screen.blit(self.enemy_enter, (enemy[0], enemy[1]))
                new_enemies.append(enemy)
            else:
                lives -= 1  # Enemy crossed the screen, reduce a life
                enemies = new_enemies


    def test_game_over(self):
        global lives
        lives = 0

        if self.game_over:
            game_over_text = self.text.render('Game Over', True, (255, 0, 0))
            replay_text = self.text.render('Press K to Replay', True, (255, 0, 0))
            self.screen.blit(game_over_text, (250, 250))
            self.screen.blit(replay_text, (200, 300))

            if not game_over:
        # Display lives
                for i in range(lives):
                    self.screen.blit(self.heart, (550 - i * 30, 10))

        # Increase enemy spawn rate as the score gets higher
                if score < 10:
                    enemy_spawn_interval = 60
                elif score < 20:
                    enemy_spawn_interval = 40
                else:
                    enemy_spawn_interval = 30

        # Enemy Spawning Logic
                enemy_spawn_counter += 1
                if  enemy_spawn_counter >= enemy_spawn_interval:
                    enemies.append([self.random.randint(0, 500), 0])
                    enemy_spawn_counter = 0


    def test_display_score(self):
        score_text = self.text.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))


if __name__ == '__main__':
    unittest.main(exit = False)


