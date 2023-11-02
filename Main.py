import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Shoot The Enemy')
clock = pygame.time.Clock()
text = pygame.font.Font(None, 36)

# Load game assets
game_surface = pygame.image.load('2D.jpg').convert()
wording = text.render('Shoot Them', True, 'purple')

enemy_enter = pygame.image.load('enemy.jpg').convert()
hero_entry = pygame.image.load('hero.jpg').convert()
bullet = pygame.image.load('bullet1.png').convert()
explosion = pygame.image.load('explosion.png').convert()
heart = pygame.image.load('heart.png').convert()

# Initialize game variables
enemies = []
enemy_spawn_interval = 60
enemy_spawn_counter = 0
hero_position = 500
bullets = []
bullet_cooldown = 15
bullet_cooldown_counter = 0
score = 0
explosions = []

# Player lives and game over
lives = 3
game_over = False

# Define explosion duration (in frames)
explosion_duration = 20

def draw_explosion(x, y):
    screen.blit(explosion, (x, y - explosion.get_height()))

def restart_game():
    global lives, game_over, enemies, bullets, score, hero_position
    lives = 3
    game_over = False
    enemies.clear()
    bullets.clear()
    score = 0
    hero_position = 500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(game_surface, (0, 0))
    screen.blit(wording, (200, 50))

    if not game_over:
        # Display lives
        for i in range(lives):
            screen.blit(heart, (550 - i * 30, 10))

        # Increase enemy spawn rate as the score gets higher
        if score < 10:
            enemy_spawn_interval = 60
        elif score < 20:
            enemy_spawn_interval = 40
        else:
            enemy_spawn_interval = 30

        # Enemy Spawning Logic
        enemy_spawn_counter += 1
        if enemy_spawn_counter >= enemy_spawn_interval:
            enemies.append([random.randint(0, 500), 0])
            enemy_spawn_counter = 0

        new_enemies = []
        for enemy in enemies:
            enemy[1] += 2
            if enemy[1] < 500:
                screen.blit(enemy_enter, (enemy[0], enemy[1]))
                new_enemies.append(enemy)
            else:
                lives -= 1  # Enemy crossed the screen, reduce a life
        enemies = new_enemies

        if lives <= 0:
            game_over = True

        # Check for the spacebar key press to shoot a new bullet
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and bullet_cooldown_counter <= 0:
            bullets.append([hero_position + hero_entry.get_width() / 2, 350])
            bullet_cooldown_counter = bullet_cooldown

        # Update the bullet cooldown counter
        if bullet_cooldown_counter > 0:
            bullet_cooldown_counter -= 1

        # Draw and update active bullets
        new_bullets = []
        for bullet_pos in bullets:
            bullet_hit = False
            for enemy in enemies:
                if pygame.Rect(bullet_pos[0], bullet_pos[1], bullet.get_width(), bullet.get_height()).colliderect(
                        pygame.Rect(enemy[0], enemy[1], enemy_enter.get_width(), enemy_enter.get_height())):
                    draw_explosion(enemy[0], enemy[1])  # Draw explosion at enemy position
                    bullet_hit = True
                    score += 1
                    enemies.remove(enemy)
                    break
            if not bullet_hit:
                screen.blit(bullet, (bullet_pos[0], bullet_pos[1]))
                bullet_pos[1] -= 20
            if bullet_pos[1] > 0:
                new_bullets.append(bullet_pos)
        bullets = new_bullets

        # Update explosion animations
        new_explosions = []
        for explosion_info in explosions:
            if explosion_info[1] < explosion_duration:
                draw_explosion(explosion_info[0], explosion_info[2])
                explosion_info[1] += 1
                new_explosions.append(explosion_info)
        explosions = new_explosions

        # Move the hero character
        if keys[pygame.K_LEFT]:
            hero_position -= 5
        elif keys[pygame.K_RIGHT]:
            hero_position += 5

        # Ensure the hero character stays within the screen boundaries
        hero_position = max(0, min(hero_position, 600 - hero_entry.get_width()))

        screen.blit(hero_entry, (hero_position, 350))


    # Display the score
    score_text = text.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Game over screen
    if game_over:
        game_over_text = text.render('Game Over', True, (255, 0, 0))
        replay_text = text.render('Press K to Replay', True, (255, 0, 0))
        screen.blit(game_over_text, (250, 250))
        screen.blit(replay_text, (200, 300))

    # Handle restart if game over
    keys = pygame.key.get_pressed()
    if game_over and keys[pygame.K_k]:
        restart_game()

    pygame.display.update()
    clock.tick(60)
