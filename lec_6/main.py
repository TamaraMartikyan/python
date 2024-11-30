import random

def generate_matrix(rows,cols):
    matrix = []

    for i in range(rows):
        row=[]

        for j in range(cols):
            row.append(random.randint(1,10))

        matrix.append(row)
    return matrix


def get_col_sum(matrix, index):
    col_sum=0
    for row in matrix:
        col_sum+=row[index]
    return col_sum


def get_row_average (matrix,row_index):
    average=0
    for row in matrix:
        average=sum(row)/len(row)
    return average


rows=int(input('Enter the number of rows: '))
cols=int(input('Enter the number of columns: '))
matrix= generate_matrix(rows,cols)


for row in matrix:
    print(row)

index=int(input('Enter an index of the column: '))
result=get_col_sum(matrix,index)
print(f'Sum of {index} column is {result}')

row_index=int(input('Enter an index of the row: '))
result=get_row_average(matrix,row_index)
print(f'The average of {row_index} row is {result}')




