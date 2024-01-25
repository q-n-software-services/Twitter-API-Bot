import tweepy
import time
import webbrowser
callback_uri = 'oob'
auth = tweepy.OAuthHandler('82sYf9hQSpGNuc9K8wTVGOqz0', '6tf3Iu3eiaLesTA2yxZPD2Ht7cJxs4Nk8vxBH0ltAPD3enaNGK', callback_uri)

redirect_url = auth.get_authorization_url()
print(redirect_url)
# redirect_url = 'https://api.twitter.com/oauth/authorize?oauth_token=Ne4cmgAAAAAAjsBpAAABceMWVdk'
webbrowser.open(redirect_url)
user_pint_input = input("What is the pin value? ")
auth.get_access_token(user_pint_input)

