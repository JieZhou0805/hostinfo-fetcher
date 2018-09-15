#! coding:utf-8
import sys
import ctypes
import os
import getpass  # for current username
import psutil
import pyqt5_gui as gui
import subprocess


if sys.version > "4":
    PY_VER = None
elif sys.version > "3":
    PY_VER = 3
elif sys.version > "2":
    PY_VER = 2
else:
    PY_VER = None

from PyQt5.QtCore import QTimer, Qt, QEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPainter, QColor, QBrush
from PyQt5 import sip



class Transparent_Window(QWidget):
    
    def __init__(self):
        
        super(Transparent_Window, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.ui = gui.Ui_Form()
        self.ui.setupUi(self)

        # Timer
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.refresh_contents)
        self.refresh_timer.start(10000)

        self.refresh_contents()
        
        # Systray
        self.create_systray()
        self.tray_icon.show()

        self.ui.label_Drag.setAttribute(
            Qt.WA_TransparentForMouseEvents
        )

        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
        )

        self.show()

        
    def create_systray(self):

        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(
            QAction("Show on top", self, triggered=self.activateWindow)
        )

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.png'))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.activated.connect(self.activateWindow)
        

    def get_printer_name(self):

        if sys.platform == 'win32':
            
            try:
                printer_name_raw = subprocess.check_output('wmic printer get name', creationflags=0x08000000).decode()
            except subprocess.CalledProcessError:
                return 'No printer found'
            
            printer_name_list = printer_name_raw.split('\r\r\n')

            printer_name_str = str()
            for elem in printer_name_list:
            
                # Ignore useless info
                if elem == '':
                    continue
                elif elem[0:4] == 'Name' or elem[0:4] == 'Micr':
                    continue

                printer_name_str += elem + '<br>'

            # Remove the last '<br>' for better output
            printer_name_str = printer_name_str[0:len(printer_name_str)-4]
            
            return printer_name_str

        else:
            return str()


    def get_network_info(self, target):

        if target == 'card':

            result = str()
            for element in self.get_netcard():

                # Ignore invaild pairing
                if element[1][0:7] == '169.254':
                    continue
                
                result += (element[0] + '<br>')
                
            # Remove the last '<br>' for better display
            result = result[0:len(result)-4]
            
            return result

        elif target == 'ip':

            result = str()
            for element in self.get_netcard():

                # Ignore invaild pairing
                if element[1][0:7] == '169.254':
                    continue

                result += (element[1] + '<br>')

            # Remove the last '<br>' for better display
            result = result[0:len(result)-4]    
                
            return result
    
        
    def refresh_contents(self):

        computer_name = "<font color=white>" + self.get_computer_name() + "</font>"
        user_name = "<font color=white>" + getpass.getuser() + "</font>"
        network_adapter_name = "<font color=white>" + self.get_network_info('card') + "</font>"
        ip_address = "<font color=white>" + self.get_network_info('ip') + "</font>"
        printer_name = "<font color=white>" + self.get_printer_name() + "</font>"

        self.ui.label_ComputerName_2.setText(computer_name)
        self.ui.label_CurrentUser_2.setText(user_name)
        self.ui.label_CurrentUser_7.setText(network_adapter_name)
        self.ui.label_CurrentUser_8.setText(ip_address)
        self.ui.label_CurrentUser_6.setText(printer_name)
        
        
    def paintEvent(self, event):
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(QBrush(QColor(0, 0, 0, 210)))
        qp.setPen(Qt.transparent)
        window_rect = self.rect()
        window_rect.setWidth(window_rect.width() - 1)
        window_rect.setHeight(window_rect.height() - 1)
        qp.drawRoundedRect(window_rect, 15, 15)
        # qp.fillRect(self.rect(), QColor(0, 0, 0, 180));  #QColor最后一个参数80代表背景的透明度

        
    def mousePressEvent(self, event):
        
        print("mousePressEvent")
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            print(self.dragPosition)
            QApplication.postEvent(self, QEvent(174))
            # event.accept()
            

    def mouseMoveEvent(self, event):
        
        # self.move(event.globalPos());
        print("mouseMoveEvent")
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


    # 获取计算机名
    def get_computer_name(self):
        
        if sys.platform == 'win32':
            pcName = ctypes.c_char_p("".encode("utf-8"))
            pcSize = 16
            pcName = ctypes.cast(pcName, ctypes.c_char_p)
            try:
                ctypes.windll.kernel32.GetComputerNameA(
                    pcName, ctypes.byref(ctypes.c_int(pcSize))
                )
            except Exception:
                print("Sth wrong in getname!")
                
            return pcName.value.decode("utf-8")

        elif sys.platform == 'linux':
            hostname = check_output('hostname').decode()
            
            # Remove the '\n' at the end of string
            hostname = hostname[:-1]
        
            return hostname


    # 获取网卡名称和其ip地址，不包括回环
    def get_netcard(self):
        netcard_info = []
        status = psutil.net_if_stats()
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == "127.0.0.1":
                    netcard_info.append((k, item[1]))
                    
        return netcard_info

            

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    transparent_window = Transparent_Window()  # will execute show()
    # transparent_window.showFullScreen()
    exit_val = app.exec_()  # Execute app
    sys.exit(exit_val)
