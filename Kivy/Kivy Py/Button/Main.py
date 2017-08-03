
# -*- coding: utf-8 -*-

import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder


'''

Markup define que o texto tem marcação

On press define a ação quando o click
ocorre, on release define quando acaba


btn.bind ( on_press = click, on_release = endclick)

Liga um evento a uma função

'''

comand = '''

Button:
    # size_hint_y: None
    markup: True
    text: "Hey, [b]Clique[/b]"
    font_size: 15
    on_press: self.text = 'Clicando'
    on_release: self.text = 'Clicque Terminado'

'''

class Apl ( App ) :

    def build ( self ) :

        self.title = 'Test'

        return Builder.load_string ( comand )


Apl ().run ()
