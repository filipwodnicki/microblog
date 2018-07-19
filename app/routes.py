from flask import render_template
from app import app

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
