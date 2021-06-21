# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gateways.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
#
# __Author__ Yuule


from PyQt5 import QtCore, QtGui, QtWidgets

import socket
import CRC8
from toast import Toast
import time
import os
import binascii


class Ui_Form(object):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_list = ''
    port = 20215
    buffersize = 1024
    msg = 'REQUEST'
    ip_port = ('', port)
    data_list = [[]]
    server_addr_list = [[]]

    SynHEAD = 'GWCF' #同步字
    ProtocalVER = '1' #协议版本
    PayloadLEN = '0' #负载长度
    CRC = '0' #crc校验

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 522)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FindGWCB = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FindGWCB.setFont(font)
        self.FindGWCB.setObjectName("FindGWCB")
        self.FindGWCB.addItem("")
        self.horizontalLayout.addWidget(self.FindGWCB)
        self.FindGWBTN = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FindGWBTN.setFont(font)
        self.FindGWBTN.setObjectName("FindGWBTN")
        self.horizontalLayout.addWidget(self.FindGWBTN)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.FunctionLB = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.FunctionLB.setFont(font)
        self.FunctionLB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FunctionLB.setAutoFillBackground(True)
        self.FunctionLB.setTextFormat(QtCore.Qt.AutoText)
        self.FunctionLB.setAlignment(QtCore.Qt.AlignCenter)
        self.FunctionLB.setObjectName("FunctionLB")
        self.gridLayout.addWidget(self.FunctionLB, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.FirmwaveED = QtWidgets.QLineEdit(self.tab)
        self.FirmwaveED.setEnabled(True)
        self.FirmwaveED.setReadOnly(True)
        self.FirmwaveED.setObjectName("FirmwaveED")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FirmwaveED)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.HardwareED = QtWidgets.QLineEdit(self.tab)
        self.HardwareED.setEnabled(True)
        self.HardwareED.setReadOnly(True)
        self.HardwareED.setObjectName("HardwareED")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.HardwareED)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.MACED = QtWidgets.QLineEdit(self.tab)
        self.MACED.setReadOnly(True)
        self.MACED.setObjectName("MACED")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.MACED)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.SerialED = QtWidgets.QLineEdit(self.tab)
        self.SerialED.setDragEnabled(False)
        self.SerialED.setReadOnly(True)
        self.SerialED.setObjectName("SerialED")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SerialED)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.IPAED = QtWidgets.QLineEdit(self.tab)
        self.IPAED.setReadOnly(True)
        self.IPAED.setObjectName("IPAED")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.IPAED)
        self.dial = QtWidgets.QDial(self.tab)
        self.dial.setMaximum(360)
        self.dial.setObjectName("dial")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.dial)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.DHCPCB = QtWidgets.QComboBox(self.groupBox_3)
        self.DHCPCB.setObjectName("DHCPCB")
        self.DHCPCB.addItem("")
        self.DHCPCB.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DHCPCB)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.IPED = QtWidgets.QLineEdit(self.groupBox_3)
        self.IPED.setObjectName("IPED")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.IPED)
        self.GatewayED = QtWidgets.QLineEdit(self.groupBox_3)
        self.GatewayED.setObjectName("GatewayED")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GatewayED)
        self.NetmaskED = QtWidgets.QLineEdit(self.groupBox_3)
        self.NetmaskED.setObjectName("NetmaskED")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.NetmaskED)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.WireSecurityCB = QtWidgets.QComboBox(self.groupBox_2)
        self.WireSecurityCB.setObjectName("WireSecurityCB")
        self.WireSecurityCB.addItem("")
        self.WireSecurityCB.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.WireSecurityCB)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_13)
        self.WifiSSIDED = QtWidgets.QLineEdit(self.groupBox_2)
        self.WifiSSIDED.setObjectName("WifiSSIDED")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.WifiSSIDED)
        self.WifikeyED = QtWidgets.QLineEdit(self.groupBox_2)
        self.WifikeyED.setObjectName("WifikeyED")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.WifikeyED)
        self.OpenWifiCK = QtWidgets.QCheckBox(self.groupBox_2)
        self.OpenWifiCK.setText("")
        self.OpenWifiCK.setObjectName("OpenWifiCK")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.OpenWifiCK)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.NetworkBTN = QtWidgets.QPushButton(self.tab_2)
        self.NetworkBTN.setObjectName("NetworkBTN")
        self.gridLayout_2.addWidget(self.NetworkBTN, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setObjectName("label_21")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.RSSIFLCB = QtWidgets.QComboBox(self.groupBox_5)
        self.RSSIFLCB.setObjectName("RSSIFLCB")
        self.RSSIFLCB.addItems(("Default","1m","3m","5m","10m","15m"))
        self.RSSIFLCB.setCurrentIndex(0)
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.RSSIFLCB)
        self.AdvFLCB = QtWidgets.QComboBox(self.groupBox_5)
        self.AdvFLCB.setObjectName("AdvFLCB")
        self.AdvFLCB.addItems(("Allow All Advertising Data","iBeacon only","Eddystone UID only","Eddystone URL only"))
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AdvFLCB)
        self.DupliFLCB = QtWidgets.QComboBox(self.groupBox_5)
        self.DupliFLCB.setObjectName("DupliFLCB")
        self.DupliFLCB.addItems(("No","Yes"))
        self.DupliFLCB.setCurrentIndex(0)
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DupliFLCB)
        self.AutoRSTCB = QtWidgets.QComboBox(self.groupBox_5)
        self.AutoRSTCB.setObjectName("AutoRSTCB")
        self.AutoRSTCB.addItems(("Disable","1h","2h","3h","4h","6h","8h","12h","24h"))
        self.AutoRSTCB.setCurrentIndex(0)
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.AutoRSTCB)
        self.ReqIntvSB = QtWidgets.QSpinBox(self.groupBox_5)
        self.ReqIntvSB.setMinimum(1)
        self.ReqIntvSB.setMaximum(10)
        self.ReqIntvSB.setObjectName("ReqIntvSB")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ReqIntvSB)
        self.gridLayout_3.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.ConnTypeCB = QtWidgets.QComboBox(self.groupBox_4)
        self.ConnTypeCB.setObjectName("ConnTypeCB")
        self.ConnTypeCB.addItems(("WebSocket Client","HTTP Client","MQTT Client"))
        self.ConnTypeCB.setCurrentIndex(2)
        # self.ConnTypeCB.currentText()
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ConnTypeCB)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.HostED = QtWidgets.QLineEdit(self.groupBox_4)
        self.HostED.setObjectName("HostED")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.HostED)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.PortED = QtWidgets.QLineEdit(self.groupBox_4)
        self.PortED.setObjectName("PortED")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PortED)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.URIED = QtWidgets.QLineEdit(self.groupBox_4)
        self.URIED.setObjectName("URIED")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.URIED)

        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.UsrNameED = QtWidgets.QLineEdit(self.groupBox_4)
        self.UsrNameED.setObjectName("UsrNameED")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.UsrNameED)
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setObjectName("label_27")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.PssWordED = QtWidgets.QLineEdit(self.groupBox_4)
        self.PssWordED.setObjectName("PssWordED")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.PssWordED)

        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.ApplicationBTN = QtWidgets.QPushButton(self.tab_3)
        self.ApplicationBTN.setObjectName("ApplicationBTN")
        self.gridLayout_3.addWidget(self.ApplicationBTN, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayout_6 = QtWidgets.QFormLayout(self.tab_4)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.OTAupdateBTN = QtWidgets.QPushButton(self.tab_4)
        self.OTAupdateBTN.setObjectName("OTAupdateBTN")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.OTAupdateBTN)
        self.OTARSTBTN = QtWidgets.QPushButton(self.tab_4)
        self.OTARSTBTN.setObjectName("OTARSTBTN")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.OTARSTBTN)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowIcon(QtGui.QIcon("./BLElogoxx.png"))
        # func
        self.FindGWBTN_onclik()
        self.NetworkBTN_setting()
        self.AppBTN_setting()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BLM Gataways v1.0.2"))
        self.groupBox.setTitle(_translate("Form", "Gateways:"))
        self.FindGWCB.setItemText(0, _translate("Form", "Find Gateways"))
        self.FindGWBTN.setText(_translate("Form", "Reload"))
        self.FunctionLB.setText(_translate("Form", "Dashboard"))
        self.label_2.setText(_translate("Form", "Firmware Version："))
        self.label_3.setText(_translate("Form", "Hardware Version："))
        self.label_4.setText(_translate("Form", "MAC："))
        self.label_5.setText(_translate("Form", "Serial Number："))
        self.label_6.setText(_translate("Form", "IP Address："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Dashboard"))
        self.groupBox_3.setTitle(_translate("Form", "Ethernet Setting"))
        self.label_9.setText(_translate("Form", "DHCP"))
        self.DHCPCB.setItemText(1,_translate("Form", "Enable"))
        self.DHCPCB.setItemText(0, _translate("Form", "Disable"))
        self.label_10.setText(_translate("Form", "IP"))
        self.label_23.setText(_translate("Form", "Gateway"))
        self.label_24.setText(_translate("Form", "Netmask"))
        self.groupBox_2.setTitle(_translate("Form", "WiFi Station Setting"))
        self.WireSecurityCB.setItemText(0, _translate("Form", "WPA-PSK/WPA2-PSK"))
        self.WireSecurityCB.setItemText(1, _translate("Form", "WPA2-Enterprise"))
        self.label_7.setText(_translate("Form", "Wireless Security"))
        self.label_8.setText(_translate("Form", "Wi-Fi SSID"))
        self.label_11.setText(_translate("Form", "Security Key"))
        self.label_12.setText(_translate("Form", "Open Wi-Fi Network"))
        self.label_13.setText(_translate("Form", "* WPA2 Enterprise is only available for firmware version >= 1.2.0"))
        self.NetworkBTN.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Network"))
        self.label_16.setText(_translate("Form", "Req Interval/s"))
        self.label_17.setText(_translate("Form", "RSSI Filter"))
        self.label_20.setText(_translate("Form", "Advertising Filter"))
        self.label_21.setText(_translate("Form", "Duplicate Filter"))
        self.label_22.setText(_translate("Form", "Auto Restart"))
        self.label_14.setText(_translate("Form", "Connection Type"))
        self.label_15.setText(_translate("Form", "Host"))
        self.label_18.setText(_translate("Form", "Port"))
        self.label_19.setText(_translate("Form", "URI/Topic"))
        self.label_26.setText(_translate("Form", "UsrName"))
        self.label_27.setText(_translate("Form", "PssWord"))

        self.ApplicationBTN.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Application"))
        self.label_25.setText(_translate("Form", "OTA Firmware Update"))
        self.OTAupdateBTN.setText(_translate("Form", "Update"))
        self.OTARSTBTN.setText(_translate("Form", "Restart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Advanced"))


    def FindGWBTN_onclik(self):

        def cao():
            toast = Toast()
            toast.make_text(QtCore.QPointF(900, 600), "Waiting...", 2.5)

            data = [0, 0, 0]
            idx = 0
            for i in range(231, 235, 1):
                try:
                    ''' search client ip '''
                    self.ip_list = '192.168.1.' + str(i)
                    print(' ', self.ip_list)

                    # ip_port = ('192.168.1.232', 20215)
                    self.client.sendto(self.msg.encode('utf-8'), (self.ip_list, self.port))
                    # self.client.sendto((b'REQUEST'), (self.ip_list, self.port))

                    self.client.settimeout(0.2)
                    data, server_addr = self.client.recvfrom(self.buffersize)
                    print(type(data), type(server_addr), data, server_addr, type(data[0]))

                except IOError as e:
                    print(e)
                finally:
                    if (data[0] == ord('R') and data[1] == ord('S') and data[2] == ord('P')):
                        self.ip_port = (self.ip_list, self.port)
                        self.data_list[idx] = data
                        self.server_addr_list[idx] = server_addr
                        idx+=1
                        print('idx:',idx)
                        print('IP_PORT IS Okay.')
                        print("recvform:", server_addr, 'data:', data)

                        self.FindGWCB.addItem(server_addr[0])
                        self.FindGWCB_choose(data, server_addr)
                        self.DHCP_choose()
                        self.APP_choose()

                        data, server_addr = b'0', (0, 0)
                    pass
                if (i == 254):
                    print('please restart.')
            pass
        self.FindGWBTN.clicked.connect(cao)

        pass

    def FindGWCB_choose(self, data, server_addr):
        print('FindGWCB_choose IS Okay.')
        def cao():
            self.FirmwaveED.setText(str(data[3:8].decode('utf-8')))
            self.HardwareED.setText(str(data[8:13].decode('utf-8')))
            self.MACED.setText(bytes.hex(data[13:19]))
            self.SerialED.setText(str(data[19:31].decode('utf-8')))
            self.IPAED.setText(server_addr[0])
            pass

        self.FindGWCB.currentTextChanged.connect(cao)
        pass

    def NetworkBTN_setting(self):
        msgTYPE = '1' #报文类型

        def cao():
            networkHead = self.SynHEAD + self.ProtocalVER + msgTYPE #CRC
            network_setstr = ''
            data = ''
            # print('checkbox:', type(self.OpenWifiCK.checkState()),self.OpenWifiCK.checkState(), type(self.OpenWifiCK.isChecked(), self.OpenWifiCK.isChecked()))
            print('currentidx:', type(self.WireSecurityCB.currentIndex()),self.WireSecurityCB.currentIndex())
            ''' Wifi Station Setting '''
            if(self.OpenWifiCK.isChecked()):
                network_setstr = network_setstr + '1'
            else:
                network_setstr = network_setstr + '0'
            network_setstr = network_setstr + str(self.WireSecurityCB.currentIndex()) + str(len(self.WifiSSIDED.text())) + '+' +self.WifiSSIDED.text() + str(len(self.WifikeyED.text())) + '+' +self.WifikeyED.text()
            print('1, ',network_setstr)
            if(self.DHCPCB.currentIndex() == 0):
                print('enter DHCP.')
                ''' Ethernet Setting '''
                network_net = ':' +str(self.DHCPCB.currentIndex()) + str(len(self.IPED.text())) + '+' + self.IPED.text() + str(len(self.GatewayED.text())) + '+' + self.GatewayED.text() + str(len(self.NetmaskED.text())) + '+' + self.NetmaskED.text()
                self.PayloadLEN = str(len(network_setstr) + len(network_net))
                networkHead = networkHead + self.PayloadLEN
                network_setstr = networkHead + network_setstr + network_net
                print('2, ', network_setstr, type(network_setstr))
                network_encode = network_setstr.encode('utf-8')
                networkcrc = CRC8.crc8(network_encode).to_bytes(1, byteorder='little', signed=False)
                self.client.sendto(
                    network_encode + networkcrc,
                    (self.ip_list, self.port))
                self.client.settimeout(1)

                ''' Need to handle Rsp. '''
                data, server_addr = self.client.recvfrom(self.buffersize)
                print(type(data), type(server_addr), data, server_addr)


            else:
                # self.IPED.setReadOnly(True)
                # self.GatewayED.setReadOnly(True)
                # self.NetmaskED.setReadOnly(True)
                ''' Ethernet Setting '''
                network_net = ':' + str(self.DHCPCB.currentIndex())
                self.PayloadLEN = str(len(network_setstr) + len(network_net))
                networkHead = networkHead + self.PayloadLEN
                network_setstr = networkHead + network_setstr + network_net
                print('3, ', network_setstr, type(network_setstr))
                network_encode = network_setstr.encode('utf-8')
                networkcrc = CRC8.crc8(network_encode).to_bytes(1, byteorder='little', signed=False)
                self.client.sendto(
                    network_encode + networkcrc,
                    (self.ip_list, self.port))

                ''' Need to handle Rsp. '''
                data, server_addr = self.client.recvfrom(self.buffersize)
                print(type(data), type(server_addr), data, server_addr)


                pass

            pass
        self.NetworkBTN.clicked.connect(cao)
        pass

    def DHCP_choose(self):

        def cao():
            if(self.DHCPCB.currentIndex() == 0):
                self.IPED.setReadOnly(False)
                self.GatewayED.setReadOnly(False)
                self.NetmaskED.setReadOnly(False)
            else:
                self.IPED.setText('')
                self.GatewayED.setText('')
                self.NetmaskED.setText('')
                self.IPED.setReadOnly(True)
                self.GatewayED.setReadOnly(True)
                self.NetmaskED.setReadOnly(True)
            pass
        self.DHCPCB.currentTextChanged.connect(cao)
        pass

    def AppBTN_setting(self):
        msgTYPE = '2'  # 报文类型

        def cao():
            appHead = self.SynHEAD + self.ProtocalVER + msgTYPE #CRC
            app_server = ''
            app_msg = ''
            app_setstr = ''

            if(self.ConnTypeCB.currentIndex() == 0):
                app_server = '0' + str(len(self.HostED.text())) + '+' + self.HostED.text() + str(len(self.PortED.text())) + '+' + self.PortED.text() + str(len(self.URIED.text())) + '+' + self.URIED.text()
                if(self.ReqIntvSB.text() != '10'):
                    app_msg = self.ReqIntvSB.text() + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                else:
                    app_msg = '0' + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                app_setstr = app_server + ':' + app_msg
                pass

            elif(self.ConnTypeCB.currentIndex() == 1):
                app_server = '1' + str(len(self.HostED.text())) + '+' + self.HostED.text() + str(len(self.PortED.text())) + '+' + self.PortED.text() + str(len(self.URIED.text())) + '+' + self.URIED.text()
                if(self.ReqIntvSB.text() != '10'):
                    app_msg = self.ReqIntvSB.text() + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                else:
                    app_msg = '0' + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                app_setstr = app_server + ':' + app_msg
                pass

            elif(self.ConnTypeCB.currentIndex() == 2):
                app_server = '2' + str(len(self.HostED.text())) + '+' + self.HostED.text() + str(len(self.PortED.text())) + '+' + self.PortED.text() + str(len(self.URIED.text())) + '+' + self.URIED.text()
                if(self.ReqIntvSB.text() != '10'):
                    app_msg = self.ReqIntvSB.text() + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                else:
                    app_msg = '0' + str(self.RSSIFLCB.currentIndex()) + str(
                        self.AdvFLCB.currentIndex()) + str(self.DupliFLCB.currentIndex()) + str(
                        self.AutoRSTCB.currentIndex())
                app_setstr = app_server + ':' + app_msg
                pass
            print('app setting:',app_setstr)
            self.PayloadLEN = str(len(app_setstr))
            appHead = appHead + self.PayloadLEN
            app_setstr = appHead + app_setstr
            app_encode = app_setstr.encode('utf-8')
            app_crc = CRC8.crc8(app_encode).to_bytes(1, byteorder='little', signed=False)
            self.client.sendto(
                app_encode + app_crc,
                (self.ip_list, self.port))

            ''' Need to handle Rsp. '''
            data, server_addr = self.client.recvfrom(self.buffersize)
            print(type(data), type(server_addr), data, server_addr)

            pass

        self.ApplicationBTN.clicked.connect(cao)
        pass

    def APP_choose(self):

        def cao():
            if(self.ConnTypeCB.currentIndex() == 2):
                self.UsrNameED.setReadOnly(False)
                self.PssWordED.setReadOnly(False)
            else:
                self.UsrNameED.setText('')
                self.PssWordED.setText('')
                self.UsrNameED.setReadOnly(True)
                self.PssWordED.setReadOnly(True)
            pass
        self.ConnTypeCB.currentTextChanged.connect(cao)
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()


    sys.exit(app.exec_())

    pass