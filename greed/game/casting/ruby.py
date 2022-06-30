from game.casting.gem import Gem

class Ruby(Gem):
    # Rubys will increase the player's movement speed for a time.
    def __init__(self):
        super().__init__()
        self._point_value = 2
        