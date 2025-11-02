class Solution(object):
    def transpose(self, matrix):
        n=len(matrix[0])
        new=[]
        for i in range(n):
            l=[]
            for j in range(0,len(matrix)):
                l.append(matrix[j][i])
            new.append(l)
        return new
