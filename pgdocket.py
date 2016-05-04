#from selenium import webdriver

#webdriver.get("webdriver.chrome.driver", "C:\\michellechavez\\Desktop\\chromedriver.exe"); 
#driver = '/Users/michellechavez/Desktop/chromedriver'
#driver.get("http://casesearch.courts.state.md.us/casesearch/");

#driver = '/Users/michellechavez/Desktop/chromedriver'
#browser = webdriver.Chrome(executable_path = path_to_chromedriver)
#url = 'http://casesearch.courts.state.md.us/casesearch/'
#browser.get(url)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://casesearch.courts.state.md.us/casesearch/")
checkbox = driver.find_element_by_name('disclaimer').click()
button = driver.find_element_by_name('action')
button.click()
case_num = driver.find_element_by_name('caseId')
case_num = 5
#case_num.send_keys('5')

#USE FIREFOX!!!!!!!!!!!!!!!!!!!!!!!!!!!

# start looping through names from docket scrape results
#for name in docket_names:
#	last_name.send_keys(name) # whatever last name you have




#driver.close()
