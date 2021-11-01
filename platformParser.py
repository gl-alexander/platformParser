import tweepy
import matplotlib.pyplot as plt

consumer_key = 'vtTMbUE6zexuXV1EZKHfbcHSF'
consumer_secret = 'nuL2mTakgCpxiFs40TLLJqgWiLvPpmXknQCkJrDekk5ew0Et8a'
access_token = '2883012641-EfiNeBj1YuUBdvdCUCkAumhS9znUUMCMYc1ktIt'
access_token_secret = 'tINpA939jcTh37XKsSrGyfFRfRFKQRSJK2vkE9O6OjCG4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('Twitter handle: ')
person_id = input()

if person_id.count('@') > 0:
    person_id.replace('@', '')

others = []
ios = []
android = []
web = []

print("Loading tweets. Please wait... ")
for tweet in tweepy.Cursor(api.user_timeline,id=person_id).items():
    try:
        #print("Posted from: " + tweet.source + '\n-Date: ' + str(tweet.created_at))
        if "Android" in tweet.source:
            android.append(tweet)
        elif "iPhone" in tweet.source:
            ios.append(tweet)
        elif "Web" in tweet.source:
            web.append(tweet)
        else:
            others.append(tweet.source)
    except Exception:
        pass


print("\nParsed all tweets from @" + person_id)
print("On iPhone: " + str(len(ios)))
print("On Android: " + str(len(android)))
print("On Web: " + str(len(web)))
print ("Others: " + str(len(others)) )
for u in list(set(others)):
    print("-- " + u)
