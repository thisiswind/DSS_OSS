# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SECUIRTY_FILTER.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SECURITY_FILTER(object):
    def setupUi(self, SECURITY_FILTER):
        SECURITY_FILTER.setObjectName("SECURITY_FILTER")
        SECURITY_FILTER.resize(1267, 696)
        self.centralwidget = QtWidgets.QWidget(SECURITY_FILTER)
        self.centralwidget.setObjectName("centralwidget")
        self.OP_NAME = QtWidgets.QComboBox(self.centralwidget)
        self.OP_NAME.setGeometry(QtCore.QRect(50, 30, 211, 21))
        self.OP_NAME.setEditable(True)
        self.OP_NAME.setObjectName("OP_NAME")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 161, 16))
        self.label.setObjectName("label")
        self.RMT_FILTER_NAME = QtWidgets.QComboBox(self.centralwidget)
        self.RMT_FILTER_NAME.setGeometry(QtCore.QRect(50, 80, 501, 22))
        self.RMT_FILTER_NAME.setObjectName("RMT_FILTER_NAME")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 161, 16))
        self.label_3.setObjectName("label_3")
        self.FILTER_DESCRIPTION = QtWidgets.QTextEdit(self.centralwidget)
        self.FILTER_DESCRIPTION.setGeometry(QtCore.QRect(50, 130, 1081, 41))
        self.FILTER_DESCRIPTION.setObjectName("FILTER_DESCRIPTION")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 161, 16))
        self.label_4.setObjectName("label_4")
        self.TABLE_NAME_A = QtWidgets.QLineEdit(self.centralwidget)
        self.TABLE_NAME_A.setGeometry(QtCore.QRect(50, 210, 251, 21))
        self.TABLE_NAME_A.setObjectName("TABLE_NAME_A")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 240, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 190, 161, 16))
        self.label_6.setObjectName("label_6")
        self.REALMS = QtWidgets.QLineEdit(self.centralwidget)
        self.REALMS.setGeometry(QtCore.QRect(610, 30, 521, 21))
        self.REALMS.setObjectName("REALMS")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 10, 211, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(860, 60, 161, 16))
        self.label_8.setObjectName("label_8")
        self.FILTER_DIRECTION = QtWidgets.QLineEdit(self.centralwidget)
        self.FILTER_DIRECTION.setGeometry(QtCore.QRect(860, 80, 271, 21))
        self.FILTER_DIRECTION.setObjectName("FILTER_DIRECTION")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 60, 161, 16))
        self.label_9.setObjectName("label_9")
        self.FILTER_TYPE = QtWidgets.QLineEdit(self.centralwidget)
        self.FILTER_TYPE.setGeometry(QtCore.QRect(610, 80, 181, 21))
        self.FILTER_TYPE.setText("")
        self.FILTER_TYPE.setObjectName("FILTER_TYPE")
        self.KEY1_ALIAS_A = QtWidgets.QLineEdit(self.centralwidget)
        self.KEY1_ALIAS_A.setGeometry(QtCore.QRect(50, 260, 251, 21))
        self.KEY1_ALIAS_A.setObjectName("KEY1_ALIAS_A")
        self.TABLE_TYPE_A = QtWidgets.QLineEdit(self.centralwidget)
        self.TABLE_TYPE_A.setGeometry(QtCore.QRect(320, 210, 251, 21))
        self.TABLE_TYPE_A.setObjectName("TABLE_TYPE_A")
        self.KEY2_ALIAS_A = QtWidgets.QLineEdit(self.centralwidget)
        self.KEY2_ALIAS_A.setGeometry(QtCore.QRect(320, 260, 251, 21))
        self.KEY2_ALIAS_A.setObjectName("KEY2_ALIAS_A")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 240, 161, 16))
        self.label_10.setObjectName("label_10")
        self.VALUE_ALIAS_A = QtWidgets.QLineEdit(self.centralwidget)
        self.VALUE_ALIAS_A.setGeometry(QtCore.QRect(50, 310, 521, 21))
        self.VALUE_ALIAS_A.setObjectName("VALUE_ALIAS_A")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 290, 161, 16))
        self.label_11.setObjectName("label_11")
        self.KEY1_ALIAS_B = QtWidgets.QLineEdit(self.centralwidget)
        self.KEY1_ALIAS_B.setGeometry(QtCore.QRect(610, 260, 241, 21))
        self.KEY1_ALIAS_B.setObjectName("KEY1_ALIAS_B")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(610, 190, 161, 16))
        self.label_12.setObjectName("label_12")
        self.KEY2_ALIAS_B = QtWidgets.QLineEdit(self.centralwidget)
        self.KEY2_ALIAS_B.setGeometry(QtCore.QRect(870, 260, 261, 21))
        self.KEY2_ALIAS_B.setObjectName("KEY2_ALIAS_B")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(610, 240, 161, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(610, 290, 161, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(870, 190, 161, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(880, 240, 161, 16))
        self.label_16.setObjectName("label_16")
        self.TABLE_TYPE_B = QtWidgets.QLineEdit(self.centralwidget)
        self.TABLE_TYPE_B.setGeometry(QtCore.QRect(870, 210, 261, 21))
        self.TABLE_TYPE_B.setObjectName("TABLE_TYPE_B")
        self.VALUE_ALIAS_B = QtWidgets.QLineEdit(self.centralwidget)
        self.VALUE_ALIAS_B.setGeometry(QtCore.QRect(610, 310, 521, 21))
        self.VALUE_ALIAS_B.setObjectName("VALUE_ALIAS_B")
        self.TABLE_NAME_B = QtWidgets.QLineEdit(self.centralwidget)
        self.TABLE_NAME_B.setGeometry(QtCore.QRect(610, 210, 241, 21))
        self.TABLE_NAME_B.setObjectName("TABLE_NAME_B")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 350, 161, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 350, 161, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(50, 420, 41, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(50, 540, 161, 16))
        self.label_20.setObjectName("label_20")
        self.MAPCACHE_KEY = QtWidgets.QTextEdit(self.centralwidget)
        self.MAPCACHE_KEY.setGeometry(QtCore.QRect(50, 440, 251, 91))
        self.MAPCACHE_KEY.setObjectName("MAPCACHE_KEY")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(610, 350, 161, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(880, 350, 161, 16))
        self.label_22.setObjectName("label_22")
        self.TWO_D_LIST_VALUE1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TWO_D_LIST_VALUE1.setGeometry(QtCore.QRect(320, 440, 251, 91))
        self.TWO_D_LIST_VALUE1.setObjectName("TWO_D_LIST_VALUE1")
        self.TWO_D_MAP_KEY1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TWO_D_MAP_KEY1.setGeometry(QtCore.QRect(610, 440, 251, 71))
        self.TWO_D_MAP_KEY1.setObjectName("TWO_D_MAP_KEY1")
        self.LIST_VALUE = QtWidgets.QTextEdit(self.centralwidget)
        self.LIST_VALUE.setGeometry(QtCore.QRect(880, 440, 251, 211))
        self.LIST_VALUE.setObjectName("LIST_VALUE")
        self.MAPCACHE_VALUE = QtWidgets.QTextEdit(self.centralwidget)
        self.MAPCACHE_VALUE.setGeometry(QtCore.QRect(50, 560, 251, 91))
        self.MAPCACHE_VALUE.setObjectName("MAPCACHE_VALUE")
        self.TWO_D_LIST_VALUE2 = QtWidgets.QTextEdit(self.centralwidget)
        self.TWO_D_LIST_VALUE2.setGeometry(QtCore.QRect(320, 560, 251, 91))
        self.TWO_D_LIST_VALUE2.setObjectName("TWO_D_LIST_VALUE2")
        self.TWO_D_MAP_KEY2 = QtWidgets.QTextEdit(self.centralwidget)
        self.TWO_D_MAP_KEY2.setGeometry(QtCore.QRect(610, 530, 251, 71))
        self.TWO_D_MAP_KEY2.setObjectName("TWO_D_MAP_KEY2")
        self.MAP_REGION = QtWidgets.QComboBox(self.centralwidget)
        self.MAP_REGION.setGeometry(QtCore.QRect(50, 400, 51, 20))
        self.MAP_REGION.setObjectName("MAP_REGION")
        self.MAP_ADD = QtWidgets.QPushButton(self.centralwidget)
        self.MAP_ADD.setGeometry(QtCore.QRect(110, 400, 41, 20))
        self.MAP_ADD.setObjectName("MAP_ADD")
        self.MAP_RELOAD = QtWidgets.QPushButton(self.centralwidget)
        self.MAP_RELOAD.setGeometry(QtCore.QRect(160, 400, 41, 20))
        self.MAP_RELOAD.setObjectName("MAP_RELOAD")
        self.TOW_D_LIST_RELOAD = QtWidgets.QPushButton(self.centralwidget)
        self.TOW_D_LIST_RELOAD.setGeometry(QtCore.QRect(420, 400, 41, 20))
        self.TOW_D_LIST_RELOAD.setObjectName("TOW_D_LIST_RELOAD")
        self.TWO_D_LIST_REGION = QtWidgets.QComboBox(self.centralwidget)
        self.TWO_D_LIST_REGION.setGeometry(QtCore.QRect(320, 400, 51, 20))
        self.TWO_D_LIST_REGION.setObjectName("TWO_D_LIST_REGION")
        self.TWO_D_LIST_ADD = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_LIST_ADD.setGeometry(QtCore.QRect(380, 400, 31, 20))
        self.TWO_D_LIST_ADD.setObjectName("TWO_D_LIST_ADD")
        self.TWO_D_MAP_RELOAD = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_MAP_RELOAD.setGeometry(QtCore.QRect(710, 400, 41, 20))
        self.TWO_D_MAP_RELOAD.setObjectName("TWO_D_MAP_RELOAD")
        self.TWO_D_MAP_REGION = QtWidgets.QComboBox(self.centralwidget)
        self.TWO_D_MAP_REGION.setGeometry(QtCore.QRect(610, 400, 51, 20))
        self.TWO_D_MAP_REGION.setObjectName("TWO_D_MAP_REGION")
        self.TWO_D_MAP_ADD = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_MAP_ADD.setGeometry(QtCore.QRect(670, 400, 31, 20))
        self.TWO_D_MAP_ADD.setObjectName("TWO_D_MAP_ADD")
        self.LIST_RELOAD = QtWidgets.QPushButton(self.centralwidget)
        self.LIST_RELOAD.setGeometry(QtCore.QRect(980, 400, 41, 20))
        self.LIST_RELOAD.setObjectName("LIST_RELOAD")
        self.LIST_REGION = QtWidgets.QComboBox(self.centralwidget)
        self.LIST_REGION.setGeometry(QtCore.QRect(880, 400, 51, 20))
        self.LIST_REGION.setObjectName("LIST_REGION")
        self.LIST_ADD = QtWidgets.QPushButton(self.centralwidget)
        self.LIST_ADD.setGeometry(QtCore.QRect(940, 400, 31, 20))
        self.LIST_ADD.setObjectName("LIST_ADD")
        self.MAPCACHE = QtWidgets.QLineEdit(self.centralwidget)
        self.MAPCACHE.setGeometry(QtCore.QRect(50, 370, 251, 21))
        self.MAPCACHE.setObjectName("MAPCACHE")
        self.TWO_D_LISTCACHE = QtWidgets.QLineEdit(self.centralwidget)
        self.TWO_D_LISTCACHE.setGeometry(QtCore.QRect(320, 370, 251, 21))
        self.TWO_D_LISTCACHE.setObjectName("TWO_D_LISTCACHE")
        self.TWO_D_MAPCACHE = QtWidgets.QLineEdit(self.centralwidget)
        self.TWO_D_MAPCACHE.setGeometry(QtCore.QRect(610, 370, 251, 21))
        self.TWO_D_MAPCACHE.setObjectName("TWO_D_MAPCACHE")
        self.LISTCACHE = QtWidgets.QLineEdit(self.centralwidget)
        self.LISTCACHE.setGeometry(QtCore.QRect(880, 370, 251, 21))
        self.LISTCACHE.setObjectName("LISTCACHE")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(880, 420, 41, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(320, 420, 41, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(610, 420, 41, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(320, 540, 41, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(610, 510, 41, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(610, 610, 41, 16))
        self.label_28.setObjectName("label_28")
        self.TWO_D_MAP_VALUE = QtWidgets.QLineEdit(self.centralwidget)
        self.TWO_D_MAP_VALUE.setGeometry(QtCore.QRect(610, 630, 251, 21))
        self.TWO_D_MAP_VALUE.setObjectName("TWO_D_MAP_VALUE")
        self.MAP_CHECK = QtWidgets.QPushButton(self.centralwidget)
        self.MAP_CHECK.setGeometry(QtCore.QRect(210, 420, 91, 21))
        self.MAP_CHECK.setObjectName("MAP_CHECK")
        self.TWO_D_LIST_CHECK = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_LIST_CHECK.setGeometry(QtCore.QRect(470, 420, 101, 20))
        self.TWO_D_LIST_CHECK.setObjectName("TWO_D_LIST_CHECK")
        self.TWO_D_MAP_CHECK = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_MAP_CHECK.setGeometry(QtCore.QRect(760, 420, 101, 20))
        self.TWO_D_MAP_CHECK.setObjectName("TWO_D_MAP_CHECK")
        self.LIST_CHECK = QtWidgets.QPushButton(self.centralwidget)
        self.LIST_CHECK.setGeometry(QtCore.QRect(940, 420, 191, 20))
        self.LIST_CHECK.setObjectName("LIST_CHECK")
        self.IMSIS = QtWidgets.QLineEdit(self.centralwidget)
        self.IMSIS.setGeometry(QtCore.QRect(280, 30, 271, 21))
        self.IMSIS.setObjectName("IMSIS")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(280, 10, 211, 16))
        self.label_29.setObjectName("label_29")
        self.MAP_DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.MAP_DELETE.setGeometry(QtCore.QRect(210, 400, 91, 20))
        self.MAP_DELETE.setObjectName("MAP_DELETE")
        self.TWO_D_LIST_DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_LIST_DELETE.setGeometry(QtCore.QRect(470, 400, 101, 20))
        self.TWO_D_LIST_DELETE.setObjectName("TWO_D_LIST_DELETE")
        self.TWO_D_MAP_DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.TWO_D_MAP_DELETE.setGeometry(QtCore.QRect(760, 400, 101, 20))
        self.TWO_D_MAP_DELETE.setObjectName("TWO_D_MAP_DELETE")
        self.LIST_DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.LIST_DELETE.setGeometry(QtCore.QRect(1030, 400, 101, 20))
        self.LIST_DELETE.setObjectName("LIST_DELETE")
        SECURITY_FILTER.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SECURITY_FILTER)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 21))
        self.menubar.setObjectName("menubar")
        SECURITY_FILTER.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SECURITY_FILTER)
        self.statusbar.setObjectName("statusbar")
        SECURITY_FILTER.setStatusBar(self.statusbar)

        self.retranslateUi(SECURITY_FILTER)
        QtCore.QMetaObject.connectSlotsByName(SECURITY_FILTER)

    def retranslateUi(self, SECURITY_FILTER):
        _translate = QtCore.QCoreApplication.translate
        SECURITY_FILTER.setWindowTitle(_translate("SECURITY_FILTER", "MainWindow"))
        self.label.setText(_translate("SECURITY_FILTER", "Operator Name"))
        self.label_2.setText(_translate("SECURITY_FILTER", "Security Filter  Name in RMT"))
        self.label_3.setText(_translate("SECURITY_FILTER", "Security Filter Description"))
        self.label_4.setText(_translate("SECURITY_FILTER", "Table Name A"))
        self.label_5.setText(_translate("SECURITY_FILTER", "Key1 Alias A"))
        self.label_6.setText(_translate("SECURITY_FILTER", "Table Type A"))
        self.label_7.setText(_translate("SECURITY_FILTER", "Operator DRACustomerRealmName"))
        self.label_8.setText(_translate("SECURITY_FILTER", "Security Filter  Direction"))
        self.label_9.setText(_translate("SECURITY_FILTER", "Security Filter  Type"))
        self.label_10.setText(_translate("SECURITY_FILTER", "Key2 Alias A"))
        self.label_11.setText(_translate("SECURITY_FILTER", "Value Alias A"))
        self.label_12.setText(_translate("SECURITY_FILTER", "Table Name B"))
        self.label_13.setText(_translate("SECURITY_FILTER", "Key1 Alias B"))
        self.label_14.setText(_translate("SECURITY_FILTER", "Value Alias B"))
        self.label_15.setText(_translate("SECURITY_FILTER", "Table Type B"))
        self.label_16.setText(_translate("SECURITY_FILTER", "Key2 Alias B"))
        self.label_17.setText(_translate("SECURITY_FILTER", "MAPCACHE"))
        self.label_18.setText(_translate("SECURITY_FILTER", "2D_LISTCACHE"))
        self.label_19.setText(_translate("SECURITY_FILTER", "Keys"))
        self.label_20.setText(_translate("SECURITY_FILTER", "Values"))
        self.label_21.setText(_translate("SECURITY_FILTER", "2D_MAPCACHE"))
        self.label_22.setText(_translate("SECURITY_FILTER", "LISTCACHE"))
        self.MAP_ADD.setText(_translate("SECURITY_FILTER", "Add"))
        self.MAP_RELOAD.setText(_translate("SECURITY_FILTER", "Reload"))
        self.TOW_D_LIST_RELOAD.setText(_translate("SECURITY_FILTER", "Reload"))
        self.TWO_D_LIST_ADD.setText(_translate("SECURITY_FILTER", "Add"))
        self.TWO_D_MAP_RELOAD.setText(_translate("SECURITY_FILTER", "Reload"))
        self.TWO_D_MAP_ADD.setText(_translate("SECURITY_FILTER", "Add"))
        self.LIST_RELOAD.setText(_translate("SECURITY_FILTER", "Reload"))
        self.LIST_ADD.setText(_translate("SECURITY_FILTER", "Add"))
        self.label_23.setText(_translate("SECURITY_FILTER", "Values"))
        self.label_24.setText(_translate("SECURITY_FILTER", "Value1s"))
        self.label_25.setText(_translate("SECURITY_FILTER", "key1s"))
        self.label_26.setText(_translate("SECURITY_FILTER", "Value2s"))
        self.label_27.setText(_translate("SECURITY_FILTER", "key2s"))
        self.label_28.setText(_translate("SECURITY_FILTER", "Value"))
        self.MAP_CHECK.setText(_translate("SECURITY_FILTER", "Check by Keys"))
        self.TWO_D_LIST_CHECK.setText(_translate("SECURITY_FILTER", "Check by Value1s"))
        self.TWO_D_MAP_CHECK.setText(_translate("SECURITY_FILTER", "Check by Key1s"))
        self.LIST_CHECK.setText(_translate("SECURITY_FILTER", "Check by Values (Verify On)"))
        self.label_29.setText(_translate("SECURITY_FILTER", "Operator IMSI Prefix"))
        self.MAP_DELETE.setText(_translate("SECURITY_FILTER", "Delete"))
        self.TWO_D_LIST_DELETE.setText(_translate("SECURITY_FILTER", "Delete"))
        self.TWO_D_MAP_DELETE.setText(_translate("SECURITY_FILTER", "Delete"))
        self.LIST_DELETE.setText(_translate("SECURITY_FILTER", "Delete"))
