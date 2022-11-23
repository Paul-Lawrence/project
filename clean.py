import numpy
import pandas



def pitch_class(df):
	df['pitch_type']=df['pitch_type'].replace({'FF': 1, 'FC':2, 'SI':3,'CU':4, 'SL':5, 'CH':6, 'EP':7})
	df['if_fielding_alignment']=df['if_fielding_alignment'].replace({'Infield Shift':2, 'Standard':1, 'Strategic':3})
	df['game_type']=df.['game_type'].replace({'R':1, 'S':2})
	df['stand']=df.['stand'].replace({'L':1,'R':2})
	df['p_throws']=df.['p_throws'].replace({'R':1,'L':2})
	df['of_fielding_alignment']=df['of_fielding_alignment'].replace({'4th outfielder':2, 'Standard':1}, 'Strategic':3})
	df.drop(columns=['pitch_name'])
	return df

def main():
	print("Reading in file...")
	df=pandas.read_excel('Greinke.xlsx')
	df=pitch_class(df)
	print("Writing cleaned file...")
	df.to_excel('Greinke_clean.xlsx')


main()