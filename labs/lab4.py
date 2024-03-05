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

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear)

        self.point_random = QPushButton('Рандомная точка')
        self.point_random.clicked.connect(self.random_points)

        self.add_curve = QPushButton('Добавить кривую')
        self.add_curve.clicked.connect(self.add_curves)


        self.range_label = QLabel('Введите координаты точки:')
        self.range_start_input = QLineEdit()
        self.range_end_input = QLineEdit()
        self.range_start_input.setFixedSize(25,25)
        self.range_end_input.setFixedSize(25,25)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['k', 'n', 'b'])
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('k'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('n'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('b'))


        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addWidget(self.check_point)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.point_random)
        layout.addRow(self.table)
        layout.addWidget(self.add_curve)

        self.section = []
        self.grafik()

    def grafik(self):
        plt.grid(True)
        plt.title('График')
        self.canvas.draw()
        plt.xlabel('x')
        plt.ylabel('y')

    def check_points(self):
        ax = plt.subplot()

        def fig1_check(x, y):
            r = 2
            if (x + 1) ** 2 + (y - 3) ** 2 <= r ** 2 and x <= 1:
                return True
            elif x <= 1 and 3 >= y >= (-4 / 3) * x - 1 and y >= 2 * x - 1:
                return True
            else:
                return False

        def fig2_check(x, y):

            r = 2
            if (x - 5) ** 2 + y ** 2 <= r ** 2 and y < 0:
                return True
            elif x - 3 >= y >= 0 and y <= -x + 7:
                return True
            else:
                return False

        x, y = map(float, [self.range_start_input.text(), self.range_end_input.text()])
        if fig1_check(x, y):
            ax.scatter(x, y, color="green")
        elif fig2_check(x, y):
            ax.scatter(x, y, color='blue')
        else:
            ax.scatter(x, y, color='red')
        self.canvas.draw()

    def clear(self):
        for ax in self.fig.axes:
            ax.clear()
        self.grafik()

    def add_curves(self):
        k = float(self.table.item(0, 0).text())
        n = float(self.table.item(0, 1).text())
        b = float(self.table.item(0, 2).text())

        x = np.linspace(-1, 1, 25)
        y = k * x ** (n) + b

        plt.plot(x, y, color='black')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        self.canvas.draw()
    def random_points(self):
        coords = []
        coordinates = random.randint(1, 1)
        for i in range(coordinates):
            coords.append([random.randint(-1, 1), random.randint(-1, 1)])
        for point in coords:
            plt.scatter(point[0], point[1], color='g')

        self.canvas.draw()

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()



