# -*- coding: utf-8 -*-

import kivy

kivy.require ( kivy.__version__ )

from kivy.app import App

from kivy.lang import Builder

from kivy.core.window import Window


Window.size = ( 350, 450 )

comand = '''

#:import chex kivy.utils.get_color_from_hex

PageLayout:

	Button:
		markup: True
		text: '[i]Test 1[/i]'
		color: chex ( '#222222')
		font_fize: 20
		background_normal: ''
		background_color: chex ( '#e1e1e1')
		on_press: self.font_size = 25
		on_release: self.font_size = 20
		background_down: 'images/button_down.png'

	Button:
		markup: True
		font_name: 'Roboto-Italic'
		text: '[b]Test 2[/b]'
		font_size: 20
		color: chex ( '#e1e1e1' )
		background_normal: ''
		background_color: chex ( '#222222' )
		background_down: 'images/button_down.png'
		on_press: self.font_size = 15
		on_release: self.font_size = 20

'''

class Apl ( App ) :

	def build ( self ) :

		self.title = 'Test'

		return Builder.load_string ( comand )


Apl ().run ()
