import scraperwiki
import re
from lxml import html
import csv

url = "http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx"
doc_text = scraperwiki.scrape(url)
doc = html.fromstring(doc_text)

for row in doc.cssselect("pre"):
	pre_text = row.cssselect("pre").pop()
	docket = pre_text.text
	clean_text = re.sub(r'\s{2,}','|',docket)

with open('data.txt', 'w') as f:
    f.write(clean_text)

# to do:
# add line break after 4 "|" characters or ~76 total characters
# don't print 1st and 2nd line, write new header row