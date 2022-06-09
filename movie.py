import sys                      # 시스템 접근 모듈
from PyQt5.QtWidgets import *   # ui의 widjet 접근 모듈
from PyQt5 import uic           # ui 사용 모듈
from PyQt5.QtCore import *      # 타이머
from PyQt5.QtGui import QIcon

import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Chrome('chromedriver.exe')

form_class = uic.loadUiType("movie.ui")[0] # [0] 꼭 입력

class MyWindow(QMainWindow, form_class):
    def __init__(self):      # 생성자
        super().__init__()   # 부모의 생성자 사용
        self.setupUi(self)   # ui 활성화
        self.setWindowIcon(QIcon('web.png'))

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self) :
        driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220608')

        response = driver.page_source
        soup = bs(response)

        movies = soup.select('td.title')
        points = soup.select('td.point')

        ran = 1

        for i in range(len(movies)):
            titl = movies[i].text.strip()
            poin = points[i].text.strip()

            rank = QTableWidgetItem(str(ran))
            title = QTableWidgetItem(titl)
            point = QTableWidgetItem(poin)

            self.tableWidget.setItem(i, 0, rank)
            self.tableWidget.setItem(i, 1, title)
            self.tableWidget.setItem(i, 2, point)

            ran += 1

app = QApplication(sys.argv) # 창 객체 생성
window = MyWindow()          # 창 생성
window.show()                # 창 띄우기
app.exec_()                  # 창 계속 유지


# pyinstaller --noconsole --onefile movie.py
# 위 명령어를 터미널에 입력해서 윈도우 어플 만들기

