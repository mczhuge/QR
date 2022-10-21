import numpy as np
from qr import Gram_Schimidt, Householder, Givens
from scipy import linalg

np.set_printoptions(suppress=True)


if __name__=='__main__':

    #  np.random.seed(22)
    A = np.random.randn(4, 4)


    print('\033[1;32;32m ###################################################################################### \033[1;m')
    print('\033[1;32;32m We regrad the results calculated by SciPy as Ground Truth (GT). \033[1;m')
    print('\033[1;32;32m *. [Q_gt, R_gt] are the right answers. \033[1;m ')
    print('\033[1;32;32m Press "1". [Q1, R1] are the answers calculated by Householder. \033[1;m ')
    print('\033[1;32;32m Press "2". [Q2, R2] are the answers calculated by Gram-Schimidt. \033[1;m ')
    print('\033[1;32;32m Press "3". [Q3, R3] are the answers calculated by Givens. \033[1;m ')
    print('\033[1;32;32m ###################################################################################### \033[1;m \n')

    choose_mode=input("please choose the mode:")

    print('\033[1;32;32m SciPy GT. \033[1;m')
    Q_gt, R_gt = linalg.qr(A)
    print('\033[1;34;34m Q_gt: \033[1;m \n'+ str(Q_gt))
    print('\033[1;34;34m R_gt: \033[1;m \n'+ str(R_gt))
    print("\033[1;34;34m Verify A=Q_gt*R_gt  \033[1;m \n", np.allclose(A, Q_gt @ R_gt))

    if choose_mode=="1":

        print('\033[1;32;32m Householder. \033[1;m')
        Q, R = Householder(A)
        print('\033[1;34;34m Q: \033[1;m \n'+ str(Q))
        print('\033[1;34;34m R: \033[1;m \n'+ str(R))
        print("\033[1;34;34m Verify A=Q*R  \033[1;m \n", np.allclose(A, Q @ R))

    if choose_mode=="2":

        print('\033[1;32;32m Gram_Schimidt. \033[1;m')
        Q, R  = Gram_Schimidt(A)
        print('\033[1;34;34m Q: \033[1;m \n'+ str(Q))
        print('\033[1;34;34m R: \033[1;m \n'+ str(R))
        print("\033[1;34;34m Verify A=Q*R  \033[1;m \n", np.allclose(A, Q @ R))

    if choose_mode=="3":
        print('\033[1;32;32m Givens. \033[1;m')
        Q,R = Givens(A)
        print('\033[1;34;34m Q: \033[1;m \n'+ str(Q))
        print('\033[1;34;34m R: \033[1;m \n'+ str(R))
        print("\033[1;34;34m Verify A=Q*R  \033[1;m \n", np.allclose(A, Q @ R))



