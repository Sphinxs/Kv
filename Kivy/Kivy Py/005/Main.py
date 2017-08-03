
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.label import Label


class Application ( App, object ) :

    def build ( self ) :

        return Label ( text = 'Hello' )


Application ().run ()
