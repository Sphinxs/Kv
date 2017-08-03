
# -*- coding: utf-8 -*-

import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder

from kivy.core.window import Window

'''

application.ids['textinput'] # Dict dos ids / application.ids.text_input

readonly faz com que apenas leitura seja possível

foreground_color altera a cor do texto

tab_width define o espaço horizontal do tab

write_tab = False desativa o tab

padding define a margem

'''

Window.size = ( 350, 500 )

comand = '''

#:import chex kivy.utils.get_color_from_hex

FloatLayout:

    TextInput:
        id: texto
        size_hint: None, None
        width: root.width
        height: root.height
        readonly: False
        font_name: 'Roboto'
        font_size: 20
        foreground_color: chex ( '#a3a3a3' )
        write_tab: False
        padding: 10
'''

class Apl ( App ) :

    def build ( self ) :

        self.title = 'Text Editor'

        return Builder.load_string ( str ( comand ) )


Tx = Apl ()

print ( Apl ().__dict__ )

Tx.run ()
