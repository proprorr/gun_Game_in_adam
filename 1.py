import pygame, controles
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controles.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controles.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            controles.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controles.update_bullets(screen, stats, sc, inos, bullets)
            controles.update_inos(stats, screen, sc, gun, inos, bullets)
run()






