import fbconsole
import tweepy

def update(social, filetype, filename):
	File = open(filename,'r')
	content = File.read()
	File.close()

	if 'facebook' in social:
		fbconsole.AUTH_SCOPE=['publish_stream','publish_checkins']
        fbconsole.authenticate()
        if filetype=='image':
        	fbconsole.post('/me/photos', {'source':open(filename)})
        else:
        	fbconsole.post('/me/feed',{'message':content})
	
	if 'twitter' in social:
		CONSUMER_KEY = 'yZhLq6yet3ff2GpfYJpzYw'
		CONSUMER_SECRET = 'oGdqctzEbTJZSv6jwLp0pxEsXuhKZobmU0MKEGyKA'
		ACCESS_KEY = '229359792-tCaMBJtr6arMk83En9oNSwOkm0gavxBopW2s1U5W'
		ACCESS_SECRET = 'nv6M9A9Mnu2NxFiZ8O9GxQd7VP7N8xLr9JhhRg88k'

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		api = tweepy.API(auth)
		tweet = content
		api.update_status(content)

	if 'gmail' in social:
		print 'Now connecting to google accounts'
	
	if 'youtube' in social:
		print 'Now grabbing metadata from youtube'