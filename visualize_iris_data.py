import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from IPython.display import display

#Load example data
iris_dataset = load_iris()

#sklearn train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

#create panda dataframe
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

plotted_data = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o', hist_kwds={'bins':20}, s= 60, alpha=.8)

plt.show()
