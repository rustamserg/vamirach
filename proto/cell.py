class Cell:
    def __init__(self, row, column, entities):
        self.row = row
        self.column = column
        self.entities = entities

    def draw(self, surface, px, py):
        for entity in self.entities:
            entity.draw(surface, px, py)

    def get_round_bbox(self):
        yield Cell(self.row - 2, self.column, self.entities)
        yield Cell(self.row + 2, self.column, self.entities)
        yield Cell(self.row - 1, self.column - 1, self.entities)
        yield Cell(self.row - 1, self.column + 1, self.entities)
        yield Cell(self.row + 1, self.column - 1, self.entities)
        yield Cell(self.row + 1, self.column + 1, self.entities)
