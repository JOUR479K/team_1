import scraperwiki
import re
from lxml import html

url = "http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx"
doc_text = scraperwiki.scrape(url)
doc = html.fromstring(doc_text)

for row in doc.cssselect("pre"):
	pre_text = row.cssselect("pre").pop()
	docket = pre_text.text
	no_head = docket.replace(docket[:229], '')
	# cut off the header
	clean = re.sub(r"(\S)\ {2,}(\S)(\n?)", r"\1\t\2\3", no_head)
	# replaces white space with tab delimeter and adds line break

with open('data.tsv', 'w') as f:
	f.write(clean)