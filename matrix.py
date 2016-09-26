import re
import traceback
from pdb import set_trace as st

""" This is a python program  which does various matrix operations 
    """

mat1 = [
          [1,2],
          [3,4]
       ]
       
mat2 = [
          [1,2],
          [3,4]
       ]

mat3 = [ [ mat1[i][j] + mat2[i][j] for j in range(0, len(mat2[0])) ] for i in range(0,len(mat1)) ]
print ("\n\n*************MATRIX ADDITION*****************\n\n")
print("MAT1={}\n + \nMAT2={} \n--------\nMAT3={}". format(mat1, mat2, mat3))

mat1 = [
          [1,2],
          [3,4],
          [5,6]
       ]

mat1_transpose = [ [mat1[row_num][col_num] for row_num in range(0, len(mat1))] for col_num in range(0, len(mat1[0])) ]
print("MAT1 ={}\n--------\nTRANSPOSE ={}". format(mat1, mat1_transpose))

mat2_transpose = [ list(t1) for t1 in zip(*mat1)]
print("MAT1 ={}\n--------\nTRANSPOSE USING ZIP ={}". format(mat1, mat1_transpose))

mat1 = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
       ]

mat2 = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
       ]

mat4 = [ [0 for col in range(0, len(mat1[0]))] for row in range(0, len(mat2))]
# For matrix mulitiplication .. no of columns in 1st Matrix == no of rows in 2nd Matrix
st()
for row_num1 in range(0, len(mat1)):
    for col_num2 in range(0, len(mat2[0])):
        mat4[row_num1][col_num2] = 0
        for row_num2 in range(0, len(mat2)):
            print "row_num2 = {}".format(row_num2)
            mat4[row_num1][col_num2] +=  (mat1[row_num1][row_num2] * mat2[row_num2][col_num2])
print ("\n\n*************MATRIX MULTIPLICATION*****************\n\n")
print("MAT1={}\n + \nMAT2={} \n--------\nMAT3={}". format(mat1, mat2, mat4))
     
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*mat2)] for X_row in mat1]
print ("\n\n*************MATRIX MULTIPLICATION*****************\n\n")
print("MAT1={}\n + \nMAT2={} \n--------\nMAT3={}". format(mat1, mat2, result))
