from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit
import random

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("Randomiser")
                self.resize(500, 150)
                self.line1 = QLineEdit(self)
                self.btnPress1 = QPushButton("start")
                self.line = QLineEdit(self)
                self.line2 = QLineEdit(self)
                layout = QVBoxLayout()
                layout.addWidget(self.line1)
                layout.addWidget(self.btnPress1)
                layout.addWidget(self.line)
                layout.addWidget(self.line2)
                layout.addStretch()
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)

                file1 = open("MEchar1.txt", "r", encoding="utf8")
                self.a = []
                while True:
                        line = file1.readline()
                        if not line:
                                break
                        self.a.append(line.strip())
                file1.close
                self.b = set(self.a)
                self.a = list(self.b)

        def btnPress1_Clicked(self):
            self.char1 = random.choice(self.a)
            self.char2 = random.choice(self.a)
            self.line1.setText(f"{self.char1}/{self.char2}")
            self.line.setText(f"https://masseffect.fandom.com/ru/wiki/{self.char1}")
            self.line2.setText(f"https://masseffect.fandom.com/ru/wiki/{self.char2}")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())
