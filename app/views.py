from flask import render_template
from app import app
from train import next_upfield, c_time, next_batman

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)


@app.route('/train')
def train():
	curtime = c_time()
	battrain = next_batman()
	uptrain = next_upfield()
	return render_template("train.html",
    	title = 'Train',
    	uptrain = uptrain,
    	battrain = battrain,
    	curtime = curtime)
