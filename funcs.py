import pandas as pd
import numpy as np
#import torch
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt



def shuffle(df):
	df=df.sample(frac=1).reset_index(drop=True)
	return df

def read_clean_file(name):
	print("Reading in {}.....".format(name))
	return pd.read_excel("{}_clean.xlsx".format(name))
	
def read_clean_sheet(name):
	print("Reading in {}.....".format(name))
	return pd.read_excel('second_try_clean.xlsx',sheet_name=name)

def write(df, fname):
	df.to_excel(fname)
	
def split_labels(df): #Returns tensors 
	labels=df['pitch_type'].values
	arr = df.drop('pitch_type', axis=1).values
	return arr, labels
	
def totensor(arr):
	return torch.from_numpy(ARR.astype(dtype=np.float32))

def split_datasets(df): #Splits into train and test, along with labels
	df = shuffle(df)
	traindf=df.loc[:int(len(df)*0.8)].reset_index(drop=True)
	testdf=df.loc[int(len(df)*0.8):].reset_index(drop=True)
	testdf.loc[:,'spin_axis':'estimated_woba_using_speedangle']=0
	traindf.loc[:int(len(traindf)*0.2),'spin_axis':'estimated_woba_using_speedangle']=0
	return shuffle(traindf),testdf
	
def split_datasets_2(df):
	traindf=df.loc[:int(len(df)*0.8)].reset_index(drop=True)
	testdf=df.loc[int(len(df)*0.8):].reset_index(drop=True)
	return traindf,testdf
	
def pre_post(df):
	predict=get_predict_set(df)
	recog=get_recog_set(df)
	return predict, recog
	
def get_predict_set(df):
	return df.loc[:,'pitch_type':'of_fielding_alignment'].reset_index(drop=True)
	
def get_recog_set(df):
	df.drop(df.iloc[:,1:3], axis=1, inplace=True)
	df.drop(df.iloc[:,4:13], axis=1, inplace=True)
	return df
	
def givedict():
	return {1:'Fastball',2:'Sinker',3:'Curveball',4:'Slider',5:'Changeup',6:'Cutter',7:'Knuckle Curve'}
	
def cleandf(df, pitcher):
	df = df[df['pitch_type'].notna()]
	df['pitch_type']=df['pitch_type'].replace({'FF': 1, 'SI':2, 'CU':3, 'CS':3, 'SL':4, 'CH':5, 'FC':6, 'KC':7})
	df['if_fielding_alignment']=df['if_fielding_alignment'].replace({'Infield shift':2, 'Standard':1, 'Strategic':3})
	df['stand']=df['stand'].replace({'L':1,'R':2})
	df['p_throws']=df['p_throws'].replace({'R':1,'L':2})
	df['of_fielding_alignment']=df['of_fielding_alignment'].replace({'4th outfielder':2, 'Standard':1, 'Strategic':3})
	df['description']=df['description'].replace({'ball':1, 'blocked_ball':1, 'called_strike':2, 'foul':3, 'foul_bunt':3, 'foul_tip':3, 'bunt_foul_tip':3, 'hit_by_pitch':1, 'missed_bunt':5, 'swinging_strike_blocked':5, 'hit_into_play':4, 'swinging_strike':5})
	df['bb_type']=df['bb_type'].replace({'fly_ball':1, 'ground_ball':2,'line_drive':3, 'popup':4})
	df=replacedates(df)
	if (pitcher=='Greinke'):
		df=df[(df['pitch_type']!='FC') & (df['pitch_type']!='EP') & (df['pitch_type']!='FS')]	
	if (pitcher=='Wainwright'):
		df=df[(df['pitch_type']!='EP')]
	if (pitcher=='Verlander'):
		df=df[(df['pitch_type']!='FC')]
	if (pitcher=='Alcantara'):
		df=df[(df['pitch_type']!='CU')]
	if (pitcher=='Kershaw'):
		df=df[(df['pitch_type']!='CH') & (df['pitch_type']!='SI')]
	df=df.drop('Unnamed: 0', axis=1)
	df=df.drop('pitch_name', axis=1)
	df=df.drop('inning_topbot', axis=1)
	df=df.drop('events', axis=1)
	df=df.drop('type', axis=1)
	df=df.drop('game_type',axis=1)
	df=df.drop('bat_score', axis=1)
	df=df.drop('fld_score', axis=1)
	#df=df.drop('pitcher', axis=1) Keep for now, possibly drop later.
	df.fillna(0,inplace=True)
	return df
	
def clean2(df, pitcher):
	df=shuffle(df)
	df = df[df['pitch_type'].notna()]
	df['pitch_type']=df['pitch_type'].replace({'FF': 1, 'SI':2, 'CU':3, 'CS':3, 'SL':4, 'CH':5, 'FC':6, 'KC':3})
	df['if_fielding_alignment']=df['if_fielding_alignment'].replace({'Infield shift':2, 'Standard':1, 'Strategic':3})
	df['stand']=df['stand'].replace({'L':1,'R':2})
	df['p_throws']=df['p_throws'].replace({'R':1,'L':2})
	df['of_fielding_alignment']=df['of_fielding_alignment'].replace({'4th outfielder':2, 'Standard':1, 'Strategic':3})
	#df['description']=df['description'].replace({'ball':1, 'blocked_ball':1, 'called_strike':2, 'foul':3, 'foul_bunt':3, 'foul_tip':3, 'bunt_foul_tip':3, 'hit_by_pitch':1, 'missed_bunt':5, 'swinging_strike_blocked':5, 'hit_into_play':4, 'swinging_strike':5})
	#df['bb_type']=df['bb_type'].replace({'fly_ball':1, 'ground_ball':2,'line_drive':3, 'popup':4})
	#df=replacedates(df)
	if (pitcher=='Greinke'):
		df=df[(df['pitch_type']!='FC') & (df['pitch_type']!='EP') & (df['pitch_type']!='FS')]	
	if (pitcher=='Wainwright'):
		df=df[(df['pitch_type']!='EP')]
	if (pitcher=='Verlander'):
		df=df[(df['pitch_type']!='FC')]
	if (pitcher=='Alcantara'):
		df=df[(df['pitch_type']!='CU')]
	if (pitcher=='Kershaw'):
		df=df[(df['pitch_type']!='CH') & (df['pitch_type']!='SI')]
	if (pitcher=='Bieber'):
		df=df[(df['pitch_type']!='SI')]
	#df=df.drop('bb_type', axis=1)
	df=df.drop('description', axis=1)
	df=df.drop('Unnamed: 0', axis=1)
	df=df.drop('pitch_name', axis=1)
	df=df.drop('inning_topbot', axis=1)
	df=df.drop('events', axis=1)
	df=df.drop('type', axis=1)
	df=df.drop('game_type',axis=1)
	#df=df.drop('pitcher', axis=1) Keep for now, possibly drop later.
	df.fillna(0,inplace=True)
	return df
	
def cleanfile2(pitcher):
	print("Reading in {}...".format(pitcher))
	df = pd.read_excel('second_try.xlsx', sheet_name=pitcher)
	#print(df)
	df = clean2(df, pitcher)
	print("Writing cleaned file...")
	with pd.ExcelWriter('second_try_clean.xlsx', engine='openpyxl', mode='a') as writer:
		df.to_excel(writer, sheet_name=pitcher, index=False)
	return df
	
def cleanfile(fname, pitcher):
	print("Reading in {}...".format(fname))
	df = pd.read_excel(fname)
	#print(df)
	df = cleandf(df, pitcher)
	cleanname=pitcher+"_clean.xlsx"
	print("Writing cleaned file to {}...".format(cleanname))
	df.to_excel(cleanname, index=False)
	return df
	
def per_pitch_acc(y, pred): #Plots per-pitch accuracy based on prediction model.
	cm = metrics.confusion_matrix(y, pred)
	cm=cm.astype('float')/cm.sum(axis=1)[:, np.newaxis]
	return cm.diagonal()
	
	
def replacedates(df):
	le=preprocessing.LabelEncoder()
	le.fit(df.loc[:,'game_date'])
	df['game_date']=le.transform(df.loc[:,'game_date'])
	return df

def concat(pitchers):
	frames=[]
	for p in pitchers:
		print("Loading {}...".format(p))
		df=pd.read_excel('second_try_clean.xlsx',sheet_name=p)
		frames.append(df)
	print("Writing concatenated file...")
	con=shuffle(pd.concat(frames))
	con.to_excel('concat_pitchers.xlsx', index=False)
	return con

def main():
	pitchers=['Alcantara','Bieber','Nola','Verlander','Wainwright']
	concat(pitchers)
#	with pd.ExcelWriter('second_try_clean.xlsx', engine='openpyxl', mode='a') as writer:
#		df.to_excel(writer, sheet_name='Bieber', index=False)
	#df=pd.read_excel('second_try_clean.xlsx',sheet_name='Alcantara')
	#print(df)
	#print(get_predict_set(df))
	#print(get_recog_set(df))

#main()