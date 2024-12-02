import random

class Matrix:
    def __init__(self, n, m):
        self.matrix = []
        self.row = n
        self.col = m

        for i in range(n):
            row = []
            for j in range(m):
                row.append(random.randint(1, 10))
            self.matrix.append(row)

    def display(self):

        print("Matrix:")
        for row in self.matrix:
            print(row)


    def mean(self):

        total = sum(sum(row) for row in self.matrix)
        length = self.row * self.col
        return total / length if length > 0 else ZeroDivisionError

    def sum_of_row(self, row_index):

        if 0 <= row_index < self.row:
            return sum(self.matrix[row_index])
        else:
            raise IndexError("Row index out of range.")

    def average_of_col(self, col_index):

        if 0 <= col_index < self.col:
            col_sum = sum(row[col_index] for row in self.matrix)
            return col_sum / self.row
        else:
            raise IndexError("Column index out of range.")

    def submatrix(self,row1,row2,col1,col2):
        if 0 <= row1 <= row2 <= self.row and 0 <= col1 <= col2 <= self.col:
            print('Submatrix is: ')
            for i in range(row1,row2+1):
                print(self.matrix[i][col1:col2+1])


matrix = Matrix(3, 3)
matrix.display()
print(f"Mean of the matrix: {matrix.mean():}")
print(f"Sum of row 0: {matrix.sum_of_row(0)}")
print(f"Average of column 1: {matrix.average_of_col(1):}")
matrix.submatrix(0,1,1,2)
