from pybaseball import statcast
from pybaseball import playerid_lookup
import openpyxl
import pandas 


def lookup(Name):
	print(playerid_lookup(Name[1],Name[0])["key_mlbam"])


def main():
	names=[['Kyle', 'Gibson']]
	for n in names:
		lookup(n)
main()