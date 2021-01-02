import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), np.int)

    def count_surrounding(self, row, col):
        total = 0
        if row == 0:
            if col == 0:
                total = total + self.board[0][1]
                total = total + self.board[1][1]
                total = total + self.board[1][0]
            elif col == self.size - 1:
                total = total + self.board[0][col-1]
                total = total + self.board[1][col-1]
                total = total + self.board[1][col]
            else:
                total = total + self.board[0][col-1]
                total = total + self.board[0][col+1]
                total = total + self.board[1][col-1]
                total = total + self.board[1][col]
                total = total + self.board[1][col+1]
        elif row == self.size - 1:
            if col == 0:
                total = total + self.board[row][1]
                total = total + self.board[row-1][1]
                total = total + self.board[row-1][0]
            elif col == self.size - 1:
                total = total + self.board[row][col-1]
                total = total + self.board[row-1][col-1]
                total = total + self.board[row-1][col]
            else:
                total = total + self.board[row][col-1]
                total = total + self.board[row][col+1]
                total = total + self.board[row-1][col-1]
                total = total + self.board[row-1][col]
                total = total + self.board[row-1][col+1]
        else:
            if col == 0:
                total = total + self.board[row][1]
                total = total + self.board[row-1][1]
                total = total + self.board[row-1][0]
                total = total + self.board[row+1][1]
                total = total + self.board[row+1][0]
            elif col == self.size - 1:
                total = total + self.board[row][col-1]
                total = total + self.board[row-1][col-1]
                total = total + self.board[row-1][col]
                total = total + self.board[row+1][col-1]
                total = total + self.board[row+1][col]
            else:
                total = total + self.board[row][col-1]
                total = total + self.board[row][col+1]
                total = total + self.board[row-1][col-1]
                total = total + self.board[row-1][col]
                total = total + self.board[row-1][col+1]
                total = total + self.board[row+1][col-1]
                total = total + self.board[row+1][col]
                total = total + self.board[row+1][col+1]
        return total

    def next_generation(self):
        new_arr = np.zeros((self.size, self.size), np.int)
        for i in range(self.size):
            for j in range(self.size):
                surrounding = self.count_surrounding(i, j)
                if self.board[i][j] == 1 and 1 < surrounding < 4:
                    new_arr[i][j] = 1
                elif self.board[i][j] == 0 and surrounding == 3:
                    new_arr[i][j] = 1
                else:
                    new_arr[i][j] = 0
        self.board = new_arr
