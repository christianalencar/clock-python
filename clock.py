
import time
import math

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Relógio Digital")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def draw_clock():
    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, (250, 250), 200, 5)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = 250 + math.cos(angle) * 160
        y = 250 + math.sin(angle) * 160
        number = pygame.font.Font(None, 40).render(str(i), True, WHITE)
        number_rect = number.get_rect(center=(x, y))
        window.blit(number, number_rect)

    now = time.localtime()
    hour_angle = math.radians(now.tm_hour * 30 - 90)
    minute_angle = math.radians(now.tm_min * 6 - 90)
    second_angle = math.radians(now.tm_sec * 6 - 90)

    # Desenhar ponteiro das horas
    pygame.draw.line(window, GREEN, (250, 250), (250 + math.cos(hour_angle) * 80, 250 + math.sin(hour_angle) * 80), 10)
    # Desenhar ponteiro dos minutos
    pygame.draw.line(window, WHITE, (250, 250), (250 + math.cos(minute_angle) * 120, 250 + math.sin(minute_angle) * 120), 5)
    # Desenhar ponteiro dos segundos
    pygame.draw.line(window, GREEN, (250, 250), (250 + math.cos(second_angle) * 140, 250 + math.sin(second_angle) * 140), 2)

    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    time.sleep(1)

pygame.quit()