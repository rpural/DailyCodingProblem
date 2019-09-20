#! /usr/bin/env python3

import pygame
import random

from pygame.locals import (
        RLEACCEL,
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        )

# Define constants for the width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a Player object by extending Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("rocket.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

        # Keep the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                    )
                )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passws the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Something for the background
class Flare(pygame.sprite.Sprite):
    def __init__(self):
        super(Flare, self).__init__()
        self.image = pygame.image.load("flare_0.png").convert()
        self.rect = self.image.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 50, SCREEN_WIDTH + 200),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constants defined above
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDFLARE = pygame.USEREVENT + 2
pygame.time.set_timer(ADDFLARE, 1000)

# Create the player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
flares = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Set up the event loop
running = True

# Main event loop
while running:
    # Look at every event fired and in the queue
    for event in pygame.event.get():
        # Did the user press a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, end the game
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create a new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new flare?
        elif event.type == ADDFLARE:
            # create a new flare and add it to sprite groups
            new_flare = Flare()
            flares.add(new_flare)
            all_sprites.add(new_flare)


    # Get all the keys pressed since the last pass
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on the keys pressed
    player.update(pressed_keys)

    # Update the enemy position(s)
    enemies.update()

    # Update the flares
    flares.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Add the sprites to the screen
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Check for collisions with enemies
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop.
        player.kill()

    # Render the screen
    pygame.display.flip()
