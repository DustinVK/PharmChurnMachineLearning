import sklearn as sk
from sklearn.model_selection import train_test_split
import pandas as pd
import tkinter as tk
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import preprocessing

data = pd.read_csv('processed_data.csv')
target = pd.read_csv('out_of_time_test_oct.csv')
iris = load_iris()


##  Preprocessing 
target = target.sort_values(by=['customer_ref_id'])
#print(target.tail())
#print(data.tail())
data=data.drop(["customer_ref_id"],axis=1)
target=target.drop(["customer_ref_id"], axis=1)
print(data.size)
print(y.size)
#print(data.sample(5))

##  Preprocessing 

## TODO
## fix scaler to only scale numeric columns
data=data.drop(["payment_method","store_ref_id","customer_ref_id","doctor_ref_id","payment_method","created_at_bill","bill_ref_id"],axis=1)
#scaler = preprocessing.MinMaxScaler()
#names = data.columns
#d = scaler.fit_transform(data)
#scaled_df = pd.DataFrame(d, columns=names)
#scaled_df.head()

X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
#   print(scaled_df.sample(5))

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)



n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # start with the root node id (0) and its depth (0)
while len(stack) > 0:
    # `pop` ensures each node is only visited once
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # If the left and right child of a node is not the same we have a split
    # node
    is_split_node = children_left[node_id] != children_right[node_id]
    # If a split node, append left and right children and depth to `stack`
    # so we can loop through them
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print("The binary tree structure has {n} nodes and has "
      "the following tree structure:\n".format(n=n_nodes))
for i in range(n_nodes):
    if is_leaves[i]:
        print("{space}node={node} is a leaf node.".format(
            space=node_depth[i] * "\t", node=i))
    else:
        print("{space}node={node} is a split node: "
              "go to node {left} if X[:, {feature}] <= {threshold} "
              "else to node {right}.".format(
                  space=node_depth[i] * "\t",
                  node=i,
                  left=children_left[i],
                  feature=feature[i],
                  threshold=threshold[i],
                  right=children_right[i]))

                  