import os
import tweepy

def send_tweet(tweet_text, image_path):
    """
    Esta función envía un tweet con una imagen a través de la API de Twitter.
    """
    consumer_key = os.environ.get("TW_CONSUMER_KEY")
    consumer_secret = os.environ.get("TW_CONSUMER_SECRET")
    access_token = os.environ.get("TW_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TW_ACCESS_TOKEN_SECRET")
    bearer_token = os.environ.get("TW_BEARER_TOKEN")

    # V1 Twitter API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    client = tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

    # Upload image and get media ID
    media_id = api.media_upload(filename=image_path).media_id_string
    
    # Send tweet with media
    client.create_tweet(text=tweet_text, media_ids=[media_id])