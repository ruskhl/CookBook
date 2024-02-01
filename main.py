import webbrowser

from kivy.app import App

class MainApp(App):
    def build(self):
        webbrowser.open('http://ruslanak.pythonanywhere.com/', new = 0)
        #webbrowser.open_new_tab('http://ruslanak.pythonanywhere.com/')



if __name__ == '__main__':
    app =MainApp()
    app.run()
