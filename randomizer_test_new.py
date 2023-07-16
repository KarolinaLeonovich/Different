import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QRadioButton, QHBoxLayout, QButtonGroup
import random

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.sex = ("Мужской", "Женский")
                self.race = ('Люди', 'Азари', 'Волусы', 'Саларианцы', 'Турианцы', 'Жнецы', 'Ханары', 'Элкоры', 'Кроганы', 'Батарианцы', 'Искусственный интеллект', 'Кварианцы', 'Рахни', 'ВИ', 'Коллекционеры', 'Дреллы', 'Геты', 'Яги', 'Варрены', 'Ворка', 'Молотильщики')
                self.setWindowTitle("Randomiser")
                self.resize(500, 150)
                self.line1 = QLineEdit(self)
                self.btnPress1 = QPushButton("start")
                self.line = QLineEdit(self)
                self.line2 = QLineEdit(self)
                self.radio1 = QRadioButton("Гет+слеш", self)
                self.radio1.setChecked(True)
                self.radio2 = QRadioButton("Только гет", self)
                self.radio3 = QRadioButton("Только слеш", self)
                self.radio4 = QRadioButton("Только фемслеш", self)
                layout = QVBoxLayout()
                layout.addWidget(self.radio1)
                layout.addWidget(self.radio2)
                layout.addWidget(self.radio3)
                layout.addWidget(self.radio4)
                layout.addWidget(self.line1)
                layout.addWidget(self.btnPress1)
                layout.addWidget(self.line)
                layout.addWidget(self.line2)
                layout.addStretch()
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)

        def file_reading(self):
                file1 = open("ME_Char_Sex_Race_all.txt", "r")
                self.a = []
                while True:
                        line = file1.readline()
                        if not line:
                                break
                        self.pure = line.strip()
                        self.res = self.pure.split(",")
                        if self.res not in self.a:
                                self.a.append(self.res)
                file1.close()
                return self.a

        def radio_func(self):
                characters_array = self.file_reading()
                if self.radio1.isChecked():
                        self.char1 = random.choice(characters_array)
                        self.char2 = random.choice(characters_array)
                elif self.radio2.isChecked():
                        self.char1 = random.choice([i for i in characters_array if i[1] == "Мужской"])
                        self.char2 = random.choice([i for i in characters_array if i[1] == "Женский"])
                elif self.radio3.isChecked():
                        characters_array_men = [i for i in characters_array if i[1] == "Мужской"]
                        self.char1 = random.choice(characters_array_men)
                        self.char2 = random.choice(characters_array_men)
                elif self.radio4.isChecked():
                        characters_array_women = [i for i in characters_array if i[1] == "Женский"]
                        self.char1 = random.choice(characters_array_women)
                        self.char2 = random.choice(characters_array_women)
                return [self.char1, self.char2]

        def btnPress1_Clicked(self):
                result = self.radio_func()
                self.line1.setText(f"{result[0][0]}/{result[1][0]}")
                self.line.setText(f"https://masseffect.fandom.com/ru/wiki/{result[0][0]}")
                self.line2.setText(f"https://masseffect.fandom.com/ru/wiki/{result[1][0]}")


if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())
