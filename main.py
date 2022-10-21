import numpy as np
from qr import householder_reduce, qr_householder
from scipy import linalg

np.set_printoptions(suppress=True)



#np.random.seed(22)
A = np.random.randn(5, 3)

print('\033[1;32;32m ###################################################################################### \033[1;m')
print('\033[1;32;32m We regrad the results calculated by SciPy as Grount Truth (GT). \033[1;m')
print('\033[1;32;32m 1. [Q_gt, R_gt] is the right answers. \033[1;m ')
print('\033[1;32;32m 2. [Q, R] is the answers by our writtern code. \033[1;m ')
print('\033[1;32;32m 3. [Q_zhihu, R_zhihu] is the answers calculated by the code in Zhihu. \033[1;m ')
print('\033[1;32;32m ###################################################################################### \033[1;m \n')

print('\033[1;31;31m----- Matrix A: -----\033[1;m \n'+ str(A)+'\n')

# Compute the QR decomposition
Q, R = qr_householder(A)

Q2, R2 = householder_reduce(A)

# Using Scipy
Q_gt, R_gt = linalg.qr(A)


# Compare Q with Q_gt
print('\033[1;31;31m Q_gt: \033[1;m \n'+ str(Q_gt))
print('\033[1;31;31m Q: \033[1;m \n'+ str(Q))
print('\033[1;31;31m Q_zhihu: \033[1;m \n'+ str(Q2))


# Compare R with R_gt
print('\033[1;31;31m R_gt: \033[1;m \n'+ str(R_gt))
print('\033[1;31;31m R: \033[1;m \n'+ str(R))
print('\033[1;31;31m R_zhihu: \033[1;m \n'+ str(R2))

# Verify A=QR
print('\033[1;31;31m Compute A=Q_gt*R_gt: \033[1;m \n'+ str(Q @ R))
print(np.allclose(A, Q_gt @ R_gt))
print('\033[1;31;31m Compute A=QR: \033[1;m \n'+ str(Q @ R))
print(np.allclose(A, Q @ R))
print('\033[1;31;31m Compute A=Q_zhihu*R_zhihu: \033[1;m \n'+ str(Q @ R))
print(np.allclose(A, Q2 @ R2))

