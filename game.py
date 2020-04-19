from copy import deepcopy

class PuzzleGame:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.matrix = []

        self.MOVE = {
            'UP'    :   (-1, 0),
            'DOWN'  :   (1, 0), 
            'LEFT'  :   (0, -1),
            'RIGHT' :   (0, 1)
            }

    def get_matrix(self):
        matrix = ''
        for row in self.matrix:
            matrix += str(row) + '\n'

        return matrix

    def __str__(self):
        return self.get_matrix()

    def check_moves(self, prev_move):
        if prev_move == None:
            return tuple(self.MOVE.keys())

        if prev_move == 'UP':
            return ('UP', 'LEFT', 'RIGHT')

        if prev_move == 'DOWN':
            return ('DOWN', 'LEFT', 'RIGHT')

        if prev_move == 'LEFT':
            return ('UP', 'DOWN', 'LEFT')

        if prev_move == 'RIGHT':
            return ('UP', 'DOWN', 'RIGHT')

    def move_allowed(self, place, move):
        row, col = self.new_place(place, move)
        if row > 0 and row < 5 and col > 0 and col < 5:
            return True

        else:
            return False

    def new_place(self, place, move):
        return (place[0]+move[0], place[1]+move[1])

    def apply_move(self, place, new_place):
        o_r, o_c = place
        n_r, n_c = new_place

        new_matrix = deepcopy(self.matrix)

        new_matrix[n_r-1][n_c-1] = new_matrix[o_r-1][o_c-1]
        new_matrix[o_r-1][o_c-1] = self.matrix[n_r-1][n_c-1]

        return new_matrix

    def value_replaced(self, new_place):
        n_r, n_c = new_place
        return self.matrix[n_r-1][n_c-1]

    def distance(self, prev_place, new_place):
        x1, y1 = prev_place
        x2, y2 = new_place
        d = abs(x2 - x1) + abs(y2 - y1)

        return d

    def count_dissimilar(self, matrix):
        dissmilar = 0
        count = 1
        for row in matrix:
            for col in row:
                if col and col is not count:
                    dissmilar += 1

                count += 1

        return dissmilar

    def generate_matrix(self, initial_state):
        return [initial_state[i:i+4] for i in range(0, len(initial_state), 4)]

    def generate_numbers(self, grid_size):
        return [i for i in range(1, grid_size)] + [None]

    def is_solvable(self):
        self.place = self.get_block_place(block=None, matrix=self.matrix)
        result = self.sum_less_i() + self.x(block_place=self.place)

        return (result % 2 == 0)

    def get_block_place(self, block, matrix):
        for row in range(0, 4):
            for col in range(0, 4):
                if (matrix[row][col] is block):
                    return (row+1, col+1)

    def sum_less_i(self):
        sumission = 0
        for num in range(0, 16):
            if self.initial_state[num] is None:
                sumission += (16 - (num + 1))
                continue
            
            for current in range(num + 1, 16):
                if (self.initial_state[current] is None):
                    continue

                if (self.initial_state[num] > self.initial_state[current]):
                    sumission += 1

        return sumission

    def x(self, block_place):
        row, col = block_place
        # block is at even row and even col
        # or odd row and odd col 
        if (row + col) % 2 == 0:
            return 0

        else:
            return 1