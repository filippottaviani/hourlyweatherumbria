import tweepy
import weather
import time

# Chiavi di accesso
bearer_token = ("AAAAAAAAAAAAAAAAAAAAAOi6uQEAAAAAp609wcEUv1tp7bDqx76mRZn4ZY8"
                "%3DECSC9xwwPtz086trG4HFaqJWzfgYL0I8rhOgRiyc1DXuGsvq4C")
consumer_key = "S0z7reQoU1HzlY96rK4i7j1cN"
consumer_secret = "UJdpwZERtDGklmnEd9FiW7wbaJDjfETyF9tLhnfKrbrNMRKkCN"
access_token = "1804183367123943424-6CChzbcrEeC5SRi1hATvkDFLZIQxQr"
access_token_secret = "Mk7gkTxANcn9eWvkFeoZlCPSV4uyJiQn68idXO4eh1kXj"

# Ciclo orario
while True:
    # Autorizzazione
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Test della connessione con Twitter
    try:
        api.verify_credentials()
        print("Autenticazione riuscita")
    except Exception as e:
        print(f"Errore durante l'autenticazione: {e}")

    tweet = weather.current_weather(weather.terni) + weather.current_weather(weather.perugia) + weather.current_weather(weather.foligno) + weather.current_weather(
        weather.orvieto) + weather.current_weather(weather.citta_di_castello) + weather.current_weather(weather.norcia)

    # Scrittura del post
    try:
        orario = time.strftime("%H:%M")
        client.create_tweet(text=tweet)
        print(f"Tweet pubblicato correttamente alle {orario}!")

    except tweepy.TweepyException as e:
        print(f"Errore durante la pubblicazione del tweet: {e}")

    time.sleep(3600)
