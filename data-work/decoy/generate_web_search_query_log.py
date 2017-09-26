#!/usr/bin/python

import uuid
import random
import time 
import sys

def strTimeProp(start, end, format, prop):
  """Get a time at a proportion of a range of two formatted times.

  start and end should be strings specifying times formated in the
  given format (strftime-style), giving an interval [start, end].
  prop specifies how a proportion of the interval to be taken after
  start.  The returned time will be in the specified format.
  """

  stime = time.mktime(time.strptime(start, format))
  etime = time.mktime(time.strptime(end, format))

  ptime = stime + prop * (etime - stime)

  return time.strftime('%d/%m/%Y %I:%M:%S', time.localtime(ptime))

def randomDate(start, end, prop):
  return strTimeProp(start, end, '%d/%m/%Y %I:%M %p', prop)

class userObject:
  def __init__(self,fullname,emailaddr):
    self._guid = str(uuid.uuid4())
    self._name = fullname
    self._email = emailaddr
    # self._username = username
    self._useragent = random.choice(["Opera/8.56.(Windows 95; en-US) Presto/2.9.182 Version/11.00","Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_1 rv:6.0; en-US) AppleWebKit/534.42.4 (KHTML, like Gecko) Version/4.0.3 Safari/534.42.4","Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 4.0; Trident/5.1)"])
    self._ipaddress = "%d.%d.%d.%d" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
    self._starttime = "22/06/2016 19:03:35"
    self.queries = []
  
  def addQuery(self,query):
    self.queries.append(query)

  def writeToCsv(self,f):
    for i in self.queries:
      print ",".join([self._guid,self._name,self._email,"","","","",i,self._ipaddress,str(random.randint(0,65535)),self._ipaddress,randomDate("01/07/2016 1:30 AM", "17/08/2016 5:30 PM",random.random()),self._useragent])
      f.write(",".join([self._guid,self._name,self._email,"","","","",i,self._ipaddress,str(random.randint(0,65535)),self._ipaddress,randomDate("01/07/2016 1:30 AM", "17/08/2016 5:30 PM",random.random()),self._useragent]))
      f.write("\n")

_file = open("out.csv","w")

currentObject = None
while True:
  if currentObject is None:
    x = raw_input(" > ").rstrip()
  else:
    x = raw_input(" [%s] > " % currentObject._guid).rstrip()
  tokens = x.split(" ")
  if tokens[0] == "new" and len(tokens[1:]) == 2 and currentObject is None:
    currentObject = userObject(tokens[1].replace("_"," "),tokens[2])
  elif tokens[0] == "write" and len(tokens) == 1:
    currentObject.writeToCsv(_file)
    currentObject = None
  elif tokens[0] == "add" and len(tokens) > 1 and currentObject is not None:
    currentObject.addQuery(" ".join(tokens[1:]))
  elif tokens[0] == "q" and len(tokens) == 1:
    print "wrapping up..."
    _file.close()
    sys.exit(0)
  else:
    print "nope"
