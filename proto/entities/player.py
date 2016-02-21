import pygame
from core.cell import Cell
from core.entity import Entity
from entities.ground import GroundType


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell

    def draw(self, map_view, surface):
        if map_view.is_in_view(self.cell):
            px, py = map_view.cell_to_screen(self.cell)
            pygame.draw.circle(surface, pygame.Color(255, 0, 0), (px, py), 10)
            pygame.draw.circle(surface, pygame.Color(0, 0, 0), (px, py), 10, 1)

    def on_cell_click(self, map_view, cell):
        for c in Cell.round_bbox(self.cell):
            if c == cell:
                ground_layer = map_view.get_layer('GroundLayer')
                if ground_layer:
                    for ent in ground_layer.entities:
                        if ent.cell == cell and ent.ground_type == GroundType.GRASS:
                            map_view.move_view(cell)
                            self.cell = cell
                            break