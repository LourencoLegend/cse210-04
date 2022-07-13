from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest.
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
        _type (string): The type of artifact - 'stone' or 'gem'
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._type = ""
        self._value = 0

    def get_message(self):
        """Gets the artifact's message.
        Returns:
            string: The message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given one.
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_type(self):
        """Gets the artifact's type.
        Returns:
            string: The type.
        """
        return self._type

    def set_type(self, type):
        """Updates the type to the given one.
        Args:
            type (string): The given type.
        """
        self._type = type   # 'stone' or 'gem'
        if type == "gem":
            self._value = 1
        else:
            self._value = -1

    def get_value(self):
        """Gets the artifact's value.
        Returns:
            int: The value - either 1 or -1.
        """
        return self._value