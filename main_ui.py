# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.styleSheet = QtWidgets.QFrame(self.centralwidget)
        self.styleSheet.setStyleSheet("")
        self.styleSheet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.styleSheet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.styleSheet.setObjectName("styleSheet")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.styleSheet)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.styleSheet)
        self.stackedWidget.setObjectName("stackedWidget")
        self.all_users = QtWidgets.QWidget()
        self.all_users.setObjectName("all_users")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.all_users)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.all_users)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.stackedWidget.addWidget(self.all_users)
        self.all_orders = QtWidgets.QWidget()
        self.all_orders.setObjectName("all_orders")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.all_orders)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.all_orders)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.all_orders)
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.gridLayout = QtWidgets.QGridLayout(self.profile)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.profile)
        self.frame.setMinimumSize(QtCore.QSize(0, 120))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 1, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.profile)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget_3, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.profile)
        self.order = QtWidgets.QWidget()
        self.order.setObjectName("order")
        self.site_view1 = QtWidgets.QRadioButton(self.order)
        self.site_view1.setGeometry(QtCore.QRect(0, 290, 82, 17))
        self.site_view1.setObjectName("site_view1")
        self.site_view2 = QtWidgets.QRadioButton(self.order)
        self.site_view2.setGeometry(QtCore.QRect(80, 290, 151, 17))
        self.site_view2.setObjectName("site_view2")
        self.name_site = QtWidgets.QLineEdit(self.order)
        self.name_site.setGeometry(QtCore.QRect(0, 20, 251, 20))
        self.name_site.setObjectName("name_site")
        self.label_10 = QtWidgets.QLabel(self.order)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 111, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.order)
        self.label_11.setGeometry(QtCore.QRect(0, 50, 101, 16))
        self.label_11.setObjectName("label_11")
        self.design = QtWidgets.QCheckBox(self.order)
        self.design.setGeometry(QtCore.QRect(0, 330, 241, 17))
        self.design.setObjectName("design")
        self.label_12 = QtWidgets.QLabel(self.order)
        self.label_12.setGeometry(QtCore.QRect(0, 450, 291, 16))
        self.label_12.setObjectName("label_12")
        self.line = QtWidgets.QFrame(self.order)
        self.line.setGeometry(QtCore.QRect(0, 350, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.order)
        self.line_2.setGeometry(QtCore.QRect(0, 310, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.order)
        self.line_3.setGeometry(QtCore.QRect(0, 270, 771, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.desc = QtWidgets.QTextEdit(self.order)
        self.desc.setGeometry(QtCore.QRect(0, 80, 421, 191))
        self.desc.setObjectName("desc")
        self.term = QtWidgets.QLineEdit(self.order)
        self.term.setGeometry(QtCore.QRect(0, 480, 171, 20))
        self.term.setObjectName("term")
        self.line_4 = QtWidgets.QFrame(self.order)
        self.line_4.setGeometry(QtCore.QRect(0, 430, 771, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_13 = QtWidgets.QLabel(self.order)
        self.label_13.setGeometry(QtCore.QRect(0, 370, 271, 16))
        self.label_13.setObjectName("label_13")
        self.price = QtWidgets.QLineEdit(self.order)
        self.price.setGeometry(QtCore.QRect(0, 400, 171, 20))
        self.price.setObjectName("price")
        self.submit = QtWidgets.QPushButton(self.order)
        self.submit.setGeometry(QtCore.QRect(664, 492, 91, 41))
        self.submit.setObjectName("submit")
        self.stackedWidget.addWidget(self.order)
        self.auth = QtWidgets.QWidget()
        self.auth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.auth.setObjectName("auth")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.auth)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.auth)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.auth_login = QtWidgets.QLineEdit(self.frame_3)
        self.auth_login.setObjectName("auth_login")
        self.verticalLayout_5.addWidget(self.auth_login)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.auth_pass = QtWidgets.QLineEdit(self.frame_3)
        self.auth_pass.setObjectName("auth_pass")
        self.verticalLayout_5.addWidget(self.auth_pass)
        self.but_auth = QtWidgets.QPushButton(self.frame_3)
        self.but_auth.setObjectName("but_auth")
        self.verticalLayout_5.addWidget(self.but_auth)
        self.verticalLayout_4.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.auth)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.styleSheet)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setChecked(False)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????????"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "???????? ????????????????"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "???????????????? ??????????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "?????? ??????????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "???????? ???? ????????????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "???????? ????"))
        self.label_5.setText(_translate("MainWindow", "??????"))
        self.label_6.setText(_translate("MainWindow", "???????? ??????????????"))
        self.label_7.setText(_translate("MainWindow", "??????????????"))
        self.label_8.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "???????????????? ??????????"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????????????"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "?????? ??????????"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "???????? ???? ????????????"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "???????? ????"))
        self.site_view1.setText(_translate("MainWindow", "??????????????"))
        self.site_view2.setText(_translate("MainWindow", "?????????????????????????????? ????????"))
        self.label_10.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.label_11.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.design.setText(_translate("MainWindow", "???????? ???? ?? ?????? ?????? ?????????????? ???????????? ?????????????"))
        self.label_12.setText(_translate("MainWindow", "?????????? ?????????????????????? ???????? ????????????? (??????????????: 2 ????????????)"))
        self.label_13.setText(_translate("MainWindow", "???? ?????????? ?????????? ????????????????????????? (??????????????: 5000 ??????)"))
        self.submit.setText(_translate("MainWindow", "????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.label_9.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.but_auth.setText(_translate("MainWindow", "??????????"))
        self.menu.setTitle(_translate("MainWindow", "??????????????????????????"))
        self.menu_2.setTitle(_translate("MainWindow", "????????????????????????"))
        self.action.setText(_translate("MainWindow", "???????????? ??????????????????????????"))
        self.action_2.setText(_translate("MainWindow", "???????????? ??????????????"))
        self.action_3.setText(_translate("MainWindow", "?????? ??????????????"))
        self.action_4.setText(_translate("MainWindow", "?????? ????????????"))
        self.action_5.setText(_translate("MainWindow", "????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
