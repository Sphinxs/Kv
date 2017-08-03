
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout


class Root ( FloatLayout, object ) :

    pass

class Main ( App, object ) :

    def build ( self ) :

        return Root ()


Main ().run ()
