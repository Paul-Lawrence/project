from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np
import pandas as pd
import funcs



def fit_LinReg(clf, X, y):
	print("Fitting model...")
	clf.fit(X,y)
	return clf
	
def get_acc(clf,X,y):
	print("Getting accuracy...")
	pred=clf.predict(X)
	return metrics.accuracy_score(y,pred)
	
def get_log_loss(clf,X,y):
	print("Getting log loss...")
	pred=clf.predict_proba(X)
	return metrics.log_loss(y,pred)

def main():
	fname='Alcantara_clean.xlsx'
	print("Reading {}...".format(fname))
	df = pd.read_excel(fname)
	print("Splitting into labels and data...")
	train_set, test_set = funcs.split_datasets(df)
	train_x, train_y = funcs.split_labels(train_set)
	test_x,test_y=funcs.split_labels(test_set)
	clf=LogisticRegression()
	clf=fit_LinReg(clf,train_x,train_y)
	print("Getting scores...")
	train_ll=get_log_loss(clf,train_x,train_y)
	test_ll=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy: {}. Train loss: {}".format(train_acc,train_ll))
	print('Test accuracy: {}. Test loss: {}'.format(test_acc,test_ll))	
	
	


main()