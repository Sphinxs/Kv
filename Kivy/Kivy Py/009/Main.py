
# -*- coding: utf-8 -*-

import kivy

kivy.require ( '1.9.1' )

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button


class Sco ( BoxLayout ) :

    def pres ( self ) :

        Wind.root_window.remove_widget ( Wind.root )

        Wind.root_window.add_widget ( Sct () )

    def __init__ ( self, ** kargs ) :

        super ( Sco, self ).__init__( ** kargs )

        self.orientation = 'vertical'

        bton = Button ( text = 'One' )

        bton.on_press = self.pres

        self.add_widget ( bton )

        self.add_widget ( Button ( text = 'Two' ) )

        self.add_widget ( Button ( text = 'Three' ) )

class Sct ( BoxLayout ) :

    def pres ( self ) :

        Wind.root_window.remove_widget ( Wind.root )

        Wind.root_window.add_widget ( Sco () )

    def __init__ ( self, ** kargs ) :

        super ( Sct, self ).__init__ ( ** kargs)

        self.orientation = 'vertical'

        bt = Button ( text = 'Click' )

        bt.on_press = self.pres

        self.add_widget ( bt )

class Apl ( App ) :

    def build ( self ) :

        return Sco ()


Wind = Apl ()

Wind.run ()
