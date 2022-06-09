# 3대 음원 사이트 순위 조회 프로그램

# API를 이용한 10개 코인 테이블 위젯 조회기

import sys                      # 시스템 접근 모듈
from PyQt5.QtWidgets import *   # ui의 widjet 접근 모듈
from PyQt5 import uic           # ui 사용 모듈
import pybithumb                # 빗썸 코인 조회 API
import pykorbit                 # 빗썸 코인 조회 API
from PyQt5.QtCore import *      # 타이머
from PyQt5.QtGui import QIcon

import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Chrome('chromedriver.exe')

form_class = uic.loadUiType("chart.ui")[0] # [0] 꼭 입력
tickers = ['BTC', 'ETH', 'XRP', 'ADA', 'LTC', 'KLAY', 'TRX', 'DOGE', 'EOS', 'ZIL']

class MyWindow(QMainWindow, form_class):
    def __init__(self):      # 생성자
        super().__init__()   # 부모의 생성자 사용
        self.setupUi(self)   # ui 활성화
        self.setWindowIcon(QIcon('web.png'))

        self.pushButton.clicked.connect(self.btn_clicked1)
        self.pushButton_2.clicked.connect(self.btn_clicked2)
        self.pushButton_3.clicked.connect(self.btn_clicked3)


    # btn_clicked1 호출되는 메서드 벅스
    def btn_clicked1(self) :

        response = requests.get('https://music.bugs.co.kr/chart')   # 분석할 웹 페이지 가져오기
        soup = bs(response.text)                                    # 가져온 소스에 bs 정제

        songs = soup.select('table.list.trackList.byChart > tbody > tr')


        for i, song in enumerate(songs) :                     
            ran = song.select('div.ranking > strong')[0].text
            titl = song.select('p.title > a')[0].text
            singe = song.select('p.artist > a')[0].text

            service = QTableWidgetItem("bugs")
            rank = QTableWidgetItem(ran)
            title = QTableWidgetItem(titl)
            singer = QTableWidgetItem(singe)

            self.tableWidget.setItem(i, 0, service)
            self.tableWidget.setItem(i, 1, rank)
            self.tableWidget.setItem(i, 2, title)
            self.tableWidget.setItem(i, 3, singer)


    # btn_clicked2 호출되는 메서드 멜론
    def btn_clicked2(self) :
        driver.get('https://www.melon.com/chart/index.htm')
        response = driver.page_source
        soup = bs(response)

        songs = soup.select('tr.lst50')
        songs2 = soup.select('tr.lst100')

        for i, song in enumerate(songs) :
            titl = song.select('div.ellipsis > span > a')[0].text
            singe = song.select('div.ellipsis > a')[0].text
            ran = song.select('span.rank')[0].text

            service = QTableWidgetItem("Melon")
            rank = QTableWidgetItem(ran)
            title = QTableWidgetItem(titl)
            singer = QTableWidgetItem(singe)

            self.tableWidget.setItem(i, 0, service)
            self.tableWidget.setItem(i, 1, rank)
            self.tableWidget.setItem(i, 2, title)
            self.tableWidget.setItem(i, 3, singer)

        for i, song in enumerate(songs2) :
            titl = song.select('div.ellipsis > span > a')[0].text
            singe = song.select('div.ellipsis > a')[0].text
            ran = song.select('span.rank')[0].text

            service = QTableWidgetItem("Melon")
            rank = QTableWidgetItem(ran)
            title = QTableWidgetItem(titl)
            singer = QTableWidgetItem(singe)

            self.tableWidget.setItem(50 + i, 0, service)
            self.tableWidget.setItem(50 + i, 1, rank)
            self.tableWidget.setItem(50 + i, 2, title)
            self.tableWidget.setItem(50 + i, 3, singer)



    # btn_clicked1 호출되는 메서드 지니
    def btn_clicked3(self) :
        driver.get('https://www.genie.co.kr/chart/top200')
        response = driver.page_source

        soup = bs(response)
        songs = soup.select('tr.list')

        for i, song in enumerate(songs) :
            titl = song.select('a.title')[0].text.split('\n')[-1].strip()
            singe = song.select('a.artist')[0].text
            ran = song.select('td.number')[0].text.split('\n')[0]

            service = QTableWidgetItem("Genie")
            rank = QTableWidgetItem(ran)
            title = QTableWidgetItem(titl)
            singer = QTableWidgetItem(singe)

            self.tableWidget.setItem(i, 0, service)
            self.tableWidget.setItem(i, 1, rank)
            self.tableWidget.setItem(i, 2, title)
            self.tableWidget.setItem(i, 3, singer)

        page2 = driver.find_element_by_css_selector('div.rank-page-nav > a:nth-child(2)')
        page2.click()

        time.sleep(2)
        response = driver.page_source
        
        soup = bs(response)
        songs = soup.select('tr.list')
        
        for i, song in enumerate(songs) :
            titl = song.select('a.title')[0].text.split('\n')[-1].strip()
            singe = song.select('a.artist')[0].text
            ran = song.select('td.number')[0].text.split('\n')[0]

            service = QTableWidgetItem("Genie")
            rank = QTableWidgetItem(ran)
            title = QTableWidgetItem(titl)
            singer = QTableWidgetItem(singe)

            self.tableWidget.setItem(50+i, 0, service)
            self.tableWidget.setItem(50+i, 1, rank)
            self.tableWidget.setItem(50+i, 2, title)
            self.tableWidget.setItem(50+i, 3, singer)
        



app = QApplication(sys.argv) # 창 객체 생성
window = MyWindow()          # 창 생성
window.show()                # 창 띄우기
app.exec_()                  # 창 계속 유지


# pyinstaller --noconsole --onefile movie.py
# 위 명령어를 터미널에 입력해서 윈도우 어플 만들기
