# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:15:53 2021

@author: 1229290416
"""

#row vector r times column vector c
def row_times_column(r, c):
    lenth = len(r)
    result = 0
    for i in range(0, lenth, 1):
        result = result + r[i] * c[i]
    
    return result

class Matrix():
    def __init__(self, m):
        
        #initialize, Matrix contains the matrix, its number of rows and columns, and its row vectors and column vectors
        self.dimension = len(m)
        self.number_of_row = len(m)
        self.number_of_column = len(m[0])
        self.matrix = m
        self.column_vectors = []
        self.row_vectors = []
        
        #construct lists for row vectors and column vectors
        for i in range(0, self.number_of_row, 1):
            self.row_vectors.append(self.matrix[i])
            
        for j in range(0, self.number_of_column, 1):
            column = []
            
            for k in range(0, self.number_of_row, 1):
                column.append(self.matrix[k][j])
            
            self.column_vectors.append(column)

    #return true if the matrix is square, false if not
    def check_valid(self):
        if len(self.matrix) == len(self.matrix[0]):
            return True
            
        else: 
            return False
    
    #return column vectors
    def get_column_vectors(self):
        return self.column_vectors
    
    #return row vectors
    def get_row_vectors(self):
        return self.row_vectors
    
    #return the number of rows
    def get_number_of_row(self):
        return self.number_of_row
    
    #return the number of columns
    def get_number_of_column(self):
        return self.number_of_column
    
    #return the value in row i and column j
    def get_number(self, i, j): 
        return self.matrix[i - 1][j - 1]
    
    #return the matrix itself
    def get_matrix(self):
        return self.matrix
           
    #multiply row n by number a
    def multiply_row_by(self, n, a):
        new_row = []
        for i in range(0, self.dimension, 1):
           new_row.append(self.matrix[n - 1][i] * a)
        self.matrix[n - 1] = new_row
        self = Matrix(self.get_matrix())
         
    #subtract row n1 by a times row n2         
    def subtract_row_by_n_times_row(self, n1, a, n2):
        new_row  = []
        for i in range(0, self.dimension, 1):
            new_row.append(
                self.matrix[n1 - 1][i] - a * self.matrix[n2 - 1][i])
        self.matrix[n1 - 1] = new_row
        self = Matrix(self.get_matrix())
    
    #return the inverse of the matrix, by Gaussian elimination
    def inverse_by_gaussian_elimination(self):
        
        #if it is a square matrix, find its inverse
        if self.check_valid() == True:
            D = self.dimension
            temp = [[self.matrix[i][j] for j in range(0, D, 1)] 
                    for i in range(0, D, 1)]
            temp_matrix = Matrix(temp)
            
            unity = [[0.0 for i in range(0, D, 1)] 
                for i in range(0, D, 1)]
            for i in range(0, D, 1):
                unity[i][i] = 1.0
              
            #construct unit matrix
            I = Matrix(unity)
            
            for i in range(1, D + 1, 1):
                
                a = temp_matrix.get_number(i, i)
                counter = 1 + i

                #if the number on position(i, i) is 0, try to use it subtruct next row
                while a == 0 and counter <= D:
                    temp_matrix.subtract_row_by_n_times_row(i, 1, counter)
                    a = temp_matrix.get_number(i, i)
                    counter = counter + 1
                    
                #if the number on position (i, i) is still 0, it is a singular matrix
                if a == 0:
                    return(Matrix(["This is a singular matrix !"]))
                    break
                    
                #start doing Gaussian elimination
                temp_matrix.multiply_row_by(i, 1 / a)
                I.multiply_row_by(i, 1 / a)
                
                for j in range(1, D + 1, 1):
                    if j != i:
                        b = temp_matrix.get_number(j, i)
                        temp_matrix.subtract_row_by_n_times_row(j, b, i)
                        I.subtract_row_by_n_times_row(j, b, i)

            #return the result
            return Matrix(I.get_matrix())
          
        #if it is not a square matrix
        else:
            print("Only a square matrix can have the inverse !")

    #matrix multiplication
    def multiply(self, m):
        if self.get_number_of_column() == m.get_number_of_row():
            row_vectors = self.get_row_vectors()
            column_vectors = m.get_column_vectors()
            result = [[row_times_column(row_vectors[i], column_vectors[j]) 
                      for j in range(0, m.get_number_of_column(), 1)]
                      for i in range(0, self.get_number_of_row(), 1)]
            
            return Matrix(result)
        
        else:
            return Matrix(["The column number and the row number dose not consistence !"])
        
    #transpose of matrix
    def transpose(self):
        result = [[self.get_matrix()[i][j]
                  for i in range(0, self.get_number_of_row(), 1)]
                  for j in range(0, self.get_number_of_column(), 1)]
        
        return Matrix(result)
    
    #return the cominor matrix M_ij
    def cominor(self, i, j):
        result = []
        [i, j] = [i - 1, j - 1]
        
        #row m
        for m in range(0, self.get_number_of_row(), 1):
            row = []
            
            #column n
            for n in range(0, self.get_number_of_column(), 1):
                if m != i and n != j :
                    row.append(self.get_matrix()[m][n])
                    
                else:
                    pass
                
            if row != []:                
                result.append(row)
            else: 
                pass
    
        return Matrix(result)
    
    
    #return the determinant of the matrix
    def det(self):
        
        #if it is a square matrix
        if self.check_valid() == True:
            if self.dimension == 1:
                return self.get_matrix()[0][0]
            
            else:
                D = self.dimension
                first_row = self.get_matrix()[0]
                result = 0
                for i in range(0, D, 1):
                    result = (result + 
                              first_row[i] * self.cominor(1, i + 1).det() * (-1)**i)
                
                return result
        
        #if it is not a square matrix
        else:
            print("Only a square matrix can have determinant !")
            
    #return the adjoit matrix
    def adjoint(self):
       
        #if it is a square matrix
        if self.check_valid() == True:
            D = self.dimension
            result = [[self.cominor(j + 1, i + 1).det() * (-1) ** (i + j)
                for j in range(0, D, 1)]
                for i in range(0, D, 1)]
            
            return Matrix(result)
        
        #if it is not a square matrix
        else:
            print("Only a square matrix can have adjoint matrix !")       
        
    def inverse(self):
       
        #if it is a square matrix
        if self.check_valid() == True:
            
            if self.det() != 0:
                D = self.dimension
                result = [[self.cominor(j + 1, i + 1).det() 
                           * (-1) ** (i + j) / self.det()
                           for j in range(0, D, 1)]
                          for i in range(0, D, 1)]
            
                return Matrix(result)
            
            else:
                return (Matrix(["This is a singular matrix !"]))
        
        #if it is not a square matrix
        else:
            print("Only a square matrix can have the inverse !")        
    
    
    




