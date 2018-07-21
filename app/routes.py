from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Filip'}
	posts = [
		{
			'author' : {'username': 'Jan'},
			'body' : 'I love the OBX!'
		},
		{
			'author' : {'username': 'Magda'},
			'body' : 'Look at this amazing sunrise. I SOOO needed this beach holiday!'
		},
		{
			'author' : {'username': 'Michal'},
			'body' : 'Surf\'s up dude!'
		},
		{
			'author': {'username': 'Bartus'},
			'body': 'Getting mad inspo for my sneaker line'
		}
	]
	return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    	return redirect( url_for('index') )
    return render_template('login.html', title='Sign In', form=form)
