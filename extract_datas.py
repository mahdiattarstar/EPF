from bs4 import BeautifulSoup
import requests
from data_base import Data_base
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sys.stdout.reconfigure(encoding='utf-8')

class Extract_data:
    def __init__(self):
            
        self.add_new_data = Data_base()

    def request_site(self):
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        })
        try:
            driver = webdriver.Chrome()
            driver.get('https://bama.ir/car/pride-131')
        
            for _ in range(5):
                driver.execute_script('window.scrollBy(0, 1000);')

            page_source=driver.page_source
            driver.quit()
        except requests.exceptions.HTTPError as e:
            print(e)
            return
        except requests.exceptions.RequestException as e:
            print(e)
            return
        self.findall(page_source)

    def findall(self,page_source):

        self.soup = BeautifulSoup(page_source, 'html.parser')
        findall = self.soup.find_all('a', class_='bama-ad listing')

#creating a list for sorting and collecting datas
        lis_car=[]
        for information in findall:
            name, year, operation, price = self.extract(information)
                                                                   
            lis_car.append((name,year,operation,price))
           
        self.add_new_data.add_data_base(lis_car)
        lis_car.clear()

    def extract(self, information):
#extracing just an specific value
    
        car = information.select_one('span.text> span:nth-child(3)')
        year = information.select_one('div.bama-ad__detail-row > span:first-child')
        operation = information.find('span', class_='dir-ltr')
        price = information.find('div', class_='bama-ad__price-holder')
#getting their texts
        text_car = car.get_text(strip=True) if car else 'Unknown'
        text_year = year.get_text(strip=True) if year else 'Unknown'
        text_operation = operation.get_text(strip=True) if operation else 'Unknown'
        text_price = price.get_text(strip=True) if price else 'Unknown'

        return text_car, text_year, text_operation, text_price
      
        
    
