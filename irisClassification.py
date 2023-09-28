from sklearn.datasets import load_iris

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
print(iris_dataset['data'].shape)
"""

