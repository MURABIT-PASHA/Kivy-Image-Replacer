from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

Window.size = (350, 580)


class MainApp(MDApp):
    floating_action_options = {
        'Camera': 'camera',
        'Gallery': 'image'
    }
    items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address = None
        self.founded_devices = None
        self.home_screen = Builder.load_file('home.kv')
        self.splash_screen = Builder.load_file('splash.kv')
        self.screen_manager = ScreenManager()

    # Define the build method that returns the app's UI
    def build(self):
        self.screen_manager.add_widget(self.splash_screen)
        self.screen_manager.add_widget(self.home_screen)
        self.theme_cls.theme_style = "Dark"
        return self.screen_manager

    def on_start(self):
        Clock.schedule_once(self.go_to_home, 3)

    def splash_animation(self, **kwargs):
        if kwargs['logo'] is not None and kwargs['text'] is not None:
            logo_anim = Animation(pos_hint={"center_x": .2, "center_y": .55}, duration=1)
            logo_anim.start(kwargs['logo'])
            text_anim = Animation(opacity=1, duration=3)
            text_anim.start(kwargs['text'])
    def go_to_home(self, *args):
        self.screen_manager.current = self.home_screen.name


if __name__ == "__main__":
    MainApp().run()
