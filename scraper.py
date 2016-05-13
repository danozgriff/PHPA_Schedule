import scraperwiki, urllib2
import lxml
import re
import sys

u=urllib2.urlopen("http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf")
 
x=scraperwiki.pdftoxml(u.read())
# Get Schedule Date
Schedule_Date = re.search(r'jpg((.|\n)+)</text>', x).group(0)
Schedule_Date = re.search(r'<b>(.*?)</b>', Schedule_Date).group(0).replace('<b>', '').replace('</b>', '').strip(' ')
print Schedule_Date

# Scan PDF
test1 = re.search(r'Duty Helo:((.|\n)+)TIDES', x).group(0)
#print test1
#test1 = re.search(r'Day\'s Volume(.*?)<br \/><\/div>', html).group()
tuples = re.findall(r'((left="|">)(.*?)(</text>|"))', test1.replace('<b>', '').replace('</b>', ''))
cnt=0
obj = ''
row=''
lineout=''
headers=1
colcnt=0
#hdcnt=0
HeadersList = []
for tuple in tuples:

 #print 'Testing: ' + tuple[2]

 if headers==1:
  if cnt == 0:
   #DWT = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'VESSEL: ' + tuple[2].strip(' ')
  if cnt == 2:
   #DWT = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'DWT: ' + tuple[2].strip(' ')
  elif cnt == 4:
   #AGENT = int(tuple[2].strip(' ')) 
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'AGENT: ' + tuple[2].strip(' ')
  elif cnt == 6:
   #ETA = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'ETA: ' + tuple[2].strip(' ')
  elif cnt == 8:
   #FROM = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'FROM: ' + tuple[2].strip(' ')
  elif cnt == 10:
   #TO = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'TO: ' + tuple[2].strip(' ')
  elif cnt == 12:
   #VHF = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'VHF: ' + tuple[2].strip(' ')
  elif cnt == 14:
   #PILOT = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'PILOT: ' + tuple[2].strip(' ')
  elif cnt == 16:
   #HARBOUR_PV = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'HARBOUR_PV: ' + tuple[2].strip(' ')
  elif cnt == 20:
   #HC_OR_PV = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'HC_OR_PV: ' + tuple[2].strip(' ')
  elif cnt == 24:
   #POB = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'POB: ' + tuple[2].strip(' ')
  elif cnt == 26:
   #TUGS = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'TUGS: ' + tuple[2].strip(' ')
  elif cnt == 28:
   #BPN_DPN = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'BPN_DPN: ' + tuple[2].strip(' ')
  elif cnt == 32:
   #REMARKS = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   print 'REMARKS: ' + tuple[2].strip(' ')
   headers=0
   #print 'Headers End: ' + tuple[2].strip(' ')
   #hdcnt=-1
   cnt=-1
  #hdcnt=hdcnt+1

   
 if headers==0 and cnt >= 0:
  #print 'Main End: ' + tuple[2].strip(' ')
  if cnt == 0:
   obj = tuple[2].strip(' ')
   #obj = tuple[2].strip(' ')
   #print 'in: cnt=0'
   #cnt=cnt+1
  elif cnt == 1:
   loc = tuple[2].strip(' ')
   #print 'in: cnt=1'
   #obj = tuple[2].strip(' ') + '|' + obj
   cnt=-1
   #hdcnt=hdcnt+1
   
   ##print 'loc: ' + str(loc) + ' obj: ' + obj
   #print colcnt
   #print HeadersList[colcnt]
   #print loc

   if loc >= HeadersList[colcnt]-5 and loc <= HeadersList[colcnt]+5:
    lineout = lineout + obj + ','
    colcnt=colcnt+1
   else:
    lineout = lineout + ','
    colcnt=colcnt+1
   
   if colcnt > 12:
    print lineout[:-1]
    colcnt = 0

 cnt=cnt+1
  
  
     #if (delim==0 and int(obj[:obj.find('|')]) < DWT):
   # print 'in: delim'
   # record = re.search(r'\|((.|\n)+)', obj).group(0)[1:]
   # print record
   # colcnt=colcnt+1

   
    #row = obj
    #obj = ''
   #else:
    #row = row + obj
    #obj = ''
  
  
   #sys.stdout.write('|') 
  #cnt=cnt+1
 # sys.stdout.write(tuple[2])
  #print(tuple[2],end="")
  #,flush=True
 # print tuple[3]
 #str(test1.replace(" ", "")).replace("><", ""))
 #tuples = re.findall(r'(\">|\'>|img\/)(.*?)(<\/|\.gif)', str(test1.replace(" ", "")).replace("><", ""))
 
 
 #<text top="97" left="28" width="329" height="19" font="0"><b>THURSDAY 12th MAY 2016          </b></text>
 


