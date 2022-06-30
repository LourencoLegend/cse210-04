from game.casting.rock import Rock

class Lead(Rock):
    # Lead is a heavier rock that will penalize the player more, and also slow the ship.
    def __init__(self):
        super().__init__()
        self._point_value = -5
    
    