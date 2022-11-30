import pandas as pd
import numpy as np
import torch
from sklearn import preprocessing



def shuffle(df):
	df=df.sample(frac=1).reset_index(drop=True)
	return df


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
	
def cleanfile(fname, pitcher):
	print("Reading in {}...".format(fname))
	df = pd.read_excel(fname)
	#print(df)
	df = cleandf(df, pitcher)
	cleanname=pitcher+"_clean.xlsx"
	print("Writing cleaned file to {}...".format(cleanname))
	df.to_excel(cleanname, index=False)
	return df
	
def replacedates(df):
	le=preprocessing.LabelEncoder()
	le.fit(df.loc[:,'game_date'])
	df['game_date']=le.transform(df.loc[:,'game_date'])
	return df

def main():
	plist=['Bieber','Kershaw','Verlander','Alcantara','Nola','Greinke','Wainwright']
	for pitcher in plist:
		fname=pitcher+".xlsx"
		cleanfile(fname, pitcher)

#main()