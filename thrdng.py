#!/usr/bin/python
import sys
sys.path.insert(1, "/nfs/2016/o/omartyno/python_pachages")
from threading import Thread
from random import randint
import time

class SuperThread(Thread):
	def __init__(self, val):
		'''Constructor'''

		Thread.__init__(self)
		self.val = val

	def run(self):
		for i in range(1, self.val):
			print ('Value %d in thread %s, selfval - %d' % (i, self.getName(), self.val))
			secondsToSleep = randint(1, 5)
			print ('%s sleeping for %d seconds...' % (self.getName(), secondsToSleep))
			time.sleep(secondsToSleep)

# if __name__=='__main__':
	# ThArray = []
myThOb1 = SuperThread(10)
myThOb1.setName('Thread 1')

myThOb2 = SuperThread(4)
myThOb2.setName('Thread 2')

myThOb1.start()
myThOb2.start()

# myThOb1.join()
# myThOb2.join()
print (myThOb1)
print (myThOb2)
print ('Main bb')
