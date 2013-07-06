import json
import sys
import csv
import operator

def hw(tweet_file):

  all_hashtags = {}

  for line in tweet_file:
    tweet_dict = json.loads(line)
    if 'entities' in tweet_dict and len(tweet_dict['entities']['hashtags']) > 0:
      hashtags = tweet_dict['entities']['hashtags']
      for hs in hashtags:
        hashtag = hs['text'].encode('utf-8').replace('\n', '')
        if hashtag in all_hashtags:
          all_hashtags[hashtag] += 1
        else:
          all_hashtags[hashtag] = 1
  
  sorted_hashtags = sorted(all_hashtags.iteritems(), key=operator.itemgetter(1))
  sorted_hashtags.reverse()
  for i in range(0, 10):
    print sorted_hashtags[i][0] + ' ' + str(float(sorted_hashtags[i][1]))
      
  
def main():
  tweet_file = open(sys.argv[1])
  hw(tweet_file)

if __name__ == '__main__':
  main()
