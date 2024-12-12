import mysql.connector
import sys
class Data_base:
    def __init__(self):
         sys.stdout.reconfigure(encoding='utf-8') 
         self.mys=mysql.connector.connect(
               user='mahdi',
               host='localhost',
               password='MahdiAttarzade2002',
               database='bama_site',
               charset='utf8mb4',
              collation='utf8mb4_unicode_ci' )

         self.corsur=self.mys.cursor()
    
    def create_data_base(self):
      self.corsur.execute('''
      CREATE TABLE IF NOT EXISTS car_information(
      id INT PRIMARY KEY AUTO_INCREMENT,
      car VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
      year VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
      car_operation VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
      price VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci)''')
      self.mys.commit()
      self.mys.close()
#adding datas into the database
    def add_data_base(self,lis):
       try:
         item=('INSERT IGNORE INTO car_information(car,year,car_operation,price)VALUES(%s,%s,%s,%s)')
         value= (lis)
         self.corsur.executemany(item,value)
  
         self.mys.commit()
         
       except mysql.connector.Error as err:

          print(f'ERROR :{err}')  
       finally:
         self.mys.close()  
#reading data base and put it into the table  
    def read_data_base(self):
    
      self.corsur.execute('SELECT * FROM car_information')
    
      rows=self.corsur.fetchall()
      self.mys.close()
     
      return rows
    
   
      
         

create=Data_base()
create.create_data_base()
