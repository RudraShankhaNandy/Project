import tweepy

# Set your Twitter API credentials
#consumer_key = "zjytp1vtpmI6NaOtu1QKW5DMR"
#consumer_secret = "D1cX4zJnFeTZSLbnprmD6YDoSwO2VBkxVXtV3lG2cwqEiGoJZz"
access_token = "1646884496187457536-mcxyHIWulEhvjLmOcgIS0KtoxX0Mga"
access_token_secret = "AiFl0cFMXyjsE39E3bZHiSMyFAF00j5QZ1MqzW7k15JVd"
client_id= "VWNCNGZYeks4OUpBWTM2WWoxZmw6MTpjaQ"
client_secret = "rpKHuW_aE8rSQy86kXseCTvJnkwdNbcRdKvhf4xAkaLMeqQ1jD"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(client_id, client_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Specify the username of the "Kolkata Traffic Police" profile
username = "KPTrafficDept"

# Scrape accident data from the profile page
try:
    # Get user's tweets (max 200)
    tweets = api.user_timeline(screen_name=username, count=10, tweet_mode="extended")
    
    for tweet in tweets:
        # Check if the tweet contains accident-related information
        if "accident" in tweet.full_text.lower():
            # Access accident-related tweet data
            tweet_text = tweet.full_text
            tweet_date = tweet.created_at
            
            # Process or save the accident data as desired
            print("Accident Tweet:", tweet_text)
            print("Date:", tweet_date)
            print("----------------------")
            
except tweepy.TweepError as e:
    # Handle API errors
    print("Error:", str(e))
