import pandas as pandas
from sklearn.model_selection import train_test_split

iris = pandas.read_csv("iris.csv")
valores_da_class = iris['class'].value_counts()

X, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify = iris.iloc[:,4])

value_counts = y.value_counts()

infert = pandas.read_csv("infert.csv")

education_counts = infert['education'].value_counts()

X1, _, y1, _ = train_test_split(infert.iloc[:,2:9], infert.iloc[:,1], test_size=0.6, stratify = infert.iloc[:,1])