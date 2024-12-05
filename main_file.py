import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from predict import Predict
from kivy.graphics import Color, Rectangle
#making a class for the first page
class Main_page(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        
#first row on the top
        self.top_layout=BoxLayout(orientation='horizontal',size_hint=(1,0.5))

        with self.top_layout.canvas.before:
           Color(1, 1, 0, 1)  # رنگ زرد
           self.top_re=Rectangle(size=self.top_layout.size, pos=self.top_layout.pos)
        self.top_layout.bind(size=self.update_re, pos=self.update_re)
        
        
#for creating size and location
        self.predict=Predict()

        self.top_layout.add_widget(self.predict)

      
#main label
        self.label=Label(text='Webintellibase',
                  size_hint=(0.4,0.1),
                    pos_hint={'x':0.5,'y':0.85} ,font_size=40,color=(0,0,0,1))
#adding to the floatlayout
        self.top_layout.add_widget(self.label)
#predict_label

        self.label_pr=Label(text='predict',
            size_hint=(0.5,0.1),
            pos_hint={'x':0.55,'y':0.82},font_size=20,color=(1,0,0,1))
        
        self.top_layout.add_widget(self.label_pr)

           
#we have to add to the main layout(all the staff) 
#     
        self.add_widget(self.top_layout)
#creating a tabel on the bottom  
          
        self.bottom_layout=BoxLayout(orientation='horizontal',size_hint=(1,0.5))
        with self.bottom_layout.canvas.before:
            Color(0,0,0,1)
            self.bottom_re=Rectangle(size=self.bottom_layout.size,pos=self.bottom_layout.pos)
        self.bottom_layout.bind(size=self.update_re,pos=self.update_re)

       # self.add_widget(self.bottom_row)

       
        self.add_widget(self.bottom_layout)
        
    def update_re(self,indstance,value):
#setting for top
       self.top_re.pos=self.top_layout.pos
       self.top_re.size=self.top_layout.size
#setting for bottom
       self.bottom_re.pos=self.bottom_layout.pos
       self.bottom_re.size=self.bottom_layout.size

         
class Myapp(App):
    def build(self):
        return Main_page()
    
    
 
    
  # Run the app
if __name__ == "__main__":  
    Myapp().run()