import json
import sys
import csv
import re
import operator

def hw(file_name, sent_scores):
  
  loc_coords = {}
  master_state_list = {'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','District':'DC','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Montana':'MT','Nebraska':'NE','Nevada':'NV','Hampshire':'NH','Jersey':'NJ','Mexico':'NM','York':'NY','Carolina':'NC','Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Pennsylvania':'PA','Rhode':'RI','Carolina':'SC','Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'}
  states = {}
  state_count = {}

  for s in master_state_list:
    abbr = master_state_list[s].lower()
    name = s.lower()
    states[name] = abbr
    states[abbr] = name
    state_count[abbr] = 0

  tweet_file = open(file_name)
  
  # use place, geocoordinates or location to determine state
  tweet_file = open(file_name)
  for line in tweet_file:
    tweet_dict = json.loads(line)
    
    if 'text' in tweet_dict and 'lang' in tweet_dict and tweet_dict['lang'] == 'en':
      user = tweet_dict['user']
      tweet = tweet_dict['text'].encode('utf-8').replace('\n', '')
      tweet_sent_score = get_sentiment_score(tweet, sent_scores)
      coord = tweet_dict['coordinates']
      loc = re.sub(r'\s+', ' ',re.sub(r'([^\s\w]|_)+', '', user['location']).strip().lower())
      place = tweet_dict['place']
      
      state = None
      if place:
        state = get_state_from_place(place, states)
      if loc:
        state = get_state_from_tokens(loc.split(), states)

      if state != None and len(state) > 2:
        state = states[state]
        
      if state != None and state !='us':
        if state in state_count:
          state_count[state] += tweet_sent_score
        else:
          state_count[state] = tweet_sent_score
          
  sorted_states = sorted(state_count.iteritems(), key=operator.itemgetter(1))
  sorted_states.reverse()
  for i in range(0, 1):
    print sorted_states[i][0].upper()

def get_state_from_place(place, states):
  state = None
  if place != None and place['country'] == 'United States':
    state = place['full_name'].split(',')[1].strip().lower()
    if state in states and len(state) > 2:
      state = states[state]
    if len(state) > 2:
      return None
  return state
  
def create_sentiment_scores(file_name):
  sent_file = open(file_name)
  scores = {}
  for line in sent_file:
    term, score  = line.split("\t")
    scores[term] = int(score)
  return scores
  
def get_sentiment_score(tweet, scores):
  sentiment_lines = []
  sentiment_score = float(0)
  tweet_sentiment = float(0)
  tweet_words = tweet.split()
  for word in tweet_words:
    if word in scores:
      tweet_sentiment += float(scores[word])
  return tweet_sentiment

def get_state_from_tokens(loc_tokens, states):
  state = None
  for token in loc_tokens:
    if token != 'in' and token != 'me':
      if token in states:
        state = states[token]
      if state != None and len(state) > 2:
        state = states[state]
  return state

def main():
  sent_file = sys.argv[1]
  tweet_file = sys.argv[2]
  sent_scores = create_sentiment_scores(sent_file)
  hw(tweet_file, sent_scores)

if __name__ == '__main__':
  main()
