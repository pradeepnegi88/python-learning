import pygame
import random
import math
from pygame import mixer

# Initialize the game
pygame.init()
# Create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
# Score
score = 0
my_font = pygame.font.Font('FreeSansBold.ttf', 32)
text_x = 10
text_y = 10

# add music
mixer.music.load("background_music.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

factor = 1
# show score
def show_score(x, y):
    text = my_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# end of game text
end_fornt = pygame.font.Font('FreeSansBold.ttf', 40)


def final_text():
    my_final_font = end_fornt.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_final_font, (width / 2, height / 2))


# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
# Player variable
img_player = pygame.image.load("rocket.png")
player_x = width / 2 - 64
player_y = height - 64 - 100
player_x_change = 0
# enemy variable
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 8
for e in range(number_of_enemies):
    img_enemy.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, width - 64))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)

# bullet variable
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 10
visible_bullet = False


# Player Function
def player(x, y):
    screen.blit(img_player, (x, y))


# Enemy Function
def enemy(x, y, em):
    screen.blit(img_enemy[em], (x, y))


# Shoot bullet
def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x + 16, y + 10))


# Detect collision
def there_is_a_collision(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if dist < 27:
        return True
    else:
        return False


# Game loop
is_running = True
while is_running:
    # RGB
    screen.fill((205, 144, 228))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -factor
            if event.key == pygame.K_RIGHT:
                player_x_change = factor
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('shot.mp3')
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(player_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    # Modify player location
    player_x += player_x_change
    # Keep Player inside screen logic
    if player_x <= 0:
        player_x = 0
    elif player_x >= width - 64:
        player_x = width - 64

    # Modify enemy location
    for enem in range(number_of_enemies):
        # end of game
        if enemy_y[enem] > height:
            for k in range(number_of_enemies):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[enem] += enemy_x_change[enem]
        # Keep enemy inside screen logic
        if enemy_x[enem] <= 0:
            enemy_x_change[enem] = 0.8
            enemy_y[enem] += enemy_y_change[enem]
        elif enemy_x[enem] >= width - 64:
            enemy_x_change[enem] = -0.8
            enemy_y[enem] += enemy_y_change[enem]
        # Collision
        collision = there_is_a_collision(enemy_x[enem], enemy_y[enem], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound('punch.mp3')
            collision_sound.play()
            bullet_y = height - 64 - 100
            visible_bullet = False
            score += 1
            enemy_x[enem] = random.randint(0, width - 64)
            enemy_y[enem] = random.randint(50, 200)
        enemy(enemy_x[enem], enemy_y[enem], enem)

    # Bullet movements
    if bullet_y <= -64:
        bullet_y = height - 64 - 100
        visible_bullet = False

    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
