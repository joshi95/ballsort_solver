def does_move_solve_the_board(board, moves):
    clone_board = board.clone()
    for move in moves:
        clone_board.move_ball(move)
    return clone_board.is_complete()
