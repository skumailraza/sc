import unittest
# ---- ITERATIVE SOLUTION Starts ------

def iter_mult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print "Cannot multiply the two matrices. Incorrect dimensions."
        return

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print C
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# ----- ITERATIVE SOLUTION ENDS --------



# _____ STRASSEN'S METHOD STARTS ________

# n*n additions 

def add(A, B):
	n = len(A)
	C = [[0 for j in range(n)] for i in range(n)]

    for j in range(n):
        for i in range (n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def sub(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

# strassens multiplication
def strassens(A, B):
	m = 0
	n = len(A[0])
	C = [[0 for j in range(n)] for i in range(n)]
	if n==1:
		C[0][0] = A[0][0]*B[0][0]
	else:
		m = n/2
        A11 = [[0 for j in range(m)] for i in range(m)]
        A12 = [[0 for j in range(m)] for i in range(m)]
        A21 = [[0 for j in range(m)] for i in range(m)]
        A22 = [[0 for j in range(m)] for i in range(m)]

        B11 = [[0 for j in range(m)] for i in range(m)]
        B12 = [[0 for j in range(m)] for i in range(m)]
        B21 = [[0 for j in range(m)] for i in range(m)]
        B22 = [[0 for j in range(m)] for i in range(m)]

        AR = [[0 for j in range(m)] for i in range(m)]
        BR = [[0 for j in range(m)] for i in range(m)]

        # create 4 sub-matrices(top left, top right bottom letf and right:
        for i in range(m):
            for j in range(m):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j + m]
                A21[i][j] = A[i + m][j]    
                A22[i][j] = A[i + m][j + m] 

                B11[i][j] = B[i][j]            
                B12[i][j] = B[i][j + m]    
                B21[i][j] = B[i + m][j]    
                B22[i][j] = B[i + m][j + m]

            BR = sub(B12, B22) #(b12-b22)
            p1 = strassens(A11, BR) # p1 = (a11) * (b12-b22)

            AR = add(A11, A12)      # a11 + a12
            p2 = strassens(AR, B11)  # p2 = (a21+a22) * (b11)

            AR = add(A21, A22) # a21 + a22
            p3 = strassens(B11, AR)  # p3 = (b11) * (a21 + a22)

            BR = sub(B21, B11) # b21 - b11
            p4 =strassens(A22, BR)   # p4 = (a22) * (b21 - b11)

            BR =  add(B11,B22)     #b11+b22
            AR = add(A11, A12)      # a11 + a12
            p5 = strassens(AR, BR)  # p5 = (a11+a12) * (b11+b22)   

            AR = sub(A12, A22) # a12 - a22
            BR = add(B21, B22)      # b11 + b12
            p6 = strassens(AR, BR) # p6 = (a21-a11) * (b11+b12)

            AR = sub(A11, A21) # a12 - a21
            BR = add(B11, B12)      # b11 + b12
            p7 = strassens(AR, BR) # p7 = (a12-a21) * (b11+b12)

        # reqrouping all the ps into c11, c22,c21,c12

            AR = add(p5, p4) # p5 + p4
            BR = add(AR, p6) # p5 + p4 + p6
            c11 = sub(BR, p2) # c11 = p1 + p4 - p2 + p6

            c12 = add(p1, p2) # c12 = p1 + p2
            c21 = add(p3, p4)  # c21 = p3 + p4



            AR = add(p5, p1) # p5 + p1
            BR = sub(AR, p3) # p5 + p1 - p3
            c22 = sub(BR, p7) # c22 = p5 + p1 - p3 - p7

        # results 
            C = [[0 for j in range(n)] for i in range(n)]
            for i in range(m):
                for j in range(m):
                    C[i][j] = c11[i][j]
                    C[i][j + m] = c12[i][j]
                    C[i + m][j] = c21[i][j]
                    C[i + m][j + m] = c22[i][j]
            return C

# ________ STRASSEN's METHOD ENDS ___________

def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


class TestMultiplicationMethods(unittest.TestCase):

    def test_nomult(self):
    	X = [[1,2,3],[1,2,2]]
    	Y = [1]
        self.assertEqual(iter_mult(X,Y), 'Cannot multiply the two matrices. Incorrect dimensions.')

    def test_checkboth(self):
    	X = [[1,1,1],[1,1,1]]
    	Y = [[1,1,1],[1,1,1]]
        self.assertEqual(iter_mult(X,Y), strassens(X,Y))

    def test_dim(self):
    	X = [[1,1,1],[1,1,1]]
    	Y = [[1,1,1],[1,1,1]]
        self.assertTrue(len(X[0]) == len(Y))


if __name__ == '__main__':
    unittest.main()




