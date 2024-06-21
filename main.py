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
# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#from PyQt5 import QtCore, QtGui, QtWidgets

import add_paper
import diastaseis
import remove_paper
import sys
from view import *


class Ui_MainWindow(object):
    papers = ["610x860", "640x880", "700x1000"]

    def __init__(self):
        self.window = None
        self.ui = None
        self.Dialog = None

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setStyleSheet("background-color: rgb(0, 0, 0);" "color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.splitter)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.gridLayout_5.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QtCore.QRect(6, 6, 63, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 32, 178, 196))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 2, 1, 3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 4, 2, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setObjectName("comboBox")
        for i in range(0, self.papers.__len__()):
            self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        # self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 3, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_7)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_6.addWidget(self.toolButton, 0, 0, 1, 1)

        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_7)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/minus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_6.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 7, 0, 1, 5)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(-1, 290, 181, 86))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 380, 181, 151))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_9)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 230, 181, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 30, 111, 190))
        self.checkBox_5.setObjectName("checkBox_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.checkBox_2.toggled['bool'].connect(self.groupBox_6.setEnabled)
        self.checkBox_3.clicked.connect(self.checkBox_4.toggle)
        self.checkBox_4.clicked.connect(self.checkBox_3.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.calc)
        self.toolButton.clicked.connect(self.addPaper)
        self.toolButton_3.clicked.connect(self.removePaper)
    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Page to be imposed</p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Page"))
        self.groupBox.setTitle(_translate("MainWindow", "Dimensions"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Width of imposed page</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "210"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Height of imposed page</p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "280"))
        self.checkBox.setText(_translate("MainWindow", "Single Page"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.groupBox_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Results</p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Montaz"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Paper"))
        self.label_4.setText(_translate("MainWindow", "Height"))
        self.label_3.setText(_translate("MainWindow", "Width"))
        self.label_5.setText(_translate("MainWindow", "Pages"))
        self.label_6.setText(_translate("MainWindow", "Usage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "main"))
        self.checkBox_2.setToolTip(_translate("MainWindow","<html><head/><body><p><span style=\" color:#ff0000;\">Dangerous AREA</span></p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "Enable"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Set Paper"))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>Page Bleed</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "bleed"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>Offset gap at botom of the paper</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Gap"))
        self.label_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Papers list which calculation take place</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Papers"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "3"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "10"))
        # self.comboBox.setItemText(0, _translate("MainWindow", "ALL"))
        for i in range(0, self.papers.__len__()):
            self.comboBox.setItemText(i,_translate("MainWindow", self.papers[i]))
        #self.comboBox.setItemText(0, _translate("MainWindow", "580x860"))
        #self.comboBox.setItemText(1, _translate("MainWindow", "610x860"))
        #self.comboBox.setItemText(2, _translate("MainWindow", "640x880"))
        #self.comboBox.setItemText(3, _translate("MainWindow", "700x1000"))
        self.toolButton.setText(_translate("MainWindow", "add"))
        #self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "rm"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Single Page"))
        self.checkBox_3.setText(_translate("MainWindow", "Work and Turn"))
        self.checkBox_4.setText(_translate("MainWindow", "Work and Tumble"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">By checking this button the utility open a new window with the </span><span style=\" font-weight:600; color:#ff5500;\">scheme</span><span style=\" font-weight:600;\"> of the impose template.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">IF Single Page Impose</span></p></body></html>"))
        self.checkBox_5.setText(_translate("MainWindow", "Auto- Draw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "preferences"))
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.setMaxLength(3)
        self.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.lineEdit_2.setMaxLength(3)

    def calc(self):

        papers = []
        try:
            pass
            if self.checkBox_2.isChecked():
                papers.append([int(self.comboBox.currentText().split('x', 1)[j]) for j in range(2)])
            else:
                for i in range(self.comboBox.count()):
                    papers.append([int(self.comboBox.itemText(i).split('x', 1)[j]) for j in range(2)])
            try:
                width = int(self.lineEdit.text())
                height = int(self.lineEdit_2.text())
            # print(len(papers))
                page = [width, height]
            except ValueError:
                print("no page has given use the default")
                page = [210,280]
                pass
            monofyllo = self.checkBox.isChecked()
            print(monofyllo)
            if self.lineEdit_7.text():
                bleed = int(self.lineEdit_7.text())
            else:
                bleed = int(self.lineEdit_7.placeholderText())
            if self.lineEdit_8.text():
                gap = int(self.lineEdit_8.text())
            else:
                gap = int(self.lineEdit_8.placeholderText())

            result = diastaseis.betterUse(papers, page, monofyllo, bleed, gap)

            self.lineEdit_3.setText(QtCore.QCoreApplication.translate("MainWindow", str(result[1][1])))
            self.lineEdit_4.setText(QtCore.QCoreApplication.translate("MainWindow", str(result[1][0])))
            self.lineEdit_5.setText(QtCore.QCoreApplication.translate("MainWindow", result[0]))
            self.lineEdit_6.setText(QtCore.QCoreApplication.translate("MainWindow", str(result[2])))
            if self.checkBox_5.isChecked():
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow1(self.window, [result[1][1], result[1][0]], page, result[3], monofyllo)
                self.window.show()
        except Exception as X :
            print(X)
            #pass

    def addPaper(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = add_paper.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        #self.papers.append("%sx%s" % (self.ui.lineEdit.text(),  self.ui.lineEdit_2.text()))
        #print(("%sx%s" % (self.ui.lineEdit.text(),  self.ui.lineEdit_2.text())))

        self.Dialog.show()
        if self.Dialog.exec_():
            self.comboBox.addItem(self.ui.accept()[1] + "x" + self.ui.accept()[0])
            self.papers.append(self.ui.accept()[1] + "x" + self.ui.accept()[0])
            self.comboBox.update()
        #return

    def removePaper(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = remove_paper.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        model = QtGui.QStandardItemModel()

        for i in self.papers:
            item = QtWidgets.QListWidgetItem(i)
            self.ui.listWidget.addItem(item)
            #model.appendRow(item)
        if self.Dialog.exec_():
            index = self.ui.listWidget.currentRow()
            #self.ui.listWidget.clear()
            self.papers.pop(index)
            self.comboBox.removeItem(index)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
