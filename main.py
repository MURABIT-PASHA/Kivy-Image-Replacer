# Import necessary Kivy and KivyMD modules
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (350, 580)


# Define the main app class that inherits from MDApp
class MainApp(MDApp):
    floating_action_options = {
        'Camera': 'camera',
        'Gallery': 'image'
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Define the build method that returns the app's UI
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_color = (0.05, 0.07, 0.09, 1)
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        screen_manager.current = "login"

if __name__ == "__main__":
    MainApp().run()
