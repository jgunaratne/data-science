import json
import sys
import csv

def hw(tweet_file):
  
  all_occurrences = 0
  terms = {}

  for line in tweet_file:
    tweet_dict = json.loads(line)
    if 'text' in tweet_dict and 'lang' in tweet_dict and tweet_dict['lang'] == 'en':
      tweet = tweet_dict['text']
      tweet_words = tweet.split()
      for word in tweet_words:
        term = word.encode('utf-8').replace('\n', '')
        if term in terms:
          terms[term] += 1
        else:
          terms[term] = 1
          all_occurrences += 1

  for key, val in terms.items():
    term_occurrences = float(val)/float(all_occurrences)
    print key + ' ' + str(term_occurrences)
  
def main():
  tweet_file = open(sys.argv[1])
  hw(tweet_file)

if __name__ == '__main__':
  main()
