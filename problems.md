We’re struggling between feasibility for us and usefulness for reporters as we figure out which site is best suited for our scraping project. Options we’ve laid out:

- Scrape this [daily docket](http://www.princegeorgescountymd.gov/sites/circuitcourt/sitepages/dailydocket.aspx) every day and email it to a reporter/tweet it out
    - OR it searches every docket for certain names and emails docket to reporter if there's a match 
    - OR it searches the daily docket for certain names every day and, if there's a match, inputs the case # into the [case search](http://casesearch.courts.state.md.us/casesearch/) and sends full case details for that case # to the reporter 
    - OR there's the Baltimore county court uploads [pdf docket](http://www.baltimorecountymd.gov/Agencies/circuit/dailydocket/index.html), which a bot could tweet/email every day 

- Scrape all new cases (that meet a certain requirement) added to this full case [database](http://casesearch.courts.state.md.us/casesearch/)
    - Maybe it searches for certain name every hour and emails reporter the case results 

- Changes to the docket in upcoming cases