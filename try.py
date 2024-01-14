import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycasting Example")
clock = pygame.time.Clock()

# Dot properties
dot_radius = 10
dot_pos = [WIDTH // 2, HEIGHT // 2]

# Obstacle properties
obstacles = [
    pygame.Rect(300, 200, 50, 200),
    pygame.Rect(400, 100, 100, 50),
    pygame.Rect(600, 300, 50, 150),
]

# Ray properties
ray_count = 8
ray_length = 100
ray_width = 3

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 255, 0), obstacle)

    # Draw the dot
    pygame.draw.circle(screen, RED, (int(dot_pos[0]), int(dot_pos[1])), dot_radius)

    # Cast rays from the dot
    for i in range(ray_count):
        angle = i * (2 * math.pi) / ray_count
        end_point = (dot_pos[0] + math.cos(angle) * ray_length, dot_pos[1] + math.sin(angle) * ray_length)

        ray = pygame.draw.line(screen, RED, dot_pos, end_point, ray_width)

        # Check for intersection with obstacles
        for obstacle in obstacles:
            if ray.colliderect(obstacle):
                intersection_point = ray.clipline(obstacle.topleft, obstacle.bottomright)
                if intersection_point:
                    pygame.draw.circle(screen, RED, (int(intersection_point[0][0]), int(intersection_point[0][1])), 5)

                    # Calculate distance
                    distance = math.hypot(intersection_point[0][0] - dot_pos[0], intersection_point[0][1] - dot_pos[1])
                    print(f"Intersection at {intersection_point}, Distance: {distance}")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()