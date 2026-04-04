#Этот файл будет проверять, может ли Python подключиться к вашей базе.
import psycopg2
from config import params

def check_connection():
    try:
        connection = psycopg2.connect(**params)
        print("Подключение к PostgreSQL успешно выполнено!")
        connection.close()
    except Exception as error:
        print(f"Ошибка при подключении: {error}")

if __name__ == "__main__":
    check_connection()