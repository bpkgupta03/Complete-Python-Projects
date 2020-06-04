import tweepy

auth=tweepy.OAuthHandler('ooGq5oELtrFPafp5B8NNIR5pA','fEh74nGKdf1kj3b9VuJh0no58snyRZ9qCldBLzcK4QZlCjivXA')
auth.set_access_token('2611347551-zq2BMLETvDEcjJkRNyBo4BvaHYMtfVrl98rHSzB','1BVA80T4G5g2mhSFVlMRXjST0pNJFT342VqKOm5GVV4I2')

api=tweepy.API(auth)
search_string='disha'
no_of_tweets=5

for search in tweepy.Cursor(api.search,search_string).items(no_of_tweets):
	try:
		search.favorite()
		print('I liked the post')

	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break



