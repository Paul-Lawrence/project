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
	
	
	ax1.set_xticklabels(['Train_acc','Test_acc,','Train_loss','Test_loss'])
	plt.show()
	
def plot_per_pitch_acc(pitchers, pitcher_acc):
	labels=np.arange(1,len(pitcher_acc[0])+1)
	ax1=plt.subplot()
	ax1.set_xticks(labels)
	colors=['black','green','red','yellow','purple']
	labs=[]
	#print(labels)
	#print(pitcher_acc)
	#print(colors)
	for i in range(len(pitchers)):
		labs.append(plt.scatter(labels,pitcher_acc[i], color=colors[i]))
	ax1.set_xticklabels(['Fastball','Sinker','Curveball','Slider','Changeup','Cutter',])
	plt.legend(labs,pitchers)
	plt.ylabel("Per-Pitch Accuracy")
	plt.grid()
	plt.show()
	
def plot_svm_reg_acc(svm_tr,svm_t,reg_tr,reg_t,pitchers):
	labels=np.arange(1,len(pitchers)+1)
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
	labels=np.arange(1,len(pitchers)+1)
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
	
def predict_svm_reg(pitchers):
	svm_train_loss=[0]*len(pitchers)
	svm_test_loss=[0]*len(pitchers)
	reg_train_loss=[0]*len(pitchers)
	reg_test_loss=[0]*len(pitchers)
	svm_train_acc=[0]*len(pitchers)
	svm_test_acc=[0]*len(pitchers)
	reg_train_acc=[0]*len(pitchers)
	reg_test_acc=[0]*len(pitchers)
	for i in range(len(pitchers)):
		df=funcs.read_clean_sheet(pitchers[i])
		df=funcs.get_predict_set(df)
		train_set, test_set = funcs.split_datasets_2(df)
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
	
def recog_svm_reg(pitchers):
	svm_train_loss=[0]*len(pitchers)
	svm_test_loss=[0]*len(pitchers)
	reg_train_loss=[0]*len(pitchers)
	reg_test_loss=[0]*len(pitchers)
	svm_train_acc=[0]*len(pitchers)
	svm_test_acc=[0]*len(pitchers)
	reg_train_acc=[0]*len(pitchers)
	reg_test_acc=[0]*len(pitchers)
	for i in range(len(pitchers)):
		df=funcs.read_clean_sheet(pitchers[i])
		df=funcs.get_recog_set(df)
		train_set, test_set = funcs.split_datasets_2(df)
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
	
def recog_ppa(pitchers):
	pitcher_acc=[]
	for i in range(len(pitchers)):
		df=funcs.read_clean_sheet(pitchers[i])
		df=funcs.get_recog_set(df)
		train_set, test_set = funcs.split_datasets_2(df)
		train_x, train_y = funcs.split_labels(train_set)
		test_x,test_y=funcs.split_labels(test_set)
		acc=regression.per_pitch_reg(train_x,train_y,test_x,test_y, pitchers[i])
		pitcher_acc.append(pad_zeroes(pitchers[i],acc))
	plot_per_pitch_acc(pitchers,pitcher_acc)
	
def svm_ppa(pitchers):
	pitcher_acc=[]
	for i in range(len(pitchers)):
		df=funcs.read_clean_sheet(pitchers[i])
		df=funcs.get_recog_set(df)
		train_set, test_set = funcs.split_datasets_2(df)
		train_x, train_y = funcs.split_labels(train_set)
		test_x,test_y=funcs.split_labels(test_set)
		acc=svm.per_pitch_svm(train_x,train_y,test_x,test_y, pitchers[i])
		pitcher_acc.append(pad_zeroes(pitchers[i],acc))
	plot_per_pitch_acc(pitchers,pitcher_acc)
		
def pad_zeroes(pitcher, pitches):
	if (pitcher=='Alcantara'):
		pitches=np.append(pitches,0)
	elif (pitcher=='Bieber'):
		pitches=np.insert(pitches,1,0)
	elif (pitcher=='Nola'):
		pitches=np.insert(pitches,3,0)
	elif (pitcher=='Verlander'):
		pitches=np.insert(pitches,1,0)
		pitches=np.append(pitches,0)
	elif (pitcher=='Wainwright'):
		pitches=np.insert(pitches,3,0)
	return pitches

def learn_concat(con):
	train_set,test_set=funcs.split_datasets_2(con)
	train_x,train_y=funcs.split_labels(train_set)
	test_x,test_y=funcs.split_labels(test_set)
	train_acc,train_loss,test_acc,test_loss=regression.regress(train_x,train_y,test_x,test_y)
	acc=regression.per_pitch_reg(train_x,train_y,test_x,test_y)
	labels=np.arange(1,len(acc)+1)
	ax1=plt.subplot()
	ax1.set_xticks(labels)
	plt.plot(labels,acc)
	ax1.set_xticklabels(['Fastball','Sinker','Curveball','Slider','Changeup','Cutter'])
	plt.ylabel("Per-Pitch Accuracy")
	plt.grid()
	plt.show()
	
	
def predict_con():
	print("Reading in file...")
	df=pd.read_excel('concat_pitchers.xlsx')
	df=funcs.get_predict_set(df)
	learn_concat(df)
	
def recog_con():
	print("Reading in file...")
	df=pd.read_excel('concat_pitchers.xlsx')
	df1=funcs.get_recog_set(df)
	learn_concat(df1)
	#df2=funcs.get_predict_set(df)
	#learn_concat(df2)
	
def main():
	#pitchers=['Alcantara','Bieber','Nola','Verlander','Wainwright']
	predict_con()
	#test=[1,1,1,1,1]
	#plot_svm_reg_loss(test,test,test,test,pitchers)
	#svm_reg_att_1(pitchers)

	
main()