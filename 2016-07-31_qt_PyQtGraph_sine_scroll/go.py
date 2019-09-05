from PyQt4 import QtGui,QtCore
import sys
import ui_main
import numpy as np
import pylab
import time
import pyqtgraph

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.update)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        #self.X=[]
        #self.Y=[]
        self.index=0
        self.X=np.arange(1)
        self.Y=np.arange(1)

    def update(self):

        self.X= np.append(self.X,self.index+1)
        self.index=self.index+1
        print self.X
        if self.index<20:
            self.Y= np.append(self.Y,0)
        elif self.index>60:
            self.Y= np.append(self.Y,0)
        else:
            self.Y= np.append(self.Y,(self.index+1-20)*(self.index+1-20)*1.00/1000)
        #for x in self.X:
        #    print x
        print self.Y
        
        t1=time.clock()
        points=100 #number of data points
        X=np.arange(points)
        #print np.sin(np.arange(points))
        Y=np.sin(np.arange(points)*3*np.pi+time.time())
        #print np.arange(points)
        #print np.arange(points)/points*3*np.pi+time.time()
        #Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
        #print Y
        C=pyqtgraph.hsvColor(time.time()/5%1,alpha=.5)
        pen=pyqtgraph.mkPen(color=C,width=5)
        self.grPlot.plot(self.X,self.Y,pen=pen,clear=True)
        print("update took %.02f ms"%((time.clock()-t1)*1000))
        time.sleep(0.5)
        if self.chkMore.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")
