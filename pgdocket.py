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

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()