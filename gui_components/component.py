from base.dimensions import Dimensions
from base.important_variables import *


class Component(Dimensions):
    color = (0, 0, 0)

    def run(self):
        pass

    def render(self):
        pygame.draw.rect(game_window.get_window(), self.color, (self.left_edge, self.top_edge, self.length, self.height))
