from fractions import Fraction
from functools import reduce

# Absorbing Markov Chains
def answer(mtrx):

    if len(mtrx) is 1:
        return [1,1]
    std_mtrx, q_pos = _standard_form(mtrx)
    #print_matrix(std_mtrx)

    if q_pos is len(std_mtrx):
        return []

    q_mtrx = _get_sub_mtrx(std_mtrx, q_pos, q_pos)


    i = _get_id_matrix(len(mtrx) - q_pos)

    i_minus_q = _subtract_matrices(i, q_mtrx)
    f = getMatrixInverse(i_minus_q)

    # r
    r = _get_sub_mtrx(std_mtrx, q_pos, 0)
    r = [i[:q_pos] for i in r]


    # final probabilities
    final_m = _matrix_product(f, r)

    final_m = reduce_and_fraction(final_m[0])

    return final_m



# given a matrix
# returns the standardized transition matrix
def _standard_form(mtrx):
    absorbing_indexs = []
    not_absorbing_indexs = []
    for c, row in enumerate(mtrx):
        row_sum = sum(row)
        mtrx[c] = [x/max(float(row_sum), 1.) for x in row]
        if row_sum == 0:
            absorbing_indexs.append(c)
        else:
            not_absorbing_indexs.append(c)

    absorbing_indexs.extend(not_absorbing_indexs)

    return _reorder_list(mtrx, absorbing_indexs), (len(absorbing_indexs) - len(not_absorbing_indexs))

# given a list and an order the list should be in
# returns a new list in that order
def _reorder_list(lst, order):
    pos = 0
    new_lst = [0] * len(lst)
    for idx in order:
        item = lst[idx]
        new_lst[pos] = _reorder_list(lst[idx], order) if type(item) is list else lst[idx]
        pos += 1

    return new_lst

# given two matricies m1, m2
# returns m1 - m2
def _subtract_matrices(m1, m2):

    return_mtrx = __zero_matrix(min(len(m1), len(m2)), min(len(m1[0]), len(m2[0])))
    i = 0

    for a, b in zip(m1, m2):
        j = 0
        for c, d in zip(a, b):
            return_mtrx[i][j] = c - d
            j += 1
        i += 1

    return return_mtrx

# returns a matrix filled with zeros of given size
def __zero_matrix(rows, colums):
    zm = [[]] * rows
    for idx in range(0,len(zm)):
        zm[idx] = [0] * colums

    return zm


# given two matracies a , b
# returns a * b
def _matrix_product(a, b):

    zip_b = zip(*b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


# returns the lower right side of a matrix of given size
def _get_sub_mtrx(mtrx, row_start, col_start, end=True, end_pos=None):
    if end:
        return [x[col_start:] for x in mtrx[row_start:]]
    else:
        return [x[col_start:] for x in mtrx[row_start:end_pos]]

# returns an identity matrix of given size
def _get_id_matrix(size):
    idm = __zero_matrix(size, size)
    for i in range(0,size):
        idm[i][i] = 1

    return idm

# given matrix of floats
# put each row in to a fraction and reduce
# returns matrix with last element in each row the denominator
def reduce_and_fraction(top):
    top = [Fraction(d).limit_denominator(10000) for d in top]
    list_of_denoms = [d.denominator for d in top]
    denoms_lcm = reduce(lcm, list_of_denoms)
    for i, val in enumerate(top):
        top[i] = val.numerator * (denoms_lcm / val.denominator)

    top.append(denoms_lcm)

    return top

# greatest common divisor
def gcd(a, b):

    while b:
        a, b = b, a % b
    return a

# lowest common multiple
def lcm(a, b):
    return a * b // gcd(a, b)


# ===========================================================================
# https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
# ===========================================================================
def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


# returns the inverse of the given matrix
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
# ===========================================================================
# ===========================================================================
# ===========================================================================


# #TEST CASE 1
# m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# a = [7, 6, 8, 21]
# print ("Test Case 1")
# print (answer(m) == a)
# #TEST CASE 2
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# a = [0, 3, 2, 9, 14]
# print ("Test Case 1")
#
# print (answer(m) == a)
# #TEST 2
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# a = [0, 3, 2, 9, 14]
# print ("Test 2")
# print (answer(m) == a)
# #TEST 3
# m = [[1, 2, 3, 0, 0, 0], [4, 5, 6, 0, 0, 0], [7, 8, 9, 1, 0, 0], [0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# a = [1, 2, 3]
# print ("Test 3")
# print((answer(m) == a))
# #TEST 4
# m = [[0]]
# a = [1, 1]
# print ("Test 4")
# print (answer(m) == a)
# #TEST 5
# m = [[0, 0, 12, 0, 15, 0, 0, 0, 1, 8], [0, 0, 60, 0, 0, 7, 13, 0, 0, 0], [0, 15, 0, 8, 7, 0, 0, 1, 9, 0], [23, 0, 0, 0, 0, 1, 0, 0, 0, 0], [37, 35, 0, 0, 0, 0, 3, 21, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [1, 2, 3, 4, 5, 15]
# print ("Test 5")
# print (answer(m) == a)
# #TEST 6
# m = [[ 0,  7,  0, 17,  0,  1,  0,  5,  0,  2], [ 0,  0, 29,  0, 28,  0,  3,  0, 16,  0], [ 0,  3,  0,  0,  0,  1,  0,  0,  0,  0], [48,  0,  3,  0,  0,  0, 17,  0,  0,  0], [ 0,  6,  0,  0,  0,  1,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
# a = [4, 5, 5, 4, 2, 20]
# print ("Test 6")
# print (answer(m) == a)
# #TEST 7
# m = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [1, 1, 1, 1, 1, 5]
# print ("Test 7")
# print (answer(m) == a)
# #TEST 8
# m = [[1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [2, 1, 1, 1, 1, 6]
# print ("Test 8")
# print (answer(m) == a)
# #TEST 9
# m = [[0, 86, 61, 189, 0, 18, 12, 33, 66, 39], [0, 0, 2, 0, 0, 1, 0, 0, 0, 0], [15, 187, 0, 0, 18, 23, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [6, 44, 4, 11, 22, 13, 100]
# print ("Test 9")
# print (answer(m) == a)
#
# #TEST 10
# m = [[0, 0, 0, 0, 3, 5, 0, 0, 0, 2], [0, 0, 4, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 4, 4, 0, 0, 0, 1, 1], [13, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 1, 8, 7, 0, 0, 0, 1, 3, 0], [1, 7, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [1, 1, 1, 2, 5]
print ("Test 10")
print(answer(m))
print (answer(m) == a)


