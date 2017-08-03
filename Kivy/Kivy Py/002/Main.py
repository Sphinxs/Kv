
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.button import Button


def click () :

    print ( 'Clicked' )

def build () :

    btn = Button ( text = 'Click', font_size = 20 )

    btn.on_press = click

    return btn


Root = App ()

Root.build = build

Root.run ()
