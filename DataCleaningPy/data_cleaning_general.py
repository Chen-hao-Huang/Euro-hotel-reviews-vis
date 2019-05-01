import csv
import json


def w():
	scoreList = {}
	
	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:	
			#hotel_name, review_date, avg(reviewer_score)
			date = csvRow["Review_Date"].split("/")
			review_date = date[0] + "/" + date[2]
			hotel_name = csvRow["Hotel_Name"]
			reviewer_score = float(csvRow["Reviewer_Score"])
			
			if hotel_name not in scoreList.keys():
				scoreList[hotel_name] = {}
			
			if review_date not in scoreList[hotel_name].keys():
				scoreList[hotel_name][review_date] = [0,0,0]
			
			totalScore = scoreList[hotel_name][review_date][0] 
			cnt = scoreList[hotel_name][review_date][1] 
			avgScore = scoreList[hotel_name][review_date][2]
			
			totalScore += reviewer_score
			cnt += 1
			avgScore = round(totalScore / cnt, 2)
			
			scoreList[hotel_name][review_date][0] = totalScore
			scoreList[hotel_name][review_date][1] = cnt
			scoreList[hotel_name][review_date][2] = avgScore
			
#			print(scoreList)
	
	data = []

	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:	
			csvRow["Average_Score"] = float(csvRow["Average_Score"])
			csvRow["Total_Number_of_Reviews"] = int(csvRow["Total_Number_of_Reviews"])
			csvRow["Total_Number_of_Reviews_Reviewer_Has_Given"] = int(csvRow["Total_Number_of_Reviews_Reviewer_Has_Given"])
			csvRow["Reviewer_Score"] = float(csvRow["Reviewer_Score"])
			csvRow["days_since_review"] = int(csvRow["days_since_review"])
			csvRow["Coordinates"] = json.loads(csvRow["Coordinates"])
			csvRow["Negative_Review"] = None
			csvRow["Positive_Review"] = None
			hotel_name = csvRow["Hotel_Name"]
			
			nightsStay = int(csvRow["Nights_Stay"].split()[1])
			csvRow["Nights_Stay"] = nightsStay
			
			date = csvRow["Review_Date"].split("/")
			mydate = date[0] + "/" + date[2]
			csvRow["Review_Date"] = mydate
			
			score = float(csvRow["Average_Score"])
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
				
			
			csvRow["Avg_Score_Per_Month"] = scoreList[hotel_name][mydate][2]
			
			data.append(csvRow)
#			print(data[-1])

	with open(jsonfile, 'w') as jsonFile:
#		print(json.dumps(data))
		jsonFile.write("hotels_reviews = ")
		jsonFile.write(json.dumps(data))
	
	
def r():
	with open(jsonfile) as json_data:
		jsonDoc = json.load(json_data)
	print(jsonDoc)

#csvfile = 'Hotel_Reviews_clean_test_v2.csv'
#jsonfile = 'Hotel_Reviews_clean_test_v2.json'	
	
csvfile = 'Hotel_Reviews_clean_v2.csv'
jsonfile = 'Hotels_Reviews.json'

w()
#r()
	