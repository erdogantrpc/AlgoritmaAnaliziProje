from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QDesktopWidget, QCheckBox, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QIcon, QCursor
from PyQt5 import Qt
from PyQt5 import QtCore

import sys
import math
import random
import time

class CountingSort(QWidget):
    def __init__(self, minRange = 0, maxRange = 10000, uret = 1000):
        super().__init__()
        self.minRange = int(minRange)
        self.maxRange = int(maxRange)
        self.uret = int(uret)
        self.setUI()
    
    def setUI(self):
        self.Sayilar = []
        self.sayiUret(self.uret)
        global count
        self.count = 0

        self.algorithm = QLabel(self)
        self.algorithm.move(370,10)
        self.algorithm.setText("Kullanılan Algoritma: Quick Sort")
        self.algorithm.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.label = QLabel(self)
        self.label.setText("Kullanılan Dizi: ")
        self.label.move(10,50)
        self.label.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.kullanilanDizi = QPlainTextEdit(self)
        self.kullanilanDizi.setGeometry(150,50,790,150)
        self.kullanilanDizi.insertPlainText(str(self.Sayilar))
        self.kullanilanDizi.setStyleSheet("background-color: #000066;border-style: outset;color: white;border-color: white;border-width: 2px;border-radius: 10px;font: bold 14px;")
        self.kullanilanDizi.setReadOnly(True)

        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("Sonuclar")
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.setGeometry(self.centerPoint.x() - 475, self.centerPoint.y() - 225,950,450)
        self.setMinimumSize(QSize(950,450))
        self.setMaximumSize(QSize(950,450))
        self.setStyleSheet("background-color: #000066")

        self.hesapla()
        
    def sayiUret(self, x):
        for a in range(x):
            EklenecekSayi = random.randint(self.minRange, self.maxRange)
            self.Sayilar.append(EklenecekSayi)

    def hesapla(self):
        self.BaslamaZamani = time.time()
        self.sirali = self.countingSort(self.Sayilar, max(self.Sayilar))
        self.BitisZamani = time.time()
        self.zaman = self.BitisZamani-self.BaslamaZamani

        self.label2 = QLabel(self)
        self.label2.setText("Sıralanmış Hali: ")
        self.label2.move(10,210)
        self.label2.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.siralananDizi = QPlainTextEdit(self)
        self.siralananDizi.setGeometry(150,210,790,150)
        self.siralananDizi.insertPlainText(str(self.sirali))
        self.siralananDizi.setStyleSheet("background-color: #000066;border-style: outset;color: white;border-color: white;border-width: 2px;border-radius: 10px;font: bold 14px;")
        self.siralananDizi.setReadOnly(True)

        self.adimSayisi = QLabel(self)
        self.adimSayisi.move(370,370)
        self.adimSayisi.move(345,370)
        self.adimSayisi.setText(f"Sıralama için yapılan işlem sayısı:  {self.count}")
        self.adimSayisi.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.sure = QLabel(self)
        self.sure.move(325,390)
        self.sure.setText("Algoritmanın çalışma süresi: {:.8f} saniye".format(self.zaman))
        self.sure.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

    def countingSort(self, sayilar, enBuyukDeger):
        m = enBuyukDeger + 1
        count = [0] * m
        i = 0
        for a in sayilar:
            self.count += 1
            count[a] += 1
        for a in range(m):
            self.count += 1
            for c in range(count[a]):
                self.count += 1
                sayilar[i] = a
                i += 1
        return sayilar
