
import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder


code = '''

BoxLayout:

    Button:
        text: 'Btn 1'

    Button:
        text: 'Btn 2'

'''

# Builder.load_file ( )

class Study ( App ) :

    def build ( self ) :

        return Builder.load_string ( code )


Study ().run ()
