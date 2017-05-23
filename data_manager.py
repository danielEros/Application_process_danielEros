import connect_psql


def mentors_fill_form():
    result_dict = {}
    result_dict['title'] = 'Mentors and schools page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the mentors plus '
                                  'the name and country of the school (joining with the schools table) ordered by '
                                  'the mentors id column.')
    result_dict['column_list'] = ['mentors.first_name', 'mentors.last_name', 'schools.name', 'schools.country']
    result_dict['sql_query'] = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                  FROM mentors
                                  INNER JOIN schools ON mentors.city=schools.city
                                  ORDER BY mentors.id;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict
