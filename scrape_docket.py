import scraperwiki
import re
from lxml import html
from sys import argv #for mail
import os #for mail

script, case = argv #for mail

url = "http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx"
doc_text = scraperwiki.scrape(url)
doc = html.fromstring(doc_text)

for row in doc.cssselect("pre"):
	pre_text = row.cssselect("pre").pop()
	docket = pre_text.text
	no_head = docket.replace(docket[:229], '')
	#this should cut off the header
	clean = re.sub(r"(\S)\ {2,}(\S)(\n?)", r"\1\t\2\3", no_head)
	# this replaces white space with tab delimeter and adds line break

with open('data.tsv', 'w') as f:
	f.write(clean)

filename = 'data.tsv'
f = open(filename, 'r')
if 'BROWN' in f.read().upper():
	
	SENDMAIL = "/usr/sbin/sendmail" # sendmail location

	FROM = "ayshabkhan@gmail.com"
	TO = ["aysha@umd.edu"]

	SUBJECT = "Update in PG case!"

	TEXT = "Looks like a case involving BROWN at the Prince George's County Court will be taking place soon. Check it out: http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx"

	# Prepare actual message

	message = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

	# Send the mail	

	p = os.popen('%s -t -i' % SENDMAIL, 'w')
	p.write(message)
	status = p.close()
	if status:
		print "Sendmail exit status", status