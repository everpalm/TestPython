
import matplotlib.pyplot as plt
import numpy as np
import logging
import csv
import os

''' Trial of Plot'''
'''
x = np.arange(0,360)
y = np.sin(x * np.pi / 180)

x1 = np.arange(0,360,5)
y1 = np.cos(x1 * np.pi /180)

#plt.title("Performance")
plt.subplot(211)
plt.plot(x,y)
plt.subplot(212)
plt.subplots_adjust(left=None,top=None,bottom=None,right=None)
plt.plot(x1,y1)
plt.xlim(-30,390)
plt.ylim(-1.5,1.5)
plt.xlabel("Sector Size")
plt.ylabel("y-axis")

plt.show()
#plt.savefig("filename.png",dpi=300,format="png")

'''

logging.basicConfig(level=logging.DEBUG)

#f=open('test.csv',"r")
##f=open('test.csv',"r",newline="\n")
#reader = csv.reader(f)
#with open('test.csv',"r") as f:
#    reader = csv.reader(f)
with open('test.csv',"r") as f:
    reader = csv.reader(f)
    #reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #data_SR = [0]*12
    data_SR = []
    data_SR512 = []
    data_SR1K = []
    data_SR2K = []
    data_SR4K = []
    data_SR8K = []
    data_SR16K = []
    data_SR32K = []
    data_SR64K = []
    data_SR128K = []
    data_SR256K = []
    data_SR512K = []
    data_SR1M = []

    #phase_count = 1
    for row in reader:
        if row[0] == 'ALL' and row[2] == 'SR_512':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR512.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_1K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR1K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_2K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR2K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_4K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR4K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_8K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR8K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_16K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR16K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_32K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR32K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_64K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR64K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_128K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR128K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_256K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR256K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_512K':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR512K.append(float(row[13]))
        if row[0] == 'ALL' and row[2] == 'SR_1M':
            logging.debug('row[2] = {}, row[13] = {}'.format(row[2],row[13]))
            data_SR.append(row[13])
            data_SR1M.append(float(row[13]))
            '''
            if phase_count == 1:
                plt.subplot(221)
                plt.plot(data_SR)
            if phase_count == 2:
                plt.subplot(222)
                plt.plot(data_SR)
            if phase_count == 3:
                plt.subplot(223)
                plt.plot(data_SR)
            if phase_count == 4:
                plt.subplot(224)
                plt.plot(data_SR)
            data_SR = []
            phase_count+=1
            '''
logging.debug('data_SR512 = {}'.format(data_SR512))
logging.debug('data_SR1K = {}'.format(data_SR1K))
logging.debug('data_SR2K = {}'.format(data_SR2K))
logging.debug('data_SR4K = {}'.format(data_SR4K))
logging.debug('data_SR8K = {}'.format(data_SR8K))
logging.debug('data_SR16K = {}'.format(data_SR16K))
logging.debug('data_SR32K = {}'.format(data_SR32K))
logging.debug('data_SR64K = {}'.format(data_SR64K))
logging.debug('data_SR128K = {}'.format(data_SR128K))
logging.debug('data_SR256K = {}'.format(data_SR256K))
logging.debug('data_SR512K = {}'.format(data_SR512K))
logging.debug('data_SR1M = {}'.format(data_SR1M))
logging.debug('SR512 mean = {}'.format(np.mean(data_SR512)))
logging.debug('SR1K mean = {}'.format(np.mean(data_SR1K)))
logging.debug('SR2K mean = {}'.format(np.mean(data_SR2K)))
logging.debug('SR4K mean = {}'.format(np.mean(data_SR4K)))
logging.debug('SR8K mean = {}'.format(np.mean(data_SR8K)))
logging.debug('SR16K mean = {}'.format(np.mean(data_SR16K)))
logging.debug('SR32K mean = {}'.format(np.mean(data_SR32K)))
logging.debug('SR64K mean = {}'.format(np.mean(data_SR64K)))
logging.debug('SR128K mean = {}'.format(np.mean(data_SR128K)))
logging.debug('SR256K mean = {}'.format(np.mean(data_SR256K)))
logging.debug('SR512K mean = {}'.format(np.mean(data_SR512K)))
logging.debug('SR1M mean = {}'.format(np.mean(data_SR1M)))
mean_SR = []
SR512 = np.mean(data_SR512)
mean_SR.append(SR512)
SR1K = np.mean(data_SR1K)
mean_SR.append(SR1K)
SR2K = np.mean(data_SR2K)
mean_SR.append(SR2K)
SR4K = np.mean(data_SR4K)
mean_SR.append(SR4K)
SR8K = np.mean(data_SR8K)
mean_SR.append(SR8K)
SR16K = np.mean(data_SR16K)
mean_SR.append(SR16K)
SR32K = np.mean(data_SR32K)
mean_SR.append(SR32K)
SR64K = np.mean(data_SR64K)
mean_SR.append(SR64K)
SR128K = np.mean(data_SR128K)
mean_SR.append(SR128K)
SR256K = np.mean(data_SR256K)
mean_SR.append(SR256K)
SR512K = np.mean(data_SR512K)
mean_SR.append(SR512K)
SR1M = np.mean(data_SR1M)
mean_SR.append(SR1M)

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array(mean_SR)
my_xticks = ['512','1K','2K','4K','8K','16K','32K','64K','128K','256K','512K','1M']
plt.xticks(x, my_xticks)

plt.xlabel('Sector Size (Byte)')
plt.ylabel('Trasfer Rate (MBps)')

plt.plot(x,y)
plt.grid()
plt.show()

'''
'''
           
#with open('test_write.csv','a') as fd:
#with open('test_write.csv','a') as fd:
    #writer = csv.writer(fd,delimiter=';',lineterminator='\n')
    #writer = csv.writer(fd)
    #writer.writerows([data_SR])
    #writer.writerows(data_SR)# Will write string to list
    #print(data_SR)
   
#plt.plot(data_SR)
#plt.show()
'''
    if row[0] == 'SR_512':
        print('row[1] = {}'.format(row[1]))
'''  
#logging.DEBUG('row[0] =')
#print('row[0] = {}'.format(row[0]))
#if row[0] == 'WORKER':
#   for column_count in row[0]:
#      print('row[0][{}] = {}'.format(column_count,row[0][column_count]))
        
'''Trial of Try-Except'''
'''
a = 22
b = 33

try:
    if a < b:
        print('n')
        #print(n)
except:
    print('except')
print('after exception...')
'''

