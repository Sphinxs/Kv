
# -*- coding: utf-8 -*-

import kivy

kivy.require ( '1.9.1' )

from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class screenone ( BoxLayout ) :

    def on_press_bt ( self ) :

        wind.root_window.remove_widget ( wind.root )

        wind.root_window.add_widget ( screentwo () )

class screentwo ( BoxLayout ) :

    def on_press_bt ( self ) :

        wind.root_window.remove_widget ( wind.root )

        wind.root_window.add_widget ( screenone () )

class main ( App ) :

    def build ( self ) :

        return screenone ()


wind = main ()

wind.run ()
