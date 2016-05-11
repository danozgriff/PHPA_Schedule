import scraperwiki 
import urllib2, lxml.etree

url = 'http://pilbaraports.com.au/Shipping_Schedule/Current_Shipping_Schedule.pdf'
pdfdata = urllib2.urlopen(url).read() 
xmldata = scraperwiki.pdftoxml(pdfdata) 
root = etree.fromstring(xmldata)

pages = list(root) 
print "There are",len(pages),"pages"

print etree.tostring(root, pretty_print=True)


