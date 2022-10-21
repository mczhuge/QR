# QR decomposition
We can compute the QR decomposition by 
* Householder transformations ✅
* Gram Schmidt orthogonalization ✅
* Givens transformations ✅)

**Theorem:**

If <img src="https://render.githubusercontent.com/render/math?math=A \in \mathbb{R}^{m \times n}"> has full column rank, i.e, Rank(<img src="https://render.githubusercontent.com/render/math?math=A">)=<img src="https://render.githubusercontent.com/render/math?math=n"> then <img src="https://render.githubusercontent.com/render/math?math=A"> has the QR decomposition:

<img src="https://render.githubusercontent.com/render/math?math=A = Q \begin{bmatrix}R \\0 \end{bmatrix} = Q_1 R">

where <img src="https://render.githubusercontent.com/render/math?math=Q=[Q_1, Q_2] \in \mathbb{R}^{m \times m}"> is orthogonal and <img src="https://render.githubusercontent.com/render/math?math=R \in \mathbb{R}^{n \times n}"> is nonsingular upper triangular.

## Example
```python
python main.py
```

## Result 1
```
 ###################################################################################### 
 We regrad the results calculated by SciPy as Ground Truth (GT). 
 *. [Q_gt, R_gt] are the right answers.  
 Press "1". [Q1, R1] are the answers calculated by Householder.  
 Press "2". [Q2, R2] are the answers calculated by Gram-Schimidt.  
 Press "3". [Q3, R3] are the answers calculated by Givens.  
 ######################################################################################  

please choose the mode:1
 SciPy GT. 
 Q_gt:  
[[-0.36169609 -0.35157952 -0.71494587 -0.48416959]
 [-0.57677371 -0.60546255  0.54432597  0.06675641]
 [-0.14994178 -0.15526948 -0.43857857  0.8723862 ]
 [-0.71695571  0.6969206   0.01450782  0.00810616]]
 R_gt:  
[[-1.99093655  0.68073746 -0.06990261  0.54731977]
 [ 0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.         -1.50568904  1.0198967 ]
 [ 0.          0.          0.          1.36232617]]
 Verify A=Q_gt*R_gt?    True
 Householder. 
 Q:  
[[ 0.36169609 -0.35157952  0.71494587 -0.48416959]
 [ 0.57677371 -0.60546255 -0.54432597  0.06675641]
 [ 0.14994178 -0.15526948  0.43857857  0.8723862 ]
 [ 0.71695571  0.6969206  -0.01450782  0.00810616]]
 R:  
[[ 1.99093655 -0.68073746  0.06990261 -0.54731977]
 [-0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.          1.50568904 -1.0198967 ]
 [-0.         -0.         -0.          1.36232617]]
 Verify A=Q*R?    True
```

## Result 2
```
 ###################################################################################### 
 We regrad the results calculated by SciPy as Ground Truth (GT). 
 *. [Q_gt, R_gt] are the right answers.  
 Press "1". [Q1, R1] are the answers calculated by Householder.  
 Press "2". [Q2, R2] are the answers calculated by Gram-Schimidt.  
 Press "3". [Q3, R3] are the answers calculated by Givens.  
 ######################################################################################  

please choose the mode:1
 SciPy GT. 
 Q_gt:  
[[-0.36169609 -0.35157952 -0.71494587 -0.48416959]
 [-0.57677371 -0.60546255  0.54432597  0.06675641]
 [-0.14994178 -0.15526948 -0.43857857  0.8723862 ]
 [-0.71695571  0.6969206   0.01450782  0.00810616]]
 R_gt:  
[[-1.99093655  0.68073746 -0.06990261  0.54731977]
 [ 0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.         -1.50568904  1.0198967 ]
 [ 0.          0.          0.          1.36232617]]
 Verify A=Q_gt*R_gt?    True
 Householder. 
 Q:  
[[ 0.36169609 -0.35157952  0.71494587 -0.48416959]
 [ 0.57677371 -0.60546255 -0.54432597  0.06675641]
 [ 0.14994178 -0.15526948  0.43857857  0.8723862 ]
 [ 0.71695571  0.6969206  -0.01450782  0.00810616]]
 R:  
[[ 1.99093655 -0.68073746  0.06990261 -0.54731977]
 [-0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.          1.50568904 -1.0198967 ]
 [-0.         -0.         -0.          1.36232617]]
 Verify A=Q*R?    True
```


## Result 3
```
 ###################################################################################### 
 We regrad the results calculated by SciPy as Ground Truth (GT). 
 *. [Q_gt, R_gt] are the right answers.  
 Press "1". [Q1, R1] are the answers calculated by Householder.  
 Press "2". [Q2, R2] are the answers calculated by Gram-Schimidt.  
 Press "3". [Q3, R3] are the answers calculated by Givens.  
 ######################################################################################  

please choose the mode:1
 SciPy GT. 
 Q_gt:  
[[-0.36169609 -0.35157952 -0.71494587 -0.48416959]
 [-0.57677371 -0.60546255  0.54432597  0.06675641]
 [-0.14994178 -0.15526948 -0.43857857  0.8723862 ]
 [-0.71695571  0.6969206   0.01450782  0.00810616]]
 R_gt:  
[[-1.99093655  0.68073746 -0.06990261  0.54731977]
 [ 0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.         -1.50568904  1.0198967 ]
 [ 0.          0.          0.          1.36232617]]
 Verify A=Q_gt*R_gt?    True
 Householder. 
 Q:  
[[ 0.36169609 -0.35157952  0.71494587 -0.48416959]
 [ 0.57677371 -0.60546255 -0.54432597  0.06675641]
 [ 0.14994178 -0.15526948  0.43857857  0.8723862 ]
 [ 0.71695571  0.6969206  -0.01450782  0.00810616]]
 R:  
[[ 1.99093655 -0.68073746  0.06990261 -0.54731977]
 [-0.          2.1897361   0.06099599  0.03200864]
 [ 0.          0.          1.50568904 -1.0198967 ]
 [-0.         -0.         -0.          1.36232617]]
 Verify A=Q*R?    True
```

## SSH
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```
