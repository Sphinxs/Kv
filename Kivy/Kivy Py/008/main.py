
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout


class root ( FloatLayout, object ) :

    pass

class main ( App, object ) :

    def build ( self ) :

        return root ()


main ().run ()
