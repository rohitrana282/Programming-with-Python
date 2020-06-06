# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'booklist1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

book=sqlite3.connect("m5assignment.db")
curbook=book.cursor()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 265)
        self.l1 = QtWidgets.QLabel(Form)
        self.l1.setGeometry(QtCore.QRect(80, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(160, 60, 113, 20))
        self.t1.setObjectName("t1")
        self.p1 = QtWidgets.QPushButton(Form)
        self.p1.setGeometry(QtCore.QRect(300, 60, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.p1.setFont(font)
        self.p1.setObjectName("p1")
        self.p1.clicked.connect(self.findprice)
        self.l2 = QtWidgets.QLabel(Form)
        self.l2.setGeometry(QtCore.QRect(80, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l2.setObjectName("l2")
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.t2.setObjectName("t2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(120, 140, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.l3 = QtWidgets.QLabel(Form)
        self.l3.setGeometry(QtCore.QRect(80, 160, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLabel(Form)
        self.l4.setGeometry(QtCore.QRect(80, 190, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l4.setFont(font)
        self.l4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l4.setObjectName("l4")
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setGeometry(QtCore.QRect(160, 160, 113, 20))
        self.t3.setObjectName("t3")
        self.p2 = QtWidgets.QPushButton(Form)
        self.p2.setGeometry(QtCore.QRect(300, 160, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.p2.setFont(font)
        self.p2.setObjectName("p2")
        self.p2.clicked.connect(self.totalprice)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setGeometry(QtCore.QRect(160, 190, 113, 20))
        self.t4.setObjectName("t4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l1.setText(_translate("Form", "Book Title"))
        self.p1.setText(_translate("Form", "Find Price"))
        self.l2.setText(_translate("Form", "Price"))
        
        self.l3.setText(_translate("Form", "Quantity"))
        self.l4.setText(_translate("Form", "Total"))
        self.p2.setText(_translate("Form", "Find Total"))
        

    def findprice(self):
        b=self.t1.text()
        sql="SELECT * FROM books WHERE title='"+b+"';"
        curbook.execute(sql)
        rec=curbook.fetchone()
        if rec!=None:
            self.t2.setText('Rs. '+ str(rec[3]))
        else:
            self.t2.setText('Book Unavailable!!!')
            print("Book is not found...")

    def totalprice(self):
        b=self.t1.text()
        q=self.t3.text()
        sql="SELECT * FROM books WHERE title='"+b+"';"
        curbook.execute(sql)
        rec=curbook.fetchone()
        if rec!=None:
            totl=rec[3]*int(q)
            self.t4.setText('Rs. '+ str(totl))
        else:
            self.t4.setText('Book Unavailable!!!')
            print("Book is not found...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
