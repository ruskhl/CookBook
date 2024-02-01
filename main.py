import webbrowser

from kivy.app import App

class MainApp(App):
    def build(self):
        webbrowser.open_new_tab('http://ruslanak.pythonanywhere.com/')



if __name__ == '__main__':
    app =MainApp()
    app.run()
