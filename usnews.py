from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('http://www.google.com')
browser.get("https://www.usnews.com/best-graduate-schools/top-science-schools/earth-sciences-rankings")

universities = []

for i in range(2,270):
  try:
    name = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[' + str(i) + ']/td[1]/span/div/h3/a').get_attribute('innerHTML')
    score = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[' + str(i) + ']/td[2]/span/span').get_attribute('innerHTML')
    print(name,score)
    if (score != 'N/A'):
      universities.append([name, score])
  except:
    print("--- fail at " + str(i))
   
  try:
    btn = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[1]/div[2]/div/div/div[2]/button/div')
    btn.click()
    print("*** Load More Button Clicked!")
  except:
    pass

  time.sleep(0.1)
  browser.execute_script("window.scrollTo(0, window.scrollY + 800)")

print(len(universities))
print(universities)
