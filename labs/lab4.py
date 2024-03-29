import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QMainWindow, QWidget, QFormLayout, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QTableWidget, QTableWidgetItem)
import random


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('Проверка попадания точки')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        central_widget = QWidget()
        layout = QFormLayout()
        central_widget.setLayout(layout)

        layout.addWidget(self.canvas)
        self.setCentralWidget(central_widget)

        self.check_point = QPushButton('Проверка точки')
        self.check_point.clicked.connect(self.check_points)

        self.add_function_button = QPushButton('Добавить функцию в список')
        self.function_input = QLineEdit(' Введите функцию для добавление в список ')
        self.function_widget = QComboBox()
        self.function_widget.addItems(['x', '2*x', 'x**2', 'x**3'])
        self.add_function_button.clicked.connect(self.add_function)

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear)

        self.point_random = QPushButton('Рандомная точка')
        self.point_random.clicked.connect(self.random_points)

        self.range_label = QLabel('Введите координаты точки:')
        self.range_start_input = QLineEdit()
        self.range_end_input = QLineEdit()
        self.range_start_input.setFixedSize(50,25)
        self.range_end_input.setFixedSize(50,25)

        layout.addWidget(self.function_widget)
        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        # layout.addWidget(self.check_point)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.point_random)
        layout.addRow(self.add_function_button, self.function_input)

        self.grafik()

    def grafik(self):
        plt.grid(True)
        plt.title('График')
        self.canvas.draw()
        plt.xlabel('x')
        plt.ylabel('y')

    def check_points(self):
        gdfgr


    def clear(self):
        for ax in self.fig.axes:
            ax.clear()
        self.grafik()

    def add_curves(self):



        self.canvas.draw()
    def random_points(self):
        a = str(random.uniform(-1, 1))[0:4]
        b = str(random.uniform(-1, 1))[0:4]
        self.start_diapazon.setText(a)
        self.end_diapazon.setText(b)
        self.canvas.draw()

    def add_function(self):
        text_x = self.function_input.text()
        self.function_widget.addItems([text_x])

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QMainWindow, QWidget, QFormLayout, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QTableWidget, QTableWidgetItem)
from matplotlib.patches import Rectangle
from PIL import Image

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)
        self.img = Image.open(r'C:\Users\user.AD\Desktop\white_background.PNG')
        self.img.thumbnail((500,500))

        self.setCentralWidget(cental_widget)

        self.table1 = QTableWidget()
        self.table1.setRowCount(2)
        self.table1.setColumnCount(5)
        self.table1.setHorizontalHeaderLabels(['X', 'Y', 'L', 'H', 'A'])
        self.table1.setFixedSize(550,100)

        self.table2 = QTableWidget()
        self.table2.setRowCount(2)
        self.table2.setColumnCount(4)
        self.table2.setHorizontalHeaderLabels(['Тип объекта', 'X2', 'Y2', 'R'])
        self.table2.setFixedSize(550, 100)

        self.create_object_button = QPushButton('создать')
        self.create_object_button.clicked.connect(self.create_object)

        self.create_ns_pv_button = QPushButton('создать объект')
        self.create_ns_pv_button.clicked.connect(self.create_circle)

        plt.grid(True)

        layout.addRow(self.table1, self.table2)
        layout.addRow(self.create_object_button, self.create_ns_pv_button)
        layout.addRow(self.canvas)

        for i in range(self.table2.rowCount()+1):
            self.table2_widget = QComboBox()
            self.table2_widget.addItems(['ПВ', 'НС'])
            self.table2.setCellWidget(i, 0, self.table2_widget)

    def create_object(self):
        x = float(self.table1.item(0,0).text())
        y = float(self.table1.item(0,1).text())
        l = float(self.table1.item(0,2).text())
        h = float(self.table1.item(0,3).text())
        a = float(self.table1.item(0,4).text())

        ax = plt.subplot()
        ax.imshow(self.img)

        rect = Rectangle((x,y), l, h, linewidth=1, edgecolor='black', facecolor='white', angle=a)
        ax.add_patch(rect)
        self.canvas.draw()

    def create_object1(self):
        x2 = float(self.table2.item(0,1).text())
        y2 = float(self.table2.item(0,2).text())
        r = float(self.table2.item(0,3).text())

        ax = plt.subplot()
        ax.imshow(self.img)
        circle = plt.Circle((x2,y2), linewidth=1, edgecolor='red', facecolor='red', radius=r)
        ax.add_patch(circle)
        self.canvas.draw()

    def create_object2(self):
        x2 = float(self.table2.item(0,1).text())
        y2 = float(self.table2.item(0,2).text())

        ax = plt.subplot()
        ax.imshow(self.img)
        circle = plt.Circle((x2,y2), linewidth=1, edgecolor='green', facecolor='green', radius=5)
        ax.add_patch(circle)
        self.canvas.draw()

    def create_circle(self):
        obj = str(self.table2.cellWidget(0,0).currentText())
        if obj == 'ПВ':
            self.create_object1()
        else:
            self.create_object2()
        self.canvas.draw()


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()


