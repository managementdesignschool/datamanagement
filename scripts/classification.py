from sklearn import tree
from sklearn.datasets import load_iris
import pydotplus 
from IPython.display import Image 

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
clf.predict([[2., 2.]])
clf.predict_proba([[2., 2.]])


