import numpy as np
from qr import *
from scipy import linalg

np.set_printoptions(suppress=True)

#np.random.seed(22)
A = np.random.randn(5, 3)
print('----- Matrix A: -----\n'+ str(A)+'\n')

# Compute the QR decomposition
Q, R = qr_householder(A)

# Using Scipy
Q_gt, R_gt = linalg.qr(A)


# Compare Q with Q_gt
print('\033[1;31;31m Q: \033[1;m \n'+ str(Q))
print('\033[1;31;31m Q_gt: \033[1;m \n'+ str(Q_gt))

# Compare R with R_gt
print('\033[1;31;31m R: \033[1;m \n'+ str(R))
print('\033[1;31;31m R_gt: \033[1;m \n'+ str(R_gt))

# Verify A=QR
print('\033[1;31;31m Compute A=Q_gt*R_gt: \033[1;m \n'+ str(Q @ R))
print(np.allclose(A, Q_gt @ R_gt))
print('\033[1;31;31m Compute A=QR: \033[1;m \n'+ str(Q @ R))
print(np.allclose(A, Q @ R))

