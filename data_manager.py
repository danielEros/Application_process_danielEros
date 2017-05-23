import connect_psql


def mentors_fill():
    result_dict = {}
    result_dict['title'] = 'Mentors and schools page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the mentors plus '
                                  'the name and country of the school (joining with the schools table) ordered by '
                                  'the mentors id column.')
    result_dict['column_list'] = ['mentors.first_name', 'mentors.last_name', 'schools.name', 'schools.country']
    result_dict['sql_query'] = """SELECT m.first_name, m.last_name, s.name, s.country
                                  FROM mentors m
                                  INNER JOIN schools s ON m.city=s.city
                                  ORDER BY m.id;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def all_school_fill():
    result_dict = {}
    result_dict['title'] = 'All school page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the mentors plus the '
                                  'name and country of the school (joining with the schools table) ordered by the '
                                  'mentors id column, including all the schools, even if there\' no mentor yet.')
    result_dict['column_list'] = ['mentors.first_name', 'mentors.last_name', 'schools.name', 'schools.country']
    result_dict['sql_query'] = """SELECT m.first_name, m.last_name, s.name, s.country
                                  FROM mentors m
                                  RIGHT JOIN schools s ON m.city=s.city
                                  ORDER BY m.id;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def mentors_by_country_fill():
    result_dict = {}
    result_dict['title'] = 'Mentors by country page'
    result_dict['description'] = ('This page shows the result of a query that returns the number of the mentors per '
                                  'country ordered by the name of the countries.')
    result_dict['column_list'] = ['country', 'count']
    result_dict['sql_query'] = """SELECT s.country, COUNT(m)
                                  FROM mentors m
                                  INNER JOIN schools s ON m.city=s.city
                                  GROUP BY s.country
                                  ORDER BY s.country;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def contacts_fill():
    result_dict = {}
    result_dict['title'] = 'Contacts page'
    result_dict['description'] = ('This page shows the result of a query that returns the name of the school plus the '
                                  'name of contact person at the school (from the mentors table) ordered by the name '
                                  'of the school.')
    result_dict['column_list'] = ['schools.name', 'mentors.first_name', 'mentors.last_name']
    result_dict['sql_query'] = """SELECT s.name, m.first_name, m.last_name
                                  FROM schools s
                                  INNER JOIN mentors m ON s.contact_person=m.id
                                  ORDER BY s.name;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def applicants_fill():
    result_dict = {}
    result_dict['title'] = 'Applicants page'
    result_dict['description'] = ('This page shows the result of a query that returns the first name and the code of '
                                  'the applicants plus the creation_date of the application (joining with the '
                                  'applicants_mentors table) ordered by the creation_date in descending order, only '
                                  'for applications later than 2016-01-01.')
    result_dict['column_list'] = ['applicants.first_name', 'applicants.application_code',
                                  'applicants_mentors.creation_date']
    result_dict['sql_query'] = """SELECT a.first_name, a.application_code, am.creation_date
                                  FROM applicants a
                                  INNER JOIN applicants_mentors am ON a.id=am.applicant_id
                                  WHERE am.creation_date > '2016-01-01'
                                  ORDER BY am.creation_date DESC;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict


def applicants_and_mentors_fill():
    result_dict = {}
    result_dict['title'] = 'Applicants and mentors page'
    result_dict['description'] = ('This page shows the result of a query that returns the first name and the code of '
                                  'the applicants plus the name of the assigned mentor (joining through the '
                                  'applicants_mentors table) ordered by the applicants id column. All the '
                                  'applicants are shown, even if they have no assigned mentor in the database. In this '
                                  'case the string \'None\' is used instead of the mentor name.')
    result_dict['column_list'] = ['applicants.first_name', 'applicants.application_code', 'mentors.first_name',
                                  'mentors.last_name']
    result_dict['sql_query'] = """SELECT a.first_name, a.application_code, m.first_name, m.last_name
                                  FROM applicants a
                                  LEFT JOIN applicants_mentors am ON a.id=am.applicant_id
                                  LEFT JOIN mentors m ON am.mentor_id=m.id
                                  ORDER BY a.id;"""
    result_dict['sql_result'] = connect_psql.handle_database(result_dict['sql_query'])
    return result_dict
