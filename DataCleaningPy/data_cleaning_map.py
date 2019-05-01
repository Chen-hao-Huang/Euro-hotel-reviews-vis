import csv
import json


def w():
	hotelList = []
	data = []

	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:	
			hotel_name = csvRow["Hotel_Name"]
			
			if hotel_name not in hotelList:
				hotelList.append(hotel_name)
			else:
				continue;			
			
			score = float(csvRow["Average_Score"])
			csvRow["Average_Score"] = score
			csvRow["Total_Number_of_Reviews"] = int(csvRow["Total_Number_of_Reviews"])
			csvRow["Coordinates"] = json.loads(csvRow["Coordinates"])
#			address = csvRow["Hotel_Address"]		
			csvRow["Negative_Review"] = None
			csvRow["Positive_Review"] = None
			
			if score >= 9:
				csvRow["group"] = "A"
			elif 8 <= score < 9:
				csvRow["group"] = "B"
			elif 7 <= score < 8:
				csvRow["group"] = "C"
			elif 6 <= score < 7:
				csvRow["group"] = "D"
			else:
				csvRow["group"] = "E"

			
			data.append(csvRow)
#			print(data[-1])

	with open(jsonfile, 'w') as jsonFile:
#		print(json.dumps(data))
		jsonFile.write("hotels = ")
		jsonFile.write(json.dumps(data))
	
	
def r():
	with open(jsonfile) as json_data:
		jsonDoc = json.load(json_data)
	print(jsonDoc)

#csvfile = 'Hotel_Reviews_clean_test_v2.csv'
#jsonfile = 'Hotel_Reviews_clean_mapData.json'	
	
csvfile = 'Hotel_Reviews_clean_v2.csv'
jsonfile = 'Hotels_MapData.json'

w()
#r()
	