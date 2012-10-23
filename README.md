astover
=======

Android Astrid task extractor to be used with the Android app Tasker

Prereqs
=======

- Tasker (http://tasker.dinglisch.net)
- Astrid (http://astrid.com)
- SL4A (http://tasker.wikidot.com/sl4a)


Howto
=====

Use in tasks -> Select Action Category -> Scripts -> Run SL4A Scripts

1. Run Run SL4A Scripts -> astextract.py
2. Run Task -> Wait 10 sec (works for me)
3. Run a task to get the values (they are availible in the %Clipboard Contents)
	I use Zoom element Text.
	But this works as well with popups or other elements.


TODO
====

- Add active profiles as inparam to astextract.py
- Support multiple filters
- Support filter on prio (use arrays/hashes?)
- Use script with scene on top of lockscreen
- Python seems to default to Ascii, scripts should use UTF-8 instead to be able to parse all data 
  (script outputs remoteID when it fails to parse task names.)
- general cleanup
