import funcs
import regression
import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def svm_reg_att_1(pitchers):
	svm_train_loss=[0]*len(pitchers)
	svm_test_loss=[0]*len(pitchers)
	reg_train_loss=[0]*len(pitchers)
	reg_test_loss=[0]*len(pitchers)
	svm_train_acc=[0]*len(pitchers)
	svm_test_acc=[0]*len(pitchers)
	reg_train_acc=[0]*len(pitchers)
	reg_test_acc=[0]*len(pitchers)
	for i in range(len(pitchers)):
		df=funcs.read_clean_file(pitchers[i])
		train_set, test_set = funcs.split_datasets(df)
		train_x, train_y = funcs.split_labels(train_set)
		test_x,test_y=funcs.split_labels(test_set)
		rtrain_acc,rtrain_loss,rtest_acc,rtest_loss=regression.regress(train_x,train_y,test_x,test_y, pitchers[i])
		reg_train_loss[i]=rtrain_loss
		reg_test_loss[i]=rtest_loss
		reg_train_acc[i]=rtrain_acc
		reg_test_acc[i]=rtest_acc
		svtr_loss,svtr_acc,svt_loss,svt_acc=svm.vector(train_x,train_y,test_x,test_y,pitchers[i])
		svm_train_loss[i]=svtr_loss
		svm_test_loss[i]=svt_loss
		svm_train_acc[i]=svtr_acc
		svm_test_acc[i]=svt_acc		
	plot_svm_reg_loss(svm_train_loss,svm_test_loss,reg_train_loss,reg_test_loss, pitchers)
	plot_svm_reg_acc(svm_train_acc,svm_test_acc,reg_train_acc,reg_test_acc,pitchers)
	
def plot_svm_reg_acc(svm_tr,svm_t,reg_tr,reg_t,pitchers):
	labels=[1,2,3,4,5]
	ax1=plt.subplot()
	ax1.set_xticks(labels)
	b=plt.scatter(labels,svm_tr, color='black')
	g=plt.scatter(labels,svm_t, color='green')
	r=plt.scatter(labels,reg_tr, color='red')
	y=plt.scatter(labels, reg_t, color='yellow')
	ax1.set_xticklabels(pitchers)
	plt.legend((b,g,r,y),('SVM train','SVM test','Reg train', 'Reg test'))
	plt.ylabel("Accuracy")
	plt.show()
	
def plot_svm_reg_loss(svm_tr,svm_t,reg_tr,reg_t,pitchers):
	labels=[1,2,3,4,5]
	ax1=plt.subplot()
	ax1.set_xticks(labels)
	b=plt.scatter(labels,svm_tr, color='black')
	g=plt.scatter(labels,svm_t, color='green')
	r=plt.scatter(labels,reg_tr, color='red')
	y=plt.scatter(labels, reg_t, color='yellow')
	ax1.set_xticklabels(pitchers)
	plt.legend((b,g,r,y),('SVM train','SVM test','Reg train', 'Reg test'))
	plt.ylabel("Loss")
	plt.show()
	
def main():
	pitchers=['Alcantara','Bieber','Nola','Verlander','Wainwright']
	#svm_reg_att_1(pitchers)
	#test=[1,1,1,1,1]
	#plot_svm_reg_loss(test,test,test,test,pitchers)
	svm_reg_att_1(pitchers)
	
	
	
main()