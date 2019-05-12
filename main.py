import tweepy
from textblob import TextBlob

if __name__ == '__main__':

    consumer_key = 'your_consumer_key'
    consumer_key_secret = 'your_secret_consumer_key'

    access_token = 'your_access_token'
    access_token_secret = 'your_secret_token'

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.search('bitcoin')

    for tweet in tweets:
        print(tweet.text)
        sent_analysis = TextBlob(tweet.text)
        print('\n' + str(sent_analysis.sentiment))
        print('=' * 100)
