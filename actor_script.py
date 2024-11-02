import pygame
import item_script

class actor:
    def __init__(self, size:tuple = (50, 100), color: tuple = (255,255,0),
            x:float = 0, y:float = 0):
        self.actor_size = size
        self.actor_color = color
        self.actor_surf = pygame.surface.Surface(size=self.actor_size)
        self.actor_body = self.actor_surf.get_rect(x=x,y=y)
        self.rendering_surf = None
        self.backpack = []

    def rendering(self,rendering_surf: pygame.surface.Surface = None, color: tuple = None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf

        rendering_surf = self.rendering_surf
        if color is None:
            color = self.actor_color
        self.actor_surf.fill(color)
        rendering_surf.blit(self.actor_surf,self.actor_body)

    def get_hit(self,projectile: pygame.rect.Rect):
        if self.actor_body.colliderect(projectile):
            self.rendering(color = (255,0,0))

    def take_item(self, item_list):
        if self.actor_body.collidelist(item_list)!= -1:
            current_item_index = self.actor_body.collidelist(item_list)
            item_list[current_item_index].x = self.actor_body.centerx
            item_list[current_item_index].y = self.actor_body.centery
            self.backpack.append(item_script.weapon_list[current_item_index])


