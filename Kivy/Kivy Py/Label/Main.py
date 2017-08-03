
# -*- coding: utf-8 -*-

# import kivy

# kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder

from kivy.core.window import Window

from kivy.utils import get_color_from_hex as chex


Window.clearcolor = chex ( '#e1e1e1' )

comand = """

#:import chex kivy.utils.get_color_from_hex

StackLayout:

    orientation: 'bt-lr'

    padding: 50

    Button:
        text: 'Btn'
        # bold: True
        font_size: 50
        italic: True
        color: chex ( '#56c76e' )
        disabled: True
        # espaço entre as linhas - life_height: 3
        # define o máximo de linhas - max_line: 2

"""


class Mid ( App ) :

    def build ( self ) :

        return Builder.load_string ( comand )


Wind = Mid ()

Wind.run ()
