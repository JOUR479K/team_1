from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://casesearch.courts.state.md.us/casesearch/")
checkbox = driver.find_element_by_name('disclaimer').click()
button = driver.find_element_by_name('action')
button.click()

el = driver.find_element_by_name('locationCode')
opt = [option for option in el.find_elements_by_tag_name('option') if option.text == "Prince George's County Circuit Court"][0]
opt.click()
driver.find_element_by_name("caseId").send_keys("CT151304X") # that string is a placeholder ID
# for version 2.0: loop through case IDs (column 1) from data file scraped from docket (data.tsv)
driver.find_elements_by_name('action')[2].click()