import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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
print(X_train.shape) #75% of row
print(X_test.shape)  #Remaining 25%
print(y_train.shape)
print(y_test.shape)
"""

#knn for k nearest neighbors is a very simple machine learning
#model, we will do k=1
knn = KNeighborsClassifier(n_neighbors=1)
#like every scikit machine learning model this is called an
#estimator class. We can use the fit method to train it
knn.fit(X_train, y_train)
 
#The instance knn is now trained!
#Let's try it out:
X_new = np.array([[3, 4, 3, 0.8]])
#scikit always expects 2D numpy arrays

"""
prediction = knn.predict(X_new)
print(prediction, iris_dataset['target_names'][prediction])
#0:setosa
"""

#How can we see if our model is correct? That is why we have
#X_test!
#print(y_test)

y_pred = knn.predict(X_test)
#print(y_pred)

print("Score : {:.2f}".format(np.mean(y_pred == y_test)))
#print(np.mean(y_pred == y_test))
