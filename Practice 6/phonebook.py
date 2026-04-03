import psycopg2
import csv
from config import params  # Импортируем настройки из вашего файла config.py

# Функция для добавления одного контакта вручную
def add_contact(name, phone):
    query = "INSERT INTO phone_book (contact_name, phone_number) VALUES (%s, %s);"
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query, (name, phone))
        conn.commit()
        print(f"Контакт {name} успешно добавлен!")
        cur.close()
        conn.close()
    except Exception as error:
        print(f"Ошибка при добавлении: {error}")

# Функция для импорта данных из файла contacts.csv
def import_from_csv(file_name):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(file_name, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок (первую строку)
            for row in reader:
                cur.execute(
                    "INSERT INTO phone_book (contact_name, phone_number) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    (row[0], row[1])
                )
        conn.commit()
        print(f"Данные из {file_name} успешно загружены в базу!")
        cur.close()
        conn.close()
    except Exception as error:
        print(f"Ошибка импорта: {error}")

# Точка запуска программы
if __name__ == "__main__":
    # 1. Попробуем добавить один контакт
    add_contact('Test User', '87001112233')
    
    # 2. Попробуем загрузить всё из CSV (убедитесь, что файл contacts.csv создан)
    import_from_csv('contacts.csv')