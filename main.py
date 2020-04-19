import random
from time import sleep
from game import PuzzleGame

initial_state = [5, 1, 7, 3, 9, 2, 11, 4, 13, 6, 15, 8, None, 10, 14, 12]
# initial_state = [1, 2, 3, 4, 5, 6, None, 8, 9, 10, 7, 11, 13, 14, 15, 12]

# initial_state = [12, 1, 10, 2, 7, 11, 4, 14, 5, None, 9, 15, 8, 13, 6, 3]
# initial_state = [2, 5, 13, 12, 1, None, 3, 15, 9, 7, 14, 6, 10, 11, 8, 4]
# initial_state = [5, 2, 4, 8, 10, None, 3, 14, 13, 6, 11, 12, 1, 15, 9, 7]
# initial_state = [11, 4, 12, 2, 5, 10, 3, 15, 14, 1, 6, 7, None, 9, 8, 13]
# initial_state = [5, 8, 7, 11, 1, 6, 12, 2, 9, None, 13, 10, 14, 3, 4, 15]

game = PuzzleGame(initial_state)

game.matrix = game.generate_matrix(initial_state)
print(game)

if (game.is_solvable()):
    random.seed(0)
    print("Goal is reachable!")
    dissimilars = game.count_dissimilar(game.matrix)
    place = game.get_block_place(block=None, matrix=game.matrix)
    prev_move = None
    level = 0

    ## Initiate game
    while(dissimilars > 0):
        level += 1

        moves = game.check_moves(prev_move)
        print("Moves at level {}: {}".format(level, moves))
        dissimilar = {}
        for move in moves:
            if (game.move_allowed(place, game.MOVE[move])):
                new = game.new_place(place, game.MOVE[move])
                new_matrix = game.apply_move(place, new)

                dissimilars = game.count_dissimilar(new_matrix)
                dissimilar[move] = dissimilars

        print("Dissimilars : {}".format(dissimilar))

        dissimilars = min(dissimilar.values())

        dissimilar_moves = list(dissimilar.keys())
        random.shuffle(dissimilar_moves)

        for move in dissimilar_moves:
            if dissimilar[move] == dissimilars:
                prev_move = move

        # dissimilars -= level

        print("Selected move : {}".format(prev_move))

        new_place = game.new_place(place, game.MOVE[prev_move])
        game.matrix = game.apply_move(place, new_place)
        place = new_place
        print(game)
        sleep(0.2)

    print("Total path cost = {}".format(level - 1))

else:
    print("Goal is unreachable!")