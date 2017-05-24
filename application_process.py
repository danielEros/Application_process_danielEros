from flask import Flask, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/mentors')
def mentors():
    render_data = data_manager.mentors_fill()
    return render_template('sql_form.html', **render_data)


@app.route('/all-school')
def all_school():
    render_data = data_manager.all_school_fill()
    return render_template('sql_form.html', **render_data)


@app.route('/mentors-by-country')
def mentors_by_country():
    render_data = data_manager.mentors_by_country_fill()
    return render_template('sql_form.html', **render_data)


@app.route('/contacts')
def school_mentor_contacts():
    render_data = data_manager.contacts_fill()
    return render_template('sql_form.html', **render_data)


@app.route('/applicants')
def list_applicants():
    render_data = data_manager.applicants_fill()
    return render_template('sql_form.html', **render_data)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    render_data = data_manager.applicants_and_mentors_fill()
    return render_template('sql_form.html', **render_data)

if __name__ == '__main__':
    app.run(debug=True)
