
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup)
from random import (shuffle, randint)


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Португалии?', 'Португальский', 'Английский', 'Французский', 'Испанский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

button = QPushButton('Ответить')

text = QLabel('Какой национальности не существует?')

radio_group_box = QGroupBox('Варианты ответов')

radio_button1 = QRadioButton('')
radio_button2 = QRadioButton('')
radio_button3 = QRadioButton('')
radio_button4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(radio_button1)
RadioGroup.addButton(radio_button2)
RadioGroup.addButton(radio_button3)
RadioGroup.addButton(radio_button4)

HLine = QHBoxLayout()
VLine1 = QVBoxLayout()
VLine2 = QVBoxLayout()

VLine1.addWidget(radio_button1)
VLine1.addWidget(radio_button2)
VLine2.addWidget(radio_button3)
VLine2.addWidget(radio_button4)

HLine.addLayout(VLine1)
HLine.addLayout(VLine2)

radio_group_box.setLayout(HLine)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

ans_vline1 = QVBoxLayout()
ans_vline1.addWidget(lb_Result)
ans_vline1.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_vline1)

HLine1 = QHBoxLayout()
HLine2 = QHBoxLayout()
HLine3 = QHBoxLayout()

HLine1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
HLine2.addWidget(radio_group_box)
HLine2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

HLine3.addStretch(1)
HLine3.addWidget(button, stretch=2)
HLine3.addStretch(1)

VLine3 = QVBoxLayout()

VLine3.addLayout(HLine1)
VLine3.addLayout(HLine2)
VLine3.addLayout(HLine3)

main_win.setLayout(VLine3)

def show_result():
    radio_group_box.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    radio_group_box.show()
    AnsGroupBox.hide()
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    radio_button1.setChecked(False)
    radio_button2.setChecked(False)
    radio_button3.setChecked(False)
    radio_button4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [radio_button1, radio_button2, radio_button3, radio_button4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    lb_Result.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Correct.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total * 100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
            print('Рейтинг:', main_win.score/main_win.total * 100, '%')

main_win.cur_question = -1

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total * 100, '%')
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]

def click_on():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

q = Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
ask(q)
button.clicked.connect(click_on)

main_win.score = 0
main_win.total = 0

next_question()

AnsGroupBox.hide()

main_win.resize(400, 300)
main_win.show()
app.exec_()