from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

def answer():
    

    app2 = QApplication([])
    main_win2 = QWidget()

    main_win2.resize(400,300)
    main_win2.move(460, 280)

    main_win2.setWindowTitle('АНКЕТА АБІТУРІЄНТА(ЗАВЕРШЕНА)')
    
    dani = QLabel("Ваші дані збережено, очікуйте дзвінка а бо посилання на e-mail(З нашим вирішеням)")
    
    but2 = QPushButton('OK')

    line_v2 = QVBoxLayout()

    line_v2.addWidget(dani, alignment = Qt.AlignCenter)
    line_v2.addWidget(but2, alignment = Qt.AlignCenter)
    
    main_win2.setLayout(line_v2)

    but2.clicked.connect(quit)

    main_win2.show()
    app2.exec_()

answer()