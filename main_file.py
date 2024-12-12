from kivy.app import App
from predict import Predict
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from extract_datas import Extract_data
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from data_base import Data_base
#making a class for the first page
class Main_page(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
           
#first row on the top
        self.top_layout=FloatLayout(size_hint=(1,0.5),pos_hint={'x':0,'y':0.5})
#the color of above
        with self.top_layout.canvas.before:
           Color(1, 1, 0, 1)  # رنگ زرد
           self.top_re=Rectangle(size=self.top_layout.size, pos=self.top_layout.pos)
        self.top_layout.bind(size=self.update_top_re, pos=self.update_top_re)
    
#for creating size and location
        self.predict=Predict()
        self.top_layout.add_widget(self.predict)
#creating confirm button for prediction
        self.Button_pre=Button(text='confirm',
                         size_hint=(0.2,0.1),
                          pos_hint={'x':0.78,'y':0.20})
        self.Button_pre.bind(on_press=self.predict.evaluate)
        self.top_layout.add_widget(self.Button_pre)

#for creating a button for adding new datas
        self.extract_data=Extract_data()
        self.button_add = Button(
            text='Add new data',
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.40, 'y': 0.05}
        )
        self.button_add.bind(on_press=lambda instance: self.extract_data.request_site())
        self.top_layout.add_widget(self.button_add)
     
#main label
        label=Label(text='MADE BY Korosh',
                  size_hint=(None,None),
                    pos_hint={'x':0.4,'y':0.75} ,font_size=40,color=(0,0,0,1))
#adding to the floatlayout
        self.top_layout.add_widget(label)
#predict_label
        label_pr=Label(text='predict',
            size_hint=(0.5,0.1),
            pos_hint={'x':0.60,'y':0.82},font_size=20,color=(1,0,0,1))
        
        self.top_layout.add_widget(label_pr)
      

 #__________________________________________________________________________________ 
#the frame of bottom and its color          
        self.bottom_layout=FloatLayout(size_hint=(1,0.5),pos_hint={'x':0,'y':0})
        with self.bottom_layout.canvas.before:
            Color(0,0,0,1)
            self.bottom_re=Rectangle(size=self.bottom_layout.size,pos=self.bottom_layout.pos)
        self.bottom_layout.bind(size=self.update_bottom_re,pos=self.update_bottom_re)

#ceating a scroll bar for table
        self.scroll=ScrollView(size_hint=(1,1),pos_hint={'x':0.0,'y':0.01})
        
        self.read_data=Data_base()
        self.table_layout=GridLayout(cols=5,size_hint_y=None) 
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))
        self.scroll.add_widget(self.table_layout)
        self.bottom_layout.add_widget(self.scroll)
        self.header_table()

        self.update_btn=Button(text='Update table',
                         size_hint=(0.2,0.1),
                         pos_hint={'x':0.4,'y':0.50})
        self.update_btn.bind(on_press=lambda instance : self.Update_table())
        
        
        self.top_layout.add_widget(self.update_btn)

#we have to add to the main layout(all the staff)     
        self.add_widget(self.top_layout)   
        self.add_widget(self.bottom_layout)
#setting for top
    def update_top_re(self,indstance,value):

       self.top_re.pos=self.top_layout.pos
       self.top_re.size=self.top_layout.size
#setting for bottom
    def update_bottom_re(self,instance,value):

       self.bottom_re.pos=self.bottom_layout.pos
       self.bottom_re.size=self.bottom_layout.size
   
    def header_table(self):
        headers=['Id','Car','Model','operation','price']
        for header in headers:
            self.header=Label(text=header,bold=True,size_hint_y=None,size_hint_x=0.40)
            self.header.height=20
            self.table_layout.add_widget(self.header)

    def Update_table(self):
        self.table_layout.clear_widgets()
        self.header_table()
        show_datas=self.read_data.read_data_base()
        for row in show_datas:
                for item in row:
                    self.table_layout.add_widget(Label(text=str(item),size_hint_y=None,height=30))
            
        
         
class Myapp(App):
    def build(self):
        return Main_page()
    
    
       
  # Run the app
if __name__ == "__main__":  
    Myapp().run()