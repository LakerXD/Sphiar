import pygame
from sys import exit


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        size = width, height = int(input()), int(input())
    except Exception:
        print("Неверный формат ввода")
        pygame.quit()
        exit()
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, width-1, height-1))
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
