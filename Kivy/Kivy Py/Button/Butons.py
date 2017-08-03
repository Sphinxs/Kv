
# -*- coding: utf-8 -*-

import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder

from kivy.core.window import Window


Window.size = ( 350, 500 )

comand = '''

#:import chex kivy.utils.get_color_from_hex

Button:
    markup: True
    text: '[i]Humsn[/i]'
    font_size: 15
    color: chex ( '#222222' )
    background_normal: ''
    background_color: chex ( '#e1e1e1')
    size_hint: .2, .1
    pos_hint: { 'center_x': .5, 'center_y': .5 }
    on_press: app.click ()
    on_release: app.clicked ()

'''

class Apl ( App ) :

    def click ( self ) :

        print ( '\n\nClick - On\n' )

    def clicked ( self ) :

        print ( '\n\nClick - Off\n' )

    def build ( self ) :

        self.title = 'Human'

        return Builder.load_string ( str ( comand ) )


Apl ().run ()
