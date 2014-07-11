import urllib2

url = "http://pooky.local:32400/status/sessions"
try:
	connection = urllib2.urlopen(url)
	print connection.getcode()
	connection.close()
except urllib2.HTTPError, e:
	print e.getcode()
	print e.reason
