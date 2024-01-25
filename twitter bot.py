import tweepy
import time

auth = tweepy.OAuthHandler('ceGUMigRu0xklG7IgCaJhuJBp', 'y0J01Az1binWh8QvDjMMTGH7T0ekEzdsRRhIBjlJ1G0xFsW1YA')

auth.set_access_token('AAAAAAAAAAAAAAAAAAAAAFpekAEAAAAANliUriJrNuBCotth2jby3fGiXlE%3DHMMwkgisY', 'Ajbl4pnibp6d7p9kDFSeWFohqf5F46lLv1vaOw2A9')

api = tweepy.API(auth, wait_on_rate_limit=True)
api.create_friendship()
api.retweet()
api.create_favorite()

# handling tweets
tweet_id = '1533805130021224448'
status_obj = api.get_status(tweet_id)
print(status_obj.text())

# Retweeting
api.retweet(tweet_id)

# Liking
api.create_favorite(tweet_id)

# comment / reply
tweet = api.get_status(tweet_id)
my_reply = api.update_status(f"@{tweet.user.screen_name()}your comment ges here", tweet_id)

# following tweet author
# user = api.get_user(tweet.user.screen_name())
api.create_friendship(tweet.user.screen_name())



img_obj = api.media_upload('my_img.png')

my_timeline = api.home_timeline()
user = api.get_user()

print(user.screen_name)

for follower in tweepy.Cursor(api.get_followers).items():
    print(follower.name)

    if follower.name == "Muhammad Mohib":
        follower.follow()

search = 'giveaway'
number_of_tweets = 500


for tweet in tweepy.Cursor(api.search_tweets, search).items(number_of_tweets):
    try:
        print('Tweet Liked')
        tweet.favourite()
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(2)
        tweet

    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
