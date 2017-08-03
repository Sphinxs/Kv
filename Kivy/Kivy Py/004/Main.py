
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.button import Button

from kivy.core.window import Window

from kivy.uix.textinput import TextInput

from kivy.uix.floatlayout import FloatLayout


def click () :

    print ( '\n\nHey\n\n')

def build () :

    ly = FloatLayout ()


    et = TextInput ( text = '\n\tText : ', size_hint = ( None, None ), height = 200, width = 500 )

    # global et - Errado

    et.y = 220; et.x = 200

    ly.add_widget ( et )


    bt = Button ( text = '\nPress : ', size_hint = ( None, None ), width = 200, height = 50, font_size = 20 )

    bt.y = 100; bt.x = 340

    bt.on_press = click

    ly.add_widget ( bt )

    return ly


Root = App ()

Window.size = ( 900, 500 )

Root.title = 'Hello Kivy'

Root.build = build

Root.run ()
