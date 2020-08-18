import pygame

pygame.init()
window = pygame.display.set_mode([800, 580])

while True:
  window.fill((255, 255, 255))

  pygame.draw.rect(
    window,
    (0, 0, 255),
    [100, 100, 100, 200]
  )

  pygame.draw.circle(
    window,
    (0, 255, 0),
    [650, 200],
    50
  )

  pygame.draw.ellipse(
    window,
    (255, 255, 0),
    [500, 400, 250, 150]
  )

  pygame.draw.polygon(
    window,
    (255, 0, 0),
    [[50, 500], [250, 500], [150, 400]]
  )

  pygame.display.update()