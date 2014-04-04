import requests as rq
from lxml import etree

resp = rq.get("http://www.zillow.com/webservice/GetComps.htm?zws-id=X1-_3csw9&zpid=48749425&count=25")
resp = resp.content
tree = etree.fromstring(resp)

#just so we know it is workin^O
print(tree.xpath('//zipcode/text()'))

