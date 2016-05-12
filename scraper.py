import scraperwiki, urllib2
import lxml
import re
import sys

u=urllib2.urlopen("http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf")
 
x=scraperwiki.pdftoxml(u.read())
test1 = re.search(r'jpg((.|\n)+)TIDES', x).group(0)
#print test1
#test1 = re.search(r'Day\'s Volume(.*?)<br \/><\/div>', html).group()
tuples = re.findall(r'((left="|width="|">)(.*?)(</text>|"))', test1.replace('<b>', '').replace('</b>', ''))
cnt=0
obj = ''
row=''
delim=0
for tuple in tuples:
 if cnt == 0:
  obj = obj + '|' + tuple[2].strip(' ')
 elif cnt == 1:
  obj = obj + '||' + tuple[2].strip(' ')
 else:
  obj = obj + '|||' + tuple[2][:tuple[2].find('  ')]
  
  cnt=-1
  
  if delim==0 and obj[:3] == '|27':
   record = re.search(r'\|\|\|((.|\n)+)', obj).group(0)
   print record
   #print row
   
   row = obj
   obj = ''
  else:
   row = row + obj
   obj = ''
  
  #sys.stdout.write('|') 
 cnt=cnt+1
# sys.stdout.write(tuple[2])
 #print(tuple[2],end="")
 #,flush=True
# print tuple[3]
#str(test1.replace(" ", "")).replace("><", ""))
#tuples = re.findall(r'(\">|\'>|img\/)(.*?)(<\/|\.gif)', str(test1.replace(" ", "")).replace("><", ""))


#<text top="97" left="28" width="329" height="19" font="0"><b>THURSDAY 12th MAY 2016          </b></text>



