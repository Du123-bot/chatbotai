import pygame
import random

pygame.init()

# Kích thước cửa sổ trò chơi
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Tốc độ khung hình
clock = pygame.time.Clock()

# Lớp Bird (Chim)
class Bird:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = -10

# Lớp Pipe (Ống nước)
class Pipe:
    def __init__(self, x):
        self.width = 50
        self.height = random.randint(150, 400)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = SCREEN_HEIGHT - self.height

    def update(self):
        self.rect.x -= 5

# Khởi tạo đối tượng
bird = Bird()
pipes = [Pipe(SCREEN_WIDTH + 100), Pipe(SCREEN_WIDTH + 300)]

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    bird.update()
    screen.blit(bird.image, bird.rect)

    for pipe in pipes:
        pipe.update()
        if pipe.rect.x < -pipe.width:
            pipes.remove(pipe)
            pipes.append(Pipe(SCREEN_WIDTH))
        screen.blit(pipe.image, pipe.rect)

    if bird.rect.y > SCREEN_HEIGHT or bird.rect.y < 0:
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
