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
