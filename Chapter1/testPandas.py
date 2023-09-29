import pandas as pd
from IPython.display import display

data = {'Name':["Pierre", "Peter", "Pietr", "Piers"],
	'Location':["Paris", "London", "Berlin", "Dublin"],
	'Age':[24, 13, 54, 33]}

"""
#IPython display allows for beautification of dataframes printing
pandas_data = pd.DataFrame(data)
display(pandas_data)
"""

"""
#Possible to query data:
display(pandas_data[pandas_data.Age >= 18])
"""

