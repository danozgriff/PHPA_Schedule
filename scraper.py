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
  elif cnt == 2:
   #AGENT = int(tuple[2].strip(' ')) 
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 4:
   #ETA = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 6:
   #FROM = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 8:
   #TO = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 10:
   #VHF = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 12:
   #PILOT = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 14:
   #HARBOUR_PV = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 18:
   #HC_OR_PV = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 22:
   #POB = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 24:
   #TUGS = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 26:
   #BPN_DPN = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
  elif cnt == 30:
   #REMARKS = int(tuple[2].strip(' '))
   #HeadersList[hdcnt] = int(tuple[2].strip(' '))
   HeadersList.append(int(tuple[2].strip(' ')))
   headers=0
   #hdcnt=-1
   cnt=-1
  #hdcnt=hdcnt+1

   
 if headers==0 and cnt >= 0:
  if cnt == 0:
   loc = tuple[2].strip(' ')
   #obj = tuple[2].strip(' ')
   #print 'in: cnt=0'
   #cnt=cnt+1
  elif cnt == 1:
   obj = tuple[2].strip(' ')
   #print 'in: cnt=1'
   #obj = tuple[2].strip(' ') + '|' + obj
   cnt=-1
   #hdcnt=hdcnt+1
   
   print colcnt
   print HeadersList[colcnt]
   print loc

   if loc >= HeadersList[colcnt]-2 and loc <= HeadersList[colcnt]+2:
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
 


