import numpy as np

def Gram_Schimidt(A,verbose=False):
    m = A.shape[0]
    n = A.shape[1]
    R=np.zeros([m,n])
    Q=np.zeros([m,m])
    R[0,0]=np.linalg.norm(A[:,0])
    if R[0, 0] == 0:
        print("cannot realiaze Gram_Schimidt decomposition")
    else:
        Q[:,0]=A[:,0]/R[0,0]
    for i in range(1,n):
        Q[:,i]=A[:,i]
        for j in range(i):
            R[j,i]=np.dot(Q[:,j].T,Q[:,i])
            Q[:,i]-=R[j,i]*Q[:,j]
        R[i,i]=np.linalg.norm(Q[:,i])
        if R[i,i]==0:
            print("cannot realiaze Gram_Schimidt decomposition")
        else:
            Q[:, i] = Q[:, i] / R[i, i]
    if verbose:
        print("The Gram_Schimidt decomposition of A is:")
        print("The Q matrix is:")
        print(Q)
        print("The R matrix is:")
        print(R)
    return  Q,R

def Householder(A,verbose=False):
    m = A.shape[0]
    n = A.shape[1]
    E=np.eye(m)
    T=np.array(A).copy()
    P=np.eye(m)
    for i in range(n-1):
        u=T[i:,i]-np.linalg.norm(T[i:n,i])*E[i:,i]
        u=np.array([u])
        u=u.T
        I = np.eye(m)
        I[i:,i:]=np.eye(n-i)-2*np.dot(u,u.T)/(np.linalg.norm(u)*np.linalg.norm(u))
        T=np.dot(I,T)
        P=np.dot(I,P)
        Q=P.T
    if verbose:
        print("The householder_reduction of A is:")
        print("The Q matrix is:")
        print(Q)
        print("The R matrix is:")
        print(T)
    return  Q,T

def Givens(A,verbose=False):
    m = A.shape[0]
    n = A.shape[1]
    P=np.eye(m)
    R=np.array(A).copy()
    for k in range(m):
        for j in range(n-1,k,-1):
            tmpa = R[k,k]
            tmpb = R[j,k]
            mag = np.sqrt(tmpa*tmpa+tmpb*tmpb)
            c= tmpa / mag
            s= tmpb / mag
            I=np.eye(m)
            I[k,k]=c
            I[k,j]=s
            I[j,j]=c
            I[j,k]=-s
            P=np.dot(I,P)
            R=np.dot(I,R)
            Q=P.T
    if verbose:
        print("The Givens_reduction of A is:")
        print("The Q matrix is:")
        print(Q)
        print("The R matrix is:")
        print(R)
    return  Q,R

# Zhihu's version is wrong
def householder_reduce(matrix_a):
    """
    Householder reduce for QR factorization.
    :param matrix_a:
    :return: matrix_q, matrix_r
    """

    # row num: n
    # col num: m
    n, m = matrix_a.shape

    matrix_r = matrix_a

    # H_1, H_2, ..., H_n
    householder_matrix_list = []

    # project each col onto standard basis
    for j in range(m):

        # Deal with un-reduced sub-matrix.
        sub_matrix = matrix_r[j:, j:]

        """ Get a_j """
        # a_j: column vector j
        a = np.reshape(sub_matrix[:, 0],
                       (len(sub_matrix), 1))

        # Check j-col
        if not np.nonzero(a)[0].any() or len(a) == 1:
            # All rested elements in col_j are zeros.
            continue

        """ Get v_j = a - |a| e """

        # 2-norm of vector a
        a_norm_2 = np.int(np.sqrt(np.matmul(a.T, a)))

        # standard base e
        e = np.zeros_like(a)
        e[0] = 1

        # v = a - |a| e
        v = np.subtract(a, a_norm_2 * e)

        """ Get Householder matrix H_j"""

        # Household matrix H: I - 2 (vv')/(v'v)
        sub_matrix_h = np.identity(len(v)) - 2 * np.matmul(v, v.T) / np.matmul(v.T, v)

        # Augment Household matrix
        matrix_h = np.identity(n)
        matrix_h[j:, j:] = sub_matrix_h

        # Mapping current matrix
        matrix_r = np.matmul(matrix_h, matrix_r)

        # Store Household matrix
        householder_matrix_list.append(matrix_h)

    """ Reduce R matrix"""
    matrix_r = matrix_r[0:m]

    """ Compute Q' matrix """
    # Compute Q', where Q' = H_n ... H_2 * H_1 * I
    matrix_q = np.identity(n)

    for household_matrix in householder_matrix_list:
        matrix_q = np.matmul(household_matrix, matrix_q)

    """ Reduce Q matrix """
    matrix_q = np.transpose(matrix_q[0:m])

    return matrix_q, matrix_r


# Our version
def qr_householder(A):
    """ Compute QR decomposition of A using Householder reflection"""

    # M is the row number, and N is the column number
    M = A.shape[0]
    N = A.shape[1]

    # set Q to the identity matrix
    Q = np.identity(M)

    # set R to zero matrix
    R = np.copy(A)

    for n in range(N):
        # vector to transform
        x = A[n:, n]
        k = x.shape[0]

        # compute ro=-sign(x0)||x||
        ro = -np.sign(x[0]) * np.linalg.norm(x)

        # compute the householder vector v
        e = np.zeros(k)
        e[0] = 1
        v = (1 / (x[0] - ro)) * (x - (ro * e))

        # apply v to each column of A to find R
        for i in range(N):
            R[n:, i] = R[n:, i] - (2 / (v@v)) * ((np.outer(v, v)) @ R[n:, i])

        # apply v to each column of Q
        for i in range(M):
            Q[n:, i] = Q[n:, i] - (2 / (v@v)) * ((np.outer(v, v)) @ Q[n:, i])

    return [Q.transpose(), R]