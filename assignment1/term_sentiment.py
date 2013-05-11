import sys
import json

def lines(fp):
    return fp.readlines()

def processSenti(fp):
	dictsenti = {}
	for item in lines(fp):
		sentence = item.split('\t')
		dictsenti[sentence[0]] = sentence[1].rstrip()
	return dictsenti

def processTweets(fp, senti):
    sentiList = []
    for item in lines(fp):
        jsonTw = json.loads(item)
        if "text" in jsonTw:
            tweet = jsonTw["text"]
            tweet_id = jsonTw["id"]
            user = jsonTw["user"]
            if user is not None:
                if user["lang"] == "en":                 
                    sentiScore = 0.0
                    for word in tweet.split():
                        if word in senti:
                            sentiScore += int(senti[word])     
                    sentiList.append([tweet_id,sentiScore, tweet])

    filtersenti = []        
    for item in sentiList:
    	if item[1] != 0:
    		filtersenti.append(item) 
    return filtersenti

def newtermsenti(sentifilter, senti):
	newterm = {}
	for item in sentifilter:
		for word in item[2].split():
			if word not in senti:
				if word in newterm:
					newterm[word] = newterm[word] + item[1]
				else:	
					newterm[word] =item[1]
	for key,value in newterm.iteritems():
		print "%s %s" % (key.encode("utf-8"),value)			

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dictsenti = processSenti(sent_file)
    sentifilter = processTweets(tweet_file, dictsenti)
    newtermsenti(sentifilter, dictsenti)

if __name__ == '__main__':
    main()
