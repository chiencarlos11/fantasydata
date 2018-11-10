import pandas as pd
import operator

datas = pd.read_csv("data.csv")


temp_name = None

new_list = []
new_list2 = []

for index, row in datas.iterrows():

	#row 10 is 3p
	#row 22 is rebounds
	#row 23 is assists
	#row 24 is steals
	#row 25 is blocks
	#row 26 is TO
	#row 28 is points


	if temp_name and temp_name == row[1]:
		continue

	if not temp_name:
		temp_name = row[1]

	temp_name = row[1]

	calculation = (row[10] * 0.5) + (row[22] * 1.25) + (row[23] * 1.5) + (row[24] * 2) + (row[25] * 2) + (row[28] - row[26]) * .5

	player = {"name":row[1],"score": calculation}
	new_list.append(player)

	player2 = {row[1]:calculation}
	new_list2.append(player2)

for player in new_list:
	print "Name = " + player['name'] + " - " + "score = " + str(player['score'])

