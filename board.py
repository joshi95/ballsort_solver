class Board:
    def __init__(self, glasses):
        self._glasses = glasses
        self.no_of_colors = self._calculate_colors_required()

    def _is_glass_complete(self):

    def get_glasses(self):
        return self._glasses

    def _get_glass_by_idx(self, idx):
        return self._glasses[idx]

    def _calculate_colors_required(self):
        colors = set()
        for glass in self._glasses:
            balls = glass.get_all_balls()
            for ball in balls:
                colors.add(ball)
        return len(colors)
