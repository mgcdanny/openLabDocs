import requests as rq
from lxml import etree

resp = rq.get("http://www.zillow.com/webservice/GetComps.htm?zws-id=X1-ZWz1dr5zeew1e3_39zrb&zpid=48749425&count=25")
resp = resp.content
tree = etree.fromstring(resp)
#just so we know it is workin^O
#print(tree.xpath('//zipcode/text()'))

addresses = tree.xpath('//address')

for address in addresses:
    print(address)
    print("step 2")
    print("step 3")

print("this prints after loop")


"""
addresses_len = len(addresses)-1
zestimates = tree.xpath('//zestimate')
zestimates_len = len(zestimates)-1
if addresses_len != zestimates_len: print("Warning: addresses are not equal to zestimates")


for x in :
	streets[x] = addresses[x].xpath('./street/text()')
	zipcodes[x] = addresses[x].xpath('./zipcode/text()')
	cities[x] = addresses[x].xpath('./city/text()')
	states[x] = addresses[x].xpath('./state/text()')
	latitude[x] = addresses[x].xpath('./latitude/text()')
	longitude[x] = addresses[x].xpath('./longitude/text()')
	amounts[x] = zestimates[x].xpath('./amount currency="USD"/text()')
	updates[x] = zestimates[x].xpath('./last-updated/text()')
	percentiles[x] = zestimates[x].xpath('./percentile/text()')
	Range[x] = zestimates[x].xpath('./valuationRange')
	#lowRange[x] = Range[x].xpath("./low currency="USD"/text()")
	#highRange[x] = Range[x].xpath("./high currency="USD"/text()")
"""
