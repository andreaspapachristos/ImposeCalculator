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
from PyQt5.QtGui import QPdfWriter, QPageSize, QPageLayout
from PyQt5.QtWidgets import QFileDialog




class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1000, 700)
        
        toolbar = MainWindow.addToolBar("Export")
        export_action = toolbar.addAction("Export PDF")
        export_action.triggered.connect(self.export_pdf)

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

        
    def export_pdf(self):
        from PyQt5.QtCore import QRectF, Qt
        from PyQt5.QtGui import (
            QPdfWriter,
            QPageSize,
            QPageLayout,
            QPainter,
            QPen,
            QColor,
            QFont
        )
        from PyQt5.QtWidgets import QFileDialog
        from datetime import datetime

        filename, _ = QFileDialog.getSaveFileName(
            self.MainWindow,
            "Export Scheme to PDF",
            "scheme.pdf",
            "PDF Files (*.pdf)"
        )

        if not filename:
            return

        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"

        writer = QPdfWriter(filename)
        writer.setResolution(300)

        writer.setPageLayout(
            QPageLayout(
                QPageSize(QPageSize.A4),
                QPageLayout.Landscape,
                QtCore.QMarginsF(10, 10, 10, 10)
            )
        )

        painter = QPainter()

        if not painter.begin(writer):
            return

        def draw_info(label, value):
            nonlocal y

            painter.setFont(label_font)
            painter.setPen(text_pen)

            painter.drawText(
                int(info_area.left()),
                y,
                label
            )

            y += int(24 * unit)

            painter.setFont(value_font)
            painter.setPen(accent_pen)

            painter.drawText(
                int(info_area.left()),
                y,
                value
            )

            y += int(50 * unit)

        try:
            page_rect = writer.pageLayout().paintRectPixels(
                writer.resolution()
            )

            margin = 30
            info_width = int(page_rect.width() * 0.28)

            scheme_area = QRectF(
                page_rect.left() + margin,
                page_rect.top() + margin,
                page_rect.width() - info_width - 3 * margin,
                page_rect.height() - 2 * margin
            )

            info_area = QRectF(
                scheme_area.right() + margin,
                scheme_area.top(),
                info_width,
                scheme_area.height()
            )

            # Διαστάσεις σελίδας και χαρτιού
            page_width, page_height = self.page
            columns, rows, rotation = self.paper

            if rotation == 0:
                rect_width = page_width
                rect_height = page_height
            else:
                rect_width = page_height
                rect_height = page_width

            double_spread = not self.monofyllo

            total_columns = columns
            total_rows = rows

            if double_spread:
                if rotation == 0:
                    total_columns *= 2
                else:
                    total_rows *= 2

            gap = max(rect_width, rect_height) * 0.04

                     # Θέσεις των σελίδων στο μοντάζ
                      # Θέσεις των σελίδων στο μοντάζ
                       # Θέσεις των σελίδων στο μοντάζ
            x_positions = []
            y_positions = []

            if double_spread:

                if rotation == 0:
                    # ==========================
                    # Spread οριζόντια
                    # ==========================

                    # X: 2 σελίδες χωρίς gap μεταξύ τους,
                    # gap μετά από κάθε spread.
                    current_x = 0

                    for col in range(total_columns):
                        x_positions.append(current_x)

                        current_x += rect_width

                        if (col + 1) % 2 == 0:
                            current_x += gap

                    # Y: κάθε σειρά spreads έχει gap
                    current_y = 0

                    for row in range(total_rows):
                        y_positions.append(current_y)
                        current_y += rect_height + gap

                else:
                    # ==========================
                    # Spread κατακόρυφα
                    # ==========================

                    # X: κάθε στήλη spreads έχει gap
                    current_x = 0

                    for col in range(total_columns):
                        x_positions.append(current_x)
                        current_x += rect_width + gap

                    # Y: 2 σελίδες χωρίς gap μεταξύ τους,
                    # gap μετά από κάθε spread.
                    current_y = 0

                    for row in range(total_rows):
                        y_positions.append(current_y)

                        current_y += rect_height

                        if (row + 1) % 2 == 0:
                            current_y += gap

            else:
                # ==========================
                # Μονόφυλλο
                # ==========================

                current_x = 0

                for col in range(total_columns):
                    x_positions.append(current_x)
                    current_x += rect_width + gap

                current_y = 0

                for row in range(total_rows):
                    y_positions.append(current_y)
                    current_y += rect_height + gap
            # Πραγματικές διαστάσεις μοντάζ
            scheme_width = x_positions[-1] + rect_width
            scheme_height = y_positions[-1] + rect_height

            # Κλίμακα ώστε να χωράει το μοντάζ στην περιοχή σχεδίασης
            scale = min(
                scheme_area.width() / scheme_width,
                scheme_area.height() / scheme_height
            )

            offset_x = (
                scheme_area.center().x() - scheme_width * scale / 2
            )
            offset_y = (
                scheme_area.center().y() - scheme_height * scale / 2
            )

            # Σχεδίαση μοντάζ
            painter.save()
            painter.translate(offset_x, offset_y)
            painter.scale(scale, scale)

            painter.setBrush(Qt.NoBrush)

            # Κόκκινα περιγράμματα σελίδων
            red_pen = QPen(QColor("#EB5160"))
            red_pen.setWidthF(1.0 / scale)
            painter.setPen(red_pen)

            for x in x_positions:
                for y in y_positions:
                    painter.drawRect(
                        QRectF(x, y, rect_width, rect_height)
                    )

            # Μαύρο εξωτερικό περίγραμμα χαρτιού
            black_pen = QPen(QColor("black"))
            black_pen.setWidthF(1.5 / scale)
            painter.setPen(black_pen)

            painter.drawRect(
                QRectF(-5, -5, scheme_width+10, scheme_height+10)
            )

            painter.restore()

            # Πληροφορίες PDF
            text_pen = QColor("#333333")
            accent_pen = QColor("#EB5160")

            # Μετατροπή σημείων γραμματοσειράς σε μονάδες PDF
            unit = writer.resolution() / 72.0

            painter.setPen(text_pen)

            title_font = QFont("Arial", 16)
            title_font.setBold(True)
            painter.setFont(title_font)

            y = int(info_area.top() + 40 * unit)

            painter.drawText(
                int(info_area.left()),
                y,
                "SCHEME INFORMATION"
            )

            y += int(30 * unit)

            line_pen = QPen(accent_pen)
            line_pen.setWidth(2)
            painter.setPen(line_pen)

            painter.drawLine(
                int(info_area.left()),
                y,
                int(info_area.right()),
                y
            )

            label_font = QFont("Arial", 11)
            value_font = QFont("Arial", 12)
            value_font.setBold(True)

            y += int(40 * unit)

            draw_info(
                "Paper size",
                f"{self.paper[0]} x {self.paper[1]} mm"
            )
            draw_info(
                "Paper size",
                f"{self.paper_size[0]} x {self.paper_size[1]} mm"
            )
            pages_per_sheet = (
                columns * rows * (1 if self.monofyllo else 2)
            )

            draw_info(
                "Pages per sheet",
                str(pages_per_sheet)
            )

            draw_info(
                "Orientation",
                "Rotated" if rotation else "Normal"
            )

            draw_info(
                "Date",
                datetime.now().strftime("%d/%m/%Y")
            )
        finally:
            painter.end()

    def __init__(self, MainWindow, size, page, paper, monofyllo, paper_size):
        self.statusbar = None
        self.label = None
        self.verticalLayout = None
        self.centralwidget = None

        self.MainWindow = MainWindow
        self.page = page
        self.paper = paper
        self.monofyllo = monofyllo
        self.paper_size = paper_size

        MainWindow.resize(size[0], size[1])

        self.setup(MainWindow)

        self.drawrect(
            MainWindow,
            [page[0], page[1]],
            [paper[0], paper[1], paper[2]],
            monofyllo
        )
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
        painter.drawText(int(-((MainWindow.geometry().height())/2)), 10, str(MainWindow.geometry().height()))
        painter.rotate(-270)
       # painter.drawText(10, int( (MainWindow.geometry().height())/2),  str(MainWindow.geometry().height()))    
        #z =
        #
        if paper[2] == 0:
            x = page[0]
            y = page[1]
            hgap = (MainWindow.geometry().width() - x * paper[0] * self.spreads(monofyllo)) // ((paper[0] * self.spreads(monofyllo)) +1)
            vgap = (MainWindow.geometry().height() - y * paper[1]) // (paper[1] + 2)


        else:
            x = page[1]
            y = page[0]
            hgap= (MainWindow.geometry().width() - x * paper[0])//((paper[0] ) +1)
            vgap = (MainWindow.geometry().height() - y * paper[1]*self.spreads(monofyllo)) // (paper[1]* self.spreads(monofyllo) +2 )

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


