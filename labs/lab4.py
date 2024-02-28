import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QMainWindow, QWidget, QFormLayout, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QTableWidget, QTableWidgetItem)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('Проверка попадания точки')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        central_widget = QWidget()
        layout = QFormLayout()
        central_widget.setLayout(layout)
        
        items = {'выше', 'ниже'
            
        }
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels('k', 'степень x', 'b', 'выше/ниже')
        table.horizontalHeaderItem(0).setToolTip('k')
        table.horizontalHeaderItem(1).setToolTip('степень x')
        table.horizontalHeaderItem(2).setToolTip('b')
        self.combobox = QComboBox(self, 200)
        self.combobox.addItems(self.items)





        layout.addWidget(self.canvas)
        self.setCentralWidget(central_widget)

        self.check_point = QPushButton('Проверка точки')
        self.check_point.clicked.connect(self.check_points)
        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear)
        self.range_label = QLabel('Введите координаты точки:')
        self.range_start_input = QLineEdit()
        self.range_end_input = QLineEdit()

        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addWidget(self.check_point)
        layout.addWidget(self.clear_button)

        self.grafik()

    def grafik(self):
        alpha = np.linspace(0, np.pi, 150)
        radius = 2
        a1 = radius * np.cos(alpha) - 1
        b1 = radius * np.sin(alpha) + 3
        x1 = [1, 1, 0, -3]
        y1 = [3, 1, -1, 3]
        ax = plt.subplot()
        ax.plot(a1, b1, color='black')
        ax.plot(x1, y1, color='black')
        ax.set_aspect(1)
        alpha2 = np.linspace(np.pi, 2 * np.pi, 150)
        radius = 2
        a2 = radius * np.cos(alpha2) + 5
        b2 = radius * np.sin(alpha2)
        x2 = [3, 5, 7]
        y2 = [0, 2, 0]
        ax.plot(a2, b2, color='black')
        ax.plot(x2, y2, color='black')
        plt.grid()
        plt.title('ctg')
        self.canvas.draw()

    def check_points(self):
        ax = plt.subplot()

        def fig1_check(x, y):
            k = self.table.item().text()
            n = self.table.item().text()
            b = self.table.item().text()
            if

            r = 2
            if (x + 1)**2 + (y-3)**2 <= r**2 and x <= 1:
                return True
            elif x <= 1 and 3 >= y >= (-4 / 3) * x - 1 and y >= 2 * x - 1:
                return True
            else:
                return False

        def fig2_check(x, y):

            r = 2
            if (x - 5)**2 + y**2 <= r**2 and y < 0:
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


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()



