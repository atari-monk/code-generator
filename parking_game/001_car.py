import os

# Define the content for each file
files = {
    'game_window.py': '''import pygame
import sys

# Constants for window size
WIDTH, HEIGHT = 800, 600
FPS = 60

class GameWindow:
    def __init__(self, width=WIDTH, height=HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Parking Simulator")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()

    def fill(self, color):
        self.screen.fill(color)

    def tick(self):
        self.clock.tick(FPS)

    def quit(self):
        pygame.quit()
        sys.exit()
''',

    'car.py': '''from math import sin, cos, radians
import pygame

class Car:
    def __init__(self, x, y, angle=0):
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        self.image.fill((255, 0, 0))  # Car color (Red)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle

    def update(self, keys):
        # Rotate the car
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        
        # Move forward/backward
        if keys[pygame.K_UP]:
            self.rect.x += 5 * cos(radians(self.angle))
            self.rect.y -= 5 * sin(radians(self.angle))
        elif keys[pygame.K_DOWN]:
            self.rect.x -= 5 * cos(radians(self.angle))
            self.rect.y += 5 * sin(radians(self.angle))

    def draw(self, surface):
        # Rotate the image to reflect the current angle
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, new_rect.topleft)
''',

    'game_loop.py': '''import pygame

class GameLoop:
    def __init__(self, game_window, car):
        self.game_window = game_window
        self.car = car

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            # Update car movement
            self.car.update(keys)

            # Clear screen and redraw everything
            self.game_window.fill((255, 255, 255))  # White background
            self.car.draw(self.game_window.screen)

            # Update display
            self.game_window.update()
            self.game_window.tick()

        self.game_window.quit()
''',

    'main.py': '''from game_window import GameWindow
from car import Car
from game_loop import GameLoop

def main():
    # Create instances of the classes
    game_window = GameWindow()
    car = Car(400, 300)  # Start car in the center of the screen
    game_loop = GameLoop(game_window, car)

    # Run the game
    game_loop.run()

if __name__ == "__main__":
    main()
'''
}

# Create the files
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)

print("Game structure generated successfully!")
