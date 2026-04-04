import psycopg2
from psycopg2.extras import DictCursor

params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "lola2008",  
    "port": "5432"
}

def manage_contacts():
    # Данные для примера (можешь заменить на input() или аргументы функции)
    name, phone = "Ivan", "+79001112233"
    pattern = "Ivan"

    try:
        # Автоматически закроет соединение и сделает commit
        with psycopg2.connect(**params) as conn:
            # Автоматически закроет курсор
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                
                # 1. Добавляем/обновляем контакт
                cursor.execute("CALL upsert_contact(%s, %s)", (name, phone))
                print(f"Контакт {name} успешно обработан.")

                # 2. Ищем контакты
                cursor.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
                
                results = cursor.fetchall()
                if results:
                    for row in results:
                        print(f"Найдено: {row['name']} | {row['phone']}")
                else:
                    print("Ничего не найдено.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    manage_contacts()