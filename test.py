import urllib
import json

for i in range(1,10):
	url = "http://search.twitter.com/search.json?q=microsoft&page=" + str(i)
	response = urllib.urlopen(url)
	respJson = json.load(response)

	for item in respJson["results"]:
		print item["text"]