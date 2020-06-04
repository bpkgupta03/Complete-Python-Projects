import tweepy

auth=tweepy.OAuthHandler('ooGq5oELtrFPafp5B8NNIR5pA','fEh74nGKdf1kj3b9VuJh0no58snyRZ9qCldBLzcK4QZlCjivXA')
auth.set_access_token('2611347551-zq2BMLETvDEcjJkRNyBo4BvaHYMtfVrl98rHSzB','1BVA80T4G5g2mhSFVlMRXjST0pNJFT342VqKOm5GVV4I2')

api=tweepy.API(auth)

user=api.me()
#print(user.screen_name)
#print(user.followers_count)

for friend in user.friends():
	#print(f'{friend.screen_name} have {friend.followers_count} followers')
	pass

for tweet in Cursor(api.home_timeline()).pages():
	process_page(tweet)


