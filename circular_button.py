from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty, NumericProperty

class CircularButton(Button):
    path = StringProperty("")
    size_hint = ListProperty([None, None])
    width = NumericProperty(100)
    height = NumericProperty(100)
    background_color = ListProperty([0, 0, 0, 0])

    def __init__(self, path="", **kwargs):
        super().__init__(**kwargs)
        self.path = path
        self.background_normal = self.path
        self.background_down = self.path
        self.background_color = kwargs.get('background_color', [0, 0, 0, 0])
        self.size_hint = kwargs.get('size_hint', [None, None])
        self.width = kwargs.get('width', 100)
        self.height = kwargs.get('height', 100)

    def on_press(self):
        print("button clicked")
