"""Retrieve the tasks in Astrid matching the selected filters."""

__author__ = 'Knut Funkel <knut.funkel@google.com>'
__copyright__ = 'Copyright (c) 2012'
__license__ = 'Apache License, Version 2.0'


import os
import string
import urllib
import urllib2
from xml.dom import minidom

taskdir='/mnt/sdcard/astrid/' # path to your log directory

taskfiles = sorted([ f for f in os.listdir(taskdir) if f.startswith('auto')])

print "Most recent file = %s" % (taskfiles[-1],)


file_URL = taskdir+taskfiles[-1]
"""file_URL = '/mnt/sdcard/sl4a/scripts/auto.121022-1910.xml'"""
"""file_URL = 'auto.121022-1910.xml'"""

def extract_value(dom, filter, returnString):
  metaitem = dom.getElementsByTagName('metadata')
  """replace returnString with array containing more information"""
  
  for t in metaitem :
    if t.attributes['value'].value == filter:
      try:
        print dom.attributes['title'].value
        returnString += dom.attributes['title'].value
        returnString += ' '
        returnString += dom.attributes['dueDate'].value
        returnString += '\n'
      except ValueError:
        print "Oops!  That was no ascii string. remoteId: " + dom.attributes['remoteId'].value
        returnString += 'remoteId= '
        returnString += dom.attributes['remoteId'].value
        returnString += '\n'

  return returnString


def fetch_tasks(filter):
  
  returnString = file_URL + '\n'
  xmldoc = minidom.parse(file_URL)
  itemlist = xmldoc.getElementsByTagName('task') 
  print len(itemlist)

  for s in itemlist :
     
    if s.attributes['completed'].value == '0':
      returnString = extract_value (s, filter, returnString)

  xmldoc.unlink()

  return returnString


