import csv
import json


hotelPosDict = {}
hotelNegDict = {}

def readTxt():
	stopWords = []
	path = "stopwords.txt"
	f = open(path, "r") 
	for line in f:
		if (line[-1] == "\n"):	
			stopWords.append(line[0:-1])
		else:
			stopWords.append(line)
	f.close() 
	
#	print(stopWords)
	return stopWords

def count(review, stopWords, txtDict):
	#{"text":"study","size":40}
	for word in review.split():
		if word.isdigit():
			continue
		word = word.lower()
		if word not in stopWords:
			if word not in txtDict.keys():
				txtDict[word] = 1
			else:
				txtDict[word] += 1
	

def w(stopWords, pos_jsonfile, neg_jsonfile):
	posData = {}
	negData = {}

	with open(csvfile) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:	
			hotelName = csvRow["Hotel_Name"]
			posReview = csvRow["Positive_Review"]
			negReview = csvRow["Negative_Review"]
			
			if hotelName not in hotelPosDict.keys():
				hotelPosDict[hotelName] = {}
				
			if hotelName not in hotelNegDict.keys():
				hotelNegDict[hotelName] = {}
				
			count(posReview, stopWords, hotelPosDict[hotelName])	
			count(negReview, stopWords, hotelNegDict[hotelName])
			
#	print(hotelPosDict[hotelName])
	
	for hotelName, hotelDict in hotelPosDict.items():
		posData[hotelName] = []
		
		key_max = max(hotelDict.keys(), key=(lambda k: hotelDict[k]))		
#		print('Maximum Value: ',hotelDict[key_max])

		for key, value in hotelDict.items():
#			if value == 1:
#				continue
			if hotelDict[key_max] < 45:
				value *= 2
			temp = {}
			temp["text"] = key
			temp["size"] = value
			posData[hotelName].append(temp)
		
	for hotelName, hotelDict in hotelNegDict.items():
		negData[hotelName] = []
		key_max = max(hotelDict.keys(), key=(lambda k: hotelDict[k]))	
		
		for key, value in hotelDict.items():
#			if value == 1:
#				continue
			if hotelDict[key_max] < 45:
				value *= 2
			temp = {}
			temp["text"] = key
			temp["size"] = value
			negData[hotelName].append(temp)
			
#	print(posData[hotelName])

	with open(pos_jsonfile, 'w') as jsonFile:
#		print(json.dumps(data))
		jsonFile.write("Pos_Review = ")
		jsonFile.write(json.dumps(posData))
	
	with open(neg_jsonfile, 'w') as jsonFile:
#		print(json.dumps(data))
		jsonFile.write("Neg_Review = ")
		jsonFile.write(json.dumps(negData))
	
#def r():
#	with open(jsonfile) as json_data:
#		jsonDoc = json.load(json_data)
#	print(jsonDoc)

############################################################################
	
csvfile = 'Hotel_Reviews_clean_v2.csv'
pos_jsonfile = 'Pos_Review.json'
neg_jsonfile = 'Neg_Review.json'
	
#csvfile = 'Hotel_Reviews_clean_test_v2.csv'
#pos_jsonfile = 'Pos_Review.json'
#neg_jsonfile = 'Neg_Review.json'

stopWords = readTxt()
w(stopWords, pos_jsonfile, neg_jsonfile)
#r()
	