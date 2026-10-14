# -*- coding: utf-8 -*-
'''
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
'''

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPdfWriter


class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Κύριο Vertical Layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Label για το σχέδιο
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        # Δημιουργία Κουμπιού για την εξαγωγή σε PDF
        self.pdf_button = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_button.setObjectName("pdf_button")
        self.pdf_button.setText("Εξαγωγή σε PDF")
        self.pdf_button.clicked.connect(self.export_to_pdf)
        self.verticalLayout.addWidget(self.pdf_button)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Υπολογισμός κανβά με βάση το νέο ύψος (αφαιρούμε τον χώρο του κουμπιού)
        canvas = QtGui.QPixmap(MainWindow.frameGeometry().width(), MainWindow.frameGeometry().height() - 70)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)

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
        self.pdf_button = None
        self.MainWindow = MainWindow   
        
        # Δίνουμε έξτρα ύψος στο παράθυρο (+70 pixels) για να χωράει άνετα το κουμπί 
        MainWindow.resize(size[0], size[1] + 100)
        
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
        painter.rotate(270)
        real_height = MainWindow.geometry().height() -22.5
        painter.drawText(int(-(real_height/2)+22.5), 10, str(real_height-77.5))
        painter.rotate(-270)
        
        if paper[2] == 0:
            x = page[0]
            y = page[1]
            hgap = (MainWindow.geometry().width() - x * paper[0] * self.spreads(monofyllo)) // ((paper[0] * self.spreads(monofyllo)) + 1)
            vgap = (real_height - y * paper[1]) // (paper[1] + 2)
        else:
            x = page[1]
            y = page[0]
            hgap = (MainWindow.geometry().width() - x * paper[0]) // ((paper[0]) + 1)
            vgap = (real_height  - y * paper[1] * self.spreads(monofyllo)) // (paper[1] * self.spreads(monofyllo) + 2)

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
                    z = vgap -20
                    for m in range(0, paper[1]):
                        painter.drawRect(int(n), int(z), int(x), int(y))
                        z += vgap + y
                    if (p + 1) % 2 == 0:
                        n += 2*hgap
                    n += x
            else:
                for p in range(0, paper[0]):
                    z = vgap
                    for m in range(0, paper[1] * 2):
                        painter.drawRect(int(n), int(z), int(x), int(y))
                        z += y
                        if (m + 1) % 2 == 0:
                            z += 2*vgap
                    n += x + hgap
        
        painter.end()

    def export_to_pdf(self):
        """Εξάγει το σχέδιο σε PDF προσαρμοσμένο σε Α4 χωρίς περιττά πλαίσια."""
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.MainWindow, 
            "Αποθήκευση σε PDF", 
            "scheme_output.pdf", 
            "PDF Files (*.pdf)"
        )
        
        if not file_path:
            return  # Αν ο χρήστης ακυρώσει

        writer = QPdfWriter(file_path)
        writer.setPageSize(QPdfWriter.A4)
        writer.setResolution(300)

        painter = QtGui.QPainter(writer)
        
        page_width = writer.width()
        page_height = writer.height()

        # 1. Εκτύπωση πληροφοριών στην κορυφή της σελίδας Α4
        font = QtGui.QFont("Arial", 12)
        painter.setFont(font)
        painter.setPen(QtGui.QPen(QtGui.QColor("#222222")))

        current_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        info_text = (
            f"Ημερομηνία: {current_date}  |  "
            f"Διαστάσεις Σελίδας: {self.page[0]}x{self.page[1]}  |  "
            f"Διαστάσεις Χαρτιού: {self.paper[0]}x{self.paper[1]}"
        )
        
        painter.drawText(150, 200, info_text)

        # 2. Προσαρμογή και κλιμάκωση του σχεδίου (pixmap)
        pixmap = self.label.pixmap()
        if pixmap:
            target_x = 100
            target_y = 350
            target_width = page_width - 200
            target_height = page_height - 500

            scaled_pixmap = pixmap.scaled(
                target_width, 
                target_height, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            painter.drawPixmap(target_x, target_y, scaled_pixmap)

        painter.end()
        
        QtWidgets.QMessageBox.information(
            self.MainWindow, 
            "Επιτυχία", 
            f"Το PDF αποθηκεύτηκε επιτυχώς στο:\n{file_path}"
        )