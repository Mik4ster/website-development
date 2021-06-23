import sys
import platform
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import json

from main_ui import *
from show_orders import *

widgets = None


class MyMain(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global widgets

        widgets = self.ui

        self.json_string = {}
        self.read_data()
        self.user = None
        self.printFun()

        widgets.action.triggered.connect(self.printFun)
        widgets.action_2.triggered.connect(self.printFun)
        widgets.action_3.triggered.connect(self.printFun)
        widgets.action_5.triggered.connect(self.printFun)

        widgets.tableWidget_2.itemDoubleClicked.connect(self.show_orders)

        widgets.tableWidget.itemDoubleClicked.connect(self.del_order)

        widgets.but_auth.clicked.connect(self.auth)

        widgets.submit.clicked.connect(self.add_order)

        self.show()
    
    def add_order(self):
        name = widgets.name_site.text()
        desc = widgets.desc.toPlainText()
        site_view = None
        design = None
        if widgets.site_view1.isChecked():
            site_view = "Landing"
        elif widgets.site_view2.isChecked():
            site_view = "Multi-page"
        if widgets.design.checkState() == 2:
            design = "True"
        elif widgets.design.checkState() == 0:
            design = "False"
        price = widgets.price.text()
        term = widgets.term.text()
        if name != "" and desc != "" and site_view != None and design != None and price != "" and term != "":
            new_order = {
                "name": name,
                "desc": desc,
                "site view": site_view,
                "design": design,
                "price": price,
                "term": term
            }
            self.json_string[self.user]["orders"].append(new_order)

            widgets.term.clear()
            widgets.price.clear()
            widgets.name_site.clear()
            widgets.desc.clear()

            self.write_data()
        else:
            self.mbox("Не все данные введены!")


    def show_orders(self):
        self.read_data()
        if widgets.tableWidget_2.currentColumn() == 0:
            row = widgets.tableWidget_2.currentRow()
            order = self.json_string[row]["orders"]
            self.wo = Order(order)
            self.wo.show()

    def del_order(self):
        ans = self.mbox_2()
        if ans == 1024:
            row = widgets.tableWidget.currentRow()
            ind = 0
            p = False
            for tup in self.json_string:
                for ind1 in range(len(tup["orders"])):
                    if ind == row:
                        tup["orders"].pop(ind1)
                        p = True
                        break
                    ind += 1
                if p:
                    break
            self.write_data()
            self.printFun()
                    
                    
        

    def printFun(self):
        btn = self.sender()
        if self.user == None:
            widgets.stackedWidget.setCurrentWidget(widgets.auth)
            widgets.menubar.setVisible(False)
        else:
            self.read_data()
            widgets.menubar.setVisible(True)
            if btn.objectName() == "action":
                widgets.stackedWidget.setCurrentWidget(widgets.all_users)
                widgets.tableWidget_2.setRowCount(len(self.json_string))
                row = 0
                for tup in self.json_string:
                    col = 0
                    for item in tup:
                        if item != "rights" and item != "password" and item != "orders":
                            cel = QTableWidgetItem(tup[item])
                            if item == "login":
                                cel.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                            else:
                                cel.setFlags(QtCore.Qt.ItemIsEnabled)
                            widgets.tableWidget_2.setItem(row, col, cel)
                            col += 1        
                    row += 1

            elif btn.objectName() == "action_2":
                self.read_data()
                widgets.stackedWidget.setCurrentWidget(widgets.all_orders)
                rows = 0
                for tup in self.json_string:
                    rows += len(tup["orders"])
                widgets.tableWidget.setRowCount(rows)
                row = 0
                for tup in self.json_string:
                    if len(tup["orders"]) != 0:
                        for order in tup["orders"]:
                            col = 0
                            for key, value in order.items():
                                cel = QTableWidgetItem(value)
                                cel.setFlags(QtCore.Qt.ItemIsEnabled)
                                widgets.tableWidget.setItem(row, col, cel)
                                col += 1
                            row += 1
            elif btn.objectName() == "action_5":
                self.read_data()
                widgets.stackedWidget.setCurrentWidget(widgets.order)
            else:
                self.read_data()
                widgets.stackedWidget.setCurrentWidget(widgets.profile)
                rows = len(self.json_string[self.user]["orders"])
                widgets.tableWidget_3.setRowCount(rows)
                row = 0
                col = 0
                for order in self.json_string[self.user]["orders"]:
                    col = 0
                    for key, value in order.items():
                        cel = QTableWidgetItem(value)
                        cel.setFlags(QtCore.Qt.ItemIsEnabled)
                        widgets.tableWidget_3.setItem(row, col, cel)
                        col += 1
                    row += 1
                

    def auth(self):
        login = widgets.auth_login.text()
        password = widgets.auth_pass.text()
        index = 0
        auth_sucsess = False
        for i in self.json_string:
            if login==i["login"] and password==i["password"]:
                self.user = index
                widgets.label_1.setText(i["name"])
                widgets.label_2.setText(i["birthday"])
                widgets.label_3.setText(i["phone"])
                widgets.label_4.setText(i["email"])
                auth_sucsess = True
                break
            index += 1
        if not auth_sucsess:
            self.mbox("Логин или пароль введены не верно!")
        self.printFun()
        

    def read_data(self):
        with open("data.json") as file:
            data = file.read()
        self.json_string = json.loads(data)

    def write_data(self):
        with open("data.json", "w") as file:
            json.dump(self.json_string, file)

    def mbox(self, body, title='Ошибка!'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()
    
    def mbox_2(self, body = "Вы уверены что хотите удалить заказ?", title='Ошибка!'):
        dialog = QMessageBox(QMessageBox.Question, title, body)
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return dialog.exec_()
    

class Order(QtWidgets.QWidget):
    def __init__(self, orders):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.tableWidget228.setRowCount(len(orders))

        self.ui.tableWidget228.itemDoubleClicked.connect(self.show_orders)

        row = 0
        col = 0
        if len(orders) != 0:
            for order in orders:
                col = 0
                for key, value in order.items():
                    cel = QTableWidgetItem(value)
                    cel.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget228.setItem(row, col, cel)
                    col += 1
                row += 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyMain()
    sys.exit(app.exec_())
