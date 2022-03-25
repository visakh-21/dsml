import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()
X,y=iris.data,iris.target
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y) 
print(tree.plot_tree(clf))
tree.plot_tree(clf)
plt.show()