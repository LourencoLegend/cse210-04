from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point
import random

class Stone(Actor):
    """A visible, moving thing that can be interacted with. 
    
    The responsibility of stone is to move from the top of the screen
    down to the bottom in a straight line, adding or subtracting points
    from the score if it hits the player.
    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
        _type (string): The type of stone (rock or gem).
        _age (int): Keeps track of the age of the stone.
    """

    def __init__(self):
        """Constructs a new stone"""
        self._type = ""
        self._age = 0

    def setup_stone(self, max_y, cast):
        """Sets the information for the stone"""
        self.set_type()
        self.set_font_size(15)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        self.set_color(color)

        x = random.randint(1, 59)
        y = max_y
        position = Point(x, y)
        self.set_position(position.scale(15))

        self.set_velocity(Point(0, 15))

        cast.add_actor("stones", self)

    def set_type(self):
        """Sets the stones type."""
        random_choice = random.randint(0, 1)
        if random_choice == 0:
            self._type = "rock"
            self._text = "O"
        elif random_choice == 1:
            self._type = "gem"
            self._text = "*"

    def modify_score(self, score):
        """Adds or subtracts a point from the score depending on its type.
        Args:
            score (int): The players current score.
        Returns:
            score (int): The players score after touching stone.
        """
        if self._type == "rock":
            score -= 1
        elif self._type == "gem":
            score += 1

        return score

    def age_stone(self):
        """Increments the age of the stone by one.
        
        Returns:
            age (int): The age of the stone."""
        self._age += 1
        
        return self._age