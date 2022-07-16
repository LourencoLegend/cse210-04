import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.actor import Actor

### ADD PARAMETERS
ROCK_TEXT = 'o'
GEM_TEXT = '*'
GEM_POINTS = 1
ROCK_POINTS = -1
###

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self, cols, rows, cell_size, font_size):
        super().__init__()

        x = random.randint(1, cols - 1)
        y = random.randint(1, rows - 1)
        position = Point(x, y)
        position = position.scale(cell_size)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        self.set_text(random.choice([ROCK_TEXT, GEM_TEXT]))
        self.set_font_size(font_size)
        self.set_color(color)
        self.set_position(position)

        ### ADD POINTS
        if self._text is ROCK_TEXT:
            self.set_points(ROCK_POINTS)
        if self._text is GEM_TEXT:
            self.set_points(GEM_POINTS)
        ###