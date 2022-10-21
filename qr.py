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
