from sklearn import svm
from sklearn import metrics
import numpy as np
import time
import pandas as pd
import funcs



def fit_SVC(clf, X, y):
	print("Fitting model...")
	clf.fit(X,y)
	return clf
	
def get_acc(clf,X,y):
	pred=clf.predict(X)
	print("Per pitch accuracy: {}".format(funcs.per_pitch_acc(y, pred)))
	return metrics.accuracy_score(y,pred)
	
def get_log_loss(clf,X,y):
	pred=clf.predict_proba(X)
	#print(y)
	#print(X[0])
	#print(pred)
	#for p in pred:
	#	print(p)
	return metrics.log_loss(y,pred)
	
def vector(train_x,train_y,test_x,test_y,pitcher='X'):
	print("Fitting svm...")
	clf=svm.SVC(probability=True)
	clf=fit_SVC(clf, train_x,train_y)
	print("Getting scores...")
	train_bs=get_log_loss(clf,train_x,train_y)
	test_bs=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy for {}: {}. Train score: {}".format(pitcher,train_acc,train_bs))
	print('Test accuracy for {}: {}. Test score: {}'.format(pitcher,test_acc,test_bs))	
	return train_bs,train_acc,test_bs,test_acc
	
def test_1():
	fname='Alcantara_clean.xlsx'
	print("Reading {}...".format(fname))
	df = pd.read_excel(fname)
	print("Splitting into labels and data...")
	train_set, test_set = funcs.split_datasets(df)
	train_x, train_y = funcs.split_labels(train_set)
	test_x,test_y=funcs.split_labels(test_set)
	clf=svm.SVC(probability=True)
	clf=fit_SVC(clf, train_x,train_y)
	print("Getting scores...")
	train_bs=get_log_loss(clf,train_x,train_y)
	test_bs=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy: {}. Train score: {}".format(train_acc,train_bs))
	print('Test accuracy: {}. Test score: {}'.format(test_acc,test_bs))	
	
def test_2():
	name='Alcantara'
	df=funcs.read_clean_sheet(name)
	df1=funcs.get_predict_set(df)
	df2=funcs.get_recog_set(df)
	print("Splitting into labels and data...")
	train_set, test_set = funcs.split_datasets_2(df1)
	train_x, train_y = funcs.split_labels(train_set)
	test_x,test_y=funcs.split_labels(test_set)
	clf=svm.SVC(probability=True)
	clf=fit_SVC(clf,train_x,train_y)
	print("Getting scores...")
	train_ll=get_log_loss(clf,train_x,train_y)
	test_ll=get_log_loss(clf,test_x,test_y)
	train_acc=get_acc(clf,train_x,train_y)
	test_acc=get_acc(clf,test_x,test_y)
	print("Training accuracy: {}. Train loss: {}".format(train_acc,train_ll))
	print('Test accuracy: {}. Test loss: {}'.format(test_acc,test_ll))	

	
def main():
	test_2()
	
main()