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


from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox, QMessageBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)

        layout.addWidget(self.canvas)

        self.setCentralWidget(cental_widget)

        self.plot_button1 = QPushButton('Нарисовать график')
        self.plot_button1.clicked.connect(self.plot_data)

        self.check_point = QPushButton('Проверить точку')
        self.check_point.clicked.connect(self.proverka)

        self.random_point = QPushButton('Случайная точка')
        self.random_point.clicked.connect(self.random_points)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')
        self.range_start_input.setFixedSize(50, 25)
        self.range_end_input.setFixedSize(50,25)

        self.point_range = QLabel('Координаты точки')
        self.start_point_range = QLineEdit()
        self.end_point_range = QLineEdit()
        self.start_point_range.setFixedSize(50, 25)
        self.end_point_range.setFixedSize(50, 25)

        self.add_function_button1 = QPushButton('Добавить функцию')
        self.function_input1 = QLineEdit(' Введите функцию для добавление в список ')
        self.function_label1 = QLabel('Список функций')
        self.function_widget1 = QComboBox()
        self.function_widget1.addItems(['x', '2*x', 'x**2', 'x**3'])
        self.add_function_button1.clicked.connect(self.add_function)

        self.hl_widget1 = QComboBox()
        self.hl_widget1.addItems(['ВЫШЕ', 'НИЖЕ'])

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.error_message = QMessageBox()
        self.error_message.setText("Функция введена неверно!")
        self.error_message.setWindowTitle('Ошибка!')
        self.list_vector = []
        self.hl_vector = []

        layout.addRow(self.function_label1)
        layout.addWidget(self.function_widget1)
        layout.addWidget(self.plot_button1)
        layout.addWidget(self.hl_widget1)
        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addRow(self.point_range)
        layout.addRow(self.start_point_range, self.end_point_range)
        layout.addWidget(self.check_point)
        layout.addWidget(self.clear_button)
        layout.addRow(self.add_function_button1, self.function_input1)
        layout.addWidget(self.random_point)

    def vectors(self):
        try:
            expression = self.function_widget1.currentText()
        except NameError:
            expression = 'x'

        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
        functions = {}
        try:
            exec(f'def f(x): return {expression}', functions)
            x = np.linspace(range_start, range_end)
            function = functions['f']
            y = [function(value) for value in x]
            return x, y

        except NameError:
            self.error_message.show()
            return 0
        except SyntaxError:
            self.error_message.show()
            return 0

    def plot_data(self):
        if self.vectors() != 0:
            x, y = self.vectors()
            axes = plt.subplot()
            axes.plot(x, y)
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')
            expression = self.function_widget1.currentText()
            self.list_vector.append(expression)
            hl = self.hl_widget1.currentText()
            self.hl_vector.append(hl)
            self.centralWidget().layout().itemAt(0).widget().draw()

    def check_points(self):
        y_point_str = self.end_point_range.text()
        x_point_str = self.start_point_range.text()
        functions = {}
        cnt = 0
        for i in range(len(self.list_vector)):
            expression = self.list_vector[i]
            try:
                exec(f'def f(x): return {expression}', functions)
                function = functions['f']
                x_point = float(x_point_str)
                func = function(float(x_point))
                y_point = float(y_point_str)
            except NameError:
                return False
            except SyntaxError:
                return False

            hl = self.hl_vector[i]
            if hl == 'ВЫШЕ':
                if y_point >= func:
                    cnt += 1
            else:
                if y_point <= func:
                    cnt += 1

        if cnt == len(self.hl_vector):
            return True
        else:
            return False

    def proverka(self):
        g = self.check_points()

        x_point = float(self.start_point_range.text())
        y_point = float(self.end_point_range.text())

        if g != 0:
            plt.scatter(x_point, y_point, color='green')
        else:
            plt.scatter(x_point, y_point, color='red')

        self.canvas.draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()
        self.hl_vector = []
        self.list_vector = []

    def add_function(self):
        text_x = self.function_input1.text()
        self.function_widget1.addItems([text_x])

    def random_points(self):
        a1 = float(self.range_start_input.text())
        a2 = float(self.range_end_input.text())
        a = str(random.uniform(a1, a2))[0:4]
        b = str(random.uniform(a1, a2))[0:4]
        self.start_point_range.setText(a)
        self.end_point_range.setText(b)
        self.proverka()

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()

from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox, QMessageBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)
        layout.addWidget(self.canvas)
        plt.grid(True)
        self.setCentralWidget(cental_widget)

        self.plot_button = QPushButton('Нарисовать график')
        self.plot_button.clicked.connect(self.plot_data)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('-10')
        self.range_end_input = QLineEdit('10')

        self.add_function_button = QPushButton('Добавить функцию в список')
        self.function_input = QLineEdit(' Введите функцию для добавление в список ')
        self.function_widget = QComboBox()
        self.function_widget.addItems(['x', '2*x', 'x**3', ''])
        self.add_function_button.clicked.connect(self.add_function)

        self.point_amount = QLabel('Количество точек на графике:')
        self.point_input = QLineEdit('50')

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.error_message = QMessageBox()
        self.error_message.setText("Функция введена неверно!")
        self.error_message.setWindowTitle('Ошибка!')

        self.error_message2 = QMessageBox()
        self.error_message2.setText("На данном диапазоне f(c) != 0")
        self.error_message2.setWindowTitle('Ошибка!')

        self.bisection_button = QPushButton('Метод деления интервалов')
        self.bisection_button.clicked.connect(self.bisection)

        self.bisection_label = QLabel("Текущий диапазон:")
        self.bisection_range_start_current = QLineEdit('-10')
        self.bisection_range_end_current = QLineEdit('10')
        self.bisection_range_start_current.setEnabled(False)
        self.bisection_range_end_current.setEnabled(False)

        self.add_range_button = QPushButton('Изменить диапазон')
        self.add_range_button.clicked.connect(self.change_range)
        layout.addWidget(self.function_widget)
        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)
        layout.addWidget(self.add_range_button)
        layout.addWidget(self.bisection_label)
        layout.addWidget(self.bisection_range_start_current)
        layout.addWidget(self.bisection_range_end_current)
        layout.addWidget(self.bisection_button)
        layout.addWidget(self.clear_button)
        layout.addRow(self.add_function_button, self.function_input)

    def vectors(self):
        expression = self.function_widget.currentText()

        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
            points = int(self.point_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
            points = 50

        functions = {}
        try:
            exec(f'def f(x): return {expression}', functions)
            function = functions['f']
            x = np.linspace(range_start, range_end, points)
            y = [function(value) for value in x]
            return x, y

        except NameError:
            self.error_message.show()
            return 0
        except SyntaxError:
            self.error_message.show()
            return 0

    def plot_data(self):
        if self.vectors() != 0:
            x, y = self.vectors()
            axes = plt.subplot()
            axes.plot(x, y)
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')

            self.centralWidget().layout().itemAt(0).widget().draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()

    def add_function(self):
        text_x = self.function_input.text()
        self.function_widget.addItems([text_x])

    def bisection(self):
        a, b = float(self.bisection_range_start_current.text()), float(self.bisection_range_end_current.text())
        e = 10**-3
        expression = self.function_widget.currentText()
        functions = {}
        exec(f'def ff(x): return {expression}', functions)
        f = functions['ff']
        c = (a + b) / 2

        if f(c) == 0:
            plt.scatter(c, f(c))
            self.canvas.draw()
            self.bisection_range_start_current.setText(str(a))
            self.bisection_range_end_current.setText(str(b))
        elif abs(f(c)) < e:
            plt.scatter(c, f(c))
            self.canvas.draw()
        if f(c) < 0:
            if f(b) > 0:
                a = c
            elif f(a) > 0:
                b = c
        elif f(c) > 0:
            if f(b) < 0:
                a = c
            elif f(a) < 0:
                b = c
        x = np.linspace(a, b, 50)
        y = [f(value) for value in x]
        plt.plot(x, y)
        self.bisection_range_start_current.setText(str(a))
        self.bisection_range_end_current.setText(str(b))
        self.canvas.draw()

    def change_range(self):
        self.bisection_range_start_current.setText(str(self.range_start_input.text()))
        self.bisection_range_end_current.setText(str(self.range_end_input.text()))


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()

