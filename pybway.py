#!/usr/bin/env python3
# file pybway.py
import sys
import os
from PyQt4.QtGui    import *
from PyQt4.QtCore   import *
from PyQt4.QtWebKit import *
class Metro(QWebView):
  
  def __init__(self, parent=None):
    QWebView.__init__(self, parent)
    self.setWindowFlags(Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint)
    if len(QApplication.arguments()) <= 1:
      self.load(QUrl("https://metro-subway.rhcloud.com/MT.php"))
    else:
      self.load(QUrl(QApplication.arguments()[1]))
    self.showFullScreen()
    QObject.connect(self.page().mainFrame(), SIGNAL("javaScriptWindowObjectCleared()"), self.javaScriptWindowObjectCleared)
    defaultSettings = QWebSettings.globalSettings()
    defaultSettings.setAttribute(QWebSettings.JavascriptEnabled, True)
    defaultSettings.setAttribute(QWebSettings.PluginsEnabled, True)
    defaultSettings.setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
    defaultSettings.setAttribute(QWebSettings.LocalStorageDatabaseEnabled, True)
    
  def javaScriptWindowObjectCleared(self):
    hr=self.page().mainFrame().addToJavaScriptWindowObject("MetroView", self)
    print(hr)
    
  @pyqtSlot(str)
  def QtAlert(self, _str):
    QMessageBox.information(self, "QtAlert", _str)
  
  @pyqtSlot(str)
  def System(self, cmd):
    print('system',cmd)
    os.system(cmd)  #use os.system instead
  
  def RunLua(self, _str): pass        #everything about Lua won't be implemented
  def RunLuaString(self, _str): pass
  
  #def keyPressEvent(self, ke): QWebView.keyPressEvent(ke)  #what ru doing?
  
  def Hide(self): hide()   #what ru doing?
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  w = Metro()
  w.show()
  sys.exit(app.exec_())