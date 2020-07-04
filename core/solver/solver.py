from traversal.bfs import BFS
from traversal.dfs import DFS


class Node:
    def get_hash(self):
        raise NotImplementedError("error: need an implementation for get_hash")

    def get_neighbors(self):
        raise NotImplementedError("error: need an implementation for get_hash")


class GraphNode(Node):
    def __init__(self, board, prev_move, prev_node):
        self.prev_node = prev_node
        self.board = board
        self.prev_move = prev_move

    def get_neighbors(self):
        n = list()
        for move in self.board.calculate_all_potential_moves():
            if self.board.is_glass_complete(move._from):
                continue

            new_board = self.board.clone()
            new_board.move_ball(move)
            n.append(GraphNode(new_board, move, self))
        return n

    def get_hash(self):
        glasses = self.board.get_glasses()
        return ";".join([str(glass) for glass in glasses])

    def get_board(self):
        return self.board

    def get_moves_to_node(self):
        moves = []
        if self.prev_node is not None:
            moves.extend(self.prev_node.get_moves_to_node())
        if self.prev_move is not None:
            moves.append(self.prev_move)
        return moves


def solver(board):
    startNode = GraphNode(board, None, None)

    traversal = BFS(startNode)
    while not traversal.is_done():
        current_node = traversal.cur_node()
        is_solved = current_node.get_board().is_complete()
        if is_solved:
            return {
                "isSolvable": True,
                "moves": current_node.get_moves_to_node()
            }
        traversal.iterate()

    return {
        "isSolvable": False,
        "moves": []
    }
