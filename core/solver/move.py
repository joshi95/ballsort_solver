class Move:
    def __init__(self, _from, _to):
        self._to = _to
        self._from = _from

    def invert(self):
        return Move(self._to, self._from)
