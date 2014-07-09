#!/usr/bin/env python

__version__ = "0.1"

import datetime
import urllib
import xml.etree.cElementTree as ET

SERVER_HOST = 'pooky.local'
SERVER_PORT = '32400'
SERVER_PLEX_TOKEN = ''

def check_sessions(server_host, server_port, server_plex_token):
	timestamp = datetime.datetime.now()
	
#	#feed = urllib.urlopen("http://pooky.local:32400/status/sessions")
#

#	if SERVER_TOKEN:
#		feed = urllib.urlopen("http://%s:%s/status/sessions?X-Plex-Token=%s" % SERVER, SERVER_PORT, SERVER_PLEX_TOKEN)
#	else:
#		feed = urllib.urlopen("http://%s:%s/status/sessions" % SERVER, SERVER_PORT)

	tree = ET.ElementTree(file='sessions1.xml')

#	tree.getroot()
#	print tree.getroot()

	root = tree.getroot()
	root.tag, root.attrib
#	print root.tag, root.attrib

#	print 1, "-" * 40
#	for child_of_root in root:
#		print child_of_root.tag, child_of_root.attrib

#	print 2, "-" * 40
#	root[0].tag, root[0].text
#	print root[0].tag, root[0].text

#	print 3, "-" * 40
#	for elem in tree.iter():
#		print elem.tag, elem.attrib

#	print "=" * 80
#	print "-" * 40
#	print "Video"
#	print "-" * 40
#	for elem in tree.iter(tag='Video'):
#		print elem.tag, elem.attrib

#	print "-" * 40	
#	print "Media"
#	print "-" * 40
#	for elem in tree.iter(tag='Media'):
#		print elem.tag, elem.attrib

#	print "-" * 40
#	print "Part"
#	print "-" * 40
#	for elem in tree.iter(tag='Part'):
#		print elem.tag, elem.attrib

#	print "-" * 40
#	print "Stream"
#	print "-" * 40
#	for elem in tree.iter(tag='Stream'):
#		print elem.tag, elem.attrib
		
#	print "-" * 40
#	print "User"
#	print "-" * 40
#	for elem in tree.iter(tag='User'):
#		print elem.tag, elem.attrib

#	print "-" * 40
#	print "Player"
#	print "-" * 40
#	for elem in tree.iter(tag='Player'):
#		print elem.tag, elem.attrib

#	print "=" * 80

	for node in tree.iter('User'):
		user_title = node.attrib.get('title')
#		print user_title

	for node in tree.iter('Player'):
		player_platform = node.attrib.get('platform')
		player_product = node.attrib.get('product')
#		if player_platform and player_product:
#			print '  %s :: %s' % (player_platform, player_product)
#		else:
#			print player_platform
			
	for node in tree.iter('Video'):
		video_grandparentTitle = node.attrib.get('grandparentTitle')
		video_title = node.attrib.get('title')
		video_type = node.attrib.get('type')
		video_guid = node.attrib.get('guid')
		video_duration = node.attrib.get('duration')
		video_viewOffset = node.attrib.get('viewOffset')
#		if video_grandparentTitle and video_title:
#			print '  %s :: %s' % (video_grandparentTitle, video_title)
#		else:
#			print video_grandparentTitle
#		if video_type and video_guid:
#			print '  %s :: %s' % (video_type, video_guid)
#		else:
#			print video_grandparentTitle
		if video_duration and video_viewOffset:
			video_progress = float(video_viewOffset)/float(video_duration)*100
#			print '  %s :: %s' % (video_duration, video_viewOffset)
#			print '  progress :', video_progress
#		else:
#			print video_duration
			
	
	event = ("%s user_title=%s, player_platform=%s, player_product=%s, video_grandparentTitle=%s, video_title=%s, video_type=%s, video_guid=%s, video_duration=%s, video_viewOffset=%s, video_progress=%s" 
				 % (timestamp, user_title, player_platform, player_product, video_grandparentTitle, video_title, video_type, video_guid, video_duration, video_viewOffset, video_progress))
				 
	print event
	
if __name__ == '__main__':
    check_sessions(SERVER_HOST, SERVER_PORT, SERVER_PLEX_TOKEN)
