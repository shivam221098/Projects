import sqlite3


DATABASE_FILENAME = "record_holders.db"


class RecordHolder:
    def __init__(self, name, country, catches):
        self.name = name
        self.country = country
        self.catches = catches


def database_setup():
    connection = sqlite3.connect(DATABASE_FILENAME)  # establishes the connection with the specified file name
    cursor = connection.cursor()

    # Deleting any existing data
    cursor.execute('DROP TABLE IF EXISTS chainsaw')

    connection.commit()  # saving the changes

    # Create a database table with columns for record holder's name, country, catches
    cursor.execute("""
     CREATE TABLE chainsaw(name TEXT,
                           country TEXT,
                           catches INTEGER)
     """)
    connection.commit()  # saving the changes

    # adding some sample data into our tables
    # Create instances of every record holder and then insert into table
    recordholder1 = RecordHolder("Janne Mustonen", "Finland", 98)
    recordholder2 = RecordHolder("Ian Stewart", "Canada", 94)
    recordholder3 = RecordHolder("Aaron Gregg", "Canada", 88)
    recordholder4 = RecordHolder("Chad Taylor", "USA", 78)

    # Inserting instances into tables i.e. inserting data into table
    insert_record(recordholder1)
    insert_record(recordholder2)
    insert_record(recordholder3)
    insert_record(recordholder4)
    connection.close()  # closes the connection
    show_data()


def insert_record(holder):  # Inserts new records
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    with connection:
        cursor.execute("INSERT INTO chainsaw VALUES ('{}', '{}', '{}')".format(holder.name, holder.country, holder.catches))
    print("Record inserted")
    connection.close()


def search_by_name(search_name):  # Fetches records with names
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM chainsaw WHERE name = '{}'".format(search_name))
    required_data = cursor.fetchall()
    connection.close()
    for row in required_data:
        print("Name: {}, Country: {}, Catches: {}".format(row[0], row[1], row[2]))
    print("Fetched: {} records.".format(len(required_data)))
    connection.close()


def update_catches(name, catches):  # updates catches
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    with connection:
        cursor.execute("UPDATE chainsaw SET catches = '{}' WHERE name = '{}'".format(catches, name))
    print("{} with catches: {} Updated".format(name, catches))
    connection.close()


def delete_record(name):  # deletes records
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    with connection:
        cursor.execute("DELETE FROM chainsaw WHERE name = '{}'".format(name))
    print("Record deleted")
    connection.close()


def show_data():  # shows records
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM chainsaw")
    required_data = cursor.fetchall()  # fetches all the data
    for row in required_data:
        print("Name: {}, Country: {}, Catches: {}".format(row[0], row[1], row[2]))
    print("Fetched: {} records.".format(len(required_data)))
    connection.close()


def main():
    database_setup()
    while True:
        choice = input("""
Enter:
1 for inserting a record
2 for searching record by name
3 for updating catches of a record holder
4 for deleting a record by name
5 for checking records
6 for exit.
        """)
        if choice == '1':
            name = input("Enter name: ")
            country = input("Enter country: ")
            catches = int(input("Enter catches: "))
            record_holder = RecordHolder(name, country, catches)
            insert_record(record_holder)
        elif choice == '2':
            search_by_name(input("Enter name: "))
        elif choice == '3':
            name = input("Enter the name where the catch is to be updated: ")
            catch = int(input("Enter number of catches: "))
            update_catches(name, catch)
        elif choice == '4':
            name = input("Enter the name to be deleted: ")
            delete_record(name)
        elif choice == '5':
            show_data()
        elif choice == '6':
            print("Thanks, Bye")
            exit(0)
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()
