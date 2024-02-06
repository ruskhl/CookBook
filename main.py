import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtCore import QUrl

from kivy.app import App

class WebEngineUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        super().__init__(parent)

    def interceptRequest(self, info):
        print(info.requestUrl())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    profile = QWebEngineProfile()
    profile.setRequestInterceptor(WebEngineUrlRequestInterceptor())
    page = QWebEnginePage(profile)
    page.setUrl(QUrl(
        "http://ruslanak.pythonanywhere.com/"))

    view = QWebEngineView()

    view.setPage(page)
    view.resize(1024, 600)

    view.show()

    sys.exit(app.exec_())
