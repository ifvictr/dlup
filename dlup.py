#===BEGIN CONFIG===
#How many threads should be made for the use of dlup?
MAX_THREADS = 10
#How many times should each thread loop?
LOOPS_PER_THREAD = 25
#What do you want to use dlup for? Specify absolute URLs of your targets
TARGETS = []
#===END CONFIG===

import threading
import urllib2

class DownloadThread(threading.Thread):
    def __init__(self, url):
        super(DownloadThread, self).__init__()
        self.url = url
    def run(self):
        print "Started thread: %s, target: %s." % (threading.currentThread().name, self.url)
        for i in range(LOOPS_PER_THREAD):
            try:
                urllib2.urlopen(self.url).read()
                print "Sent request #%d from %s." % (i + 1, threading.currentThread().name)
            except urllib2.URLError as exception:
                print "Ran into a URLError in %s, ending thread..." % threading.currentThread().name
                return False
print """
        _|  _|
    _|_|_|  _|  _|    _|  _|_|_|
  _|    _|  _|  _|    _|  _|    _|
  _|    _|  _|  _|    _|  _|    _|
    _|_|_|  _|    _|_|_|  _|_|_|
                          _|
                          _|

  ~ dlup by Gamecrafter, made for education purposes
"""
print "Found %d target(s)." % len(TARGETS)
threads = []
for target in TARGETS:
    [threads.append(DownloadThread(target)) for i in range(int(MAX_THREADS / len(TARGETS)))]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
print "Everything seems to have been finished, bye..."
