#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from TextInputIME import TextInputIME

resource_add_path('./fonts')
#use Japanese font
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') 

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.text =  self.ids["text_box"].text

    
class ImeTestApp(App):
    def __init__(self, **kwargs):
        super(ImeTestApp, self).__init__(**kwargs)
        
    def build(self):
        return TextWidget()

if __name__ == '__main__':

   ImeTestApp().run()
