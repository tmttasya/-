import sqlite3
import aspose.words as aw
from PyQt6.QtCore import Qt

from PyQt6.QtSql import QSqlTableModel
from PyQt6.QtWidgets import *

from connection import Data
from авторизация import Ui_Form as Ui_Form1
from стол import Ui_Form as Ui_Form2
from заказ import Ui_Form as Ui_Form3
from регистрация import Ui_Form as Ui_Form4

class Zakaz(QWidget):
    def __init__(self, parent=None):
        super(Zakaz, self).__init__()
        self.parent = parent

        self.ui = Ui_Form3()
        self.ui.setupUi(self)
        self.conn = Data()

        db = sqlite3.connect('restoranDB.db')
        self.cur = db.cursor()

        self.sto = self.parent.st
        risk = self.sto
        print(risk)
        print(f'self.sto ---> {self.parent.st}')
        self.name_kasir = self.parent.kasir
        print(f'self.name_kasir ---> {self.name_kasir}')

        self.view_data(stol_id=self.sto)
        self.reload_data()

        self.ui.label_6.setText(self.sto)
        self.ui.label_7.setText(self.name_kasir)
        self.ui.pushButton_2.clicked.connect(self.krok_madam)
        self.ui.pushButton.clicked.connect(self.tartar)
        self.ui.pushButton_3.clicked.connect(self.nisyaz)
        self.ui.pushButton_4.clicked.connect(self.ratatyu)
        self.ui.pushButton_5.clicked.connect(self.petux)
        self.ui.pushButton_6.clicked.connect(self.byaybes)
        self.ui.pushButton_12.clicked.connect(self.lyk)
        self.ui.pushButton_8.clicked.connect(self.kith)
        self.ui.pushButton_7.clicked.connect(self.klafyri)
        self.ui.pushButton_13.clicked.connect(self.wine)
        self.ui.pushButton_9.clicked.connect(self.oplata)
        self.ui.pushButton_11.clicked.connect(self.exit)
        self.ui.pushButton_10.clicked.connect(self.delete_current_transaction)
    def reload_data(self):
        table = self.sto
        self.a = self.conn.total_balance(table)
        self.ui.label_2.setText(self.conn.total_balance(table))

    def get_sto(self):
        return self.sto

    def view_data(self, stol_id=None):
        self.model = QSqlTableModel(self)
        self.model.setTable('zakaz')

        # Если передано значение для фильтра, применить его
        if stol_id is not None:
            self.model.setFilter(f"Стол_ID = {stol_id}")

        self.model.select()
        self.ui.tableView.setModel(self.model)
    def krok_madam(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 1").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 1").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 1").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def tartar(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 2").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 2").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 2").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def nisyaz(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 3").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 3").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 3").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def ratatyu(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 4").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 4").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 4").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def petux(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 5").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 5").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 5").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def byaybes(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 6").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 6").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 6").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def lyk(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 7").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 7").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 7").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def kith(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 8").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 8").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 8").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def klafyri(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 9").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 9").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 9").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def wine(self):
        Name_x = self.cur.execute("SELECT [Название блюда] FROM menu WHERE id = 10").fetchone()
        Name = ' '.join(Name_x)
        Razdel_x = self.cur.execute("SELECT Категория FROM menu WHERE id = 10").fetchone()
        Razdel = Razdel_x[0]
        Price_x = self.cur.execute("SELECT Цена FROM menu WHERE id = 10").fetchone()
        Price = Price_x[0]
        Stol = self.sto

        self.conn.add_new_transaction_query(Name, Razdel, Price, Stol)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def oplata(self, table):
        # Создайте новый документ
        QMessageBox.information(self, 'Оплачено!', "Счет успешно оплачен!")
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Добавьте информацию о номере стола и кассире
        builder.write(f'Номер стола - {self.sto}\n')
        builder.write(f'Кассир - {self.name_kasir}\n')
        builder.write("Id\tНаименование    Раздел  Цена руб  Номер стола\n\n")

            # Получаем количество строк после сортировки
        row_count = self.model.rowCount()

            # Добавляем данные из таблицы в документ
        for row in range(row_count):
            row_data = []
            for column in range(self.model.columnCount()):
                data = self.model.data(self.model.index(row, column))
                row_data.append(data)
            builder.writeln('\t'.join(map(str, row_data)))  # Используем табуляцию для разделения колонок

        builder.write(f'\nОбщая сумма - {self.a}\n')
        # Сохраняем документ
        doc.save("out.docx")

        self.model.clear()  # Удаляет все данные, если это поддерживается моделью
    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction_query(id)
        self.view_data(stol_id=self.sto)
        self.reload_data()
    def exit(self):
        self.main_window = Avtoriz()
        self.main_window.show()
        self.hide()
class Avtoriz(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.login = self.ui.lineEdit
        self.password = self.ui.lineEdit_2
        self.ui.pushButton_12.clicked.connect(self.logout)
    def logout(self):
        user_login = self.login.text()
        user_password = self.password.text()

        if not user_login or not user_password:
            QMessageBox.warning(self, 'Внимание', 'Пожалуйста, заполните все поля.')
            return

        db = sqlite3.connect('restoranDB.db')
        self.cur = db.cursor()

        ans = self.cur.execute(f"SELECT * FROM authorization WHERE LOGIN = '{user_login}' AND PASSWORD = '{user_password}'").fetchone()
        if ans == None:
            QMessageBox.warning(self, "Ошибка!", "Неправильный логин или пароль!")
            return

        self.dol_x =self.cur.execute(f"SELECT Должность FROM authorization WHERE LOGIN = '{user_login}' AND PASSWORD = '{user_password}'").fetchone()
        self.dol = ' '.join(self.dol_x)
        self.x_name = self.cur.execute(f"SELECT [main name], NAME FROM authorization WHERE LOGIN = '{user_login}' AND PASSWORD = '{user_password}'").fetchone()
        self.name_zak = ' '.join(self.x_name)

        if ans != None:
            if self.dol == 'официант':
                QMessageBox.information(self, 'Успешный вход!', "Добро пожаловать!")
                self.main_window = Stol(self)
                self.main_window.show()
                self.hide()

            elif self.dol == 'менеджер':
                QMessageBox.information(self, 'Успешный вход!', "Добро пожаловать!")
                self.main_window = Reg()
                self.main_window.show()
                self.hide()

        db.close()

class Stol(QWidget):
    def __init__(self, parent=None):
        super(Stol,self).__init__()

        self.parent_2 = parent

        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.stol = self.ui.lineEdit
        self.ui.pushButton.clicked.connect(self.btn)
        self.kasir = self.parent_2.name_zak
    def btn(self):
        self.st = self.stol.text()
        self.main_window = Zakaz(self)
        self.main_window.show()
        self.hide()
class Reg(QWidget):
    def __init__(self):
        super(Reg, self).__init__()
        self.ui = Ui_Form4()
        self.ui.setupUi(self)
        self.name_x = self.ui.lineEdit
        self.golgnost_x = self.ui.lineEdit_2
        self.login_x = self.ui.lineEdit_3
        self.password_x = self.ui.lineEdit_4
        self.m_name_x = self.ui.lineEdit_5
        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.exit)

    def reg(self):
        name = self.name_x.text().strip()
        m_name = self.m_name_x.text().strip()
        golgnost = self.golgnost_x.text().strip()
        login = self.login_x.text().strip()
        password = self.password_x.text().strip()

        # Проверка, что все поля заполнены
        if not name or not golgnost or not login or not password:
            QMessageBox.warning(self, 'Внимание', 'Пожалуйста, заполните все поля.')
            return

        try:
            db = sqlite3.connect('restoranDB.db')
            self.cur = db.cursor()
            # Используем параметризованный запрос
            self.cur.execute(
                'INSERT INTO authorization (LOGIN, PASSWORD, [main name], NAME, Должность) VALUES (?, ?, ?, ?, ?)',
                (login, password,m_name, name, golgnost)
            )
            db.commit()
            db.close()

            QMessageBox.information(self, 'Успешная регистрация', 'Вы успешно зарегистрированы!')
        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Ошибка базы данных', str(e))

    def exit(self):
        self.main_window = Avtoriz()
        self.main_window.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication([])
    window = Avtoriz()
    window.show()
    app.exec()