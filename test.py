import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt


"""
#Creation of an identity matrix 3
#x = np.array([[1,0,0],[0,1,0],[0,0,1]])
#print("x:\n{}".format(x))
#Same result as
#x = np.eye(3)
#print("x:\n{}".format(x))
"""

"""
#Sparse matrix built using csr (also coo method)
sparse_matrix = sparse.csr_matrix(x)
print("sparse_matrix:\n{}".format(sparse_matrix))
"""

"""
#arange(n) create natural integer from 0 to n
print(np.arange(4)) 
# [0, 1, 2, 3]
print(type(np.arange(2)))
"""


#Generate numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
y = np.sin(x)
#plot displays graph
plt.plot(x, y)
