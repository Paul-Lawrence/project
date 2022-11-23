from pybaseball import statcast
from pybaseball import statcast_pitcher
import openpyxl
import pandas 
def main():
	ids=[['Gibson',502043]]
	for player in ids:
		get_data(player)
		
		
def get_data(player):
	fname="{}.xlsx".format(player[0])
	print("Getting data for {}....".format(player[0]))
	data=statcast_pitcher(start_dt='2018-03-01', end_dt='2022-10-10', player_id=player[1])
	print("Writing data to file....")
	data.to_excel(fname)


if __name__ == '__main__':
	main()