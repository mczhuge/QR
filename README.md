# QR decomposition
We can compute the QR decomposition by 
* Householder transformations ✅
* Gram Schmidt orthogonalization ✅
* Givens transformations ✅

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
[[-0.22449845 -0.14701545  0.13135285  0.95432349]
 [ 0.17229869 -0.97252432 -0.12679039 -0.09183577]
 [-0.10862132  0.09695988 -0.98148158  0.12447528]
 [ 0.95295069  0.15225535 -0.05800457  0.25561448]]
 R_gt:  
[[-0.54177081  0.88741156  0.61971468 -0.5685338 ]
 [ 0.          1.2231714  -1.27234912 -2.05923665]
 [ 0.          0.         -1.86608816  0.0738163 ]
 [ 0.          0.          0.         -0.35487044]]
 Verify A=Q_gt*R_gt   
 True
 Householder. 
 Q:  
[[ 0.22449845 -0.14701545 -0.13135285  0.95432349]
 [-0.17229869 -0.97252432  0.12679039 -0.09183577]
 [ 0.10862132  0.09695988  0.98148158  0.12447528]
 [-0.95295069  0.15225535  0.05800457  0.25561448]]
 R:  
[[ 0.54177081 -0.88741156 -0.61971468  0.5685338 ]
 [ 0.          1.2231714  -1.27234912 -2.05923665]
 [ 0.         -0.          1.86608816 -0.0738163 ]
 [-0.          0.          0.         -0.35487044]]
 Verify A=Q*R   
 True
```

## Result 2
```
We regrad the results calculated by SciPy as Ground Truth (GT). 
 *. [Q_gt, R_gt] are the right answers.  
 Press "1". [Q1, R1] are the answers calculated by Householder.  
 Press "2". [Q2, R2] are the answers calculated by Gram-Schimidt.  
 Press "3". [Q3, R3] are the answers calculated by Givens.  
 ######################################################################################  

please choose the mode:2
 SciPy GT. 
 Q_gt:  
[[-0.44866273 -0.55346929  0.40539809  0.57273545]
 [ 0.33963341 -0.33279768  0.69089137 -0.54457687]
 [-0.76208911 -0.13804063 -0.1717496  -0.60882431]
 [ 0.32026721 -0.75090761 -0.57343141 -0.06887009]]
 R_gt:  
[[ 1.69018432  0.44829956  0.39125491 -0.10082661]
 [ 0.         -0.77033621 -1.11526531 -1.18449026]
 [ 0.          0.         -1.13237619  2.03735831]
 [ 0.          0.          0.          0.3770548 ]]
 Verify A=Q_gt*R_gt   
 True
 Gram_Schimidt. 
 Q:  
[[-0.44866273  0.55346929 -0.40539809  0.57273545]
 [ 0.33963341  0.33279768 -0.69089137 -0.54457687]
 [-0.76208911  0.13804063  0.1717496  -0.60882431]
 [ 0.32026721  0.75090761  0.57343141 -0.06887009]]
 R:  
[[ 1.69018432  0.44829956  0.39125491 -0.10082661]
 [ 0.          0.77033621  1.11526531  1.18449026]
 [ 0.          0.          1.13237619 -2.03735831]
 [ 0.          0.          0.          0.3770548 ]]
 Verify A=Q*R   
 True
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

please choose the mode:3
 SciPy GT. 
 Q_gt:  
[[-0.19226559 -0.03612689 -0.85748615 -0.47586374]
 [-0.3035267  -0.72079242 -0.22423525  0.58141928]
 [ 0.25503492  0.55778387 -0.44341219  0.65362066]
 [-0.89769854  0.40991497  0.1334979   0.09102393]]
 R_gt:  
[[ 2.74233718 -1.24420653  0.50836465 -0.44123894]
 [ 0.          1.77774359 -0.35345856 -2.15600945]
 [ 0.          0.          0.97608152  0.0262946 ]
 [ 0.          0.          0.         -0.89003521]]
 Verify A=Q_gt*R_gt   
 True
 Givens. 
 Q:  
[[-0.19226559 -0.03612689 -0.85748615  0.47586374]
 [-0.3035267  -0.72079242 -0.22423525 -0.58141928]
 [ 0.25503492  0.55778387 -0.44341219 -0.65362066]
 [-0.89769854  0.40991497  0.1334979  -0.09102393]]
 R:  
[[ 2.74233718 -1.24420653  0.50836465 -0.44123894]
 [ 0.          1.77774359 -0.35345856 -2.15600945]
 [ 0.          0.          0.97608152  0.0262946 ]
 [ 0.          0.          0.          0.89003521]]
 Verify A=Q*R   
  True
```

## SSH
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```
