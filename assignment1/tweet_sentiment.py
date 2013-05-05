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

def processTweets(fp, senti):
    for item in lines(fp):
        tweet = json.loads(item)["text"]
        sentiScore = 0
        for word in tweet.split(' '):
            if word.lower() in senti:
                sentiScore += int(senti[word.lower()])     
        print tweet, sentiScore
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    senti = processSenti(sent_file)
    processTweets(tweet_file, senti)

if __name__ == '__main__':
    main()
