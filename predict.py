from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
class Predict(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#entry_cars model
        self.ent_model=TextInput(
            hint_text='Car',
            size_hint=(0.3,0.1),
            pos_hint={'x':2.3,'y':0.70},
             font_size=15 )
        self.add_widget(self.ent_model) 
#entry_year
        self.ent_year=TextInput(
           hint_text='year',
           size_hint=(0.3,0.1),
           pos_hint={'x':2.3,'y':0.57},
           font_size=15)
        self.add_widget(self.ent_year)

#entry_Car operation
        self.ent_ope=TextInput(
          hint_text='operation',
          size_hint=(0.3,0.1),
          pos_hint={'x':2.3,'y':0.44}
        )
        self.add_widget(self.ent_ope)
#button for confirming
        self.Button_pre=Button(text='confirm',
                         size_hint=(0.3,0.1),
                          pos_hint={'x':2.3,'y':0.30})
        self.Button_pre.bind(on_press=self.evaluate)

                          
        self.add_widget(self.Button_pre)
#output label
        self.output_label=Label(text='result will be shown here',size_hint=(0.3,0.1),
                                pos_hint={'x':1.7,'y':0.30},color=(0,0,0,1)
                                )
        self.add_widget(self.output_label)
#
#function for avaluating
    def evaluate(self):
        pass

    

