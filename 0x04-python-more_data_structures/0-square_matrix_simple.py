#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    print(matrix)
    new_matrix = [[i ** 2 for i in row] for row in matrix]
    print(new_matrix, end=" ")            

square_matrix_simple()