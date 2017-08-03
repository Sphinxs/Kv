
# -*- coding: utf-8 -*-

# import kivy

# kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder

from kivy.core.window import Window

from kivy.utils import get_color_from_hex as chex


Window.clearcolor = chex ( '#e1e1e1' )

comand = """

#:import chex kivy.utils.get_color_from_hex

<Green@FloatLayout>:

    size_hint: .2, .1

    text: 'Btn'

    canvas.before:

        Color:
            rgba: chex ( '#3db745' )

        Rectangle:
            pos: self.pos
            size: self.size

FloatLayout:

    Green:
        pos_hint: {'center_x': .5, 'center_y': .5}

"""


class Mid ( App ) :

    def build ( self ) :

        return Builder.load_string ( comand )


Wind = Mid ()

Wind.run ()
