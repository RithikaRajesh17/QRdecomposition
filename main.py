''' 
Program to QR decomposition using the Gram-Schmidt method
Developed by: Mohamed Riyaz Ahamed 
RegisterNumber: 24900085
'''
import numpy as np
def QR_Decomposition(A):
    # Write your code 
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R
    
a = np.array(eval(input()))

Q, R = QR_Decomposition(a)
print(Q)
print(R)
