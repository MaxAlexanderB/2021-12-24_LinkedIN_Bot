from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

#------Set Variables-----#
URL = 'https://www.linkedin.com/jobs/search/?f_AL=true&keywords=Python%20Developer&location=Z%C3%BCrich%2C%20Z%C3%BCrich%2C%20Schweiz&geoId=107814425&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
username = os.environ['MAIL']
password = os.environ['PW']

#------Setup Driver------#
chrome_driver_path = r"C:\Users\maxal\PycharmProjects\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

#-------Login------#
login_button = driver.find_element_by_css_selector('.nav__button-secondary')
login_button.click()
time.sleep(1)

user = driver.find_element_by_id("username")
pw = driver.find_element_by_id("password")

user.send_keys(username)
pw.send_keys(password)

login_button = driver.find_element_by_css_selector('.btn__primary--large.from__button--floating')
login_button.click()

time.sleep(1)

try:
    later_button = driver.find_element_by_css_selector('.btn__secondary--large-muted')
    later_button.click()
except NoSuchElementException:
    time.sleep(1)

time.sleep(1)

#-------Logged in locate job list-------#
joblist = driver.find_elements_by_css_selector('.jobs-search-results__list-item.occludable-update.p0.relative.ember-view')
print(len(joblist))
print(joblist)

#-------Save jobs------#
for job in joblist:
    job.click()
    time.sleep(1)
    save_button = driver.find_element_by_css_selector('.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary')
    save_button.click()
    time.sleep(1)

driver.quit()