import psycopg2
from psycopg2 import sql

def connect_db():
    connection = psycopg2.connect(
        dbname="postgres",
        user="admin",
        password="1234",
        host="localhost",
        port="5432"
    )
    return connection, connection.cursor()

def add_record(name, age):
    try:
        connection, cursor = connect_db()
        insert_query = sql.SQL("INSERT INTO users (name, age) VALUES (%s, %s)")
        cursor.execute(insert_query, (name, age))
        connection.commit()
        print('Запись добавлена')
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cursor.close()
        connection.close()

def fetch_all_records():
    try:
        connection, cursor = connect_db()
        select_query = sql.SQL("SELECT name, age FROM users")
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Все записи:")
        for row in records:
            print(f"Имя: {row[0]}, Возраст: {row[1]}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cursor.close()
        connection.close()

def clear_table():
    try:
        connection, cursor = connect_db()
        cursor.execute(sql.SQL("TRUNCATE TABLE users RESTART IDENTITY"))
        connection.commit()
        print("Таблица очищена")
    except Exception as e:
        print(f"Ошибка при очистке таблицы: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    # clear_table()
    name_input = input("Введите имя: ")
    age_input = int(input("Введите возраст: "))
    add_record(name_input, age_input)
    fetch_all_records()
