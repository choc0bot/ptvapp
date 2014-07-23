from flask import render_template
from app import app
from train import get_train_time, c_time

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)


@app.route('/train')
def train():
	work_train = (1155,14)
	home_train = (1014,0)
	curtime = c_time()
	battrain = get_train_time(home_train)
	parltrain = get_train_time(work_train)
	return render_template("train.html",
    	title = 'Train',
    	parltrain = parltrain,
    	battrain = battrain,
    	curtime = curtime)
