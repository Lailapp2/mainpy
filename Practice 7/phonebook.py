import csv
from connect import connect


def create_table():
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table is ready.")


def insert_from_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added successfully.")
    except Exception as e:
        print("Error while adding contact:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def insert_from_csv(filename):
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cur.execute(
                        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                        (row["first_name"], row["phone"])
                    )
                except Exception:
                    conn.rollback()
                    print(f"Skipped: {row}")
                else:
                    conn.commit()

        print("CSV import completed.")
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        cur.close()
        conn.close()


def show_all_contacts():
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    if rows:
        print("\nContacts:")
        for row in rows:
            print(row)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def query_by_name():
    name = input("Enter name to search: ").strip()

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        (f"%{name}%",)
    )
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")

    cur.close()
    conn.close()


def query_by_phone_prefix():
    prefix = input("Enter phone prefix: ").strip()

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (f"{prefix}%",)
    )
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")

    cur.close()
    conn.close()


def update_contact():
    print("1. Update name")
    print("2. Update phone")
    choice = input("Choose option: ").strip()

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        if choice == "1":
            old_name = input("Enter current name: ").strip()
            new_name = input("Enter new name: ").strip()

            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
                (new_name, old_name)
            )
            conn.commit()
            print("Name updated.")

        elif choice == "2":
            name = input("Enter contact name: ").strip()
            new_phone = input("Enter new phone: ").strip()

            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE first_name = %s",
                (new_phone, name)
            )
            conn.commit()
            print("Phone updated.")

        else:
            print("Invalid option.")
    except Exception as e:
        print("Error while updating:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose option: ").strip()

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        if choice == "1":
            name = input("Enter name to delete: ").strip()
            cur.execute(
                "DELETE FROM phonebook WHERE first_name = %s",
                (name,)
            )
            conn.commit()
            print("Contact deleted.")

        elif choice == "2":
            phone = input("Enter phone to delete: ").strip()
            cur.execute(
                "DELETE FROM phonebook WHERE phone = %s",
                (phone,)
            )
            conn.commit()
            print("Contact deleted.")

        else:
            print("Invalid option.")
    except Exception as e:
        print("Error while deleting:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            show_all_contacts()
        elif choice == "4":
            query_by_name()
        elif choice == "5":
            query_by_phone_prefix()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()