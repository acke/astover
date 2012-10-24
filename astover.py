"""Retrieve the tasks in Astrid matching the selected filters."""

__author__ = 'Knut Funkel <knut.funkel@google.com>'
__copyright__ = 'Copyright (c) 2012'
__license__ = 'Apache License, Version 2.0'


import os
import string
import urllib
import urllib2
from xml.dom import minidom
import time 


taskdir='/mnt/sdcard/astrid/' # path to your log directory

taskfiles = sorted([ f for f in os.listdir(taskdir) if f.startswith('auto')])

print "Most recent file = %s" % (taskfiles[-1],)


file_URL = taskdir+taskfiles[-1]
"""file_URL = '/mnt/sdcard/sl4a/scripts/auto.121022-1910.xml'"""
"""file_URL = 'auto.121022-1910.xml'"""

def get_time(epoch):

  myTime = int(epoch)
  timeseconds = time.gmtime(myTime/1000)
  print time.strftime('%Y-%m-%d %H:%M',  time.gmtime(myTime/1000))
  return time.strftime('%Y-%m-%d %H:%M',  time.gmtime(myTime/1000))


def extract_value(dom, filter, returnString):
  metaitem = dom.getElementsByTagName('metadata')
  """replace returnString with array containing more information"""
  
  for t in metaitem :

    if t.attributes['value'].value == filter and not dom.attributes['dueDate'].value == "0":
      try:
        print dom.attributes['title'].value.encode('utf-8')
        returnString += dom.attributes['title'].value.encode('utf-8')
        returnString += ' '
        returnString += get_time(dom.attributes['dueDate'].value)
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
    notCompleted = s.attributes['completed'].value == '0'
 
    if notCompleted:
      returnString = extract_value (s, filter, returnString)

  xmldoc.unlink()

  get_time(1348121757000)

  return returnString


