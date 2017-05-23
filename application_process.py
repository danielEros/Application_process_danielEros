from flask import Flask, render_template, request
import connect_psql
# import ui
# import os

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/mentors')
def mentors():
    pass


@app.route('/all-school')
def all_school():
    pass

@app.route('/mentors-by-country')
def mentors_by_country():
    pass


@app.route('/contacts')
def school_mentor_contacts():
    pass


@app.route('/applicants')
def list_applicants():
    pass


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    pass

if __name__ == '__main__':
    app.run(debug=True)
