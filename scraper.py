import scraperwiki, urllib2
import lxml

u=urllib2.urlopen("http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf")
 
r=lxml.etree.fromstring(x) r.xpath('//page[@number="1"]')
r.xpath('//text[@left="64"]/b')[0:10]
r.xpath('//text[@left="64"]/b')[8].text



