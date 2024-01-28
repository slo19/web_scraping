from selenium import webdriver
from selenium.webdriver.common.by import By

def get_upcoming_events(url):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get(url)

    events = driver.find_elements(by=By.XPATH, value='//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element(by=By.XPATH, value='h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element(by=By.XPATH, value='p/span[@class="event-location"]').text
        event_details['time'] = event.find_element(by=By.XPATH, value='p/time').text
        print(event_details)
    
    driver.close()

get_upcoming_events('https://www.python.org/events/python-events/')
