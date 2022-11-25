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
    pygame.draw.arc(screen, (255, 255, 255), (0, 0, width, height), 0, 10)
    pygame.draw.arc(screen, (255, 255, 255), (0, 10, width+10, height), 0, 10)
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
