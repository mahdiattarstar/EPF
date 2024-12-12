from bs4 import BeautifulSoup
import requests
import re
import sys
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
#create a class for button and extracting data from a site
class Extract_data(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
#create a button for adding new data
        self.button_add=Button(text='Add new data',
                                size_hint=(0.5,0.1),
                                pos_hint={'x':0.2,'y':0.1} ,
                                  )
        self.button_add.bind(on_press=self.request_site)
        self.add_widget(self.button_add)
    
#request to the site
    def request_site(self):
      self.request=requests.get('https://bama.ir/car/pride-131')
      self.request=self.request.text
      self.soup=BeautifulSoup(self.request,'html.parser')
      findall=self.soup.find_all('a',class_='bama-ad listing')
      limited_findall=findall[:20]
      for information in limited_findall:
        name,year,operation,price=self.extract(information)
    
    def extract(self,information):
       car=information.find('span',class_='text')
       year=information.find('span',{'data-v-9d0e2d7a':''})
       operation=information.find('span',class_='dir-ltr')
       price=information.find('div',class_='bama-add__price-holder')
       

      
      








        
