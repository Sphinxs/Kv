
import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class Tela ( BoxLayout ) :

    def click ( self ) :

        self.ids.lb1.text = 'Clicado 1'

        self.ids.lb2.text = 'Clicado 2'

class Study ( App ) :

    pass


Apl = Study ()

Apl.run ()
