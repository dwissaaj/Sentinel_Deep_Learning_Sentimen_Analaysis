import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    button_prequisite = ObjectProperty(None)
    button_sentiment = ObjectProperty(None)
    button_requirement = ObjectProperty(None)
    button_summary =  ObjectProperty(None)



class sentinel(App):
    def build(self):
        Window.clearcolor = (240/255,240/255,240/255,1)
        return MyGrid()


if __name__ == "__main__":
    sentinel().run()