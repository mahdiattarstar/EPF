#from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from data_base import Data_base
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

class Predict(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
#entry_year
        self.ent_year=TextInput(
           hint_text='year',
           size_hint=(0.17,0.12),
           pos_hint={'x':0.8,'y':1.55},
           font_size=15)
        self.add_widget(self.ent_year)

#entry_Car operation
        self.ent_ope=TextInput(
          hint_text='Mileage',
          size_hint=(0.17,0.12),
          pos_hint={'x':0.8,'y':1.40}
        )
        self.add_widget(self.ent_ope)

#output label
        self.output_label=Label(text='the result will be shown here:',size_hint=(0.3,0.1),
                                pos_hint={'x':0.5,'y':1.20},color=(0,0,0,1)
                                )
        self.add_widget(self.output_label)
        self.read_data=Data_base()
#
#function for avaluating
    def evaluate(self):
      try:
        year_input=int(self.ent_year.text)
        operation_input=float(self.ent_ope.text)
#caliing the data_base fro reading
        read_data=self.read_data.update_data_base()
#creating a data frame with its new column
        df=pd.DataFrame(read_data,columns=['year','Mileage','price'])
#if it is a str it gets 0 and ...(apply gets each values from column and gives it to lammda) 
        df['Mileage']=df['Mileage'].apply(lambda x :0  if 'کارکرده' in x else int(x.replace(',','').replace('km','')))
        df['price']=df['price'].apply(lambda x : 0 if 'توافقی' in x else int(x.replace(',','')))
#i learns from x and y
        x=df[['year','Mileage']]
        y=df['price']
        self.predict(x,y,year_input,operation_input)
      except ValueError :
        self.output_label.text=(f'Wrong values !')
    def predict(self,x,y,year_input,operation_input):
#calling the DecisionTreeClassifier and fit x and y
        clf = DecisionTreeClassifier()
        clf.fit(x, y)
# the users input their own values
        new_data=pd.DataFrame([[year_input,operation_input]],columns=['year','Mileage'])
# and it predicts it
        y_pred = clf.predict(new_data)
        self.output_label.text=' '.join('{:,.0f}'.format(i).replace(',','.') for i in y_pred)
     
        
            


        
             
       


      




        
        
        
            

        

    

