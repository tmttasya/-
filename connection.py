from PyQt6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('restoranDB.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS zakaz (ID integer primary key AUTOINCREMENT, Наименование TEXT, "
                   "Раздел TEXT, Цена_руб REAL, Стол_ID INTEGER)")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, Name, Razdel, Price, Stol):
        sql_query = "INSERT INTO zakaz (Наименование, Раздел, Цена_руб, Стол_ID) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query,[Name, Razdel, Price, Stol])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM zakaz WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None, sto_filter=None):
        sql_query = f"SELECT SUM({column}) FROM zakaz"

        query_values = []

        # Добавляем фильтрацию по переданному фильтру и значению
        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
            query_values.append(value)

            # Проверяем необходимость добавления фильтрации по Стол_ID
        if sto_filter is not None:
            if len(query_values) > 0:
                sql_query += " AND Стол_ID = ?"
            else:
                sql_query += " WHERE Стол_ID = ?"
            query_values.append(sto_filter)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '₽'

        return '0'

    def total_balance(self, table):
        return self.get_total(column="Цена_руб", sto_filter=table)
