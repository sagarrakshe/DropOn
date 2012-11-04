import fbconsole
import tweepy
import oauth2 as oauth
import oauth2.clients.smtp as smtplib
from Tkinter import *

def get_msg(msgText):
	return msgText.get('1.0',END)

def get_sub(subEntry):
	return subEntry.get()

def get_to(toEntry):
	return toEntry.get()

def sendEmail(filetype, msgText, subEntry, toEntry, content ,gmail):
	
	if filetype=='emailid':
		To = content
		Message = get_msg(msgText)
	else:
		To = get_to(toEntry)
		Message = content
	
	Subject = get_sub(subEntry)
	From='sagarrakshe2@gmail.com'
	Header = 'to: '+ To + '\nfrom: '+From + '\nsubject: ' + Subject + '\n'
	Email = Header+Message
	gmail.destroy()
	print Email

	consumer = oauth.Consumer('anonymous', 'anonymous')
	token = oauth.Token('1/zroTf8DZWnbTYiVyQrUPrzmDeBM4Grx9vNG0GsWLHNw', 'Eako4tFIHY_JkKQsL-51OFnH')
	url = "https://mail.google.com/mail/b/sagarrakshe2@gmail.com/smtp/"
	conn = smtplib.SMTP('smtp.googlemail.com', 587)
	conn.set_debuglevel(True)
	conn.ehlo('test')
	conn.starttls()
	conn.authenticate(url, consumer, token)
	conn.ehlo('test')
	conn.authenticate(url, consumer, token)

	conn.sendmail(From, To, Email)


def update(social, filetype, filename):
	File = open(filename,'r')
	content = File.read()
	File.close()

	if 'facebook' in social:
		print 'facebook'
		'''
		fbconsole.AUTH_SCOPE=['publish_stream','publish_checkins']
        fbconsole.authenticate()
        if filetype=='image':
        	fbconsole.post('/me/photos', {'source':open(filename)})
        else:
        	fbconsole.post('/me/feed',{'message':content})
        	'''
	
	if 'twitter' in social:
		print 'Twitter'
		'''
		CONSUMER_KEY = 'yZhLq6yet3ff2GpfYJpzYw'
		CONSUMER_SECRET = 'oGdqctzEbTJZSv6jwLp0pxEsXuhKZobmU0MKEGyKA'
		ACCESS_KEY = '229359792-tCaMBJtr6arMk83En9oNSwOkm0gavxBopW2s1U5W'
		ACCESS_SECRET = 'nv6M9A9Mnu2NxFiZ8O9GxQd7VP7N8xLr9JhhRg88k'

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		api = tweepy.API(auth)
		tweet = content
		api.update_status(content)
		'''

	if 'gmail' in social:
		global To, From, Subject
		print filetype, "Entered"

		gmail = Tk()
		gmail.title("Gmail")
		#gmail.geometry('300x200+0+0')

		toLabel = Label(gmail, text = 'To: ').pack()
		toEntry = Entry(gmail)
		toEntry.insert(0,content.rstrip('\n'))
		toEntry.pack()

		subLabel = Label(gmail, text ="Subject: ").pack()
		subEntry = Entry(gmail)
		subEntry.insert(0,'')
		subEntry.pack()

		msgLabel = Label(gmail, text ="Message: ").pack()
		msgText = Text(gmail)
		msgText.pack()
		okButton = Button(gmail, text = 'Ok', 
			command = lambda: sendEmail(filetype, msgText, subEntry, toEntry, content, gmail))
		okButton.pack()

		gmail.mainloop()

	if 'youtube' in social:
		print 'Now grabbing metadata from youtube'

