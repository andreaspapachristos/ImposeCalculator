# -*- coding: utf-8 -*-
'''''
Copyright 2021 Andreas Papachristos

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt



class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        canvas = QtGui.QPixmap(MainWindow.frameGeometry().width(), MainWindow.frameGeometry().height())
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        #self.drawrect([200, 285], [4, 2])
       # MainWindow.resize(size[0], size[1])
       # self.page = page
        #self.paper = paper
        #self.landscape = landscape
        #self.drawrect([page[0], page[1]], [paper[0], paper[1]])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheme"))
        self.label.setText(_translate("MainWindow", ""))

    def __init__(self, MainWindow, size, page, paper, monofyllo):
        self.statusbar = None
        self.label = None
        self.verticalLayout = None
        self.centralwidget = None   
        self.MainWindow = None   #Python 3.12 for some reason requires initialization, but works fine in python 3.11
        MainWindow.resize(size[0], size[1])
        self.page = page
        self.paper = paper
        self.monofyllo = monofyllo
        self.setup(MainWindow)
        self.drawrect(MainWindow, [page[0], page[1]], [paper[0], paper[1], paper[2]], monofyllo)

    def spreads(self, monofyllo):
        if monofyllo:
            return 1
        else:
            return 2

    def drawrect(self, MainWindow, page, paper, monofyllo):

        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        painter.drawText(int((MainWindow.geometry().width())/2), 10, str(MainWindow.geometry().width()))
        painter.rotate(90)
        painter.drawText(int((MainWindow.geometry().height())/2), 0, str(MainWindow.geometry().height()))
        painter.rotate(-90)
       # painter.drawText(10, int( (MainWindow.geometry().height())/2),  str(MainWindow.geometry().height()))    
        #z =
        #
        if paper[2] == 0:
            x = page[0]
            y = page[1]
            hgap = (MainWindow.geometry().width() - x * paper[0] * self.spreads(monofyllo)) // ((paper[0] * self.spreads(monofyllo)) + 1)
            vgap = (MainWindow.geometry().height() - y * paper[1]) // (paper[1] + 1)


        else:
            x = page[1]
            y = page[0]
            hgap= (MainWindow.geometry().width() - x * paper[0])//((paper[0] ) + 1)
            vgap = (MainWindow.geometry().height() - y * paper[1]*self.spreads(monofyllo)) // (paper[1]* self.spreads(monofyllo) + 1)

        n = hgap
        if monofyllo:
            for p in range(0, paper[0]):
                z = vgap

                for m in range(0, paper[1]):
                    painter.drawRect(int(n), int(z), int(x), int(y))
                    z += vgap + y
                n += hgap + x
        else:
            if paper[2] == 0:


                for p in range(0, paper[0] * 2):
                   # vgap = (MainWindow.geometry().height() - page[1] * paper[1]) // (paper[0] + 1)
                    z = vgap

                    # print(page[1] * paper[1])
                    for m in range(0, paper[1]):
                       # painter.drawRect(int(hgap), int(vgap), int(page[0]), int(page[1]))
                       painter.drawRect(int(n), int(z), int(x), int(y))

                        #vgap += vgap + page[1]
                       z += vgap + y
                    if (p + 1) % 2 == 0:
                    # hgap += (MainWindow.geometry().width() - page[0]*paper[0]*2)//(paper[0] + 1)
                      n += 2*hgap
                     #print(hgap)
                #hgap += page[0]
                    n += x
                    #print(hgap)
            else:
                for p in range(0, paper[0]):
                    # vgap = (MainWindow.geometry().height() - page[1] * paper[1]) // (paper[0] + 1)
                    z = vgap
                    # print(page[1] * paper[1])
                    for m in range(0, paper[1] * 2):
                        # painter.drawRect(int(hgap), int(vgap), int(page[0]), int(page[1]))
                        painter.drawRect(int(n), int(z), int(x), int(y))

                        # vgap += vgap + page[1]
                        z +=  y
                        #n += x + hgap
                        if (m + 1) % 2 == 0:
                        # hgap += (MainWindow.geometry().width() - page[0]*paper[0]*2)//(paper[0] + 1)
                            z += 2*vgap
                        # print(hgap)
                    # hgap += page[0]
                    n += x + hgap


