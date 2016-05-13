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
test1 = re.search(r'VESSEL((.|\n)+)TIDES', x).group(0)
#print test1
#test1 = re.search(r'Day\'s Volume(.*?)<br \/><\/div>', html).group()
tuples = re.findall(r'((left=")(.*?)(</text>|"))', test1.replace('<b>', '').replace('</b>', ''))
cnt=0
obj = ''
row=''
delim=0
headers=1
for tuple in tuples:

 if headers==1:
  if cnt == 0:
   DWT = int(tuple[2].strip(' '))
  elif cnt == 1:
   AGENT = int(tuple[2].strip(' ')) 
  elif cnt == 2:
   ETA = int(tuple[2].strip(' '))
  elif cnt == 3:
   FROM = int(tuple[2].strip(' '))
  elif cnt == 4:
   TO = int(tuple[2].strip(' '))
  elif cnt == 5:
   VHF = int(tuple[2].strip(' '))
  elif cnt == 6:
   PILOT = (tuple[2].strip(' '))
   print 'PILOT ' + PILOT
  elif cnt == 7:
   HARBOUR_PV = (tuple[2].strip(' '))
   print 'HARBOUR_PV ' + HARBOUR_PV
  elif cnt == 9:
   HC_OR_PV = tuple[2].strip(' ')
   print 'HC_OR_PV ' + HC_OR_PV
  elif cnt == 11:
   POB = tuple[2].strip(' ')
   print 'POB ' + POB
  elif cnt == 12:
   TUGS = tuple[2].strip(' ') #int
   print 'TUGS ' + TUGS
  elif cnt == 13:
   BPN_DPN = int(tuple[2].strip(' '))
  elif cnt == 14:
   REMARKS = int(tuple[2].strip(' '))
   headers=0
   cnt=0
  cnt=cnt+1

   
 if headers==0:
  if cnt == 0:
   obj = tuple[2].strip(' ')
   cnt=cnt+1
  elif cnt == 1:
   #y=tuple[2].find('  ')+1
   #obj = obj + '|||' + tuple[2][:y]
   obj = obj + '|' + tuple[2].strip(' ')
   cnt=0

  
  
   print obj
   print obj.find('|')
   #print int(obj[:obj.find('|')])
  
   if (delim==0 and int(obj[:obj.find('|')]) < DWT):
    record = re.search(r'\|((.|\n)+)', obj).group(0)
    print record

   
    row = obj
    obj = ''
   else:
    row = row + obj
    obj = ''
   
   #sys.stdout.write('|') 
  #cnt=cnt+1
 # sys.stdout.write(tuple[2])
  #print(tuple[2],end="")
  #,flush=True
 # print tuple[3]
 #str(test1.replace(" ", "")).replace("><", ""))
 #tuples = re.findall(r'(\">|\'>|img\/)(.*?)(<\/|\.gif)', str(test1.replace(" ", "")).replace("><", ""))
 
 
 #<text top="97" left="28" width="329" height="19" font="0"><b>THURSDAY 12th MAY 2016          </b></text>
 


