#from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
class Predict(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
#entry_cars model
     
        self.ent_model=TextInput(
            hint_text='Car',
            size_hint=(0.17,0.12),
            pos_hint={'x':0.8,'y':1.70},
             font_size=15 )
        

        self.add_widget(self.ent_model)

#entry_year
        self.ent_year=TextInput(
           hint_text='year',
           size_hint=(0.17,0.12),
           pos_hint={'x':0.8,'y':1.55},
           font_size=15)
        self.add_widget(self.ent_year)

#entry_Car operation
        self.ent_ope=TextInput(
          hint_text='operation',
          size_hint=(0.17,0.12),
          pos_hint={'x':0.8,'y':1.40}
        )
        self.add_widget(self.ent_ope)

#output label
        self.output_label=Label(text='result will be shown here',size_hint=(0.3,0.1),
                                pos_hint={'x':0.5,'y':1.20},color=(0,0,0,1)
                                )
        self.add_widget(self.output_label)
#
#function for avaluating
    def evaluate(self):
        pass

    

