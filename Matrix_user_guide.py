# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:05:40 2021

@author: 1229290416
"""

from Matrix import Matrix

M = Matrix([[1, 1, 3], 
            [1, 1, -3],
            [3, -3, -3]])

a = Matrix([[1], 
            [5], 
            [2]])


# print the matrix itself:
print("M.get_matrix() : ", M.get_matrix())
print()

# print the number at row 3 and column 1:
print("M.get_number(3, 1) : ", M.get_number(3, 1))
print()

# multiply row 1 by number 2:
M.multiply_row_by(1, 2)
print("M.multiply_row_by(1, 2) : ", M.get_matrix())
print()

# subtract row 1 by 2 times row 3:
M.subtract_row_by_n_times_row(1, 2, 3)
print("M.subtract_row_by_n_times_row(1, 2, 3) : ", M.get_matrix())
print()

# return the inverse of the matrix, by Gaussian elimination:
M_inverse = M.inverse_by_gaussian_elimination()
print("M.inverse_by_gaussian_elimination() : ", M_inverse.get_matrix())
print()

# matrix M multiply matrix a:
product = M.multiply(a)
print("M.multiply(a) : ", product.get_matrix())
print()

# return the transpose of matrix M:
M_transpose = M.transpose()
print("M.transpose() : ", M_transpose.get_matrix())
print()

# return the cominor matrix M_12:
M_ij = M.cominor(1, 2)
print("M.cominor(1, 2) : ", M_ij.get_matrix())
print()

# return the determinant of matrix M:
determinant = M.det()
print("M.det() : ", determinant)
print()

# return the adjoint matrix of matrix M:
M_adjoint = M.adjoint()
print("M.adjoint() : ", M_adjoint.get_matrix())
print()

# return the inverse matrix of M:
M_inver = M.inverse()
print("M.inverse() : ", M_inver.get_matrix())
print()






