from game.casting.artifact import Artifact

class Gem(Artifact):
    # A gem is an artifact that will increase the player's score when collected.
    def __init__(self):
        super().__init__()
        self._point_value = 1

    def get_point_value(self):
        # Returns the amount of points to add to the score on contact.
        return self._point_value