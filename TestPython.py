import sys
import logging
import numpy as np
import matplotlib.pyplot as plt
import sum2
import MyRead
import random

#print "Hello, world!"

#line = input("integer: ")
#print("line = ", line)

#logging.basicConfig(level = logging.DEBUG)
#logging.basicConfig(level = logging.INFO)
#logging.basicConfig(level = logging.WARNING)
#logging.basicConfig(level = logging.ERROR)
logging.basicConfig(level = logging.CRITICAL)
test_logger = logging.getLogger(__name__)
''' Practice invoke function from another script'''
'''
sum2.test_invoke('Jaron','Anny')
MyRead.test_read_file()
'''

''' Practice invoke random function'''
'''
x = random.randint(1,100)
print('x = {}'.format(x))   # CTJ170910 Notice the format of print command
'''

''' Practice starred argument'''
MyRead.product(2, 3, 5)


''' Practice logging message'''
test_logger.debug("Display debug message")
test_logger.info("Display log information")
test_logger.warning("Display warning")
test_logger.error("Display error message")
test_logger.critical("Display critical information")

#MyWrite = open('test.txt','w')
#MyWrite.write('No more check')
#MyWrite.write('Replicate your soul')
#MyWrite.close()

#MyFile = open('test.txt','r')
#MyContent = MyFile.read()
#print MyContent
#MyFile.close()
#def readfile(test)

#for line in open('test.txt','r'):
#    print line

#MyFile = open(sys.argv[1],'r')
#MyContent = MyFile.read()
#print MyContent

#import os
#cmd = 'python MyRead.py'
#os.system(cmd)
#print os.getcwd()


# Plot excercise
'''



normal_samples = np.random.normal(size = 10000)
uniform_samples = np.random.uniform(size = 1000000)
plt.hist(normal_samples)
plt.show()
'''

'''

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

text_a = 10
logger.debug('This is a test %d' % (text_a))

logger.warning('What the hell')

logger.info('Check this out')


def my_test(x):
    if x == 0:
        def test_define(y):
            logger.info('Find my_test()')
        print(test_define(1))
        
        return 'My godness'
    else:
        return 'God'

print my_test(0)
print my_test(1)
'''

'''
afa = input('afa =')
beta = input('beta =')
print('afa = %d, beta = %d' % (afa, beta))
'''
