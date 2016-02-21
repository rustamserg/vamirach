import pygame
from entity import Entity


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell

    def draw(self, map_view, surface):
        if map_view.is_in_view(self.cell):
            px, py = map_view.cell_to_screen(self.cell)
            pygame.draw.circle(surface, pygame.Color(255, 0, 0), (px, py), 10)
            pygame.draw.circle(surface, pygame.Color(0, 0, 0), (px, py), 10, 1)
