
from flask import Flask,render_template ,redirect,url_for
from models import Task
from app import app,db
from datetime import datetime
#app is the python script name and also app the instance
import forms 

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks = tasks)

@app.route('/add',methods = ['GET','POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        #Create a row in the database
        t = Task(title = form.title.data,
                 date = datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        #Add and commit to the database
        #We need redirect 

        return redirect(url_for('index'))
    return render_template('add.html',form = form)