import lexer_test as lt
from vectorClass import vector
import re
import math
class matrix:
    
    VectorRule = re.compile(lt.t_vector)

    def __init__(self, string):
        RowVecsFromRE = matrix.VectorRule.findall(string)
        self.numOfRows = len(RowVecsFromRE)
        self.RowVecs = []
        sizeOfVecs = []
        for i in range(self.numOfRows):
            self.RowVecs.append(vector(matrix.FormatColumnVectors(RowVecsFromRE[i])))
            sizeOfVecs.append(len(self.RowVecs[i]))
        maxRowSize = max(sizeOfVecs)
        for j in range(self.numOfRows):
            self.RowVecs[j] =  matrix.appendZeroes(self.RowVecs[j],self.RowVecs[j].size,maxRowSize)
        ColumnVecs = []
        temp_list = []
        for k in range(maxRowSize):
            if k != 0:
                ColumnVecs.append(temp_list[:])
                temp_list.clear()
            for z in range(self.numOfRows):
                temp_list.append(self.RowVecs[z].elems[k])
        ColumnVecs.append(temp_list[:])
        self.size = maxRowSize*self.numOfRows
        self.numOfColumns = len(ColumnVecs)
        self.ColumnVecs = []
        for i in range(self.numOfColumns):
            self.ColumnVecs.append(vector(matrix.FormatColumnVectors(ColumnVecs[i])))
        self.isSquare = False
        if math.sqrt(self.size) == math.floor(math.sqrt(self.size)):
            self.isSquare = True

    def __str__(self):
        ans = ""
        for i in range(self.numOfRows):
           ans = ans + vector.__str__(self.RowVecs[i]) + '\n'
        return ans

    def __add__(self,RightMatrix):
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfRows):
            vecList.append(self.RowVecs[vecs] + RightMatrix.RowVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def __sub__(self,RightMatrix):
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfRows):
            vecList.append(self.RowVecs[vecs] - RightMatrix.RowVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def scalar_multiplication(self, multiplier):
        vecList = []
        for i in range(self.numOfColumns):
            vecList.append(self.RowVecs[i].scalar_multiplication(multiplier))
        return matrix(matrix.formatList(vecList))
    
    def cross_product(self, rightMat): #needs refactoring
        if self.numOfColumns != rightMat.numOfRows:
            print("Left matrix's number of columns not equal to right matrix's number of rows")
            return None
        new_column_vecs = []
        temp_list = []
        for i in range(rightMat.numOfColumns):
            if i != 0:
                new_column_vecs.append(temp_list)
                del temp_list
                temp_list = []
            for j in range(self.numOfRows):
                temp_list.append(self.RowVecs[j].dot_product(rightMat.ColumnVecs[i]))
        new_column_vecs.append(temp_list)
        del temp_list
        new_mat_str_list = []
        for k in range(len(new_column_vecs)):
            new_mat_str_list.append(vector(vector.FormatColumnVectors(new_column_vecs[k])))
        return matrix(matrix.formatList(new_mat_str_list)).transpose()
    
    def transpose(self):
        new_row_vecs = []
        for i in range(self.numOfColumns):
            new_row_vecs.append(vector(matrix.FormatColumnVectors(self.ColumnVecs[i])))
        return matrix(matrix.formatList(new_row_vecs))

    def det(self):
        if self.isSquare == False:
            print("Matrix is not square")
            return None
        row_matrix = []
        for i in range(self.numOfRows):
            temp_vec = [int(x) for x in self.RowVecs[i].elems]
            row_matrix.append(temp_vec.copy())
            temp_vec.clear()
        return matrix.rec_det(row_matrix)

    def inv(self): #needs refactoring
        mat_det = self.det()
        if self.isSquare == False or mat_det == 0:
            print("Matrix is not square or matrix determinant is zero")
            return None
        row_matrix = []
        for i in range(self.numOfRows):
            temp_vec = [int(x) for x in self.RowVecs[i].elems]
            row_matrix.append(temp_vec.copy())
            temp_vec.clear()
        star_mat = matrix.star(row_matrix.copy())
        adjoint_mat = []
        temp_vec.clear()
        for row in range(self.numOfColumns):
            adjoint_mat.append(temp_vec[:])
            temp_vec.clear()
            for column in range(self.numOfColumns):
                temp_vec.append(star_mat[row][column]/mat_det)
        adjoint_mat.append(temp_vec[:])
        adjoint_mat = [x for x in adjoint_mat.copy() if x]
        vec_list = []
        for i in range(len(adjoint_mat)):
            vec_list.append(vector(matrix.FormatColumnVectors(adjoint_mat[i])))
        return matrix(matrix.formatList(vec_list))

    @staticmethod
    def rec_det(mat):
        mat_cpy = mat.copy()
        if len(mat) <= 1:
            return float(re.sub(r'\[|\]',"",str(mat_cpy)))
        else:
            sum = 0
            for row in range(len(mat)):
                sum += pow(-1,row)*mat[row][0]*matrix.rec_det(matrix.not_in_row_or_column(mat_cpy,len(mat_cpy),row,0))
            return sum

    @staticmethod
    def not_in_row_or_column(mat,size,target_row,target_column):
        temp_vec = []
        new_mat = []
        for row in range(size):
            if row != 0:
                new_mat.append(temp_vec.copy())
                temp_vec.clear()
            for column in range(size):
                if row != target_row and column != target_column:
                    temp_vec.append(mat[row][column])
        new_mat.append(temp_vec)
        new_mat = list([x for x in new_mat.copy() if x])
        return new_mat

    @staticmethod
    def FormatColumnVectors(string):
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result
    
    @staticmethod
    def appendZeroes(vec,initialSize ,maxColumnSize):
        while initialSize < maxColumnSize:
            vec.elems.append(0.0)
            vec.size = vec.size + 1
            initialSize = initialSize + 1
        return vec

    @staticmethod
    def formatList(vecList):
        tempStr = "["
        for i in range(len(vecList)):
            if i != len(vecList) - 1:
                tempStr = tempStr + vector.__str__(vecList[i]) + ';'
            else:
                tempStr = tempStr + vector.__str__(vecList[i])
        tempStr += "]"
        return tempStr
    
    @staticmethod
    def star(mat):
        off_row = True
        temp_vec = []
        adjoint_mat = []
        for row in range(len(mat)):
            adjoint_mat.append(temp_vec[:])
            temp_vec.clear()
            off_row = not off_row
            for column in range(len(mat)):
                if off_row:
                    val = pow(-1,column+1)*matrix.rec_det(matrix.not_in_row_or_column(mat,len(mat),row,column))
                else:
                    val = pow(-1,column)*matrix.rec_det(matrix.not_in_row_or_column(mat,len(mat),row,column))
                temp_vec.append(val)
        adjoint_mat.append(temp_vec[:])
        temp_vec.clear()
        adjoint_mat = [x for x in adjoint_mat.copy() if x]
        return adjoint_mat

mat = matrix("[[1 3 2];[2 2 1];[3 1 3]]")
mat1 = matrix("[[1 2 3];[4 5 6];[7 8 9]]")
mat2 = matrix("[[1 2];[3 4]]")

print(mat2.inv())

#{{1,3,2},{2,2,1},{3,1,3}}
#{{1,2,3},{4,5,6},{7,8,9}}