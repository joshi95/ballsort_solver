import copy

from move import Move


class Board:
    def __init__(self, glasses):
        self.glasses = glasses
        self.no_of_colors = self._calculate_colors_required()

    def is_glass_complete(self, glass_idx):
        glass = self._get_glass_by_idx(glass_idx)
        return glass.is_full() and glass.has_only_single_color_balls()

    def get_glasses(self):
        return self.glasses

    def _get_glass_by_idx(self, idx):
        return self.glasses[idx]

    def _calculate_colors_required(self):
        colors = set()
        for glass in self.glasses:
            balls = glass.get_all_balls()
            for ball in balls:
                colors.add(ball)
        return len(colors)

    def is_complete(self):
        completed_glass_count = 0
        for idx, _ in enumerate(self.glasses):
            if self.is_glass_complete(idx):
                completed_glass_count += 1
        return completed_glass_count == self.no_of_colors

    def calculate_all_potential_moves(self):
        moves = []
        for to_idx, to_glass in enumerate(self.glasses):
            if to_glass.is_full():
                continue
            from_indexes = self.find_all_movable_glass_indexes(to_idx)
            for from_idx in from_indexes:
                moves.append(Move(from_idx, to_idx))
        return moves

    def find_all_movable_glass_indexes(self, to_index):
        indexes = []
        to_glass = self._get_glass_by_idx(to_index)
        for from_idx, from_glass in enumerate(self.glasses):
            if from_idx == to_index:
                continue
            if from_glass.is_empty():
                continue
            if to_glass.is_empty() or from_glass.get_top() == to_glass.get_top():
                indexes.append(from_idx)
        return indexes

    def move_ball(self, move):
        ball_to_move = self._get_glass_by_idx(move._from).pop_ball()
        self._get_glass_by_idx(move._to).push_ball(ball_to_move)

    def clone(self):
        return copy.deepcopy(self)
