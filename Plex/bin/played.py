import os
import urllib
import xml.etree.ElementTree as ET

def main():
  feed = urllib.urlopen("http://pooky.local:32400/status/sessions")

  try:
    tree = ET.parse(feed)
    print "-" * 40
    print "Download ok"
    print "-" * 40

    root = tree.getroot()
    print "-" * 40
    print "root", root

    print "-" * 40
    for child in root:
      print(child.tag, child.attrib)

    print "-" * 40
    print root.findall(".")

    print "-" * 40
    print root.findall(".//Video[0]")
    eventVideo = root.findall(".//Video[0]")
    for child in eventVideo:
      print(child.tag, child.attrib)

    print "-" * 40
    print root.findall(".//Media[0]")
    eventMedia = root.findall(".//Media[0]")
    for child in eventMedia:
      print(child.tag, child.attrib)

    print "-" * 40
    print root.findall(".//Part[0]")
    eventPart = root.findall(".//Part[0]")
    for child in eventPart:
      print(child.tag, child.attrib)

    print "-" * 40
    print root.findall(".//User[0]")
    eventUser = root.findall(".//User")
    for child in eventUser:
      print(child.tag, child.attrib)

    print "-" * 40
    print root.findall(".//Player[0]")
    eventPlayer = root.findall(".//Player[0]")
    for child in eventPlayer:
      print(child.tag, child.attrib)

    print "-" * 40
    eventVideo = root.find("Video")
    for child in eventVideo:
      print(child.tag, child.attrib)


  except Exception, inst:
    print "Unexpected error opening %s: %s" % (tree, inst)

if __name__ == "__main__":
  main()
