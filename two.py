from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

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

