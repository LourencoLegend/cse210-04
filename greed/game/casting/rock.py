from game.casting.artifact import Artifact

class Rock(Artifact):
    # A rock is an artifact that will damage the player's score and ship.
    def __init__(self):
        super().__init__()
        self._point_value = -1
    
    def get_point_value(self):
        # Returns the amount of points to subtract from the score on contact.
        return self._point_value
