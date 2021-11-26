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
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


class MainWindow(Screen):
    pass

class prequisiteWindow(Screen):
    pass
class sentimentWindow(Screen):
    pass
class requirementWindow(Screen):
    pass
class modelWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("sentinel.kv")

class sentinel(App):
    Window.clearcolor = (240 / 255, 240 / 255, 240 / 255, 1)
    def build(self):
        return kv


if __name__ == "__main__":
    sentinel().run()