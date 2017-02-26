import unittest
from math import ceil, log

# ---- ITERATIVE SOLUTION Starts ------

def iter_mult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return "Cannot multiply the two matrices. Incorrect dimensions."

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print C
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# ----- ITERATIVE SOLUTION ENDS --------



# _____ STRASSEN'S METHOD STARTS ________

# Some auxilliary functions
def add(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

# STRASSEN'S RECURSIVE STEP:
def strassen_recur(A, B):
    n = len(A)

    if n <= RECURSION_DEPTH:
        return iter_mult(A, B)
    else:
        # initializing the new sub-matrices
        new_size = n/2
        a11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        b11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        ar = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        br = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                a11[i][j] = A[i][j]               # 1,1
                a12[i][j] = A[i][j + new_size]    # 1,n
                a21[i][j] = A[i + new_size][j]    # n,1
                a22[i][j] = A[i + new_size][j + new_size] # n,n

                b11[i][j] = B[i][j]            
                b12[i][j] = B[i][j + new_size]    
                b21[i][j] = B[i + new_size][j]    
                b22[i][j] = B[i + new_size][j + new_size] 

        # Calculating p's:

        ar = add(a11, a22)
        br = add(b11, b22)
        p1 = strassen_recur(ar, br) # p1 = (a11+a22) x (b11+b22)

        ar = add(a21, a22)      # a21+a22
        p2 = strassen_recur(ar, b11)  # p2 = (a21+a22) x (b11)

        br = subtract(b12, b22) # b12-b22
        p3 = strassen_recurR(a11, br)  # p3 = (a11) x (b12 - b22)

        br = subtract(b21, b11) # b21-b11
        p4 =strassen_recur(a22, br)   # p4 = (a22) x (b21 - b11)

        ar = add(a11, a12)      # a11+a12
        p5 = strassen_recur(ar, b22)  # p5 = (a11+a12) x (b22)

        ar = subtract(a21, a11) # a21-a11
        br = add(b11, b12)      # b11 + b12
        p6 = strassen_recur(ar, br) # p6 = (a21-a11) x (b11+b12)

        ar = subtract(a12, a22) # a12-a22
        br = add(b21, b22)      # b21 + b22
        p7 = strassen_recur(ar, br) # p7 = (a12-a22) x (b21+b22)

        # calculating c's
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        ar = add(p1, p4) # p1 + p4
        br = add(ar, p7) # p1 + p4 + p7
        c11 = subtract(br, p5) # c11 = p1 + p4 - p5 + p7

        ar = add(p1, p3) # p1 + p3
        br = add(ar, p6) # p1 + p3 + p6
        c22 = subtract(br, p2) # c22 = p1 + p3 - p2 + p6

        # Resultant matrix:
        C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                C[i][j] = c11[i][j]
                C[i][j + new_size] = c12[i][j]
                C[i + new_size][j] = c21[i][j]
                C[i + new_size][j + new_size] = c22[i][j]
        return C


def strassens(A, B):
    # Checking dimensions and list types:
    if (type(A) == list and type(B) == list) != 1:
        return False
    if (len(A) == len(A[0]) == len(B) == len(B[0])) != 1:
        return False

    # appending zeros
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in xrange(m)] for j in xrange(m)]
    BPrep = [[0 for i in xrange(m)] for j in xrange(m)]
    for i in xrange(n):
        for j in xrange(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassen_recur(APrep, BPrep)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            C[i][j] = CPrep[i][j]
    return C

# ________ STRASSEN's METHOD ENDS ___________

# Function to print matrix
def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))

#____________________________________________


# TO STOP COMPILER PANIC ON EXCEEDING RECURSION DEPTH:
RECURSION_DEPTH = 8


class TestMultiplicationMethods(unittest.TestCase):

    def test_nomult(self):
    	X = [[1,2,3],[1,2,2]]
    	Y = [[1]]
        self.assertEqual(iter_mult(X,Y),"Cannot multiply the two matrices. Incorrect dimensions.")
        
    def test_assertions(self):
        X = [[1,2,3],[1,2,2]]
        Y = [[1]]
        self.assertFalse(strassens(X,Y))

    def test_logic(self):
        X = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(iter_mult(X,X), X)
        self.assertEqual(strassens(X,X), X)

    def test_checkboth(self):
    	X = [[1,1,1],[1,1,1],[1,2,3]]
    	Y = [[1,1,1],[1,1,1],[1,2,3]]
        self.assertEqual(iter_mult(X,Y), strassens(X,Y))

if __name__ == '__main__':
    unittest.main()




