class Player:
    def __init__(self, identity):
        self._identity = identity
        self._name = ""

    def get_identity(self):
        return self._identity

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
