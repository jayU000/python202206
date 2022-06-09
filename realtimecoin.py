# API를 이용한 10개 코인 테이블 위젯 조회기

import sys                      # 시스템 접근 모듈
from PyQt5.QtWidgets import *   # ui의 widjet 접근 모듈
from PyQt5 import uic           # ui 사용 모듈
import pybithumb                # 빗썸 코인 조회 API
import pykorbit                 # 빗썸 코인 조회 API
from PyQt5.QtCore import *      # 타이머
from PyQt5.QtGui import QIcon

form_class = uic.loadUiType("coinprice.ui")[0] # [0] 꼭 입력
tickers = ['BTC', 'ETH', 'XRP', 'ADA', 'LTC', 'KLAY', 'TRX', 'DOGE', 'EOS', 'ZIL']

class MyWindow(QMainWindow, form_class):
    def __init__(self):      # 생성자
        super().__init__()   # 부모의 생성자 사용
        self.setupUi(self)   # ui 활성화
        self.setWindowIcon(QIcon('web.png'))

        self.timer = QTimer(self)
        self.timer.start(2000)              # 2초
        self.timer.timeout.connect(self.btn_clicked)
        #단추를 클릭하지 않아도 특정 시간마다 자동으로 호출


    # 단추를 클릭할 때 연결되어 실행되는 메서드
    def btn_clicked(self) :
        for i, ticker in enumerate(tickers) :
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)
                                #   행, 열, 넣을 값 
            pri = str(pybithumb.get_current_price(ticker))
            price = QTableWidgetItem(pri)

            # 강사님 코드
            # pri = pybithumb.get_current_price(ticker)
            # price = QTableWidgetItem(str(pri))
            self.tableWidget.setItem(i, 1, price)

            pri = str(pykorbit.get_current_price(ticker))
            price = QTableWidgetItem(pri)
            self.tableWidget.setItem(i, 2, price)


app = QApplication(sys.argv) # 창 객체 생성
window = MyWindow()          # 창 생성
window.show()                # 창 띄우기
app.exec_()                  # 창 계속 유지


# 윈도우 앱 만들기
# .py와 .ui를 한 폴더에 위치시킨다.

# pyinstaller 를 설치 

# pyinstaller --noconsole --onefile realtimecoin.py



