import tweepy
from tweepy import tweet

# Informazioni
page_id = "1804289235765129217HWUmbria"

# Chiavi di accesso
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOi6uQEAAAAApUlU13T4OyVbdcguI9JHcTCCbxo%3DAO5QqkSaUzu0tgcQNsUEDjwVAfjqjaXjnSVuhyme296Zx0Ubab"
consumer_key = "R6zRD4UqROmbVYgdbdJUV1cCJ"
consumer_secret = "MPHRQLLHj05PTVSDSapynXiqHzW6z8spzn5sM1yg9BwQSVFCd5"
access_token = "1804183367123943424-kk8ssD8vpSamt1nTjrr3ybE6EU8ZyY"
access_token_secret = "0gGxqufetz5DCiySXKrA6OU4l601ZJxP0PZtuJnK4n3Ec"

# client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token,access_token_secret)

# Autorizzazione
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# Nuovo post
try:
    #response = client.create_tweet(text="Post di prova")
    api.update_status("Post di prova")
    print("Tweet pubblicato correttamente!")
except tweepy.TweepyException as e:
  print(f"Errore durante la pubblicazione del tweet: {e}")
