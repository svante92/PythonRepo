# author: Svante Aretun
# date: March 17, 2023
# Fifteen class

from random import choice

class Fifteen:

    def __init__(self, size=4):
        self.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.size = size
        self.adj = [
            [1, 4],  # 0
            [0, 2, 5],  # 1
            [1, 3, 6],  # 2
            [2, 7],  # 3
            [0, 5, 8],  # 4
            [1, 4, 6, 9],  # 5
            [2, 5, 7, 10],  # 6
            [3, 6, 11],  # 7
            [4, 9, 12],  # 8
            [5, 8, 10, 13],  # 9
            [6, 9, 11, 14],  # 10
            [7, 10, 15],  # 11
            [8, 13],  # 12
            [9, 12, 14],  # 13
            [10, 13, 15],  # 14
            [11, 14]  # 15
        ]

    def update(self, move):
        index = self.tiles.index(move)
        empty_index = self.tiles.index(0)
        if empty_index in self.adj[index]:
            self.tiles[index], self.tiles[empty_index] = self.tiles[empty_index], self.tiles[index]

    def transpose(self, i, j):
        self.adj[i][j], self.adj[j][i] = self.adj[j][i], self.adj[i][j]

    def shuffle(self, steps=100):
        index = self.tiles.index(0)
        for i in range(steps):
            move_index = choice(self.adj[index])
            while not self.is_valid_move(self.tiles[move_index]):
                move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        index = self.tiles.index(move)
        empty_index = self.tiles.index(0)
        return empty_index in self.adj[index]

    def is_solved(self):
        return self.tiles == list(range(1, self.size ** 2)) + [0]

    def draw(self):
        for i in range(self.size):
            print('+-----+-----+-----+-----+')
            for j in range(self.size):
                index = i * self.size + j
                if self.tiles[index] == 0:
                    print('|{: ^5}'.format(' '), end='')
                else:
                    print('|{: ^5}'.format(self.tiles[index]), end='')
                if j == self.size - 1:
                    print('|')
        print('+-----+-----+-----+-----+')

    def __str__(self):
        s = ''
        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                if self.tiles[index] == 0:
                    s += '   '
                else:
                    s += f'{self.tiles[index]:2} '
                if j == self.size - 1:
                    s += '\n'
        return s

if __name__ == '__main__':
    '''
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    '''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')