import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#Load example data
iris_dataset = load_iris()

#sklearn train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

#create panda dataframe
iris_dataframe = pd.DataFrame(X_train
