
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.label import Label


def build () :

    return Label ( text = 'Hey', italic = True, font_size = 30 )


Root = App ()

Root.build = build

Root.run ()
