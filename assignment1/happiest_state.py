import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    return fp.readlines()

def processSenti(fp):
	dictSenti = {}
	for item in lines(fp):
		sentence = item.split('\t')
		dictSenti[sentence[0]] = sentence[1].rstrip()
	return dictSenti

def getGeo(fp, senti):
    sentiList = {}
    for item in lines(fp):
        jsonTw = json.loads(item)
        if "text" in jsonTw:    
            tweet = jsonTw["text"]
            place = jsonTw["place"]
            if place is not None:
                country = place["country_code"]
                if country == "US" and place["place_type"] != "poi" and place["place_type"] != "neighborhood":
                    city = place["full_name"].split(', ')
                    sentiScore = 0.0
                    for token in tweet.split(' '):
                        if token.lower() in senti:
                            sentiScore += int(senti[token.lower()])    

                    if city[1] in sentiList:
                        sentiList[city[1]] = sentiList[city[1]] + sentiScore
                    else:
                        sentiList[city[1]] = sentiScore    

    print max(sentiList, key=sentiList.get)          
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    senti = processSenti(sent_file)
    getGeo(tweet_file, senti)

if __name__ == '__main__':
    main()
