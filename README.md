# QR decomposition
We can compute the QR decomposition by 
* Householder transformations ✅
* Gram Schmidt orthogonalization 
* Givens transformations ()

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
 We regrad the results calculated by SciPy as Grount Truth (GT). 
 1. [Q_gt, R_gt] is the right answers.  
 2. [Q, R] is the answers by our writtern code.  
 3. [Q_zhihu, R_zhihu] is the answers calculated by the code in Zhihu.  
 ######################################################################################  

----- Matrix A: ----- 
[[ 0.19221278 -0.37351214 -0.27171021]
 [ 1.72252865 -0.40037842  2.59932352]
 [-0.8023016   0.43534781 -0.15470286]
 [ 1.16978519  0.68477146 -0.0997836 ]
 [ 1.38014511 -1.37904243 -0.26878788]]

 Q_gt:  
[[-0.07306339  0.21269849  0.14240509  0.32188823 -0.90858673]
 [-0.65476284 -0.10251652 -0.73840865  0.11578997 -0.04605794]
 [ 0.30496867 -0.12187958 -0.12733167  0.90277751  0.24681753]
 [-0.44465552 -0.72169988  0.51492026  0.12741223 -0.00734841]
 [-0.52461695  0.63917476  0.39130195  0.22746327  0.33373032]]
 Q:  
[[-0.07306339  0.49345516  0.02015343 -0.83674646  0.22497321]
 [-0.65476284  0.0583542   0.44961266 -0.05939708 -0.60183125]
 [ 0.30496867  0.12370227 -0.57346842 -0.16430219 -0.73200452]
 [-0.44465552  0.61964321 -0.44402916  0.43893967  0.16880118]
 [-0.52461695 -0.59484186 -0.52097444 -0.27688284  0.15120101]]
 Q_zhihu:  
[[ 0.35617274  0.19224154 -0.42391899]
 [ 0.61346318  0.2474625   0.74691111]
 [-0.28573254  0.21373184  0.12093406]
 [ 0.41660854  0.52044135 -0.47358842]
 [ 0.49152634 -0.76502614 -0.15331487]]
 R_gt:  
[[-2.63076728  0.84119205 -1.54388789]
 [ 0.         -1.46710867 -0.40519944]
 [ 0.          0.         -2.09491514]
 [ 0.          0.          0.        ]
 [ 0.          0.          0.        ]]
 R:  
[[-2.63076728  0.84119205 -1.54388789]
 [ 0.          1.09080441  0.09652359]
 [ 0.         -0.02281361  1.43626852]
 [ 0.          0.94719421  0.1290021 ]
 [ 0.         -0.25466893 -1.56972305]]
 R_zhihu:  
[[ 2.52013271 -0.89559935  1.36833011]
 [-0.15530736  1.33355139  0.71163444]
 [ 0.34247406 -0.20093194  2.12640342]]
 Compute A=Q_gt*R_gt:  
[[ 0.19221278 -0.37351214 -0.27171021]
 [ 1.72252865 -0.40037842  2.59932352]
 [-0.8023016   0.43534781 -0.15470286]
 [ 1.16978519  0.68477146 -0.0997836 ]
 [ 1.38014511 -1.37904243 -0.26878788]]
True
 Compute A=QR:  
[[ 0.19221278 -0.37351214 -0.27171021]
 [ 1.72252865 -0.40037842  2.59932352]
 [-0.8023016   0.43534781 -0.15470286]
 [ 1.16978519  0.68477146 -0.0997836 ]
 [ 1.38014511 -1.37904243 -0.26878788]]
True
 Compute A=Q_zhihu*R_zhihu:  
[[ 0.19221278 -0.37351214 -0.27171021]
 [ 1.72252865 -0.40037842  2.59932352]
 [-0.8023016   0.43534781 -0.15470286]
 [ 1.16978519  0.68477146 -0.0997836 ]
 [ 1.38014511 -1.37904243 -0.26878788]]
False
```

## SSH
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```
