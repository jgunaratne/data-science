import json
import sys

def hw(sent_file, tweet_file):
  scores = {}
  additional_scores = {}
  for line in sent_file:
    term, score  = line.split("\t")
    scores[term] = int(score)
    
  sentiment_score = float(0)
  for line in tweet_file:
    tweet_dict = json.loads(line)
    if 'text' in tweet_dict:
      line_sentiment = float(0)
      tweet = tweet_dict['text'].encode('utf-8').replace('\n', '')
      tweet_words = tweet.split()
      for word in tweet_words:
        if word in scores:
          line_sentiment += float(scores[word])
        else:
          if word in additional_scores:
            additional_scores[word] += line_sentiment
          else:
            additional_scores[word] = 0
      for word in tweet_words:
        if word in additional_scores:
          additional_scores[word] += line_sentiment
  
  for word in additional_scores:
    print word + ' ' + str(additional_scores[word])

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  hw(sent_file, tweet_file)

if __name__ == '__main__':
  main()
