import numpy
import pandas



def pitch_class(df):
	df['pitch_type']=df['pitch_type'].replace({'FF': 1, 'FC':2, 'SI':3,'CU':4, 'SL':5, 'CH':6, 'EP':7})
	df['if_fielding_alignment']=df['if_fielding_alignment'].replace({'Infield shift':2, 'Standard':1, 'Strategic':3})
	df['stand']=df['stand'].replace({'L':1,'R':2})
	df['p_throws']=df['p_throws'].replace({'R':1,'L':2})
	df['of_fielding_alignment']=df['of_fielding_alignment'].replace({'4th outfielder':2, 'Standard':1, 'Strategic':3})
	df['description']=df['description'].replace({'ball':1, 'blocked_ball':1, 'called_strike':2, 'foul':3, 'foul_bunt':3, 'foul_tip':3, 'bunt_foul_tip':3, 'hib_by_pitch':1, 'missed_bunt':5, 'swinging_strike_blocked':5, 'hit_into_play':4, 'swinging_strike':5})
	df['bb_type']=df['bb_type'].replace({'':0,'fly_ball':1, 'ground_ball':2,'line_drive':3, 'popup':4})
	df=df.drop('pitch_name', axis=1)
	df=df.drop('inning_topbot', axis=1)
	df=df.drop('events', axis=1)
	df=df.drop('type', axis=1)
	df=df.drop('game_type',axis=1)
	df=df.drop('pitcher', axis=1)
	df.fillna(0,inplace=True)
	#df.drop('game_date',axis=1)
	#df.drop(columns=['inning_topbot'])
	#df.drop(columns=['events'])
	#df.drop(columns=['type'])	
	#df.drop(columns=['game_type'])
	#df.drop(columns=['pitcher']) #Drops pitcher ID from the dataset. Remove if running model on multiple pitchers.
	#df.drop(['game_date']) #Keep for now, possibly delete later. Kind of meta gaming, but eh we're not perfect.
	return df

def main():
	print("Reading in file...")
	df=pandas.read_excel('Greinke.xlsx')
	df=pitch_class(df)
	print("Writing cleaned file...")
	df.to_excel('Greinke_clean.xlsx')


main()