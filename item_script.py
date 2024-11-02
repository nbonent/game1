import pygame
import math
weapon_body_list = []
weapon_list = []

class weapon:
    def __init__(self, size: tuple = (30, 20), color: tuple = (150, 140, 90),
             x: float = 0, y: float = 0):
        self.weapon_size = size
        self.weapon_color = color
        self.weapon_surf = pygame.surface.Surface(size=self.weapon_size)
        self.weapon_body = self.weapon_surf.get_rect(x=x, y=y)
        self.rendering_surf = None
        self.projectile = pygame.Rect(self.weapon_body.centerx, self.weapon_body.centery, 15, 15)
        self.projectile_tau = 0
        self.fire_flag = False

        weapon_list.append(self)
        weapon_body_list.append(self.weapon_body)


    def rendering(self, rendering_surf: pygame.surface.Surface = None, color: tuple = None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf

        rendering_surf = self.rendering_surf
        if color is None:
            color = self.weapon_color
        self.weapon_surf.fill(color)
        rendering_surf.blit(self.weapon_surf, self.weapon_body)

        if not self.fire_flag:
            self.projectile.x = self.weapon_body.centerx
            self.projectile.y = self.weapon_body.centery
        else:
            pygame.draw.rect(rendering_surf, color=(100, 80, 80), rect=self.projectile)
            self.projectile.x += 50 * self.projectile_tau * math.cos(math.radians(45))
            self.projectile.y -= (10 * self.projectile_tau * math.sin(math.radians(45)) - (9.81 * self.projectile_tau ** 2) / 2)
            self.projectile_tau += 0.15
            if self.projectile.y > 500 or self.projectile.x > 500:
                self.projectile_tau = 0
                self.fire_flag = False

    def fire(self):
        self.fire_flag = True


