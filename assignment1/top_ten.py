import sys
import json
import operator
from collections import defaultdict

def lines(fp):
    return fp.readlines()

def processHashTags(fp):
    hashtags = defaultdict(int)
    for item in lines(fp):
        jsonTw = json.loads(item)
        if "text" in jsonTw:
            entities = jsonTw["entities"]
            if entities is not None:
                tags = entities["hashtags"]
                for tag in tags:
                    tagtext = tag["text"]
                    hashtags[tagtext] += 1.0

    top10 = sorted(hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]    
    for h,f in top10:
        print "%s %0.1f" % (h, f) 

def main():
    tweet_file = open(sys.argv[1])
    processHashTags(tweet_file)

if __name__ == '__main__':
    main()
