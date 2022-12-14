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
	print("Per pitch accuracy: {}".format(funcs.per_pitch_acc(y, pred)))
	return metrics.accuracy_score(y,pred)
	
def get_log_loss(clf,X,y):
	#print("Getting log loss...")
	pred=clf.predict_proba(X)
	#for i in range(len(pred)):
	#	print(y[i],pred[i])
	return metrics.log_loss(y,pred)

def regress(train_x,train_y,test_x,test_y, pitcher='X'):
	clf=LogisticRegression()
	print("Fitting linear regression...")
	clf=fit_LinReg(clf,train_x,train_y)
	print("Getting scores...")
	train_ll=get_log_loss(clf,train_x,train_y)
	test_ll=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy for {}: {}. Train loss: {}".format(pitcher,train_acc,train_ll))
	print('Test accuracy for {}: {}. Test loss: {}'.format(pitcher,test_acc,test_ll))	
	return (train_acc,train_ll,test_acc,test_ll)

def test_1():
	fname="Alcantara_clean.xlsx"
	df=pd.read_excel(fname)
	train_set, test_set = funcs.split_datasets(df)
	train_x, train_y = funcs.split_labels(train_set)
	test_x,test_y=funcs.split_labels(test_set)
	clf=LogisticRegression()
	print("Fitting linear regression...")
	clf=fit_LinReg(clf,train_x,train_y)
	print("Getting scores...")
	train_ll=get_log_loss(clf,train_x,train_y)
	test_ll=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy: {}. Train loss: {}".format(train_acc,train_ll))
	print('Test accuracy: {}. Test loss: {}'.format(test_acc,test_ll))	

def test_2():
	name='Alcantara'
	df=funcs.read_clean_sheet(name)
	df1=funcs.get_predict_set(df)
	df2=funcs.get_recog_set(df)
	print("Splitting into labels and data...")
	train_set, test_set = funcs.split_datasets_2(df1)
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
	


def main():
	test_2()

#main()