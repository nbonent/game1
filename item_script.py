import pygame
weapon_list=[]

class weapon:
    def __init__(self, size: tuple = (30, 20), color: tuple = (150, 140, 90),
             x: float = 0, y: float = 0):
        self.weapon_size = size
        self.weapon_color = color
        self.weapon_surf = pygame.surface.Surface(size=self.weapon_size)
        self.weapon_body = self.weapon_surf.get_rect(x=x, y=y)
        self.rendering_surf = None
        weapon_list.append(self.weapon_body)


    def rendering(self, rendering_surf: pygame.surface.Surface = None, color: tuple = None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf

        rendering_surf = self.rendering_surf
        if color is None:
            color = self.weapon_color
        self.weapon_surf.fill(color)
        rendering_surf.blit(self.weapon_surf, self.weapon_body)
    
    '''def fire(self,projectile):
        pygame.draw.rect(main_screen, color=(155, 110, 180), rect=stone)
        projectile.x = 100 * t
        projectile.y = self.weapon_body.centery'''