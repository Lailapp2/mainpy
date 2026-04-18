import psycopg2
import csv
from config import params

def add_contact(name, phone):
    query = "INSERT INTO phone_book (contact_name, phone_number) VALUES (%s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query, (name, phone))
        conn.commit()
        print(f"Контакт {name} қосылды!")
        cur.close()
    except Exception as error:
        print(f"Қате: {error}")
    finally:
        if conn is not None:
            conn.close()

def import_from_csv(file_name):
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(file_name, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "INSERT INTO phone_book (contact_name, phone_number) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    (row[0], row[1])
                )
        conn.commit()
        print(f"Данные из {file_name} успешно загружены!")
        cur.close()
    except Exception as error:
        print(f"Ошибка: {error}")
    finally:
        if conn is not None:
            conn.close()

def update_contact(name, new_phone):
    sql = "UPDATE phone_book SET phone_number = %s WHERE contact_name = %s;"
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_phone, name))
        conn.commit()
        print(f"{name} нөмірі жаңартылды.")
        cur.close()
    except Exception as e:
        print(f"Қате: {e}")
    finally:
        if conn is not None:
            conn.close()

def search_contacts(pattern):
    sql = "SELECT * FROM phone_book WHERE contact_name ILIKE %s OR phone_number LIKE %s;"
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (f'%{pattern}%', f'{pattern}%'))
        results = cur.fetchall()
        for row in results:
            print(row)
        cur.close()
    except Exception as e:
        print(f"Қате: {e}")
    finally:
        if conn is not None:
            conn.close()

def delete_contact(identifier):
    sql = "DELETE FROM phone_book WHERE contact_name = %s OR phone_number = %s;"
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (identifier, identifier))
        conn.commit()
        print(f"Контакт өшірілді.")
        cur.close()
    except Exception as e:
        print(f"Қате: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    add_contact('Test User', '87001112233')
    import_from_csv('contacts.csv')