#!/usr/bin/env python3
# file pybway.py
import sys
from PyQt4 import QtGui, QtCore, QtWebKit
class Metro(QtWebKit.QWebView):
  
  def __init__(self, parent=None):
    QtWebKit.QWebView.__init__(self, parent)
    self.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint | QtCore.Qt.FramelessWindowHint)
    if len(QtGui.QApplication.arguments()) <= 1:
      self.load(QtCore.QUrl("https://metro-subway.rhcloud.com/MT.php"))
    else:
      self.load(QtCore.QUrl(QtGui.QApplication.arguments()[1]))
    self.showFullScreen()
    self.connect(self.page().mainFrame(), QtCore.SIGNAL("javaScriptWindowObjectCleared()"), self.javaScriptWindowObjectCleared)
  
  def javaScriptWindowObjectCleared(self):
    self.page().mainFrame().addToJavaScriptWindowObject("MetroView", self)
    
  def QtAlert(self, _str):
    QtGui.QMessageBox.information(self, "QtAlert", _str)
    
  def System(self, cmd): os.system(cmd)  #use os.system instead
  
  def RunLua(self, _str): pass        #everything about Lua won't be implemented
  def RunLuaString(self, _str): pass
  
  #def keyPressEvent(self, ke): QWebView.keyPressEvent(ke)  #what ru doing?
  
  def Hide(self): hide()   #what ru doing?
  
if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  w = Metro()
  w.show()
  sys.exit(app.exec_())