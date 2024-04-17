from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello World! this is my first program in kivy \n Im a SESIANO Student, and I love my teacher')

if __name__ == "__main__":
    MyApp().run()