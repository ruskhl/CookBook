from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import webbrowser



#def any_Function(instance):
    #webbrowser.open('http://ruslanak.pythonanywhere.com')



class MainApp(App):
    def build(self):
      self.icon = "icon.png"
      main_layout = webbrowser.open('http://ruslanak.pythonanywhere.com')
      main_layout = BoxLayout(orientation = "vertical")
     

      #btn1 = Button(text='Open Link' , size=(200,50), size_hint=(None, None))
      #btn1.bind(on_press=any_Function)

      #Bind function with button
      #return btn1

      
         
      #return webbrowser.open('http://ruslanak.pythonanywhere.com')
      return main_layout
      


if __name__ == '__main__':
    app =MainApp()
    MainApp().run()


