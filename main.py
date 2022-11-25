import pygame
from sys import exit


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    cub = input().split(" ")
    try:
        if (int(cub[0]) % 4 == 0 and int(cub[0]) <= 100) and (int(cub[1]) >= 0 and int(cub[1]) <= 360):
            wedth = int(cub[0])
            shade = int(cub[1])
        else:
            print("Неверный формат ввода")
            pygame.quit()
            exit()
    except Exception:
        print("Неверный формат ввода")
        pygame.quit()
        exit()
    screen = pygame.display.set_mode((300, 300))
    # формирование кадра:
    # команды рисования на холсте
    pygame.draw.rect(screen, shade, (50, 50, 100, 100))
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
