class Solution:
    def rotate(self,matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for arr in matrix:
            arr.reverse()
        return matrix
