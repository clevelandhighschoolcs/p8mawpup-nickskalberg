import urllib2
import threading
import datetime
from decimal import *
from twilio.rest import Client

phonenumber = "+1" + raw_input("Phone number (no spaces or dashes) for text updates (Enter 0 for no text updates): +1")
webinput = raw_input("Website: http://")
url = ("www." + webinput)
print "Connecting to http://" + url + "..."
webUrl = urllib2.urlopen("http://" + webinput)

if str(webUrl.getcode()) == "200":
	print "Connection successful."

def ratefunc():
	rate1 = input("Scraping rate (minimum 3 seconds): ")
	if rate1 < 3:
		ratefunc()
	return rate1

rate2 = '{:.1f}'.format(ratefunc())
rate = float(rate2)
x = 0

def check():

	global x
	threading.Timer(rate, check).start()
	webUrl = urllib2.urlopen("http://" + webinput)
	if x == 0:
		global starttime
		starttime = datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
		global startdata
		startdata = webUrl.read()
		x = 1

	if starttime != datetime.datetime.now().strftime("%m-%d-%Y %I:%M %p"):
		data = webUrl.read()
		if data != startdata:
			print "Change made at " + datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
			if phonenumber != 0:
				account_sid = 'AC45d3f468835bcd8e3014b485c5f9b89c'
				auth_token = '64404754b965933b7bb3c6c0613be052'
				twilio_phone_number = '+14582072973'
				client = Client(account_sid, auth_token)
				client.messages.create(
					body="Change made at " + datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"),
					to=phonenumber,
					from_=twilio_phone_number
				)

check()
