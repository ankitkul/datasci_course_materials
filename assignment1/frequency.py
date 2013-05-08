import sys
import json

def lines(fp):
    return fp.readlines()

def calcfrequency(fp):
    freq = {}
    totalword = 0.0
    for item in lines(fp):
        jsonTw = json.loads(item)
        if "text" in jsonTw:
            tweet = jsonTw["text"]
            sentiScore = 0.0
            for word in tweet.split():
                totalword += 1    
                if word.lower() in freq:
                    freq[word.lower()] = freq[word.lower()] + 1
                else:
                    freq[word.lower()] = 1    
    for key,value in freq.iteritems():
        print "%s %f" % (key.encode("utf-8"), value/totalword)       	

def main():
    tweet_file = open(sys.argv[1])
    calcfrequency(tweet_file)

if __name__ == '__main__':
    main()
