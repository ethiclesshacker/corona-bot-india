import tweepy
import os
# from dotenv import load_dotenv

# load_dotenv()


def tweet(message, FILENAME):
    auth = tweepy.OAuthHandler(os.environ.get(
        "API_KEY"), os.environ.get("API_KEY_SECRET"))
    auth.set_access_token(
        os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))

    api = tweepy.API(auth)

    # api.update_status("Hello From AVS-DEV bot!")
    api.update_with_media(FILENAME, status=message)
