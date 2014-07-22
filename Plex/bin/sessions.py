#!/usr/bin/env python

__version__ = "0.1"

import datetime
import urllib2

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

SERVER_HOST = 'pooky.local'
SERVER_PORT = '32400'
SERVER_PLEX_TOKEN = ''

DEBUG = True

def check_sessions(server_host, server_port, server_plex_token):
#	#feed = urllib.urlopen("http://pooky.local:32400/status/sessions")
#
#	if SERVER_TOKEN:
#		feed = urllib.urlopen("http://%s:%s/status/sessions?X-Plex-Token=%s" % SERVER, SERVER_PORT, SERVER_PLEX_TOKEN)
#	else:
#		feed = urllib.urlopen("http://%s:%s/status/sessions" % SERVER, SERVER_PORT)

#### FILE INPUT
#
#	tree = ET.ElementTree(file='sessions2.xml')
#	print "DEBUG tree.getroot: ", tree.getroot()

#### URL INPUT
	try:
		urlSessions = urllib2.urlopen("http://%s:%s/status/sessions"  % (SERVER_HOST, SERVER_PORT))
#		print urlSessions.getcode()
		tree = ET.parse(urlSessions)
		urlSessions.close()
	except urllib2.HTTPError, e:
#		print "DEBUG", e.getcode()
#		print "DEBUG", e.reason
		return


	root = tree.getroot()
#	print "DEBUG tree.getroot: ", tree.getroot()
#	root.tag, root.attrib
	
#	print "DEBUG root.tag, root.attrib: ", root.tag, root.attrib

	count_ElementsRoot = int(root.attrib.get('size'))
#	print "count_ElementsRoot:", count_ElementsRoot
	if count_ElementsRoot == 0:
#		print "DEBUG Mediacontainer has size 0, exiting"
		return

#	print "*" * 60

	counter = 0
	while (counter < count_ElementsRoot):
#		print "====> counter:", counter
		for user in root.findall("./Video[" + str(counter) + "]/User"):
#			print(user.attrib)
#			print(user.attrib.get("title"))
			user_title = user.attrib.get("title")

		for player in root.findall("./Video[" + str(counter) + "]/Player"):
#			print(player.attrib)
#			print(player.attrib.get("platform"))
			player_platform = player.attrib.get("platform")
#			print(player.attrib.get("product"))
			player_product = player.attrib.get("product")
#			print(player.attrib.get("title"))
			player_title = player.attrib.get("title")
#			print(player.attrib.get("state"))
			player_state = player.attrib.get("state")

		for video in root.findall("./Video[" + str(counter) + "]"):
#			print(media.attrib)
#			print(video.attrib.get("type"))
			video_type = video.attrib.get("type")
#			print(video.attrib.get("grandparentTitle"))
			video_grandparentTitle = video.attrib.get("grandparentTitle")
#			print(video.attrib.get("title"))
			video_title = video.attrib.get("title")
#			print(video.attrib.get("guid"))
			video_guid = video.attrib.get("guid")
#			print(video.attrib.get("duration"))
			video_duration = video.attrib.get("duration")
#			print(video.attrib.get("viewOffset"))
			video_viewOffset = video.attrib.get("viewOffset")

		if video_duration and video_viewOffset:
			video_progress = float(video_viewOffset)/float(video_duration)*100
#			print "video_progress:", video_progress

		data = ("%s user_title=%s,player_platform=\"%s\",player_product=\"%s\",player_title=\"%s\",video_grandparentTitle=\"%s\",video_title=\"%s\",video_type=%s,video_guid=%s,video_duration=%s,video_viewOffset=%s,video_progress=%s" 
				 % (datetime.datetime.now(), user_title, player_platform, player_product, player_title, video_grandparentTitle, video_title, video_type, video_guid, video_duration, video_viewOffset, video_progress))
		print data

		counter += 1
#		print "-" * 60


#	print "*" * 60
		
##	print 1, "-" * 40
##	for child in root:
##		print child.tag
##		
##		child.find( "Video" )
##		for x in child.iter("Video"):
##			print "-> ", x.tag, x.text
##			for node in tree.iter('User'):
##				print "--> ", node.attrib.get('title')
##	print 1, "-" * 40
#		
##	print 1, "-" * 40
##	for child_of_root in root:
##		print child_of_root.tag, child_of_root.attrib
#	
##	print 2, "-" * 40
##	root[0].tag, root[0].text
#	
##	print 3, "-" * 40
##	for elem in tree.iter():
##		print elem.tag, elem.attrib
##	print 3, "-" * 40
#	
##	print "=" * 80
##	print "-" * 40
##	print "Video"
##	print "-" * 40
##	for elem in tree.iter(tag='Video'):
##		print elem.tag, elem.attrib
#
##	print "-" * 40	
##	print "Media"
##	print "-" * 40
##	for elem in tree.iter(tag='Media'):
##		print elem.tag, elem.attrib
#
##	print "-" * 40
##	print "Part"
##	print "-" * 40
##	for elem in tree.iter(tag='Part'):
##		print elem.tag, elem.attrib
#
##	print "-" * 40
##	print "Stream"
##	print "-" * 40
##	for elem in tree.iter(tag='Stream'):
##		print elem.tag, elem.attrib
#		
##	print "-" * 40
##	print "User"
##	print "-" * 40
##	for elem in tree.iter(tag='User'):
##		print elem.tag, elem.attrib
#
##	print "-" * 40
##	print "Player"
##	print "-" * 40
##	for elem in tree.iter(tag='Player'):
##		print elem.tag, elem.attrib
#
##	print "=" * 80

###############################################################
#
#	for node in tree.iter('User'):
#		user_title = node.attrib.get('title')
##		if DEBUG:
##			print "DEBUG user_title		: ", user_title
#
#	for node in tree.iter('Player'):
#		player_platform = node.attrib.get('platform')
#		player_product = node.attrib.get('product')
#		player_title = node.attrib.get('title')
##		if DEBUG:
##			print "DEBUG player_platform		: ", player_platform
##			print "DEBUG player_product 		: ", player_product
##			print "DEBUG player_title		: ", player_title
#			
#	for node in tree.iter('Video'):
#		video_grandparentTitle = node.attrib.get('grandparentTitle')
#		video_title = node.attrib.get('title')
#		video_type = node.attrib.get('type')
#		video_guid = node.attrib.get('guid')
#		video_duration = node.attrib.get('duration')
#		video_viewOffset = node.attrib.get('viewOffset')
##		if DEBUG:
##			print "DEBUG video_grandparentTitle	: ", video_grandparentTitle
##			print "DEBUG video_title		: ", video_title
##			print "DEBUG video_type		: ", video_type
##			print "DEBUG video_guid		: ", video_guid
##			print "DEBUG video_duration		: ", video_duration
##			print "DEBUG video_viewOffset		: ", video_viewOffset
#			
#		if video_duration and video_viewOffset:
#			video_progress = float(video_viewOffset)/float(video_duration)*100
##			if DEBUG:
##				print "DEBUG video_progress		: ", video_progress
#
#
#	data = ("%s user_title=%s,player_platform=\"%s\",player_product=\"%s\",player_title=\"%s\",video_grandparentTitle=\"%s\",video_title=\"%s\",video_type=%s,video_guid=%s,video_duration=%s,video_viewOffset=%s,video_progress=%s" 
#				 % (datetime.datetime.now(), user_title, player_platform, player_product, player_title, video_grandparentTitle, video_title, video_type, video_guid, video_duration, video_viewOffset, video_progress))				 
#	print data
	
if __name__ == '__main__':
    check_sessions(SERVER_HOST, SERVER_PORT, SERVER_PLEX_TOKEN)
