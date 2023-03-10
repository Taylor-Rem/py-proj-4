from flask import Flask, render_template, redirect, url_for, request
from forms import TeamForm, ProjectForm
from model import db, User, Team, Project, connect_to_db

app = Flask(__name__)

app.secret_key = 'carrots'

user_id = 1

@app.route('/')
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    return render_template('home.html', team_form = team_form)

@app.route('/add-team', methods=['POST'])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        team_name = team_form.team_name.data
        new_team = Team(team_name, user_id)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True, port = 4321, host = 'localhost')