# -*- encoding: utf-8 -*-

__all__ = ('TextInputIME', )


from kivy.uix.textinput import TextInput
from kivy.base import EventLoop

from kivy.properties import StringProperty

class TextInputIME(TextInput):
    testtext = StringProperty()


    def __init__(self, **kwargs):
        super(TextInputIME, self).__init__(**kwargs)
        EventLoop.window.bind(on_textedit = self._on_textedit)

    def _on_textedit(self, window, text):
        #print(text)
        self.testtext = text
  
        
#    def on_textedit(self, text):
#        print(text)
#        print(self.testtext)
#        self.testtext = text
#       
#        return self.testtext
        
if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.lang import Builder

    class TextInputIMEApp(App):

        def build(self):

            Builder.load_string('''
<TextInput>
    on_text:
        self.suggestion_text = ''
        self.suggestion_text = 'ion_text'

''')
            root = BoxLayout(orientation='vertical')
            textinput = TextInputIME(multiline=True, use_bubble=True,
                                  use_handles=True)
            # textinput.text = __doc__
            root.add_widget(textinput)
            textinput2 = TextInputIME(multiline=False, text='monoline textinput',
                                   size_hint=(1, None), height=30)
            root.add_widget(textinput2)
            textinput3 = TextInputIME(multiline=True, use_bubble=True,
                                  use_handles=True)
            return root

    TextInputIMEApp().run()
