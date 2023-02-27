# Import necessary Kivy and KivyMD modules
from kivy.lang import Builder
from kivymd.app import MDApp

# Define the main app class that inherits from MDApp
class MainApp(MDApp):
    floating_action_options = {
        'Camera': 'camera',
        'Gallery': 'image'
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = None  # Initialize label attribute to None
        self.counter = 0  # Initialize counter attribute to zero

    # Define the build method that returns the app's UI
    def build(self):
        self.theme_cls.theme_style = "Dark"  # or "Light", "normal", "darkest"
        return Builder.load_file('home.kv')

    # Define a method to increment the counter and update the label text
    def increment_counter(self):
        self.counter += 1
        self.label.text = str(self.counter)


# Create an instance of the MainApp class and run it
if __name__ == "__main__":
    MainApp().run()
