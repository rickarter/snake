import kivy
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '410')
Config.set('graphics', 'height', '410')

from kivy.graphics import (Color, Ellipse, Rectangle, Line)
class SnakeDraw(Widget):
    def __init__(self, **kwargs):
        super(SnakeDraw, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            Rectangle(pos = (250, 100), size = (50, 50))

class SnakeApp(App):
    def build(self):
        self.sd = SnakeDraw()
        self.sd.canvas.ask_update()
        return self.sd

if __name__ == '__main__':
    SnakeApp().run()