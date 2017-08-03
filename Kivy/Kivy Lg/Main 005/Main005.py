
import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button


def clickself ( val) :

    print ( '\nSelf\n' )

Button.clickself = clickself


class Tela ( BoxLayout ) :

    def clickroot ( self ) :

        print ( '\nRoot\n' )

class Study ( App ) :

    def clickapp ( self ) :

        print ( '\nApp\n' )

Apl = Study ()

Apl.run ()
