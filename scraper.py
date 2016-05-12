import scraperwiki, urllib2
import lxml
import re
import sys

u=urllib2.urlopen("http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf")
 
x=scraperwiki.pdftoxml(u.read())
#print x
#r=lxml.etree.fromstring(x)
#r.xpath('//page[@number="1"]')
#r.xpath('//text[@left="64"]/b')[0:10]
#r.xpath('//text[@left="64"]/b')[8].text

#html = response.read()
#print r
#test1 = re.search('pdf2xml(.*?)</page>', x).group()
test1 = re.search(r'jpg((.|\n)+)TIDES', x).group(0)
#print test1
#test1 = re.search(r'Day\'s Volume(.*?)<br \/><\/div>', html).group()
tuples = re.findall(r'((left="|width="|">)(.*?)(</text>|"))', test1.replace('<b>', '').replace('</b>', ''))
cnt=0
obj = ''
row=''
for tuple in tuples:
 if cnt <> 2:
  obj = obj + '|' + tuple[2] + '|'
 else:
  #sys.stdout.write(tuple[2])
  obj = obj + '||' + tuple[2]
  print obj
  cnt=-1
  
  if obj[:4] == '|27|':
   
   
   print row
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



