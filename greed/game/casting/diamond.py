from game.casting.gem import Gem

class Diamond(Gem):
    # A diamond is a special gem that gives more points than normal gems.
    def __init__(self):
        super().__init__()
        self._point_value = 5