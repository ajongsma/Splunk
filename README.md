Splunk - Sessions
======

Reference
======
http://pymotw.com/2/xml/etree/ElementTree/parse.html


Input
======
````
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1">
<Video addedAt="1399347340" art="/library/metadata/714/art/1400007807" contentRating="TV-14" duration="2581920" grandparentKey="/library/metadata/714" grandparentRatingKey="714" grandparentTheme="/library/metadata/714/theme/1400007807" grandparentThumb="/library/metadata/714/thumb/1400007807" grandparentTitle="The Blacklist" guid="com.plexapp.agents.thetvdb://266189/1/21?lang=en" index="21" key="/library/metadata/1119" librarySectionID="2" originallyAvailableAt="2014-05-05" parentIndex="1" parentKey="/library/metadata/715" parentRatingKey="715" parentThumb="/library/metadata/715/thumb/1396201245" rating="7.6999998092651403" ratingKey="1119" sessionKey="56" summary="Knowing the truth about her father, Liz refuses to work with Red; Red brings the FBI a compelling case; Liz reveals what she knows about Tom&apos;s life." thumb="/library/metadata/1119/thumb/1400089898" title="Berlin" type="episode" updatedAt="1400089898" viewOffset="613495" year="2014">
<Media aspectRatio="1.78" audioChannels="6" audioCodec="ac3" bitrate="5269" container="mkv" duration="2581920" height="1076" id="1164" videoCodec="h264" videoFrameRate="24p" videoResolution="1080" width="1916">
<Part container="mkv" duration="2581920" file="/Users/Andries/Media/Series/The Blacklist/Season 01/The Blacklist S01E21 1080p WEB-DL-SiCKBEARD.mkv" id="1201" key="/library/parts/1201/file.mkv" size="1700396149">
<Stream bitDepth="8" bitrate="4780" cabac="1" chromaSubsampling="4:2:0" codec="h264" codecID="V_MPEG4/ISO/AVC" colorSpace="yuv" duration="2581915" frameRate="23.976" frameRateMode="cfr" hasScalingMatrix="0" height="1076" id="7333" index="0" language="English" languageCode="eng" level="40" profile="high" refFrames="4" scanType="progressive" streamType="1" title="" width="1916" />
<Stream bitDepth="16" bitrate="384" bitrateMode="cbr" channels="6" codec="ac3" codecID="A_AC3" dialogNorm="-27" duration="2581920" id="7334" index="1" language="English" languageCode="eng" samplingRate="48000" selected="1" streamType="2" title="" />
<Stream codecID="S_TEXT/UTF8" default="1" format="srt" id="7335" index="2" language="Nederlands" languageCode="dut" selected="1" streamType="3" title="" />
<Stream codec="srt" format="srt" id="7422" key="/library/streams/7422" language="English" languageCode="eng" streamType="3" />
</Part>
</Media>
<User id="1" thumb="http://www.gravatar.com/avatar/20b92fe4ad37c4af673be4e5d862aa65?d=404" title="a.jongsma" />
<Player machineIdentifier="4c1951ac-c3c4-40e5-8481-851b47e1181b" platform="Plex Home Theater" product="Plex Home Theater" state="paused" title="" />
</Video>
</MediaContainer>
````


Output
======
````
python xml_parser4.py
----------------------------------------
Download ok
----------------------------------------
----------------------------------------
root <Element 'MediaContainer' at 0x106d56610>
----------------------------------------
('Video', {'grandparentTitle': 'The Blacklist', 'grandparentKey': '/library/metadata/714', 'parentThumb': '/library/metadata/715/thumb/1396201245', 'art': '/library/metadata/714/art/1400007807', 'rating': '7.6999998092651403', 'addedAt': '1399347340', 'updatedAt': '1400089898', 'ratingKey': '1119', 'parentIndex': '1', 'key': '/library/metadata/1119', 'year': '2014', 'duration': '2581920', 'originallyAvailableAt': '2014-05-05', 'guid': 'com.plexapp.agents.thetvdb://266189/1/21?lang=en', 'grandparentRatingKey': '714', 'viewOffset': '613495', 'index': '21', 'grandparentThumb': '/library/metadata/714/thumb/1400007807', 'librarySectionID': '2', 'thumb': '/library/metadata/1119/thumb/1400089898', 'title': 'Berlin', 'parentKey': '/library/metadata/715', 'parentRatingKey': '715', 'contentRating': 'TV-14', 'summary': "Knowing the truth about her father, Liz refuses to work with Red; Red brings the FBI a compelling case; Liz reveals what she knows about Tom's life.", 'sessionKey': '56', 'grandparentTheme': '/library/metadata/714/theme/1400007807', 'type': 'episode'})
----------------------------------------
[<Element 'MediaContainer' at 0x106d56610>]
----------------------------------------
[<Element 'Video' at 0x106d56650>]
('Video', {'grandparentTitle': 'The Blacklist', 'grandparentKey': '/library/metadata/714', 'parentThumb': '/library/metadata/715/thumb/1396201245', 'art': '/library/metadata/714/art/1400007807', 'rating': '7.6999998092651403', 'addedAt': '1399347340', 'updatedAt': '1400089898', 'ratingKey': '1119', 'parentIndex': '1', 'key': '/library/metadata/1119', 'year': '2014', 'duration': '2581920', 'originallyAvailableAt': '2014-05-05', 'guid': 'com.plexapp.agents.thetvdb://266189/1/21?lang=en', 'grandparentRatingKey': '714', 'viewOffset': '613495', 'index': '21', 'grandparentThumb': '/library/metadata/714/thumb/1400007807', 'librarySectionID': '2', 'thumb': '/library/metadata/1119/thumb/1400089898', 'title': 'Berlin', 'parentKey': '/library/metadata/715', 'parentRatingKey': '715', 'contentRating': 'TV-14', 'summary': "Knowing the truth about her father, Liz refuses to work with Red; Red brings the FBI a compelling case; Liz reveals what she knows about Tom's life.", 'sessionKey': '56', 'grandparentTheme': '/library/metadata/714/theme/1400007807', 'type': 'episode'})
----------------------------------------
[<Element 'Media' at 0x106d56990>]
('Media', {'videoFrameRate': '24p', 'videoCodec': 'h264', 'container': 'mkv', 'bitrate': '5269', 'height': '1076', 'width': '1916', 'audioChannels': '6', 'duration': '2581920', 'aspectRatio': '1.78', 'videoResolution': '1080', 'id': '1164', 'audioCodec': 'ac3'})
----------------------------------------
[<Element 'Part' at 0x106d56a10>]
('Part', {'container': 'mkv', 'key': '/library/parts/1201/file.mkv', 'file': '/Users/Andries/Media/Series/The Blacklist/Season 01/The Blacklist S01E21 1080p WEB-DL-SiCKBEARD.mkv', 'duration': '2581920', 'id': '1201', 'size': '1700396149'})
----------------------------------------
[<Element 'User' at 0x106d56b50>]
('User', {'thumb': 'http://www.gravatar.com/avatar/20b92fe4ad37c4af673be4e5d862aa65?d=404', 'id': '1', 'title': 'a.jongsma'})
----------------------------------------
[<Element 'Player' at 0x106d56b90>]
('Player', {'platform': 'Plex Home Theater', 'product': 'Plex Home Theater', 'machineIdentifier': '4c1951ac-c3c4-40e5-8481-851b47e1181b', 'state': 'paused', 'title': ''})
----------------------------------------
('Media', {'videoFrameRate': '24p', 'videoCodec': 'h264', 'container': 'mkv', 'bitrate': '5269', 'height': '1076', 'width': '1916', 'audioChannels': '6', 'duration': '2581920', 'aspectRatio': '1.78', 'videoResolution': '1080', 'id': '1164', 'audioCodec': 'ac3'})
('User', {'thumb': 'http://www.gravatar.com/avatar/20b92fe4ad37c4af673be4e5d862aa65?d=404', 'id': '1', 'title': 'a.jongsma'})
('Player', {'platform': 'Plex Home Theater', 'product': 'Plex Home Theater', 'machineIdentifier': '4c1951ac-c3c4-40e5-8481-851b47e1181b', 'state': 'paused', 'title': ''})
````
