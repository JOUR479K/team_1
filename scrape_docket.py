import scraperwiki
#import shlex
import re
from lxml import html
import csv

url = "http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx"
doc_text = scraperwiki.scrape(url)
doc = html.fromstring(doc_text)

for row in doc.cssselect("pre"):
	pre_text = row.cssselect("pre").pop()
	docket_data = pre_text.text
	' '.join(docket_data.split())
	print docket_data

with open('data.txt', 'w') as f:
    f.write(docket_data)

# ','.join(shlex.split(docket_data))