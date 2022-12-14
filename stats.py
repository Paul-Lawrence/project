from pybaseball import statcast
from pybaseball import statcast_pitcher
import openpyxl
import pandas 
def main():
	ids=[['Bieber',669456],['Nola',605400],['Wainwright',425794]]
	for player in ids:
		get_data(player)
		
		
def get_data(player):
	#fname='second_try.xlsx'
	print("Getting data for {}....".format(player[0]))
	data=statcast_pitcher(start_dt='2018-03-01', end_dt='2022-10-10', player_id=player[1])
	print("Writing data to file....")
	with pandas.ExcelWriter('second_try.xlsx', engine='openpyxl', mode='a') as writer:
				data.to_excel(writer, sheet_name=player[0])


#main()