# Team 1

_JOUR479K project by Aysha Khan, Michelle Chavez and Connor Brooks._


## The project
We built a scraper for [Prince George’s County Circuit Court’s daily docket](http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx) using Python. The scraper can be [here](https://github.com/JOUR479K/team_1/blob/master/scrape_docket.py), and a sample of the .tsv data it extracts can be seen [here](https://github.com/JOUR479K/team_1/blob/master/data.tsv). We also worked on a [scraper to pull detailed case data](https://github.com/JOUR479K/team_1/blob/master/pgdocket.py) from Maryland's [state case search database](http://casesearch.courts.state.md.us/casesearch/) for each case number listed on the docket, so they can be integrated to become a useful reporting system in a local newsroom.

## Scraping docket data

We used ScraperWiki, like the example we found [from the MinnPost](https://github.com/MinnPost/minnpost-mn-court-dockets), to build the basic scraper. 

Unlike in the BeautifulSoup example we used in class, the data on [this website](http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx) isn’t formatted in an HTML table: it is uploaded as pre-formatted text, with spaces creating the columns rather than &lt;td&gt; tags. So we had to use Python regular expressions to remove all the white space between the “cells” and replace them with a delimiter (we used tabs because there were commas we couldn’t get rid of within the data itself). For that, [we got help on StackOverflow](http://stackoverflow.com/questions/36957908/removing-white-space-from-txt-with-python). This clean tsv data is saved as a separate file. You can see an example of the data it saves [here](https://github.com/JOUR479K/team_1/blob/master/data.tsv).

Ideally, we would also like to implement some kind of an email notification system that also displays this information. For example, if a reporter is interested in updates on a case involving a party named "Smith," it could be helpful for the scraper to loop through the scraped docket data and alert the reporter that the case will be heard today. It would be even better if the reporter could get further details on the case. Speaking of which...

## Scraping case search details
We also used Selenium to scrape Maryland’s [state case search database](http://casesearch.courts.state.md.us/casesearch/), so that we could link its full case details with the names and case numbers scraped from the daily docket. That’s our pie-in-the-sky plan. [Our scraper](https://github.com/JOUR479K/team_1/blob/master/pgdocket.py) gets as far as mimicking a browser user to automatically click through the disclaimer page, selecting PG County through the dropdown, inputting a sample case number, submitting and displaying the results.

Follow up steps would include looping through the docket data for live case numbers and scraping the full case details that displays.