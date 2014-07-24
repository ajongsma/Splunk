#!/usr/bin/env python

__version__ = "0.1"

import datetime
import urllib2

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

SERVER_HOST = 'localhost'
SERVER_PORT = '32400'
SERVER_PLEX_TOKEN = ''

INPUT_HTTP = True								# True/False
DEBUG = False

def check_sessions(server_host, server_port, server_plex_token):
#	#feed = urllib.urlopen("http://pooky.local:32400/status/sessions")
#
#	if not SERVER_TOKEN:
#		urlSessions = urllib2.urlopen("http://%s:%s/status/sessions?X-Plex-Token=%s" % SERVER, SERVER_PORT, SERVER_PLEX_TOKEN)
#	else:
#		urlSessions = urllib2.urlopen("http://%s:%s/status/sessions" % SERVER, SERVER_PORT)

	if INPUT_HTTP == True:
		try:
			urlSessions = urllib2.urlopen("http://%s:%s/status/sessions"  % (SERVER_HOST, SERVER_PORT))
			if DEBUG == True:
				print urlSessions.getcode()
			tree = ET.parse(urlSessions)
			urlSessions.close()
		except urllib2.HTTPError, e:
			if DEBUG == True:
				print "DEBUG", e.getcode()
				print "DEBUG", e.reason
			return
	else:
		tree = ET.ElementTree(file='sessions2.xml')

	root = tree.getroot()
	if DEBUG == True:	
		print "DEBUG root.tag, root.attrib: ", root.tag, root.attrib

	count_ElementsRoot = int(root.attrib.get('size'))
	if DEBUG == True:
		print "count_ElementsRoot:", count_ElementsRoot
	if count_ElementsRoot == 0:
		if DEBUG == True:
			print "DEBUG Mediacontainer has size 0, exiting"
		return

#	print "*" * 60

	counter = 0
	while (counter < count_ElementsRoot):
		if DEBUG == True:
			print "counter:", counter
		for user in root.findall("./Video[" + str(counter) + "]/User"):

			user_title = user.attrib.get("title")
			if DEBUG == True:
				print(user.attrib)	
				print(user.attrib.get("title"))
			
		for player in root.findall("./Video[" + str(counter) + "]/Player"):
			player_platform = player.attrib.get("platform")
			player_product = player.attrib.get("product")
			player_title = player.attrib.get("title")
			player_state = player.attrib.get("state")
			if DEBUG == True:
				print(player.attrib)
				print(player.attrib.get("platform"))
				print(player.attrib.get("product"))
				print(player.attrib.get("title"))
				print(player.attrib.get("state"))

		for video in root.findall("./Video[" + str(counter) + "]"):
			video_type = video.attrib.get("type")
			video_grandparentTitle = video.attrib.get("grandparentTitle")
			video_title = video.attrib.get("title")
			video_season = video.attrib.get("parentIndex")
			video_episode = video.attrib.get("index")
			video_guid = video.attrib.get("guid")
			video_duration = video.attrib.get("duration")
			video_viewOffset = video.attrib.get("viewOffset")
			if DEBUG == True:
				print(video.attrib)
				print(video.attrib.get("type"))			
				print(video.attrib.get("grandparentTitle"))
				print(video.attrib.get("title"))
				print(video.attrib.get("parentIndex"))		# Season;
				print(video.attrib.get("index"))			# Episode
				print(video.attrib.get("guid"))
				print(video.attrib.get("duration"))
				print(video.attrib.get("viewOffset"))
			
		if video_duration and video_viewOffset:
			video_progress = float(video_viewOffset)/float(video_duration)*100
			if DEBUG == True:
				print "video_progress:", video_progress

		for transcodesession in root.findall("./Video[" + str(counter) + "]/TranscodeSession"):
			transcode_throttled = transcodesession.attrib.get("throttled")
			transcode_speed = transcodesession.attrib.get("speed")
			transcode_progress = transcodesession.attrib.get("progress")
			if DEBUG == True:
				print(transcodesession.attrib.get("throttled"))
				print(transcodesession.attrib.get("speed"))
				print(transcodesession.attrib.get("progress"))

		data = ("%s user_title=%s,player_platform=\"%s\",player_product=\"%s\",player_title=\"%s\",player_state=%s,video_grandparentTitle=\"%s\",video_title=\"%s\",video_type=%s,video_season=%s,video_episode=%s,video_guid=%s,video_duration=%s,video_viewOffset=%s,video_progress=%s,transcode_throttled=%s,transcode_speed=%s,transcode_progress=%s" 
				 % (datetime.datetime.now(), user_title, player_platform, player_product, player_title, player_state, video_grandparentTitle, video_title, video_type, video_season, video_episode, video_guid, video_duration, video_viewOffset, video_progress, transcode_throttled, transcode_speed, transcode_progress))
		print data

		counter += 1
#		print "-" * 60

	
if __name__ == '__main__':
    check_sessions(SERVER_HOST, SERVER_PORT, SERVER_PLEX_TOKEN)
