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

def addnewline (returnString)
    
  return returnString += '\n'

def extractDueDate (returnString, dom)
  try:
    returnString += ' '
    returnString += get_time(dom.attributes['dueDate'].value)
  except ValueError:
    print "Oops!  That was no ascii string. remoteId: " + dom.attributes['remoteId'].value
    returnString += 'remoteId= '
    returnString += dom.attributes['remoteId'].value
    returnString += '\n'
   
  return returnString

def extractTitle (returnString, dom)
  try:
    print dom.attributes['title'].value.encode('utf-8')
    returnString += dom.attributes['title'].value.encode('utf-8')
  except ValueError:
    print "Oops!  That was no ascii string. remoteId: " + dom.attributes['remoteId'].value
    returnString += 'remoteId= '
    returnString += dom.attributes['remoteId'].value
    returnString += '\n'
   
  return returnString

def matching_filter_has_date(dom, metaitem, filter, returnString):

  """replace returnString with array containing more information"""

  for t in metaitem :

    if t.attributes['value'].value == filter and not dom.attributes['dueDate'].value == "0":
      returnString = extractTitle (returnString, dom)
      returnString = extractDueDate (returnString, dom)
      returnString = extractTitle (returnString)

  return returnString

def matching_filter(dom, metaitem, filter, returnString):
  """replace returnString with array containing more information"""

  for t in metaitem :

    if t.attributes['value'].value == filter:
      returnString = extractTitle (returnString, dom)
      returnString = extractDueDate (returnString, dom)
      returnString = extractTitle (returnString)

  return returnString

def fetch_tasks(filter, showAll):
  
  returnString = file_URL + '\n'
  xmldoc = minidom.parse(file_URL)
  itemlist = xmldoc.getElementsByTagName('task') 
  print len(itemlist)

  for s in itemlist :
    notCompleted = s.attributes['completed'].value == '0'
    metaitem = s.getElementsByTagName('metadata')
 
    if notCompleted and showAll:
      returnString = matching_filter (s, metaitem, filter, returnString)
    elif notCompleted:
      returnString = matching_filter_has_date (s, metaitem, filter, returnString) 

  xmldoc.unlink()

  return returnString


