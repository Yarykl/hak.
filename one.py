#We add libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from datetime import datetime
import time



def confirmation(): 
    def exitt():
        main_win.hide()

    edit_day_text=int(edit_day.text())
    edit_month_text=int(edit_month.text())
    edit_year_text=int(edit_year.text())
    year1 = year-edit_year_text
    if year1 > 16:
        text.setText('Ваша вікова категорія підходить')
        butt = QPushButton('продовжити')
        line_v.addWidget(butt, alignment = Qt.AlignCenter)
        butt.clicked.connect(exitt)
    elif year1 == 16:
        if month > edit_month_text:
            text.setText('Ваша вікова категорія підходить')
            butt = QPushButton('продовжити')
            line_v.addWidget(butt, alignment = Qt.AlignCenter)
            butt.clicked.connect(exitt)
        elif  month == edit_month_text:
            if day >= edit_day_text:
                text.setText('Ваша вікова категорія підходить')
                butt = QPushButton('продовжити')
                line_v.addWidget(butt, alignment = Qt.AlignCenter)
                butt.clicked.connect(exitt)
            else:
                text.setText('Вибачте але ваша вікова категорія не підходить')
                butt2 = QPushButton('продовжити')
                line_v.addWidget(butt2, alignment = Qt.AlignCenter)
                butt2.clicked.connect(quit)
        else:
            text.setText('Вибачте але ваша вікова категорія не підходить')
            butt2 = QPushButton('продовжити')
            line_v.addWidget(butt2, alignment = Qt.AlignCenter)
            butt2.clicked.connect(quit)  
    else:
        text.setText('Вибачте але ваша вікова категорія не підходить')
        butt2 = QPushButton('продовжити')
        line_v.addWidget(butt2, alignment = Qt.AlignCenter)
        butt2.clicked.connect(quit)

def questionnaire():
    def continuation():
        def exitt1():
            main_win1.hide()

        dani.setText('Ваші дані збережено')
        butt1 = QPushButton('Продовжити')
        line_v1.addWidget(butt1, alignment = Qt.AlignCenter)
        butt1.clicked.connect(exitt1)

    app1 = QApplication([])
    main_win1 = QWidget()

    main_win1.resize(400,300)
    main_win1.move(460, 280)

    main_win1.setWindowTitle('АНКЕТА АБІТУРІЄНТА')
    
    dani = QLabel("Ваші дані")
    name = QLabel("Ваше прізвище, ім'я та по-батькові")
    live = QLabel("Домашня адреса (Область, район, місто/село)")
    gmail = QLabel("Ваш e-mail")
    number = QLabel("Номер телефону")
    surroundings = QLabel("Розкажіть про себе(Ваші уподобання, хобі, коло інтересів)")

    but1 = QPushButton('Підтвердити')

    name_l = QLineEdit()
    live_l = QLineEdit()
    gmail_l = QLineEdit()
    number_l = QLineEdit()
    surroundings_l = QLineEdit()

    line_v1 = QVBoxLayout()

    line_v1.addWidget(dani, alignment = Qt.AlignCenter)
    line_v1.addWidget(name, alignment = Qt.AlignCenter)
    line_v1.addWidget(name_l, alignment = Qt.AlignCenter)
    line_v1.addWidget(live, alignment = Qt.AlignCenter)
    line_v1.addWidget(live_l, alignment = Qt.AlignCenter)
    line_v1.addWidget(gmail, alignment = Qt.AlignCenter)
    line_v1.addWidget(gmail_l, alignment = Qt.AlignCenter)
    line_v1.addWidget(number, alignment = Qt.AlignCenter)
    line_v1.addWidget(number_l, alignment = Qt.AlignCenter)
    line_v1.addWidget(surroundings, alignment = Qt.AlignCenter)
    line_v1.addWidget(surroundings_l, alignment = Qt.AlignCenter)
    line_v1.addWidget(but1, alignment = Qt.AlignCenter)

    main_win1.setLayout(line_v1)

    but1.clicked.connect(continuation)

    main_win1.show()
    app1.exec_()

questionnaire()

#Let's take the current time
date = datetime.now()

year = date.year
month = date.month
day = date.day

#We create "application" and "window" objects
app = QApplication([])
main_win = QWidget()

#Window dimensions and location coordinates
main_win.resize(400,300)
main_win.move(460, 280)

#Interface name
main_win.setWindowTitle('АНКЕТА АБІТУРІЄНТА')



#Text widgets
text = QLabel('Ведіть свою дату народження')
day_1 = QLabel('Чісло')
month_1 = QLabel('Місяць')
year_1 = QLabel('Рік')

#input strings
edit_day = QLineEdit('')
edit_month = QLineEdit('')
edit_year = QLineEdit('')

#
but = QPushButton('Підтвердити')
butt = QPushButton('продовжити')

#We create vertical and horizontal lines
line_v = QVBoxLayout()
line_h = QHBoxLayout()
line_h1 = QHBoxLayout()


line_v.addWidget(text, alignment = Qt.AlignCenter)
line_h1.addWidget(day_1, alignment = Qt.AlignLeft)
line_h1.addWidget(month_1, alignment = Qt.AlignLeft)
line_h1.addWidget(year_1, alignment = Qt.AlignLeft)
line_v.addLayout(line_h1)
line_h.addWidget(edit_day, alignment = Qt.AlignLeft)
line_h.addWidget(edit_month, alignment = Qt.AlignCenter)
line_h.addWidget(edit_year, alignment = Qt.AlignRight)
line_v.addLayout(line_h)
line_v.addWidget(but, alignment = Qt.AlignCenter)

main_win.setLayout(line_v)
#We make the window visible and leave the program open until the exit button is pressed

but.clicked.connect(confirmation)

main_win.show()
app.exec_()