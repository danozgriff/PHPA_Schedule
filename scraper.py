import scraperwiki, urllib2
import lxml

u=urllib2.urlopen("http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf")
 
x=scraperwiki.pdftoxml(u.read())
print x
#r=lxml.etree.fromstring(x)
#r.xpath('//page[@number="1"]')
#r.xpath('//text[@left="64"]/b')[0:10]
#r.xpath('//text[@left="64"]/b')[8].text

#html = response.read()
#test1 = re.search(r'Day\'s Volume(.*?)<br \/><\/div>', html).group()
#tuples = re.findall(r'((\">|\'>)(.*?)<\/))', str(test1.replace(" ", "")).replace("><", ""))
#tuples = re.findall(r'(\">|\'>|img\/)(.*?)(<\/|\.gif)', str(test1.replace(" ", "")).replace("><", ""))



