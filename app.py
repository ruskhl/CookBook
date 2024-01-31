#import necessary library
#from tkinter import Button
from kivy.app import App 
import webbrowser
#from kivy.uix.button import Button


def any_Function(instance):
    webbrowser.open('http://ruslanak.pythonanywhere.com')



class TutorialApp(App):
    def build(self):
      self.icon = "icon.png"
     

      #btn1 = Button(text='Open Link' , size=(200,50), size_hint=(None, None))
      #btn1.bind(on_press=any_Function)

      #Bind function with button

      return webbrowser.open('http://ruslanak.pythonanywhere.com')
      


if __name__ == '__main__':
    TutorialApp().run()

