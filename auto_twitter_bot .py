import tweepy
print("tweepy is working")

api_key = "YOUR_API_KEY"

api_secret = "API_SECECT"

access_token = "API_TOKEN"

access_token_secret= "YOUR_API_TOKEN_SECECT"

# authenticate  to twitter

auth = tweepy.OAuthHandler(api_key, api_secret)

auth.set_access_token(access_token, access_token_secret)

# create an API Object
api= tweepy.API(auth)

api.update_status("hello world! this is my first bot tweet")
