import mysql.connector
import sys
class Data_base:
    def __init__(self):
         sys.stdout.reconfigure(encoding='utf-8') 
         self.mys=mysql.connector.connect(
               user='mahdi',
               host='localhost',
               password='MahdiAttarzade2002',
               database='bama_site')

         self.corsur=self.mys.cursor()
    
    def create_data_base(self):
      self.corsur.execute('''
      CREATE TABLE IF NOT EXISTS car_information(
      id INT PRIMARY KEY AUTO_INCREMENT,
      model TEXT,
      year TEXT,
      car_operation TEXT,
      price TEXT)''')
      self.mys.commit()
      self.mys.close()
#adding datas into the database
    def add_data_base(self,name,year,operation):
       try:
         item=('INSERT IGNORE INTO car_information(car,year,operation)VALUES(%s,%s,%s)')
         value= name,year,operation
         self.corsur.execute(item,value)
         self.mys.commit()
         
       except mysql.connector.Error as err:

          print(f'ERROR :{err}')  
       finally:
         self.mys.close()  
      



      

a=Data_base()
a.create_data_base()
         
        
        

    

        
        
    
    