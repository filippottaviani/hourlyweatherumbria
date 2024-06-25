import tweepy
import weather
import time
import keys  # file non presente su GiHub per ragioni di privacy

# Ciclo orario
while True:
    # Autorizzazione
    client = tweepy.Client(keys.bearer_token, keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_token_secret)
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
