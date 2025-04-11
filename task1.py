from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.parse import urljoin
import csv
url="https://books.toscrape.com/"
driver=webdriver.Chrome()
current_url=url
with open("data.csv",'w')as file:
    writer=csv.writer(file)
    writer.writerow(['Title','Price','Availabity','Link'])
    while(True):
        driver.get(current_url)
        time.sleep(3)
        for detail in driver.find_elements(By.CLASS_NAME,"product_pod"):
            try:
                title=detail.find_element(By.TAG_NAME,'h3').text
            except:
                title='N/A'
            try:
                price=detail.find_element(By.CLASS_NAME,"price_color").text
            except:
                price="N/A"
            try:
                avalable=detail.find_element(By.CSS_SELECTOR,".instock.availability").text
            except:
                avalable='N/A'
            try:
                link=detail.find_element(By.XPATH,"./h3/a").get_attribute('href')

            except:
                link_pr='N/A'
            writer.writerow([title,price,avalable,link])
        try:
            next_page=driver.find_element(By.CLASS_NAME,'next')
            next_link=next_page.find_element(By.TAG_NAME,"a").get_attribute('href')
            current_url=urljoin(current_url,next_link)
        except:
            break
print("Done")