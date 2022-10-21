# QR decomposition
We can compute the QR decomposition by 
* Householder transformations ✅
* Gram Schmidt orthogonalization 
* Givens transformations (TBD)

**Theorem:**

If <img src="https://render.githubusercontent.com/render/math?math=A \in \mathbb{R}^{m \times n}"> has full column rank, i.e, Rank(<img src="https://render.githubusercontent.com/render/math?math=A">)=<img src="https://render.githubusercontent.com/render/math?math=n"> then <img src="https://render.githubusercontent.com/render/math?math=A"> has the QR decomposition:

<img src="https://render.githubusercontent.com/render/math?math=A = Q \begin{bmatrix}R \\0 \end{bmatrix} = Q_1 R">

where <img src="https://render.githubusercontent.com/render/math?math=Q=[Q_1, Q_2] \in \mathbb{R}^{m \times m}"> is orthogonal and <img src="https://render.githubusercontent.com/render/math?math=R \in \mathbb{R}^{n \times n}"> is nonsingular upper triangular.

## Example
```python
python main.py
```

## Results
```
###################################################################################### 
 We regrad the results calculated by SciPy as Ground Truth (GT). 
 1. [Q_gt, R_gt] are the right answers.  
 2. [Q, R] are the answers by our writtern code.  
 3. [Q_zhihu, R_zhihu] are the answers calculated by the code in Zhihu.  
######################################################################################  

----- Matrix A: ----- 
[[-1.74226396  0.6394264  -0.60030749]
 [-1.51665236  0.55953967  0.77552718]
 [ 0.27131504  0.46961015 -0.11772394]
 [-0.18711166 -1.27480409 -0.74461359]
 [ 1.47244601  1.26409315 -0.3883074 ]]

 Q_gt:  
[[-0.63146905 -0.34334421 -0.64925969 -0.23549399  0.07978737]
 [-0.54969801 -0.30031311  0.46712446  0.62405034  0.00021486]
 [ 0.09833587 -0.22572117 -0.11851594  0.06703927 -0.95960394]
 [-0.06781706  0.62210896 -0.48891303  0.60562852 -0.0505908 ]
 [ 0.53367578 -0.594943   -0.32737534  0.42874653  0.26501845]]
 Q:  
[[-0.63146905 -0.25779967 -0.14292792 -0.44513777  0.56232566]
 [-0.54969801 -0.37554978 -0.29341018  0.50545422 -0.46391914]
 [ 0.09833587 -0.22675136 -0.17632247 -0.72802905 -0.61465272]
 [-0.06781706  0.64700462 -0.75885908 -0.03007482  0.00377649]
 [ 0.53367578 -0.56786489 -0.53528063  0.12424817  0.30125847]]
 Q_zhihu:  
[[-0.50736423  0.36129833 -0.74344498]
 [-0.61089959  0.35719714  0.40011111]
 [ 0.10928427  0.21913457  0.07633517]
 [-0.07536759 -0.61843068 -0.44149821]
 [ 0.59309351  0.55802979 -0.29402879]]
 R_gt:  
[[ 2.75906469  0.09589307 -0.21553938]
 [ 0.         -2.03871183 -0.23242611]
 [ 0.          0.          1.25714889]
 [ 0.          0.          0.        ]
 [ 0.          0.          0.        ]]
 R:  
[[ 2.75906469  0.09589307 -0.21553938]
 [ 0.         -2.02410191 -0.37105822]
 [ 0.         -0.04761726  0.65192073]
 [ 0.         -0.14830021  0.7190671 ]
 [-0.          0.18734204 -0.74478378]]
 R_zhihu:  
[[ 2.7275355   0.23088072 -0.35624293]
 [-0.17438212  2.02757708  0.2781334 ]
 [ 0.35882676 -0.02450861  1.19052528]]
 Compute A=Q_gt*R_gt:  
[[-1.74226396  0.6394264  -0.60030749]
 [-1.51665236  0.55953967  0.77552718]
 [ 0.27131504  0.46961015 -0.11772394]
 [-0.18711166 -1.27480409 -0.74461359]
 [ 1.47244601  1.26409315 -0.3883074 ]]
True
 Compute A=QR:  
[[-1.74226396  0.6394264  -0.60030749]
 [-1.51665236  0.55953967  0.77552718]
 [ 0.27131504  0.46961015 -0.11772394]
 [-0.18711166 -1.27480409 -0.74461359]
 [ 1.47244601  1.26409315 -0.3883074 ]]
True
 Compute A=Q_zhihu*R_zhihu:  
[[-1.74226396  0.6394264  -0.60030749]
 [-1.51665236  0.55953967  0.77552718]
 [ 0.27131504  0.46961015 -0.11772394]
 [-0.18711166 -1.27480409 -0.74461359]
 [ 1.47244601  1.26409315 -0.3883074 ]]
False
```

## SSH
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```
