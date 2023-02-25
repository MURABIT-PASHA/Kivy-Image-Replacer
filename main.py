# Import necessary Kivy and KivyMD modules
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.toolbar import MDTopAppBar

from circular_button import CircularButton


# Define the main app class that inherits from MDApp
class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = None  # Initialize label attribute to None
        self.counter = 0  # Initialize counter attribute to zero

    # Define the build method that returns the app's UI
    def build(self):
        # Create a FloatLayout to hold the app's UI elements
        layout = BoxLayout(orientation='vertical')

        # Create a top app bar with a title and add it to the layout
        toolbar = MDTopAppBar(title="Kivy App")
        layout.add_widget(toolbar)

        # Create a vertical BoxLayout with a size hint, position hint, and add it to the layout
        box = BoxLayout(orientation='vertical', size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(box)

        # Create a label with a text, font size, position hint, and add it to the BoxLayout
        self.label = Label(text=str(self.counter), font_size=72, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        box.add_widget(self.label)

        # Create a button with a text, size hint, position hint, and bind it to the increment_counter method
        new_button = CircularButton(
            on_pressed=self.increment_counter,
            path='assets/png_buttons/button-add.png',
            size_hint=[None, None],
            width=100,
            height=100,
            background_color=[1, 0, 0, 1],
            elevation=10)
        box.add_widget(new_button)
        # Return the layout to display the UI
        return layout

    # Define a method to increment the counter and update the label text
    def increment_counter(self):
        self.counter += 1
        self.label.text = str(self.counter)


# Create an instance of the MainApp class and run it
if __name__ == "__main__":
    MainApp().run()
