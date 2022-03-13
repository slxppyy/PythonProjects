from turtle import shape
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
# Data Reading
data = pd.read_csv(r'C:\Users\ashan\OneDrive\Documents\GitHub\PythonProjects\Machine_Learning\reading_data/iris.csv')
print(data)

# Data Analysis

print(data.info())
print(data.shape)
print(data.head(20))
print(data.tail(20))
print(data.describe())
cormatrix = data.corr()
plt.subplots = data.corr()
sns.heatmap(cormatrix, annot = True)
plt.show()

# Data Visualization

data.plot(kind = 'kde', subplots = True, layout = (2,2), sharex = False, sharey = False)
plt.show()
scatter_matrix(data, diagonal='hist')
scatter_matrix(data, diagonal='kde')
plt.show()

# Data Preperation

array = data.values
print(array)

X = array[:, 0:4]
print(X.shape)

y = array[:, 4:5] # also write directly 4, same result
print(y)

from sklearn.model_selection import train_test_split as tts

X_tr, X_tst, Y_tr, Y_tst = tts(X, y, test_size=0.20, random_state=1)

print(X_tr, Y_tr, X_tst, Y_tst)

