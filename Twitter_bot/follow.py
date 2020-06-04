import tweepy

auth=tweepy.OAuthHandler('ooGq5oELtrFPafp5B8NNIR5pA','fEh74nGKdf1kj3b9VuJh0no58snyRZ9qCldBLzcK4QZlCjivXA')
auth.set_access_token('2611347551-zq2BMLETvDEcjJkRNyBo4BvaHYMtfVrl98rHSzB','1BVA80T4G5g2mhSFVlMRXjST0pNJFT342VqKOm5GVV4I2')

api=tweepy.API(auth)

#def limit_handler(Cursor):
#	try:
#		while True:
#			yield Cursor.next()
#	except tweepy.RateLimitError :
#		time.sleep(1000)

api.send_direct_message()

for follower in tweepy.Cursor(api.followers).items():
	#print(follower.name)
	if follower.name=='ANURAG R. PACHBHAVE':
		follower.follow()



