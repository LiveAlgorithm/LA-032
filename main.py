# -*- coding: utf-8 -*-

import lacode
from lacode.app import App
from lacode.uix.label import Label
from lacode.uix.boxlayout import BoxLayout

from lacode.uix.button import Button

lacode.require('1.9.1')

var = 0
def soma_um(instance):
    global var
    var += 1
    instance.text = str(var)    
    
class LATeste(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                padding=[40, 20, 40, 20])
        
        layout.add_widget(Label(text='Olá do Kivy!'))
        btn = Button(text='Pressione-me!', size=(100,50))
        
        btn.bind(on_press=soma_um)
        layout.add_widget(btn)
        return layout 
    
if __name__ == '__main__':
    LATeste().run()