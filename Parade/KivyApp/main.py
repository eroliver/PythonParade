import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import subprocess


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 4
        # add widgets to window
        self.test_label = Label(text='Kiosk1')
        self.window.add_widget(self.test_label)

        self.button1 = Button(text='Kiosk1')
        self.window.add_widget(self.button1)
        self.system_name = 'mtrmgtkiosk1'
        self.button1.bind(on_press=self.button_callback)

        self.button2 = Button(text='Kiosk2')
        self.window.add_widget(self.button2)
        # the following line calls the print function on startup..NEED to pass a function for .bind to work
        # self.button2.bind(on_press=print('button pressed'))

        self.button3 = Button(text='Kiosk3')
        self.window.add_widget(self.button3)

        return self.window

    # obviously this only works for 1 kiosk and would need to be passed the system name, but that didn't work.
    def button_callback(self, system):
        subprocess.run('ping mtrmgtkiosk1')


if __name__ == "__main__":
    SayHello().run()
