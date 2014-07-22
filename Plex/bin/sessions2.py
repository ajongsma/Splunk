#!/usr/bin/env python

__version__ = "0.1"

import datetime
import urllib

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

SERVER_HOST = 'pooky.local'
SERVER_PORT = '32400'
SERVER_PLEX_TOKEN = ''

DEBUG = True

def check_sessions(server_host, server_port, server_plex_token):
	timestamp = datetime.datetime.now()
	
#	#feed = urllib.urlopen("http://pooky.local:32400/status/sessions")
#
#	if SERVER_TOKEN:
#		feed = urllib.urlopen("http://%s:%s/status/sessions?X-Plex-Token=%s" % SERVER, SERVER_PORT, SERVER_PLEX_TOKEN)
#	else:
#		feed = urllib.urlopen("http://%s:%s/status/sessions" % SERVER, SERVER_PORT)

	tree = ET.ElementTree(file='sessions2.xml')
#	print "DEBUG tree.getroot: ", tree.getroot()

	root = tree.getroot()
#	print "DEBUG tree.getroot: ", tree.getroot()
#	root.tag, root.attrib
	
	count_ElementsRoot = root.attrib.get('size')
	print "DEBUG root.tag, root.attrib: ", root.tag, root.attrib
	
	if count_ElementsRoot == "0":
		print "DEBUG Mediacontainer has size 0, exiting"
		return

	for node in root:
		print "X", node
#		print "node.tag", node.tag
#		for y in node:
#			print "Y :", y

	print "*" * 60
	
#	print root.findall("./Video[0]/User")
	for user in root.findall("./Video[0]/User"):
#		print(user.attrib)
		print(user.attrib.get("title"))
	print "-" * 60
#	print root.findall("./Video[1]/User")
	for user in root.findall("./Video[1]/User"):
#		print(user.attrib)
		print(user.attrib.get("title"))

	print "=" * 60
	
#	print root.findall("./Video[0]/Player")
	for player in root.findall("./Video[0]/Player"):
		print(player.attrib)
		print(player.attrib.get("platform"))
		print(player.attrib.get("product"))
		print(player.attrib.get("title"))
		print(player.attrib.get("state"))
	
	print "-" * 60
	
#	print root.findall("./Video[1]/Player")
	for player in root.findall("./Video[1]/Player"):
		print(player.attrib)
		print(player.attrib.get("platform"))
		print(player.attrib.get("product"))
		print(player.attrib.get("title"))
		print(player.attrib.get("state"))
	
	print "=" * 60
	
	for media in root.findall("./Video[0]"):
#		print(media.attrib)
		print(media.attrib.get("type"))
		print(media.attrib.get("grandparentTitle"))
		print(media.attrib.get("title"))
		print(media.attrib.get("guid"))
		print(media.attrib.get("duration"))
		print(media.attrib.get("viewOffset"))
	
	print "-" * 60
	
	for media in root.findall("./Video[1]"):
#		print(media.attrib)
		print(media.attrib.get("type"))
		print(media.attrib.get("grandparentTitle"))
		print(media.attrib.get("title"))
		print(media.attrib.get("guid"))
		print(media.attrib.get("duration"))
		print(media.attrib.get("viewOffset"))
		
	print "=" * 60	
		
	
	
	
	print "*" * 60



		
	print "Media title	:", root[0].attrib.get('title')
	print "Media Section	:", root[0].attrib.get('librarySectionID')
	print "Media type	:", root[0].attrib.get('type')
	print "Media guid	:", root[0].attrib.get('guid')
	print "-" * 60
	print "Media title	:", root[1].attrib.get('title')
	print "Media Section	:", root[1].attrib.get('librarySectionID')
	print "Media type	:", root[1].attrib.get('type')
	print "Media guid	:", root[1].attrib.get('guid')

	print "-" * 60
	
#	print "[0][0]	:", root[0][0].attrib
#	print "[0][1]	:", root[0][1].attrib
#	print "[0][2]	:", root[0][2].attrib
#	print "[0][3]	:", root[0][3].attrib
#	print "[0][4]	:", root[0][4].attrib
#	print "[0][5]	:", root[0][5].attrib
#	print "[0][6]	:", root[0][6].attrib
#	print "[0][7]	:", root[0][7].attrib
#	print "[0][8]	:", root[0][8].attrib
#	print "[0][9]	:", root[0][9].attrib
#	print "[0][10]	:", root[0][10].attrib
#	print "[0][11]	:", root[0][11].attrib
#	print "[0][12]	:", root[0][12].attrib
#	print "[0][13]	:", root[0][13].attrib
#	print "[0][14]	:", root[0][14].attrib
#	print "[0][15]	:", root[0][15].attrib
#	print "[0][16]	:", root[0][16].attrib
#	print "[0][17]	:", root[0][17].attrib
#	print "[0][18]	:", root[0][18].attrib
#	print "[0][19]	:", root[0][19].attrib
#	print "[0][20]	:", root[0][20].attrib
#	print "[0][21]	:", root[0][21].attrib
#	print "[0][22]	:", root[0][22].attrib
	
	
	
	
	
	

	print "=" * 60
		
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

	for node in tree.iter('User'):
		user_title = node.attrib.get('title')
#		if DEBUG:
#			print "DEBUG user_title		: ", user_title

	for node in tree.iter('Player'):
		player_platform = node.attrib.get('platform')
		player_product = node.attrib.get('product')
		player_title = node.attrib.get('title')
#		if DEBUG:
#			print "DEBUG player_platform		: ", player_platform
#			print "DEBUG player_product 		: ", player_product
#			print "DEBUG player_title		: ", player_title
			
	for node in tree.iter('Video'):
		video_grandparentTitle = node.attrib.get('grandparentTitle')
		video_title = node.attrib.get('title')
		video_type = node.attrib.get('type')
		video_guid = node.attrib.get('guid')
		video_duration = node.attrib.get('duration')
		video_viewOffset = node.attrib.get('viewOffset')
#		if DEBUG:
#			print "DEBUG video_grandparentTitle	: ", video_grandparentTitle
#			print "DEBUG video_title		: ", video_title
#			print "DEBUG video_type		: ", video_type
#			print "DEBUG video_guid		: ", video_guid
#			print "DEBUG video_duration		: ", video_duration
#			print "DEBUG video_viewOffset		: ", video_viewOffset
			
		if video_duration and video_viewOffset:
			video_progress = float(video_viewOffset)/float(video_duration)*100
#			if DEBUG:
#				print "DEBUG video_progress		: ", video_progress


	data = ("%s user_title=%s,player_platform=\"%s\",player_product=\"%s\",player_title=\"%s\",video_grandparentTitle=\"%s\",video_title=\"%s\",video_type=%s,video_guid=%s,video_duration=%s,video_viewOffset=%s,video_progress=%s" 
				 % (timestamp, user_title, player_platform, player_product, player_title, video_grandparentTitle, video_title, video_type, video_guid, video_duration, video_viewOffset, video_progress))
				 
	print data
	
if __name__ == '__main__':
    check_sessions(SERVER_HOST, SERVER_PORT, SERVER_PLEX_TOKEN)
