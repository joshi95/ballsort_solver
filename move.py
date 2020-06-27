class Move:
    def __init__(self, _to, _from):
        self._to = _to
        self._from = _from

    def invert(self):
        return Move(self._from, self._to)
