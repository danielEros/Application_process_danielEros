import psycopg2
import os


def show_sql_result_in_table(cursor, sql_query, column_names_list):
    os.system('clear')
    cursor.execute(sql_query)
    sql_result = cursor.fetchall()
    max_cell_length = calculate_max_cell_lengths(column_names_list, sql_result)
    result = ""
    for column_id, column_name in enumerate(column_names_list):
        result += column_name.ljust(max_cell_length[column_id]+1) + " "
    for row in sql_result:
        result += "\n"
        for data_id, data_value in enumerate(row):
            result += str(data_value).ljust(max_cell_length[data_id]+1) + " "
    return result


def calculate_max_cell_lengths(column_names_list, sql_result):
    max_cell_length = list(0 for _ in range(len(column_names_list)))
    for n, cell in enumerate(column_names_list):
        if max_cell_length[n] < len(cell):
            max_cell_length[n] = len(cell)
    for i, row in enumerate(sql_result):
        for n, cell in enumerate(row):
            if max_cell_length[n] < len(str(cell)):
                max_cell_length[n] = len(str(cell))
    return max_cell_length


def mentor_names(cursor):
    sql_query = """SELECT first_name, last_name FROM mentors;"""
    result = show_sql_result_in_table(cursor, sql_query, ["first_name", "last_name"])
    return result


def mentor_nick_names(cursor):
    sql_query = """SELECT nick_name FROM mentors WHERE city='Miskolc';"""
    result = show_sql_result_in_table(cursor, sql_query, ["nick_name"])
    return result


def carol_full_name(cursor):
    sql_query = """SELECT CONCAT(first_name,' ', last_name) AS full_name, phone_number
                   FROM applicants WHERE first_name='Carol';"""
    result = show_sql_result_in_table(cursor, sql_query, ["full_name", "phone_number"])
    return result


def email_search(cursor):
    sql_query = """SELECT CONCAT(first_name,' ', last_name) AS full_name, phone_number
                   FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"""
    result = show_sql_result_in_table(cursor, sql_query, ["full_name", "phone_number"])
    return result


def add_markus(cursor):
    sql_query = """SELECT * FROM applicants WHERE application_code=54823;"""
    cursor.execute(sql_query)
    sql_result = cursor.fetchall()
    if len(sql_result) == 0:
        cursor.execute("""INSERT INTO applicants
                          (first_name, last_name, phone_number, email, application_code)
                          VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    result = show_sql_result_in_table(cursor, sql_query, ["id", "first_name",
                                                          "last_name", "phone_number", "email", "application_code"])
    return result


def change_jemimas_phone_number(cursor):
    sql_query = """UPDATE applicants SET phone_number='003670/223-7459'
                   WHERE first_name='Jemima' AND last_name='Cantu';"""
    cursor.execute(sql_query)
    sql_query = """SELECT phone_number FROM applicants
                   WHERE first_name='Jemima' AND last_name='Cantu';"""
    result = show_sql_result_in_table(cursor, sql_query, ["phone number"])
    return result


def delete_arsenio(cursor):
    os.system('clear')
    cursor.execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net'""")
    return "Delete performed"


def main():
    try:
        connect_str = "dbname='eros' user='eros' host='localhost' password='titok'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
    except Exception as exception_message:
        print("Can't connect. Invalid dbname, user or password?")
        print(exception_message)
        quit()
    os.system('clear')
    while(True):
        print("\n1. Print mentors' name"
              "\n2. Print mentors' nickname who work in Miskolc"
              "\n3. Print Carol's full name and her phone number"
              "\n4. Print the name and phone number of the applicant who has an email of @adipiscingenimmi.edu"
              "\n5. Add Markus Schaffarzyk to the applicants table"
              "\n6. Change Jemima Foreman's phone number"
              "\n7. Delete Arsenio and friend from the applicants table")
        selection = input("Enter an integer from 1 to 7 or '-' to exit: ")
        if selection == "1":
            print(mentor_names(cursor))
        elif selection == "2":
            print(mentor_nick_names(cursor))
        elif selection == "3":
            print(carol_full_name(cursor))
        elif selection == "4":
            print(email_search(cursor))
        elif selection == "5":
            print(add_markus(cursor))
        elif selection == "6":
            print(change_jemimas_phone_number(cursor))
        elif selection == "7":
            print(delete_arsenio(cursor))
        elif selection == "-":
            quit()
        else:
            continue


if __name__ == '__main__':
    main()
