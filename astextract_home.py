"""Retrieve the tasks in Astrid matching the selected filters."""

__author__ = 'Knut Funkel <knut.funkel@gmail.com>'
__copyright__ = 'Copyright (c) 2012.'
__license__ = 'Apache License, Version 2.0'

import android
import sys
import astover


"""'Personal'"""

def ast_extract(droid, filter):
 
  if (filter == ""):
    filter = 'Home'

  print 'Extract relevant data from Astrid backup xml.'
  
  if (filter == "ste"):
    result = astover.fetch_tasks(filter, False)
  else:
    result = astover.fetch_tasks(filter, True)

  """droid.notify('Astrid tasks extracted ', result)"""
  droid.setClipboard(result)
"""  droid.makeToast(result)"""


if __name__ == '__main__':
  filter = ''
  droid = android.Android()
  print 'Number of arguments:', len(sys.argv), 'arguments.'
  print 'Argument List:', str(sys.argv)
  droid.makeToast(str(sys.argv))
  ast_extract(droid, filter)
