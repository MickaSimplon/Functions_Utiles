from IPython.display import display
from pprint import pprint
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

def modelTree(X_train,y_train,X_test,y_test):
    # arbre de decision classification
    clf = DecisionTreeClassifier(random_state=0)
    # training dataset
    clf = clf.fit(X_train,y_train)
    print("max_depth ",clf.tree_.max_depth)
    print("max_features ",clf.max_features_,'\n')
    
    print('The parametres the model used:\n')
    pprint(clf.get_params())
    # parqu'un petit grahp ca fait toujours plaisir
    y_pred = clf.predict(X_test)
    # evalutation model
    model=EvaluateModelRegression(clf,X_test,y_test, y_pred)
    
    return model
    
def EvaluateModelRegression(model,X_test,y_test, y_predict):
    accuracy=accuracy_score(y_test, y_predict)
    print('\n','\033[1m' + 'Accuracy score: '+'\033[0m',accuracy) # le plus important pour le moment; précisément la première ligne
    fig = plt.figure()
    # Matrice de confusion
    ax= plt.subplot()
    sns.heatmap(confusion_matrix(y_test,y_predict), annot=True, ax = ax ,fmt='g'); #annot=True to annotate cells
    ax.set_xlabel('Valeurs prédites');ax.set_ylabel('Valeurs réelles'); 
    ax.set_title('Confusion Matrix'); 
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    ax.xaxis.set_ticklabels(['Not purchased', 'Purchased']); ax.yaxis.set_ticklabels(['Not purchased', 'Purchased']);
    
    return model,accuracy