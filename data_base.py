import mysql.connector
import sys
class Data_base:
    def __init__(self):
         sys.stdout.reconfigure(encoding='utf-8') 
         self.mys={
               'user':'mahdi',
               'host':'localhost',
               'password':'MahdiAttarzade2002',
               'database':'bama_site',
               'charset':'utf8mb4',
               'collation':'utf8mb4_unicode_ci' }

        # self.corsur=self.mys.cursor()
    
    def create_data_base(self):
      try:
        with mysql.connector.connect(**self.mys)as mys:
           with mys.cursor()as corsur:
              corsur.execute('''
        CREATE TABLE IF NOT EXISTS car_information(
        id INT PRIMARY KEY AUTO_INCREMENT,
        car VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
        year VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
        car_operation VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
        price VARCHAR(100)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci)''')
           mys.commit()
      except mysql.connector.Error as err:
         print(err)
#adding datas into the database
    def add_data_base(self,lis):
       try:
         with mysql.connector.connect(**self.mys)as mys:
            with mys.cursor()as cursor:

              query=('INSERT IGNORE INTO car_information(car,year,car_operation,price)VALUES(%s,%s,%s,%s)')
              value= (lis)
    
              cursor.executemany(query,value)
  
              mys.commit()
         
       except mysql.connector.Error as err:

          print(f'ERROR :{err}')  
    
#reading data base and put it into the table  
    def read_data_base(self):
      try:
        with mysql.connector.connect(**self.mys)as mys:
           with mys.cursor()as cursor:
    
            cursor.execute('SELECT * FROM car_information')
    
            rows=cursor.fetchall()
      
     
        return rows
      except mysql.connector.Error as err:
            print(f'ERROR :{err}')  
     
    
   
      
         

create=Data_base()
create.create_data_base()
