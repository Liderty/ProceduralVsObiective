# -*- coding: utf-8 -*-
import datetime
import traceback
from typing import List

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QLabel
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget

import OOP
import Procedural


class UIMainWindow(object):
    labels: List[QtWidgets.QLabel]
    operations_amount_fields: List[QtWidgets.QSpinBox]
    additional_operations_checkboxes: List[QtWidgets.QCheckBox]
    procedural_times_output_fields: List[QtWidgets.QLineEdit]
    oop_times_output_fields: List[QtWidgets.QLineEdit]

    def __init__(self):
        self.labels = []
        self.operations_amount_fields = []
        self.additional_operations_checkboxes = []
        self.procedural_times_output_fields = []
        self.oop_times_output_fields = []

        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)

        self.main_operations_number = 0
        self.execution_times = [[0], [0]]

    def setup_ui(self, MainWindow):
        font_size_9 = QtGui.QFont()
        font_size_9.setPointSize(9)

        font_size_10 = QtGui.QFont()
        font_size_10.setPointSize(10)

        font_size_12 = QtGui.QFont()
        font_size_12.setPointSize(12)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")

        self.labels.insert(0, QtWidgets.QLabel(self.central_widget))
        self.labels[0].setObjectName("label_operation_amount")
        self.labels[0].setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.labels[0].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Ilość operacji"
        ))

        self.labels.insert(1, QtWidgets.QLabel(self.central_widget))
        self.labels[1].setObjectName("label_operations_select")
        self.labels[1].setGeometry(QtCore.QRect(110, 40, 141, 16))
        self.labels[1].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Wybór operacji do wykonania"
        ))

        self.labels.insert(2, QtWidgets.QLabel(self.central_widget))
        self.labels[2].setObjectName("label_elapsed_time")
        self.labels[2].setGeometry(QtCore.QRect(290, 10, 231, 21))
        self.labels[2].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Czasy wykonania (milisekundy)"
        ))
        self.labels[2].setFont(font_size_12)

        self.labels.insert(3, QtWidgets.QLabel(self.central_widget))
        self.labels[3].setObjectName("label_result_console")
        self.labels[3].setGeometry(QtCore.QRect(10, 310, 111, 16))
        self.labels[3].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Konsola wynikowa"
        ))
        self.labels[3].setFont(font_size_10)

        self.labels.insert(4, QtWidgets.QLabel(self.central_widget))
        self.labels[4].setObjectName("label_time_chart_by_approach")
        self.labels[4].setGeometry(QtCore.QRect(550, 10, 321, 21))
        self.labels[4].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Wykres czasu działania programu w zależności od podejścia"
        ))
        self.labels[4].setFont(font_size_9)

        self.labels.insert(5, QtWidgets.QLabel(self.central_widget))
        self.labels[5].setObjectName("label_operations_amount")
        self.labels[5].setGeometry(QtCore.QRect(550, 260, 321, 30))
        self.labels[5].setAlignment(QtCore.Qt.AlignCenter)
        self.labels[5].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Ilość operacji (w tysiącach)"
        ))
        self.labels[5].setFont(font_size_10)

        self.labels.insert(6, VerticalLabel(self.central_widget))
        self.labels[6].setObjectName("label_chart_elapsed_time")
        self.labels[6].setGeometry(QtCore.QRect(520, 40, 30, 221))
        self.labels[6].setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labels[6].setAutoFillBackground(False)
        self.labels[6].setScaledContents(False)
        self.labels[6].setWordWrap(False)
        self.labels[6].setOpenExternalLinks(False)
        self.labels[6].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Czas wykonania (milisekundy)"
        ))
        self.labels[6].setFont(font_size_10)

        self.labels.insert(7, QtWidgets.QLabel(self.central_widget))
        self.labels[7].setObjectName("label_input_data")
        self.labels[7].setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.labels[7].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Dane wejściowe"
        ))
        self.labels[7].setFont(font_size_12)

        self.labels.insert(8, QtWidgets.QLabel(self.central_widget))
        self.labels[8].setObjectName("label_procedural")
        self.labels[8].setGeometry(QtCore.QRect(290, 40, 107, 26))
        self.labels[8].setAlignment(QtCore.Qt.AlignCenter)
        self.labels[8].setStyleSheet("background-color: #f00")
        self.labels[8].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Proceduralnie"
        ))

        self.labels.insert(9, QtWidgets.QLabel(self.central_widget))
        self.labels[9].setObjectName("label_oop")
        self.labels[9].setGeometry(QtCore.QRect(403, 40, 108, 26))
        self.labels[9].setAlignment(QtCore.Qt.AlignCenter)
        self.labels[9].setStyleSheet("background-color: #0ff")
        self.labels[9].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Obiektowo"
        ))

        self.vertical_line = QtWidgets.QFrame(self.central_widget)
        self.vertical_line.setObjectName("vertical_line")
        self.vertical_line.setGeometry(QtCore.QRect(260, 10, 21, 271))
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.horizontal_line = QtWidgets.QFrame(self.central_widget)
        self.horizontal_line.setObjectName("horizontal_line")
        self.horizontal_line.setGeometry(QtCore.QRect(10, 290, 861, 20))
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.operations_amount_widget = QtWidgets.QWidget(self.central_widget)
        self.operations_amount_widget.setGeometry(QtCore.QRect(10, 60, 91, 171))
        self.operations_amount_widget.setObjectName("operations_amount_widget")

        self.operations_amount_layout = QtWidgets.QVBoxLayout(self.operations_amount_widget)
        self.operations_amount_layout.setContentsMargins(0, 0, 0, 0)
        self.operations_amount_layout.setObjectName("operations_amount_layout")

        self.operations_amount_fields.insert(0, QtWidgets.QSpinBox(self.operations_amount_widget))
        self.operations_amount_fields[0].setObjectName("operations_amount_field_0")
        self.operations_amount_fields[0].setRange(10000, 1000000)
        self.operations_amount_fields[0].setSingleStep(1000)
        self.operations_amount_fields[0].setValue(15000)
        self.operations_amount_layout.addWidget(self.operations_amount_fields[0])

        self.operations_amount_fields.insert(1, QtWidgets.QSpinBox(self.operations_amount_widget))
        self.operations_amount_fields[1].setObjectName("operations_amount_field_1")
        self.operations_amount_fields[1].setRange(10000, 1000000)
        self.operations_amount_fields[1].setSingleStep(1000)
        self.operations_amount_fields[1].setValue(50000)
        self.operations_amount_layout.addWidget(self.operations_amount_fields[1])

        self.operations_amount_fields.insert(2, QtWidgets.QSpinBox(self.operations_amount_widget))
        self.operations_amount_fields[2].setObjectName("operations_amount_field_2")
        self.operations_amount_fields[2].setRange(10000, 1000000)
        self.operations_amount_fields[2].setSingleStep(1000)
        self.operations_amount_fields[2].setValue(150000)
        self.operations_amount_layout.addWidget(self.operations_amount_fields[2])

        self.operations_amount_fields.insert(3, QtWidgets.QSpinBox(self.operations_amount_widget))
        self.operations_amount_fields[3].setObjectName("operations_amount_field_3")
        self.operations_amount_fields[3].setRange(10000, 1000000)
        self.operations_amount_fields[3].setSingleStep(1000)
        self.operations_amount_fields[3].setValue(300000)
        self.operations_amount_layout.addWidget(self.operations_amount_fields[3])

        self.operations_amount_fields.insert(4, QtWidgets.QSpinBox(self.operations_amount_widget))
        self.operations_amount_fields[4].setObjectName("operations_amount_field_4")
        self.operations_amount_fields[4].setRange(10000, 1000000)
        self.operations_amount_fields[4].setSingleStep(1000)
        self.operations_amount_fields[4].setValue(1000000)
        self.operations_amount_layout.addWidget(self.operations_amount_fields[4])

        self.additional_operations_widget = QtWidgets.QWidget(self.central_widget)
        self.additional_operations_widget.setObjectName("additional_operations_widget")
        self.additional_operations_widget.setGeometry(QtCore.QRect(110, 60, 141, 171))

        self.additional_operations_layout = QtWidgets.QVBoxLayout(self.additional_operations_widget)
        self.additional_operations_layout.setObjectName("additional_operations_layout")
        self.additional_operations_layout.setContentsMargins(0, 0, 0, 0)

        self.additional_operations_checkboxes.insert(0, QtWidgets.QCheckBox(self.additional_operations_widget))
        self.additional_operations_checkboxes[0].setObjectName("additional_operations_checkbox_0")
        self.additional_operations_checkboxes[0].setEnabled(False)
        self.additional_operations_checkboxes[0].setChecked(True)
        self.additional_operations_checkboxes[0].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Operacji"
        ))
        self.additional_operations_layout.addWidget(self.additional_operations_checkboxes[0])

        self.additional_operations_checkboxes.insert(1, QtWidgets.QCheckBox(self.additional_operations_widget))
        self.additional_operations_checkboxes[1].setObjectName("additional_operations_checkbox_1")
        self.additional_operations_checkboxes[1].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Operacji dodatkowych"
        ))
        self.additional_operations_layout.addWidget(self.additional_operations_checkboxes[1])

        self.additional_operations_checkboxes.insert(2, QtWidgets.QCheckBox(self.additional_operations_widget))
        self.additional_operations_checkboxes[2].setObjectName("additional_operations_checkbox_2")
        self.additional_operations_checkboxes[2].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Operacji dodatkowych"
        ))
        self.additional_operations_layout.addWidget(self.additional_operations_checkboxes[2])

        self.additional_operations_checkboxes.insert(3, QtWidgets.QCheckBox(self.additional_operations_widget))
        self.additional_operations_checkboxes[3].setObjectName("additional_operations_checkbox_3")
        self.additional_operations_checkboxes[3].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Operacji dodatkowych"
        ))
        self.additional_operations_layout.addWidget(self.additional_operations_checkboxes[3])

        self.additional_operations_checkboxes.insert(4, QtWidgets.QCheckBox(self.additional_operations_widget))
        self.additional_operations_checkboxes[4].setObjectName("additional_operations_checkbox_4")
        self.additional_operations_checkboxes[4].setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Operacji dodatkowych"
        ))
        self.additional_operations_layout.addWidget(self.additional_operations_checkboxes[4])

        self.operation_times_widget = QtWidgets.QWidget(self.central_widget)
        self.operation_times_widget.setObjectName("operation_times_widget")
        self.operation_times_widget.setGeometry(QtCore.QRect(290, 72, 221, 171))

        self.operation_times_layout = QtWidgets.QHBoxLayout(self.operation_times_widget)
        self.operation_times_layout.setObjectName("operation_times_layout")
        self.operation_times_layout.setContentsMargins(0, 0, 0, 0)

        self.procedural_times_output_layout = QtWidgets.QVBoxLayout()
        self.procedural_times_output_layout.setObjectName("procedural_times_output_layout")

        self.procedural_times_output_fields.insert(0, QtWidgets.QLineEdit(self.operation_times_widget))
        self.procedural_times_output_fields[0].setObjectName("procedural_time_output_fields_0")
        self.procedural_times_output_fields[0].setAlignment(QtCore.Qt.AlignCenter)
        self.procedural_times_output_fields[0].setReadOnly(True)
        self.procedural_times_output_fields[0].setText("-")
        self.procedural_times_output_layout.addWidget(self.procedural_times_output_fields[0])

        self.procedural_times_output_fields.insert(1, QtWidgets.QLineEdit(self.operation_times_widget))
        self.procedural_times_output_fields[1].setObjectName("procedural_time_output_fields_1")
        self.procedural_times_output_fields[1].setAlignment(QtCore.Qt.AlignCenter)
        self.procedural_times_output_fields[1].setReadOnly(True)
        self.procedural_times_output_fields[1].setText("-")
        self.procedural_times_output_layout.addWidget(self.procedural_times_output_fields[1])

        self.procedural_times_output_fields.insert(2, QtWidgets.QLineEdit(self.operation_times_widget))
        self.procedural_times_output_fields[2].setObjectName("procedural_time_output_fields_2")
        self.procedural_times_output_fields[2].setAlignment(QtCore.Qt.AlignCenter)
        self.procedural_times_output_fields[2].setReadOnly(True)
        self.procedural_times_output_fields[2].setText("-")
        self.procedural_times_output_layout.addWidget(self.procedural_times_output_fields[2])

        self.procedural_times_output_fields.insert(3, QtWidgets.QLineEdit(self.operation_times_widget))
        self.procedural_times_output_fields[3].setObjectName("procedural_time_output_fields_3")
        self.procedural_times_output_fields[3].setAlignment(QtCore.Qt.AlignCenter)
        self.procedural_times_output_fields[3].setReadOnly(True)
        self.procedural_times_output_fields[3].setText("-")
        self.procedural_times_output_layout.addWidget(self.procedural_times_output_fields[3])

        self.procedural_times_output_fields.insert(4, QtWidgets.QLineEdit(self.operation_times_widget))
        self.procedural_times_output_fields[4].setObjectName("procedural_time_output_fields_4")
        self.procedural_times_output_fields[4].setAlignment(QtCore.Qt.AlignCenter)
        self.procedural_times_output_fields[4].setReadOnly(True)
        self.procedural_times_output_fields[4].setText("-")
        self.procedural_times_output_layout.addWidget(self.procedural_times_output_fields[4])

        self.operation_times_layout.addLayout(self.procedural_times_output_layout)

        self.oop_times_output_layout = QtWidgets.QVBoxLayout()
        self.oop_times_output_layout.setObjectName("oop_times_output_layout")

        self.oop_times_output_fields.insert(0, QtWidgets.QLineEdit(self.operation_times_widget))
        self.oop_times_output_fields[0].setObjectName("timeOutputField0")
        self.oop_times_output_fields[0].setAlignment(QtCore.Qt.AlignCenter)
        self.oop_times_output_fields[0].setReadOnly(True)
        self.oop_times_output_fields[0].setText("-")
        self.oop_times_output_layout.addWidget(self.oop_times_output_fields[0])

        self.oop_times_output_fields.insert(1, QtWidgets.QLineEdit(self.operation_times_widget))
        self.oop_times_output_fields[1].setObjectName("timeOutputField1")
        self.oop_times_output_fields[1].setAlignment(QtCore.Qt.AlignCenter)
        self.oop_times_output_fields[1].setReadOnly(True)
        self.oop_times_output_fields[1].setText("-")
        self.oop_times_output_layout.addWidget(self.oop_times_output_fields[1])

        self.oop_times_output_fields.insert(2, QtWidgets.QLineEdit(self.operation_times_widget))
        self.oop_times_output_fields[2].setObjectName("timeOutputField2")
        self.oop_times_output_fields[2].setAlignment(QtCore.Qt.AlignCenter)
        self.oop_times_output_fields[2].setReadOnly(True)
        self.oop_times_output_fields[2].setText("-")
        self.oop_times_output_layout.addWidget(self.oop_times_output_fields[2])

        self.oop_times_output_fields.insert(3, QtWidgets.QLineEdit(self.operation_times_widget))
        self.oop_times_output_fields[3].setObjectName("timeOutputField3")
        self.oop_times_output_fields[3].setAlignment(QtCore.Qt.AlignCenter)
        self.oop_times_output_fields[3].setReadOnly(True)
        self.oop_times_output_fields[3].setText("-")
        self.oop_times_output_layout.addWidget(self.oop_times_output_fields[3])

        self.oop_times_output_fields.insert(4, QtWidgets.QLineEdit(self.operation_times_widget))
        self.oop_times_output_fields[4].setObjectName("timeOutputField4")
        self.oop_times_output_fields[4].setAlignment(QtCore.Qt.AlignCenter)
        self.oop_times_output_fields[4].setReadOnly(True)
        self.oop_times_output_fields[4].setText("-")
        self.oop_times_output_layout.addWidget(self.oop_times_output_fields[4])

        self.operation_times_layout.addLayout(self.oop_times_output_layout)

        self.calculate_button = QtWidgets.QPushButton(self.central_widget)
        self.calculate_button.setObjectName("calculate_button")
        self.calculate_button.setGeometry(QtCore.QRect(10, 240, 241, 41))
        self.calculate_button.setText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Oblicz"
        ))
        self.calculate_button.clicked.connect(lambda: self.count())

        self.chart = PlotWidget(self.central_widget)
        self.chart.setObjectName("chart")
        self.chart.setGeometry(QtCore.QRect(550, 40, 321, 221))
        self.chart.showGrid(x=True, y=True)

        self.console = QtWidgets.QTextBrowser(self.central_widget)
        self.console.setObjectName("console")
        self.console.setGeometry(QtCore.QRect(10, 330, 861, 91))
        self.console.setAutoFillBackground(False)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(880, 430)
        MainWindow.setCentralWidget(self.central_widget)
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Porównanie czasów operacji wykonanych proceduralnie i obiektowo (M. Liber, P. Lyschik, 2020)"
        ))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def disable_ui(self):
        self.calculate_button.setEnabled(False)

        for field in self.operations_amount_fields:
            field.setEnabled(False)

        for check_box in self.additional_operations_checkboxes[1:]:
            check_box.setEnabled(False)

    def enable_ui(self):
        self.calculate_button.setEnabled(True)

        for field in self.operations_amount_fields:
            field.setEnabled(True)

        for check_box in self.additional_operations_checkboxes[1:]:
            check_box.setEnabled(True)

    def clear_time_tables(self):
        for field in self.procedural_times_output_fields:
            field.setText("-")

        for field in self.oop_times_output_fields:
            field.setText("-")

    def is_calculation_finished(self):
        for element in self.procedural_times_output_fields[:self.main_operations_number - 1]:
            if element.text() == "-":
                return False

        for element in self.oop_times_output_fields[:self.main_operations_number - 1]:
            if element.text() == "-":
                return False

        return True

    def clear_chart(self):
        self.chart.clear()

    def clear_times(self):
        self.execution_times = [[0], [0]]

    def clear_console(self):
        self.console.clear()

    def clear_data(self):
        self.clear_time_tables()
        self.clear_chart()
        self.clear_times()
        self.clear_console()

    def console_print_line(self, message):
        date_time_now = datetime.datetime.now()
        current_date_time = date_time_now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        self.console.append("[{0}] {1}".format(current_date_time, message))

    def print_execution_time(self, operation_type, operations_number, execution_time):
        self.console_print_line("Wykonanie {0:,} operacji w podejściu {1} zajęło {2} ms.".format(
            operations_number,
            operation_type,
            execution_time
        ).replace(',', ' '))

    def get_data(self):
        data_table = [0, self.operations_amount_fields[0].value()]

        if self.additional_operations_checkboxes[1].isChecked():
            data_table.append(self.operations_amount_fields[1].value())

        if self.additional_operations_checkboxes[2].isChecked():
            data_table.append(self.operations_amount_fields[2].value())

        if self.additional_operations_checkboxes[3].isChecked():
            data_table.append(self.operations_amount_fields[3].value())

        if self.additional_operations_checkboxes[4].isChecked():
            data_table.append(self.operations_amount_fields[4].value())

        return data_table

    def count(self):
        self.disable_ui()
        self.clear_data()
        self.console_print_line("Rozpoczęto obliczenia.")

        number_of_operations = self.get_data()
        self.main_operations_number = len(number_of_operations)

        for i in range(1, len(number_of_operations)):
            self.multi_thread_execute(number_of_operations[i], operation_procedural)
            self.multi_thread_execute(number_of_operations[i], operation_objective)

    def update_procedural(self, result):
        self.execution_times[0].append(result[0])
        self.procedural_times_output_fields[len(self.execution_times[0]) - 2].setText(str(result[0]))
        self.update_plots()
        self.print_execution_time("proceduralnym", result[1], self.execution_times[0][-1])

        if self.is_calculation_finished():
            self.console_print_line("Zakończono obliczenia.")
            self.enable_ui()


    def update_objective(self, result):
        self.execution_times[1].append(result[0])
        self.oop_times_output_fields[len(self.execution_times[1]) - 2].setText(str(result[0]))
        self.update_plots()
        self.print_execution_time("obiektowym", result[1], self.execution_times[1][-1])

        if self.is_calculation_finished():
            self.console_print_line("Zakończono obliczenia.")
            self.enable_ui()

    def update_plots(self):
        chart_data_procedural = self.prepare_chart_data(0)

        self.chart.plot(
            chart_data_procedural[0],
            chart_data_procedural[1],
            name='Proceduralnie',
            pen=(255, 0, 0),
            symbol='o',
            symbolSize=5,
            symbolPen=(255, 0, 0),
            symbolBrush=(255, 0, 0)
        )

        chart_data_oop = self.prepare_chart_data(1)

        self.chart.plot(
            chart_data_oop[0],
            chart_data_oop[1],
            name='Obiektowo',
            pen=(0, 255, 255),
            symbol='o',
            symbolSize=5,
            symbolPen=(0, 255, 255),
            symbolBrush=(0, 255, 255)
        )

    def prepare_chart_data(self, data_id):
        number_of_operations = self.reduce_data_for_chart_by_thousand(
            self.get_data()[:len(self.execution_times[data_id])]
        )
        times = self.execution_times[data_id]

        return self.sort_two_tables_by_first(number_of_operations, times)

    def sort_two_tables_by_first(self, sorted_table, other_table):
        while True:
            edition_flag = 0

            for i in range(len(sorted_table) - 1):
                if sorted_table[i] > sorted_table[i + 1]:
                    tmp = sorted_table[i]
                    sorted_table[i] = sorted_table[i + 1]
                    sorted_table[i + 1] = tmp

                    tmp_other = other_table[i]
                    other_table[i] = other_table[i + 1]
                    other_table[i + 1] = tmp_other

                    edition_flag += 1

            if edition_flag == 0:
                return (sorted_table, other_table)

    def reduce_data_for_chart_by_thousand(self, data):
        reduced_data = []

        for element in data:
            reduced_data.append(element / 1000)

        return reduced_data

    def multi_thread_execute(self, operations_number, operation_type):
        worker = Worker(operation_type, operations_number)

        if operation_type == operation_procedural:
            worker.signals.result.connect(self.update_procedural)
        else:
            worker.signals.result.connect(self.update_objective)

        self.thread_pool.start(worker)


def operation_procedural(size):
    accounts = {}

    Procedural.create_account(accounts, 'Foo', 'Bar', 4578220122)
    Procedural.create_account(accounts, 'Foo', 'Baz', 2347885320)
    Procedural.create_account(accounts, 'Foo', 'Baz', 1174559614)

    for _ in range(0, size):
        Procedural.make_deposit(accounts, 4578220122, 5)
        Procedural.make_deposit(accounts, 2347885320, 5)

    for _ in range(0, size):
        Procedural.make_withdraw(accounts, 4578220122, 1)
        Procedural.make_withdraw(accounts, 2347885320, 1)

    for _ in range(0, size):
        Procedural.make_transfer(accounts, 4578220122, 2347885320, 3)

    for _ in range(0, size):
        Procedural.make_transfer(accounts, 2347885320, 4578220122, 2)

    Procedural.clear_accounts(accounts)


def operation_objective(size):
    owner_fixtures = [
        OOP.Owner('Foo', 'Bar'),
        OOP.Owner('Foo', 'Baz')
    ]

    account_fixtures = [
        OOP.BankAccount(owner_fixtures[0], 4578220122),
        OOP.BankAccount(owner_fixtures[1], 2347885320),
        OOP.BankAccount(owner_fixtures[1], 1174559614)
    ]

    bank = OOP.Bank()
    bank.add_account(account_fixtures[0])
    bank.add_account(account_fixtures[1])
    bank.add_account(account_fixtures[2])

    for _ in range(0, size):
        bank.make_deposit(bank.get_account(4578220122), 5)
        bank.make_deposit(bank.get_account(2347885320), 5)

    for _ in range(0, size):
        bank.make_withdraw(bank.get_account(4578220122), 1)
        bank.make_withdraw(bank.get_account(2347885320), 1)

    for _ in range(0, size):
        bank.make_transfer(bank.get_account(4578220122), bank.get_account(2347885320), 3)

    for _ in range(0, size):
        bank.make_transfer(bank.get_account(2347885320), bank.get_account(4578220122), 2)


class Worker(QRunnable):
    def __init__(self, operation_type, operations_number):
        super(Worker, self).__init__()
        self.operation_type = operation_type
        self.operations_number = operations_number
        self.signals = WorkerSignals()

    def get_number_of_each_operation(self, number_of_operations):
        return int(number_of_operations / 4)

    def microseconds_to_miliseconds(self, time_micro):
        return time_micro / 1000

    @pyqtSlot()
    def run(self):
        try:
            each_operation_number = self.get_number_of_each_operation(self.operations_number)

            start_time = datetime.datetime.now()
            self.operation_type(each_operation_number)
            end_time = datetime.datetime.now()

            result = (self.microseconds_to_miliseconds((end_time - start_time).microseconds), self.operations_number)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class VerticalLabel(QLabel):
    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        painter.drawText(23, (self.width() / 2) + 4, self.text())
        painter.end()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
