QSS = '''
QWidget#mainWindow {
    background-color: #A68B03;  /* Задаємо фон для головного вікна */
}

QWidget {
    font: 20px "Montserrat";  /* Встановлюємо шрифт для всіх віджетів */
}

QPushButton { 
    background-color: #5b8c5a;  /* Задаємо фон для кнопки */
    color: white;  /* Колір тексту на кнопці */
}

QPushButton:pressed {
    background-color: #9e93fc;  /* Задаємо фон кнопки, коли вона натиснута */
}

QListWidget {
    background-color: #8dfecc;  /* Задаємо фон для списку */
}

QListWidget::item:selected {
    background-color: #d9ffee;  /* Задаємо фон для вибраного елемента списку */
}
'''
