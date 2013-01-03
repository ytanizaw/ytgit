#!/usr/bin/python
#coding:utf-8

import os
import re
import logging
#INPUTFILE='ERA_publist.txt'
#OUTPUTFILE='ERA_hashlist.txt'
#LOGFILE='ERA.log'

INPUTFILE='testin.txt'
OUTPUTFILE='testout3.txt'
LOGFILE='test3.log'

#test

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    filename=LOGFILE)



##  READ INPUTFILE
fi=open(INPUTFILE)
lines=fi.readlines()
fi.close()
TotalLines=len(lines)

##  READ OUTPUTFILE
os.system('touch ' + OUTPUTFILE)
fo=open(OUTPUTFILE)
WrittenLines = len(fo.readlines())
fo.close()

print WrittenLines
print TotalLines
# exit

if WrittenLines == 0:
    logging.info('Start')
    logging.info('TOTAL NUMBER of FILES {0} in {1}'.format(TotalLines,INPUTFILE))    
else:
    logging.warning('File already exists. Skip ' + str(WrittenLines) + ' lines.')






ptn=re.compile('/usr/local/ftp/.*bz2')

CurrentLine = 0
for line in lines:
    CurrentLine += 1
    if CurrentLine <= WrittenLines:continue   ### skip written lines

    m = ptn.search(line)    
    if m:
        ## os.system('md5sum ' + m.group() + ' >> ' + OUTPUTFILE)
        os.system('echo md5sum ' + m.group() + ' >> ' + OUTPUTFILE)
    else:
        logging.error('Line:' + str(CurrentLine) + '   File not found.')
        logging.error(line.strip())
        os.system('echo ERROR at ' + str(line.strip()) + ' >> ' + OUTPUTFILE)

    if CurrentLine == 150: break  ##debug

    if CurrentLine % 100 == 0:    ### checkpoint
        logging.info('{0}/{1} files have been done.'.format(CurrentLine,TotalLines))

    if CurrentLine == TotalLines:    ### EOF
        logging.info('All files have been done.')
        break



