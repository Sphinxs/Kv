
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.textinput import TextInput


def build () :

    return TextInput ( text = 'Texto : ', write_tab = False )


Root = App ()

Root.build = build

Root.run ()
