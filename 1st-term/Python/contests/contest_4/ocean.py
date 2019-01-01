from copy import deepcopy


class Game(object):
    # Число 0 кодирует пустую ячейку, 1 скалу, 2 рыбу, 3 креветку.
    def __init__(self, n_generations, w, h, field):
        self.n_generations = n_generations
        self.w = w
        self.h = h
        self.field = field
        self.freeze_field = None

    def modeling_one_generation(self):
        self.freeze_field = deepcopy(self.field)
        for i in range(self.w):
            for j in range(self.h):
                self._upd_value_in_cell(i, j)

    def play(self):
        for i in range(self.n_generations):
            self.modeling_one_generation()
        self._print_field()

    def _upd_value_in_cell(self, i, j):
        neighbours = self._get_neighbours(i, j)
        if self.freeze_field[i][j] == '0':
            if neighbours['2'] == 3:
                self.field[i][j] = '2'
            if neighbours['3'] == 3:
                self.field[i][j] = '3'

        elif self.freeze_field[i][j] == '2':
            if neighbours['2'] >= 4 or neighbours['2'] <= 1:
                self.field[i][j] = '0'

        elif self.freeze_field[i][j] == '3':
            if neighbours['3'] >= 4 or neighbours['3'] <= 1:
                self.field[i][j] = '0'

    def _get_neighbours(self, i, j):
        neighbours = dict.fromkeys(['0', '1', '2', '3'], 0)
        for ii in [i - 1, i, i + 1]:
            for jj in [j - 1, j, j + 1]:
                if ii == i and jj == j:
                    continue
                if 0 <= ii < self.w and 0 <= jj < self.h:
                    neighbours[self.freeze_field[ii][jj]] += 1
        return neighbours

    def _print_field(self):
        for i in range(self.w):
            print(' '.join(self.field[i]))


if __name__ == '__main__':
    n_generations = int(input())
    w, h = list(map(int, input().split()))
    field = []
    for i in range(w):
        field.append(input().split())

    game = Game(n_generations, w, h, field)
    game.play()
