import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
#this function returns a bunch object, similar to a python dict
#with keys
#print("keys of iris_dataset: \n{}".format(iris_dataset.keys()))

#print(iris_dataset['DESCR'])

#Data is in data (noshit) and target
"""
#print("Target names:\n{}".format(iris_dataset['target_names']))
#target key is an array of number, where 0, 1 and 2 correspond
#to the three names contained in target names
"""

"""
#Data is numpy array format (150, 4)
print(type(iris_dataset['data']))
#print(iris_dataset['data'].shape)
#print(iris_dataset['target'].shape)
print(iris_dataset['data'])
print(iris_dataset['target'])
"""
#print(iris_dataset['data'][:5])

#scikit-learn has train_test_split function that
#automatically spearates data into two arrays

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

"""
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
"""
