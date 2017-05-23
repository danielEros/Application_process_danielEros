import connect_psql


def mentors_fill():
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


def all_school_fill():
    result_dict = {}
    result_dict['title'] = 'All school page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the mentors plus the '
                                  'name and country of the school (joining with the schools table) ordered by the '
                                  'mentors id column, including all the schools, even if there\' no mentor yet.')
    result_dict['column_list'] = ['mentors.first_name', 'mentors.last_name', 'schools.name', 'schools.country']
    result_dict['sql_query'] = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                  FROM mentors
                                  RIGHT JOIN schools ON mentors.city=schools.city
                                  ORDER BY mentors.id;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def mentors_by_country_fill():
    result_dict = {}
    result_dict['title'] = 'Mentors by country page'
    result_dict['description'] = ('This page shows the result of a query that returns the number of the mentors per '
                                  'country ordered by the name of the countries')
    result_dict['column_list'] = ['country', 'count']
    result_dict['sql_query'] = """SELECT schools.country, COUNT(mentors)
                                  FROM mentors
                                  INNER JOIN schools ON mentors.city=schools.city
                                  GROUP BY schools.country
                                  ORDER BY schools.country;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def contacts_fill():
    result_dict = {}
    result_dict['title'] = 'Contacts page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the school plus the '
                                  'name of contact person at the school (from the mentors table) ordered by the name '
                                  'of the school')
    result_dict['column_list'] = ['schools.name', 'mentors.first_name', 'mentors.last_name']
    result_dict['sql_query'] = """SELECT schools.name, mentors.first_name, mentors.last_name
                                  FROM schools
                                  INNER JOIN mentors ON schools.contact_person=mentors.id
                                  ORDER BY schools.name;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict
